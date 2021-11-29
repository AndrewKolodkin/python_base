import time


class TrafficLight:
    __color = ['red']

    def running(self):
        while True:
            self.__color = 'Red'
            print(f'\r\033[2;30;41m {self.__color} \033[0;0m', end='')
            time.sleep(7)
            self.__color = 'Yellow'
            print(f'\r\033[2;30;43m {self.__color} \033[0;0m', end ='')
            time.sleep(2)
            self.__color = 'Green'
            print(f'\r\033[2;30;42m {self.__color} \033[0;0m', end='')
            time.sleep(7)


traffic_light = TrafficLight()
traffic_light.running()
