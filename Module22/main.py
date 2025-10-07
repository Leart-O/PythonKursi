from pydantic import BaseModel

# class Item(BaseModel):
#     id: int
#     name: str
#     email: str

#     user = User(id=1, name="John Doe", email="john@gmail.com")
#     print(user)

class User(BaseModel):
    id: int
    name: str
    age: int = 0
    email: str = "example@example.com"

user1 = User(id=1, name="John Doe", age=25)
print(user1)
user2 = User(id=2, name="Jane Smith", age=30)
print(user2)
user3 = User(id=3, name="Alice Johnson", age=28)
print(user3)
