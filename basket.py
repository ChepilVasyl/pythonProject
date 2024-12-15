if __name__ == "__main__":
    teamBasket = [
        {
        "id":1,
        "name":"Ivan",
        "age":35,
        "height":186
        },
        {
        "id": 2,
        "name":"Vasyl",
        "age":19,
        "height":189
        },
        {
        "id": 3,
        "name":"Petro",
        "age":33,
        "height":1195
        },
        {
        "id": 4,
        "name":"Oleg",
        "age":22,
        "height":182
        }
    ]
    id = len(teamBasket)

    def AddPlayer():
        global id
        name = input("Вкажіть ім'я гравця: ")
        age = input("Вкажіть вік гравця: ")
        height = input("Вкажіть зріст гравця: ")
        id+=1
        teamBasket.append({
            "id":id,
            "name": f'{name}',
            "age": f'{age}',
            "height": f'{height}'
        })
    def DelPlayer():
        idLoc = int(input("Вкажіть id гравця: "))
        for i in teamBasket:
            if i.get("id")==idLoc:
                teamBasket.remove(i)
                break
    def PrintPlayers():
        for i in teamBasket:
            print("id = "+str(i.get("id")))
            print("name = " + str(i.get("name")))
            print("age = " + str(i.get("age")))
            print("height = " + str(i.get("height")))
            print()
    def FindPlayer():
        PrintPlayers()
        idPlayer = int(input("Вкажіть id гравця: "))
        for i in range(len(teamBasket)):
            if teamBasket[i].get("id")==idPlayer:
                print("Гравця знайдено!")
                print("id = " + str(teamBasket[i].get("id")))
                print("name = " + str(teamBasket[i].get("name")))
                print("age = " + str(teamBasket[i].get("age")))
                print("height = " + str(teamBasket[i].get("height")))
                return i
        print(f"Гравця з id {idPlayer} немає в списку")
        return -1
    def EditPlayer():
        temp = FindPlayer()
        if temp!=-1:
            print("Оберіть поле для зміни: ")
            print("name - натисніть 1")
            print("age - натисніть 2")
            print("height - натисніть 3")
            choice2 = int(input("Зробіть свій вибір: "))
            newData = ""
            if(choice2==1):
                newData = input("Вкажіть нове ім'я: ")
                teamBasket[temp]["name"] = newData
            elif (choice2 == 2):
                newData = input("Вкажіть новий вік: ")
                teamBasket[temp]["age"] = newData
            elif (choice2 == 3):
                newData = input("Вкажіть новий зріст: ")
                teamBasket[temp]["height"] = newData



    choice = 0
    while True:
        print("Для додавання натисніть 1")
        print("Для видалення натисніть 2")
        print("Для пошуку натисніть 3")
        print("Для редагування натисніть 4")
        print("Для виводу всіх гравців натисніть 5")
        choice = int(input("Зробіть свій вибір: "))
        if choice==1:
            AddPlayer()
        elif choice==2:
            DelPlayer()
        elif choice==3:
            FindPlayer()
        elif choice==4:
            EditPlayer()
        elif choice==5:
            PrintPlayers()