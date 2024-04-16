from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql://localhost/chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationallity = Column(String)
    famous_for = Column(String)


# instead of connectiong to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# create ing the database using declarative base subclass
base.metadata.create_all(db)

ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationallity = "British",
    famous_for = "First Programmer"
)

alan_turning = Programmer(
    first_name = "Alan",
    last_name = "Turning",
    gender = "M",
    nationallity = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationallity = "American",
    famous_for = "COBOL language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationallity = "American",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationallity = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationallity = "British",
    famous_for = "World Wide Web"
)

niklas_andersson = Programmer(
    first_name = "Niklas",
    last_name = "Andersson",
    gender = "M",
    nationallity = "Swedish",
    famous_for = "Python Student"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turning)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(niklas_andersson)

# commit our session to the database
#session.commit()

# updating a single record
# programmer = session.query(Programmer).filter_by(id=11).first()
# programmer.famous_for = "World President"

# people = session.query(Programmer)
# for person in people:
#    if person.gender == "F":
#        person.gender = "Female"
#    elif person.gender == "M":
#        person.gender = "Male"
#    else:
#        print("Gender not defined")
#    session.commit()

# delete a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#    confirmation = input("Are you sure you want to delete this record? (y/n ")
#    if confirmation.lower() == "y":
#        session.delete(programmer)
#        session.commit()
#        print("Programmer has been deleted")
#    else:
#        print("Programmer not deleted")


# else:
#    print("No record found")


# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationallity,
        programmer.famous_for,
        sep = " | "
    )
