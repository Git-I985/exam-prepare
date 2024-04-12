from peewee import *

db = SqliteDatabase('db.db')

#
class BaseModel(Model):
    class Meta:
        database = db


class Position(BaseModel):
    name = TextField()
    salary = FloatField()
    vacation_days = IntegerField()


class Employee(BaseModel):
    name = TextField()
    position = ForeignKeyField(Position)


class Bonus(BaseModel):
    name = TextField()
    amount = FloatField()
    employee = ForeignKeyField(Employee)


class Vacation(BaseModel):
    employee = ForeignKeyField(Employee)
    days = IntegerField()


class Payment(BaseModel):
    employee = ForeignKeyField(Employee)


class PaymentToBonus(BaseModel):
    payment = ForeignKeyField(Payment)
    bonus = ForeignKeyField(Bonus)


class PaymentToVacation(BaseModel):
    payment = ForeignKeyField(Payment)
    vacation = ForeignKeyField(Vacation)

# TEST
class User(BaseModel):
    login=TextField()
    password=TextField()

db.create_tables([
    Position,
    Employee,
    Bonus,
    Vacation,
    Payment,
    PaymentToBonus,
    PaymentToVacation,
    User
])
