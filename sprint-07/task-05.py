class LeafElement: 
  
    def __init__(self, *args): 
  
        ''''Takes the first positional argument and assigns to member variable "position".'''
        self.position = args[0]
  
    def showDetails(self, sub=0): 
  
        '''Prints the position of the child element.'''
        print("\t" * sub + self.position)

    def __str__(self):
        return self.position
  
  
class CompositeElement: 
  
    def __init__(self, position, *args): 
  
        '''Takes the first positional argument and assigns to member 
         variable "position". Initializes a list of children elements.'''
        self.position = position
        self.children = []
  
    def add(self, child): 
  
        '''Adds the supplied child element to the list of children 
         elements "children".'''
        self.children.append(child)
  
    def remove(self, child): 
  
        '''Removes the supplied child element from the list of 
        children elements "children".'''
        if child in self.children:
            self.children.remove(child)
  
    def showDetails(self, sub = 0): 
  
        '''Prints the details of the component element first. Then, 
        iterates over each of its children, prints their details by 
        calling their showDetails() method.'''

        print("\t" * sub + self.position)
        
        for child in self.children:
            child.showDetails(sub + 1)

    def __str__(self):
        return self.children


if __name__ == '__main__':

    topLevelMenu = CompositeElement("GeneralManager")

    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")

    subMenuItem11 = LeafElement("Developer11")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer22")

    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)

    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem22)

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)

    topLevelMenu.showDetails()
    