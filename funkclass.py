# funky class instances and methods

def ff () :
    print ('Fcksds')

class testE :
    obv = ff
    
    def nope (self, text) :
        print (f'Printing ... {text}')
    
    whyNot = nope
    
class result (testE) :
    
    def dateInc (self, days) :
        self.date = 5
        self.date = self.date + days