from threading import *
import pause

class Task1(Thread):
    def run(self):
        for i in range(5):
            print("mahesh")
            pause.seconds(1)


class Task2(Thread):
    def run(self):
        for i in range(5):
            print("Deepika")
            pause.seconds(1)


t1 = Task1()
t2 = Task2()

t1.start()
pause.seconds(0.2)
t2.start()

t1.join()
t2.join()
print("Bye")