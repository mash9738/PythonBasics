from threading import *
import pause

class add(Thread):
    def run(self):
        for i in range(5):
            print(2 + 3)
            pause.seconds(1)

class sub(Thread):
    def run(self):
        for i in range(5):
            print(6 - 3)
            pause.seconds(1)


class div(Thread):
    def run(self):
        for i in range(5):
            print(6 / 3)
            pause.seconds(1)

class mul(Thread):
    def run(self):
        for i in range(5):
            print(6 * 3)
            pause.seconds(1)


t1 = add()
t2 = sub()
t3 = div()
t4 = mul()

t1.start()
pause.seconds(0.2)
t2.start()
pause.seconds(0.2)
t3.start()
pause.seconds(0.2)
t4.start()


t1.join()
t2.join()
t3.join()
t4.join()

print("Bye")