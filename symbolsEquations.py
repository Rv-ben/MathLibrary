
class Symbol:

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
            
            #Invoke Equation __add__ , returns Equation
            return Equation.fromEquationSymbol(obj,self)
        
        #if the input object is of type Equation
        if(isinstance(obj,int)):

            return Equation.fromEquationConstant(Equation([self]),obj)
    
    def __sub__(self,obj):
        
        #If the input object is of type Symbol
        if(isinstance(obj,Symbol)):
            
            #Constuct and return an equation
            return Equation.fromEquationSymbol(Equation([self]),obj,subtract=True)

        #If the input object is of type Equation 
        if(isinstance(obj,Equation)):
            
            #Invoke Equation __add__ , returns Equation
            return Equation.fromEquationSymbol(obj,self,subtract=True)
        
        #if the input object is of type Equation
        if(isinstance(obj,int)):

            return Equation.fromEquationConstant(Equation([self]),1* obj)
    
    def __eq__(self,oSymbol):
        return self.symbolName == oSymbol.symbolName
    
    def __str__(self):
        return self.symbolName

class Equation:

    def __init__(self,symbols,coefficents = [], constant = 0):
        
        self.symbols = symbols
        self.constant = constant
        self.coefficents = coefficents

        if(coefficents == []):
            for i in range(len(symbols)):
                self.coefficents.append(1)
    
    @classmethod
    def fromEquationSymbol(cls,equation,obj,subtract = False):
        
        symbols = []
        coefficents = []
        constant = 0

        if(isinstance(equation,Equation) and isinstance(obj,Symbol)):
            
            symbolInEquation = False

            #For each symbol
            for i in range(len(equation.symbols)):
                #Add each symbol to this equation
                symbols.append(equation.symbols[i])
                coefficents.append(equation.coefficents[i])

                #if the incoming symbol is in the equation
                if(not symbolInEquation and symbols[i] == obj):
                    #increment the coresponding coefficent
                    if(not subtract):
                        coefficents[i] = coefficents[i] + 1
                    else:
                        coefficents[i] = coefficents[i] - 1
                    
                    symbolInEquation = True
            
            constant = equation.constant

            if(not symbolInEquation):
                symbols.append(obj)
                
                if(not subtract):
                    coefficents.append(1)
                else:
                    coefficents.append(-1)
        
            return cls(symbols,coefficents=coefficents,constant=constant)
 
    @classmethod
    def fromEquationConstant(cls,equation,obj):
        
        symbols = []
        coefficents = []
        constant = 0

        if(isinstance(obj,int)):
            
            #For each symbol
            for i in range(len(equation.symbols)):
                #Add each symbol to this equation
                symbols.append(equation.symbols[i])
                coefficents.append(equation.coefficents[i])
            
            constant = equation.constant + obj

            return cls(symbols,coefficents=coefficents,constant=constant)

    def __add__(self,obj):
        
        if(isinstance(obj,Symbol)):
            return Equation.fromEquationSymbol(self,obj)
        
        if(isinstance(obj,int)):
            return Equation.fromEquationConstant(self,obj)
    
    def __sub__(self,obj):

        if(isinstance(obj,Symbol)):
            return Equation.fromEquationSymbol(self,obj,subtract=True)
        
        if(isinstance(obj,int)):
            return Equation.fromEquationConstant(self,-1*obj)

    def __str__(self):
        
        eqStr = ''

        for i in range(len(self.symbols)):
            
            currSym = self.symbols[i]
            currCoeff = self.coefficents[i]

            if(i > 0 and currCoeff >= 0):
                
                eqStr = eqStr + '+'
            elif(i > 0  and currCoeff < 0):
                eqStr = eqStr + '-'

            if(abs(currCoeff) != 1):
                eqStr = eqStr + str(currCoeff)

            eqStr = eqStr + str(currSym)
        
        #Will not print right if constant is the only term in Equation
        if(self.constant != 0):

            if(self.constant > 0):
                eqStr = eqStr + '+'
            else:
                eqStr = eqStr + '-'
            
            eqStr = eqStr + str(abs(self.constant))

        return eqStr
                

x = Symbol('x')
y = Symbol('y')
p = Symbol('x')

z = x + y
print(z) # x + y

z = z + p 
print(z) # 2x +y
z = z + 2
print(z+90) # 2x + y + 92
print(z) # 2x + y + 2
i = 1 
o = p + i
print(o+9) # x + 10
print(p+i+9) # x + 10
print(z+9) # 2x + y + 11
r = Symbol('r')
print(z - r)
print(z - 9)
print(x-y)
print(x + y - p)