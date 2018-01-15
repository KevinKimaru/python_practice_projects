from user_model import User

# User.create(names="Liz", email="liz@gmail.com", age="17")
# User.create(names="Kevin Chege", email="kevinkimaru99@gmail.com", age="18")
# User.create(names="Eric Ozil", email="ericozil@gmail.com", age="20")
# User.create(names="Mercy Celine", email="mercyceline@gmail.com", age="17")
# User.create(names="Robert", email="robert44@gmail.com", age="15")


users = User.select()
for person in users:
    print(person.names + " " + person.email + "\n\n\n")

person = User.get(User.id == 4)
print(person.names + ": " + person.email)

#ORM Object Relational Mapping