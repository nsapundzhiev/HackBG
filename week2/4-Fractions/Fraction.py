class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        first = self.numerator
        second = self.denominator
        remainder = 1

        while(remainder != 0):
            remainder = first % second
            first = second
            second = remainder

        if self.numerator != 1 and self.denominator != 1:
            self.numerator /= first
            self.denominator /= first


    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        eq_numerator = self.numerator == other.numerator
        eq_denominator = self.denominator == other.denominator
        return eq_denominator and eq_numerator

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator , self.denominator*other.denominator)


    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator , self.denominator*other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)


a = Fraction(18,9)
b = Fraction(2,4)

print(a == b)
print (a - b)
print (a + b)
print (a * b)
