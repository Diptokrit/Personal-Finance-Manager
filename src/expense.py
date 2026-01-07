class Expense:
    #__init__ is the constructor which automatically excecutes whenever we create an expense object
    #For example: exp = Expense(200, "Food", "2024-01-01", "Snacks")

    def __init__(self,amount , category , date , description):
        
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description
    #dunder method or the magic method
    def __str__(self):
       return f" Date:{self.date} | Category: {self.category}  Rs: {self.amount:.2f} - {self.description}"

# Convert the expense object into a list for saving into csv
    def to_row(self):  
        return [self.date , self.category , self.amount , self.description]

# Covert rows into an Expense object 
#  row = [date, category, amount, description] 

#for making objects using classes from csv files
    @classmethod 
    def from_row(cls , row):
#multi packing stores 4 parameters seperately from the row
        date , category , amount , description = row
        
        #creates objects 
        return cls(amount , category , date , description)
#exp1 = Expense(200 , "Food" , "2024-01-01","Snacks")
#exp2 = Expense(500 , "Gaming" , "2025-12-22" , "Assasins Creed")
    
#print(exp1)
#print(exp2)

