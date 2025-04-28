class car:
 def __init__(self,make,color,year,model):
    self.make=make
    self.color=color
    self.year=year
    self.model=model
 def drive1(self):
   print("The "+self.model+" is driving.")
 def stop1(self):
    print("This "+self.model+" is stopped.")
 def drive2(self):
    print("The "+self.model+" is over speed.")
 def stop2(self):
    print("This "+self.model+" is engine off.")


