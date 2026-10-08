import os




class Circuit: 
    def __init__(self):
        self.gates = {}
        
    def NAND(self, IN0, IN1): # basic gate to start with. this will allways 
        return int(not (IN0 and IN1))
    
    def AddGate(self, name, gate: function): # IN and OUT are for the amount of pins IN and OUT. not the actual pins. 
        self.gates[name] = gate
        return self.gates[name]
    
        
    
    
    
    
a = Circuit()
def NOT(a):
    x = int(not(a))
    return x

    
print(a.AddGate("test", NOT()))
