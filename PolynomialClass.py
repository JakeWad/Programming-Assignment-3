class Polynomial:
    """
    Polynomial Class:
    argument list: [a0, a1, a2, a3, a4, ..., an]
    which represents a0 + a1x^1 + a2x^2 + ... + anx^n
    """

    def __init__(self, *coefficients):
        if len(coefficients) == 0:
            self.coefficients = [0]
        else:
            self.coefficients = coefficients

    def __call__(self, x):
        result = 0
        power = 1
        for coef in self.coefficients:
            result += coef * power
            power *= x
        return result

    def dim(self):
        return len(self.coefficients) - 1

    def __add__(self, other):
        if isinstance(other, Polynomial):
            new_coef = [0] * max(len(self.coefficients), len(other.coefficients))
            for i in range(len(new_coef)):
                if i < len(self.coefficients):
                    new_coef[i] += self.coefficients[i]
                if i < len(other.coefficients):
                    new_coef[i] += other.coefficients[i]
            return Polynomial(*new_coef)
        else:
            raise TypeError("unsupported operand type(s) for +: 'Polynomial' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            new_coef = [0] * max(len(self.coefficients), len(other.coefficients))
            for i in range(len(new_coef)):
                if i < len(self.coefficients):
                    new_coef[i] += self.coefficients[i]
                if i < len(other.coefficients):
                    new_coef[i] -= other.coefficients[i]
            return Polynomial(*new_coef)
        else:
            raise TypeError("unsupported operand type(s) for -: 'Polynomial' and '{}'".format(type(other).__name__))

    def __str__(self):
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            if i == 0:
                term = str(coef)
            elif i == 1:
                term = "{}x".format(coef) if coef != 1 else "x"
            else:
                term = "{}x^{}".format(coef, i)
            terms.append(term)
        if len(terms) == 0:
            return "0"
        else:
            return " + ".join(terms)

    def __repr__(self):
        return "Polynomial({})".format(", ".join(str(coef) for coef in self.coefficients))
