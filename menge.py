class Menge:
    def __init__(self):
        self.menge = []
        
    def show(self):
        print("{", end="")
        for el in self.menge[:-1]:
            print(el, end=", ")
        if len(self.menge)>0:
            print(self.menge[-1], end="")
        print("}")
        
    def isEmpty(self):
        return self.menge==[]
    
    def insert(self,el):
        if el not in self.menge:
            self.menge += [el]
    
    def remove(self,el):
        if el in self.menge:
            self.menge.remove(el)
            
    def part(self, el):
        if el in self.menge:
            return True
        else:
            return False
        
    def lang(self):
        return len(self.menge)
    
    def vereinigen(self,partner):
        neu=Menge()
        for i in range(len(partner.menge)):
            A.insert(partner.menge[i])
        for a in range(len(partner.menge)):
            A.insert(self.menge[i])
        return A
            
    def schnitt(self,partner):
        A = Menge()
        for i in range (len(self.menge)):
            if self.menge[i] in partner.menge:
                A.insert(self.menge[i])
        return A


    def potmenge(self):
        neu=Menge()
        for i in range 
    
    
            
    
    
    
    
    
    

        
A = Menge()
A.insert(6)
A.insert(7)
A.show()
A.remove(6)
A.show()
print(A.lang())
