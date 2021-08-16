class User:

    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.ageInFuture = age + 1
        print("jestem inicjalizatorem")

    def print_age(self, message):
        print(message, self.age)


user1 = User(12, 'Sigma')
user2 = User(22, 'Ola')

print(user1.ageInFuture)

user1.print_age("age:")
user2.print_age("wiek:")



