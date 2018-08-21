class frac(object):
    """
    Author - @Antriksh Sharma
    ---------------------------
    .__init__()
    .__str__()
    .getNumer()
    .getDenom()
    .__add__()
    .__sub__()
    .__mul__()
    .reciprocal()
    .__truediv__()
    .__trueval__()
    .reduce()
    .__eq__()
    .equal()
    .__lt__()
    .__gt__()
    .__ge__()
    .__le__()
    .type()
    ---------------------------
    """
    def __init__(self, numer, denom = 1):
        assert type(numer) == int or type(numer) == float, "numerator can hold int or float values only"
        assert type(denom) == int or type(denom) == float, "denominator can hold int or float values only"
        assert denom != 0, "denominator can never be 0"
        self.numer = numer
        self.denom = denom
        if self.denom < 0:
            self.numer = -self.numer

    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    
    def __add__(self, other):
        newNumer = (self.numer * other.denom) + (other.numer * self.denom)
        newDenom = self.denom * other.denom
        return frac(newNumer, newDenom).reduce()

    def __sub__(self, other):
        newNumer = (self.numer * other.denom) - (other.numer * self.denom)
        newDenom = self.denom * other.denom
        return frac(newNumer, newDenom).reduce()

    def __mul__(self, other):
        newNumer = self.numer * other.numer
        newDenom = self.denom * other.denom
        return frac(newNumer, newDenom).reduce()

    def reciprocal(self):
        return frac(self.denom, self.numer).reduce()
    
    def __truediv__(self, other):       
        return frac.__mul__(self, frac.reciprocal(other)).reduce()

    def trueval(self):
        return (self.numer/self.denom)
    
    def reduce(self):
        if self.denom == self.numer:
            self.denom = self.numer = 1
            return self
        if self.numer == 0:
            return 0
        else:
            import math
            HCF = math.gcd(abs(self.numer), abs(self.denom))
            self.numer = int(self.numer/HCF)
            self.denom = int(self.denom/HCF)
            return self

    def __eq__(self, other):
        self.reduce()
        other.reduce()
        eq = False
        if self.numer == other.numer and self.denom == other.denom:
            eq = True
        return eq

    def equal(self, other):
        eq = False
        if self.numer == other.numer and self.denom == other.denom:
            eq = True
        return eq
    
    def __lt__(self, other):
        if  self.trueval() - other.trueval() < 0:
            return True
        else:
            return False

    def __gt__(self, other):
        if  self.trueval() - other.trueval() > 0:
            return True
        else:
            return False

    def __le__(self, other):
        if  self.trueval() - other.trueval() <= 0:
            return True
        else:
            return False

    def __ge__(self, other):
        if  self.trueval() - other.trueval() >= 0:
            return True
        else:
            return False
    def type(self):
        return 'Fraction'
