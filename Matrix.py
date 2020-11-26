import symbolsEquations

class Matrix:


    def __init__(self,matrixNumbers=[],variables={}):
        
        self.matrixNumbers = matrixNumbers
        self.variables = variables

    @classmethod
    def fromEquation(cls,equation):

        #Make sure the input is of type Equation
        if(not isinstance(equation,symbolsEquations.Equation)):
            return None
        
        matrixNumbers = []
        variables = {}
        cls.lastIndexVariables = 0
        
        matrixNumbers.append(equation.coefficents)


        #Add new entries into dict
        for i, x in enumerate(equation.symbols):
            variables[x.symbolName] = i
            cls.lastIndexVariables = i

        return cls(matrixNumbers=matrixNumbers,variables=variables)

    def addEquation(self,equation):
        
        #Make a new empty row the size of all the others
        newRow = [0 for i in range(self.lastIndexVariables+1)]

        newVariables = []

        #For every variable in the incoming equation
        for i,x in enumerate(equation.symbols):

            #If the symbol is already in the matrix
            if(x.symbolName in self.variables):
                 
                #Add the coefficent to the correct index in row
                newRow[self.variables[x.symbolName]] = equation.coefficents[i]
            
            #Else it is not in the equation
            else:
                #Store symbol and index position
                newVariables.append([x,i])
        
        #For every tuple in new variables
        for newVar in newVariables:

            #Increment the lastIndexVariable
            self.lastIndexVariables = self.lastIndexVariables + 1

            #Add the symbol and column number in dictionary
            self.variables[newVar[0].symbolName] = self.lastIndexVariables
            
            #Make a new entry for all previous rows
            self.appendToAllRows(0)
            
            #Append to newRow
            newRow.append(equation.coefficents[newVar[1]])

        #Add the row to the bottom of matrix
        self.matrixNumbers.append(newRow)

    def appendToAllRows(self,num):

        for row in self.matrixNumbers:
            row.append(num)

    def __str__(self):

        matrixStr = ''

        matrixStr = matrixStr + str(list(self.variables.keys())) + '\n'

        for row in self.matrixNumbers:

            matrixStr = matrixStr + str(row) + '\n'

        return matrixStr



x = symbolsEquations.Symbol('x')
y = symbolsEquations.Symbol('y')
r = symbolsEquations.Symbol('r')

z = Matrix.fromEquation(x+y)
z.addEquation(x+y+r)
print(z)