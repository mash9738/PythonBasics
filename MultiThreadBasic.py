import time
class Hello:
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(1)


class Hi:
    def run(self):
        for i in range(5):
            print("Hi")
            time.sleep(1)


t1 = Hello()
t2 = Hi()

t1.run()
time.sleep(0.2)
t2.run()

print("This is not Multi threading")