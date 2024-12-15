# Реалізуйте клас «Автомобіль». Збережіть у класі: назву
# моделі, рік випуску, виробника, об’єм двигуна, колір машини,
# ціну. Реалізуйте методи класу для введення-виведення даних
# та інших операцій.
class Car:
    __model = ""
    __year = None
    __produce = ""
    __value = None
    __color = ""
    __price = None
    def __init__(self,mod="Пусто",yer=0,pro="Пусто",val=0.0,col="Немає",pri=0.0):
        self.__model = mod
        self.__year = yer
        self.__produce = pro
        self.__value = val
        self.__color = col
        self.__price = pri
    @property
    def Model(self):
        return self.__model
    @Model.setter
    def Model(self,model):
        self.__model = model

    @property
    def Year(self):
        return self.__year

    @Year.setter
    def Year(self, model):
        self.__year = model

    @property
    def Produce(self):
        return self.__produce

    @Produce.setter
    def Produce(self, model):
        self.__produce = model

    @property
    def Value(self):
        return self.__value

    @Value.setter
    def Value(self, model):
        self.__value = model

    @property
    def Color(self):
        return self.__color

    @Color.setter
    def Color(self, model):
        self.__color = model

    @property
    def Price(self):
        return self.__price

    @Price.setter
    def Price(self, model):
        self.__price = model
    def __str__(self):
        return (f"Модель авто: {self.__model}\n"
                f"Рік випуску: {self.__year}\n"
                f"Виробник: {self.__produce}\n"
                f"Об'єм двигуна: {self.__value}\n"
                f"Колір: {self.__color}\n"
                f"Ціна: {self.__price}\n"
                )
car = Car("Тойота",1995)
print(car)
# Реалізуйте клас «Книга». Збережіть у класі: назву книги,
# рік видання, видавця, жанр, автора, ціну. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.
class Book:
    __name = ""
    __year = None
    __produce = ""
    __genre = ""
    __autor = ""
    __price = None
    def __init__(self,nam="Пусто",yer=0,pro="Пусто",gen=0.0,aut="Немає",pri=0.0):
        self.__name = nam
        self.__year = yer
        self.__produce = pro
        self.__genre = gen
        self.__autor = aut
        self.__price = pri
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,model):
        self.__name = model

    @property
    def Year(self):
        return self.__year

    @Year.setter
    def Year(self, model):
        self.__year = model

    @property
    def Produce(self):
        return self.__produce

    @Produce.setter
    def Produce(self, model):
        self.__produce = model

    @property
    def Genre(self):
        return self.__genre

    @Genre.setter
    def Genre(self, model):
        self.__genre = model

    @property
    def Autor(self):
        return self.__autor

    @Autor.setter
    def Autor(self, model):
        self.__autor = model

    @property
    def Price(self):
        return self.__price

    @Price.setter
    def Price(self, model):
        self.__price = model
    def __str__(self):
        return (f"Назва книги: {self.__name}\n"
                f"Рік випуску: {self.__year}\n"
                f"Видавник: {self.__produce}\n"
                f"Жанр: {self.__genre}\n"
                f"Автор: {self.__autor}\n"
                f"Ціна: {self.__price}\n"
                )
book = Book("Жага до до життя",1968)
print(book)
# Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.
class Stadium:
    __name = ""
    __date = ""
    __country = ""
    __city = ""
    __capacity = None
    def __init__(self,nam="Пусто",dat="Пусто",con="Пусто",cit="Пусто",cap="Пусто"):
        self.__name = nam
        self.__date = dat
        self.__country = con
        self.__city = cit
        self.__capacity = cap
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,model):
        self.__name = model

    @property
    def Date(self):
        return self.__date

    @Date.setter
    def Date(self, model):
        self.__date = model

    @property
    def Country(self):
        return self.__country

    @Country.setter
    def Country(self, model):
        self.__country = model

    @property
    def City(self):
        return self.__city

    @City.setter
    def City(self, model):
        self.__city = model

    @property
    def Capacity(self):
        return self.__capacity

    @Capacity.setter
    def Capacity(self, model):
        self.__capacity = model

    def __str__(self):
        return (f"Назва стадіону: {self.__name}\n"
                f"Дата відкритя: {self.__date}\n"
                f"Країна: {self.__country}\n"
                f"Місто: {self.__city}\n"
                f"Місткість: {self.__capacity}\n"
                )
stadium = Stadium("Комсомолець",1974)
print(stadium)