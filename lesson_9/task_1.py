from time import sleep  # импорт таймера задержки для имитации переключения света светофора


class TrafficLight:  # объявление класса
    __color = "red"  # приватный атрибут

    def running(self, color):  # функция, принимающая желаемый цвет светофора как аргумент
        # если пользователь желает переключить на противоположный цвет светофора:
        if TrafficLight.__color == "red" and color == "green" or TrafficLight.__color == "green" and color == "red":
            print(f"Невозможно переключить с {TrafficLight.__color} на {color}")
            exit()
            # если введен цвет, который уже горит на светофоре
        elif TrafficLight.__color == color:
            print(f"Цвет сфетофора уже является {color} в данный момент.")
            # если цвет светофора yellow
        elif TrafficLight.__color == "yellow":
            print(f"Цвет светофора: {TrafficLight.__color}")
            print("До переключения светофора осталось 2 сек")
            sleep(1)
            for i in range(1, 0, -1):
                print(f"{i} сек..")
            TrafficLight.__color = color
            print(f"Цвет светофора теперь: {TrafficLight.__color}")
            # если желаемый цвет yellow
        elif color == "yellow":
            # если на светофоре в данный момент установлен цвет green
            if TrafficLight.__color == "green":
                print(f"Цвет светофора: {TrafficLight.__color}")
                print(f"Переключение на {color}")
                print("До переключения светофора осталось 10 сек")
                sleep(1)
                for i in range(9, 0, -1):
                    sleep(1)
                    print(f"{i} сек..")
                TrafficLight.__color = color
                print(f"Цвет светофора теперь: {TrafficLight.__color}")
                # если на светофоре в данный момент установлен цвет red
            elif TrafficLight.__color == "red" and color == "yellow":
                print(f"Цвет светофора: {TrafficLight.__color}")
                print(f"Переключение на {color}")
                print("До переключения светофора осталось 7 сек")
                sleep(1)
                for i in range(6, 0, -1):
                    sleep(1)
                    print(f"{i} сек..")
                TrafficLight.__color = "yellow"
                print(f"Цвет светофора теперь: {TrafficLight.__color}")


t = TrafficLight()  # создание экземпляра класса
t.running("yellow")  # проверка функции
t.running("green")
t.running("red")  # проверка на случай невозможного переключения
t.running("yellow")
t.running("red")  # возвращение к изначальному состоянию


