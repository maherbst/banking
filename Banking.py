print('Welcome to Coastal Carolina Bank and Trust!\n')


 
bal=float(input('Please enter an initial balance: '))
rate=float(input('Please enter an interest rate: '))
years=int(input('Please enter the number of years to calculate: '))

def compute_compound_interest(bal,years,rate):
    return bal * (((1 + (rate/(100.0))) ** (years)))
amount = round(compute_compound_interest(bal,years,rate))
compound_interest=amount-bal;
print('After %d year(s) your balance will be $' % years,amount)


    
   
    
    



    
