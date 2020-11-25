import copy

class Symbol:

    #The symbol itself
    symbolName = ''

    #Contruct a symbol from a string
    def __init__(self,symbolName):
        
        #Check that the incoming variable is a string 
        if(isinstance(symbolName,str)):
            #Store the string 
            self.symbolName = symbolName
        else:
            raise RuntimeError('Symbol must be a string')
    
    #Subject to change
    def __add__(self,obj):
        
        #If the input object is of type Symbol
        if(isinstance(obj,Symbol)):
            
            #Constuct and return an equation
            return Equation([self,obj])
        
        #If the input object is of type Equation 
        if(isinstance(obj,Equation)):

            obj + self
    

    def __eq__(self,oSymbol):
        return self.symbolName == oSymbol.symbolName
    
    def __str__(self):
        return self.symbolName


class Equation:

    coefficents = []
    symbols = []

    def __init__(self,symbols):

        #If the input is a list
        if(isinstance(symbols,list)):
            
            #for all elements in list 
            for x in symbols:
                
                #if any element is not of type Symbol
                if(not isinstance(x,Symbol)):
                    raise RuntimeError('Arg 1 must be a List of Symbols')
        
        #Passed the test we can safely copy and store
        self.symbols = copy.deepcopy(symbols)

        #Each symbol gets
        for i in range(len(self.symbols)):
            self.coefficents.append(1)

    def __add__(self,obj):
        
        if(isinstance(obj,Symbol)):
            #For each symbol
            for i in range(len(self.symbols)):
                
                if(obj == self.symbols[i]):
                    self.coefficents[i] = self.coefficents[i] + 1
                    return None
            
            self.symbols.append(obj)
            self.coefficents.append(1)

    
    def __str__(self):
        
        eqStr = ''

        for i in range(len(self.symbols)):
            
            currSym = self.symbols[i]
            currCoeff = self.coefficents[i]

            if(i > 0 and currCoeff > 0):
                
                eqStr = eqStr + '+'

            if(abs(currCoeff) != 1):
                eqStr = eqStr + str(currCoeff)

            eqStr = eqStr + str(currSym)

        return eqStr
                

x = Symbol('x')
y = Symbol('y')
p = Symbol('x')

z = x + y
print(z)
p + z
print(z)
z + p
print(z)