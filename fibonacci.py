class fibonacciClass:
    def __init__(self, n1=0, n2=1):
        self.fn1 = n1 
        self.fn2 = n2 
        self.next_count = -1
     
    def next(self):
        self.next_count += 1
        return self.Calculate(self.next_count)
        
    def calculate(self, n):
        if n <= 0: return self.fn1
        if n == 1: return self.fn2
        return self.calculate(n-1)+self.calculate(n-2)
        
    def writeToFile(self,n=2, filename="fibonacci.out"):
        f = open(filename, 'w')
        for i in range (0, n):    
            f.write("%3i  %i\n" % (i, self.Calculate(i)) )
        f.close()
        
