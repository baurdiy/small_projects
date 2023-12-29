
class Quadratic:
    def __init__(self):
        self.a = float(input("Enter a: "))
        self.b = float(input("Enter b: "))
        self.c = float(input("Enter c: "))
    

    def roots(self):
        D = (self.b * self.b - 4 * self.a * self.c) ** 0.5
        x_1 = (-self.b + D) / (2 * self.a)
        x_2 = (-self.b - D) / (2 * self.a)
        print(f"{x_1=}, \n{x_2=}")


if __name__ == "__main__":
    run = Quadratic()
    run.roots()