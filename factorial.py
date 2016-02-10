class factorialClass:
    def calculate(self, n):
        if n == 0: return 1
        return n * self.calculate(n-1)

