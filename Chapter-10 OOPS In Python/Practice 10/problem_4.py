class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n*self.n*self.n}")

    @staticmethod
    def hello():
        print("hello worlds")
a = calculator(2)
a.hello()
a.square()
a.cube()
a.squareroot()