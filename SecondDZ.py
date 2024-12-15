import time
if __name__ == "__main__":
    def WrapperDecorator(func):
        def OldWrapper(b,a):
            startTime = time.time()
            for i in func(b,a):
                print(i,end=" ")
            endTime = time.time()
            print()
            print(f"Кількість секунд витрачених на обчислення всіх простих чисел = {endTime - startTime}")
        return OldWrapper
    def IsSimpleNumber(number):
        for i in range(2,number):
            if number%i==0:
                return False
        return True
    @WrapperDecorator
    def SimpleNumbers_0_1000(below,abowe):
        lst = []
        for i in range(below,abowe):
            if IsSimpleNumber(i):
                lst.append(i)
        return lst
    belowLimit = int(input("Вкажіть нижню межу для пошуку простих чисел: "))
    abowLimit = int(input("Вкажіть верхню межу для пошуку простих чисел: "))
    SimpleNumbers_0_1000(belowLimit,abowLimit)


