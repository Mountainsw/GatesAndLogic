


# define 

class gate:
    def __init__(self, inputs, outputs):
        self.inputs = []
        self.outputs = []
        
        
        
class NANDgate(gate): # starting gate
    def __init__(self, IN, inputs: list): 
        if len(inputs) > IN: raise TypeError
        self.inputs = inputs
        self.outputs = int(not (int(self.inputs[0]) and int(self.inputs[1])))
     
    def eval(self):
        return self.outputs
    
    
test = [1,1]
print(NANDgate(2, test).eval())