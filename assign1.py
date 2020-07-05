#First method to find next 20 leap year whose sum of digist must be greater than 16

def next_leap_year(year):
    
    ls = []
    while len(ls) < 20:
        
        temp = year
        tot=0
        while(temp>0):
            
            dig=temp%10
            tot=tot+dig
            temp=temp//10
        
        pass
    
    
        if((year % 4 == 0 and year%100!=0) or year%400==0) and tot > 16:

            ls.append(year)
        year +=1    
    return ls    

print(next_leap_year(2020))



#Second method to find next 20 leap year whose sum of digist must be greater than 16

'''import calendar

def check_leap_year(year):
    
    ls = []
    while len(ls) < 20:
        
        temp = year
        tot=0
        while(temp>0):
            
            dig=temp%10
            tot=tot+dig
            temp=temp//10
        
        pass
    
    
        if calendar.isleap(year) and tot > 16:

            ls.append(year)
        year +=1    
    return ls  

print(check_leap_year(2020))'''

