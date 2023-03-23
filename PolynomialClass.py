class Polynomial:
    def __init__(self, *coeffs):
        if not coeffs:
            self.coeffs = [0]
        else:
            self.coeffs = coeffs

    def __call__(self, x):
        result = 0
        for i, coeff in enumerate(self.coeffs):
            result += coeff * (x ** i)
        return result

    def dim(self):
        return len(self.coeffs) - 1

    def __add__(self, other):
        combined_coeffs = []
        max_len = max(len(self.coeffs), len(other.coeffs))
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len(self.coeffs) else 0
            c2 = other.coeffs[i] if i < len(other.coeffs) else 0
            combined_coeffs.append(c1 + c2)
        return Polynomial(*combined_coeffs)

    def __sub__(self, other):
        combined_coeffs = []
        max_len = max(len(self.coeffs), len(other.coeffs))
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len(self.coeffs) else 0
            c2 = other.coeffs[i] if i < len(other.coeffs) else 0
            combined_coeffs.append(c1 - c2)
        return Polynomial(*combined_coeffs)

    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coeffs):
            if coeff != 0:
                if i == 0:
                    terms.append(str(coeff))
                elif i == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{i}")
        if not terms:
            return "0"
        else:
            return " + ".join(reversed(terms))

    def __repr__(self):
        return f"Polynomial{tuple(self.coeffs)}"
        
    __doc__ = "Polynomial Class:\n" + \
              "  argument list: [a0, a1, a2, a3, ..., an]\n" + \
              "                 which represents\n" + \
              "                 a0 + a1x^1 + a2x^2 + ... + anx^n"
