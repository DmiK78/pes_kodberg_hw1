# task 1 Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.

class Book:

    def __init__(self, author, bookname, issue_year, genre):
        self.author = author
        self.bookname = bookname
        self.issue_year = issue_year
        self.genre = genre

    def __str__(self):
        return f'{self.author}, "{self.bookname}", {self.issue_year}, {self.genre}'

dumas = Book("A. Dumas", "The Three Musketeers", 1844, "adventure novel")
tolstoy = Book("L. Tolstoy", "War and Peace", 1865, "historical novel")
brown = Book("D. Brown", "The Da Vinci Code", 2003, "mystery thriller novel")

print(dumas)
print(tolstoy)
print(brown)

# task 2 Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї. 

class Feedback:

    def __init__(self, book:str):
        self.book = book
    
    def print_review(self):
        bad = "bad book"
        good = "good book"
        cool = "cool book"
        feedback_list = [bad, good, cool]
        print(f'The book "{self.book}" is {feedback_list}')

dumas = Feedback(book="The Three Musketeers")

dumas.print_review()

# task 4 Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів, доступних для продажу,
# і функцію продажу заданого автомобіля.

class Car:

    def __init__(self, brand:str, engine_volume:float, hp:int, cylinder_num:int, drive:str):
        self.brand = brand
        self.engine_volume = engine_volume
        self.hp = hp
        self.cylinder_num = cylinder_num
        self.drive = drive

car1 = Car("bmw", 2, 300, 4, "rear")
car2 = Car("ford", 3, 400, 6, "full")
car3 = Car("lexus", 2.5, 280, 4, "front")

class CarStore:

    def __init__(self, usa_car, germ_car, jap_car, premium, luxury):
        self.usa_car = usa_car
        self.germ_car = germ_car
        self.jap_car = jap_car
        self.premium = premium
        self.luxury = luxury
    
    def sell_car(self):
        if self.premium == "ford":
            print(f'Selling car: {self.usa_car}')
        elif self.luxury == "bmw":
            print(f'Selling car: {self.germ_car}')
        elif self.luxury == "lexus":
            print(f'Selling car: {self.jap_car}')
        
store = CarStore(usa_car=car2, germ_car=car1, jap_car=car3, premium="ford", luxury="luxury")

store.sell_car()
