from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body><h1>Make a New Restaurant</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>" \
                          "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name'>" \
                          "<input type='submit' value='create'></form>"
                output += "</html></body>"

                self.wfile.write(bytes(output, "utf-8"))

            if self.path.endswith("/edit"):
                reataurantIdPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=reataurantIdPath).one()
                if myRestaurantQuery != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1>"
                    output += str(myRestaurantQuery.name)
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit' >" % reataurantIdPath
                    output += "<input name='newRestaurantName' type='text' placeholder='%s'>" % myRestaurantQuery.name
                    output += "<input type='submit' value='Rename'></form>"
                    output += "</html></body>"

                    self.wfile.write(bytes(output, "utf-8"))

            if self.path.endswith("/delete"):
                reataurantIdPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=reataurantIdPath).one()
                if myRestaurantQuery != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete %s?"%myRestaurantQuery.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete' >" % reataurantIdPath
                    output += "<input type='submit' value='Delete'></form>"
                    output += "</html></body>"

                    self.wfile.write(bytes(output, "utf-8"))


            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<a href='/restaurants/new'>Make a New Restaurant Here</br></br></a>"
                restaurants = session.query(Restaurant).all()
                for restaurant in restaurants:
                    output += str(restaurant.name)
                    output += "</br>"
                    output += "<a href='/restaurants/%s/edit'>Edit</a>"%restaurant.id
                    output += "</br>"
                    output += "<a href='/restaurants/%s/delete'>Delete</a>"%restaurant.id
                    output += "</br></br>"
                output += "</html></body>"

                self.wfile.write(bytes(output, "utf-8"))
                return

            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello!"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>" \
                          "<h2>What would you like me to say?</h2>" \
                          "<input name='message' type='text'>" \
                          "<input type='submit' value='submit'></form>"
                output += "</html></body>"

                self.wfile.write(bytes(output, "utf-8"))
                print(output)
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>&#161Hola <a href='/hello'>Back to hello</a>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>" \
                          "<h2>What would you like me to say?</h2>" \
                          "<input name='message' type='text'>" \
                          "<input type='submit' value='submit'></form>"
                output += "</html></body>"

                self.wfile.write(bytes(output, "utf-8"))
                print(output)
                return
        except IOError:
            self.send_error(404, "File not found %s" % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers['content-type'])
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')

                restaurantIdPath = self.path.split("/")[2]

                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIdPath).one()
                if myRestaurantQuery !=[]:
                    myRestaurantQuery.name = messagecontent[0].decode("utf-8")
                    session.add(myRestaurantQuery)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(self.headers['content-type'])
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')

                restaurantIdPath = self.path.split("/")[2]

                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIdPath).one()
                if myRestaurantQuery !=[]:
                    session.delete(myRestaurantQuery)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers['content-type'])
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')

                newRestaurant = Restaurant(name=messagecontent[0].decode("utf-8"))
                session.add(newRestaurant)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

            if self.path.endswith("/hello"):
                self.send_response(301)
                self.end_headers()

                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')

                output = ""
                output += "<html><body>"
                output += "<h2> Okay, how about this: </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]

                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>" \
                          "<h2>What would you like me to say?</h2>" \
                          "<input name='message' type='text'>" \
                          "<input type='submit' value='submit'></form>"

                output += "</html></body>"

                self.wfile.write(bytes(output, "utf-8"))
                print(output)
                return
        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print("Web server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()


if __name__ == '__main__':
    main()
