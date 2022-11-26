#Write a method which throws exception, Call that method in main class without try block
class MyError():
 
    def __init__(self, value):
        self.value = value

    def division(self):
        print(self.value/0)


my=MyError(3)
my.division()