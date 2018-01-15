from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind= engine)
session = DBSession()

# myFirstRestaurant = Restaurant(name = "Pizza Palace")
# hilton = Restaurant(name = "Hilton")
# Pizza = Restaurant(name = "Pizza Inn")
# Chicken = Restaurant(name = "Chicken Inn")
# BakersInn = Restaurant(name = "Bakers Inn")
# InterContinental = Restaurant(name = "InterContinental")
# SafariPark = Restaurant(name = "Safari Park")
# Villa = Restaurant(name = "Villa")
# session.add(myFirstRestaurant)
# session.add(hilton)
# session.add(Pizza)
# session.add(Chicken)
# session.add(BakersInn)
# session.add(InterContinental)
# session.add(SafariPark)
# session.add(Villa)
#
# session.commit()

# cheesepizza = MenuItem(name="Cheese Pizza", description= "Sweet", course="Entree", price="$9.00", restaurant=myFirstRestaurant)
# chicken = MenuItem(name="Chicken", description= "Sweet", course="Entree", price="$9.00", restaurant=myFirstRestaurant)
# iceCream = MenuItem(name="Ice cream", description= "Sweet", course="Entree", price="$9.00", restaurant=myFirstRestaurant)
# pilau = MenuItem(name="Pilau", description= "Sweet", course="Entree", price="$9.00", restaurant=myFirstRestaurant)
# beef = MenuItem(name="Beef", description= "Sweet", course="Entree", price="$9.00", restaurant=myFirstRestaurant)
# session.add(cheesepizza)
# session.add(chicken)
# session.add(iceCream)
# session.add(pilau)
# session.add(beef)
# session.commit()

# firstRsult = session.query(Restaurant).first()
# print(firstRsult.name)

# results = session.query(Restaurant).all()
# for result in results:
#     print (result.name)

# pizzas = session.query(MenuItem).filter_by(name="Cheese Pizza")
# for pizza in pizzas:
#     print(pizza.name)
#     print("\n")

# cheesePizza = session.query(MenuItem).filter_by(id=1).one()
# print(cheesePizza.price)
# cheesePizza.price = '$5.00'
# session.add(cheesePizza)
# session.commit()

# results = session.query(MenuItem).all()
# for result in results:
#     print (result.name)
#     print (result.price)

# iceCream = session.query(MenuItem).filter_by(name="Ice cream").one()
# print(iceCream.restaurant)
# print(iceCream.restaurant.name)
# session.delete(iceCream)
# session.commit()


