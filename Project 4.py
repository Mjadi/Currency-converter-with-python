
    
def change_To_Rupess(i1):
        return i1*60

    
def change_To_Euro(i1):
        return i1/1.20

    
def change_To_Pound(i1):
        return i1/0.71

    
def change_To_Yen(i1):
        return i1*109

i1=int(input('Enter the ammount: '))
i2=input('Enter the new currency: ')

if i2=='Rupess':
    print(change_To_Rupess(i1))

elif i2=='Euro':
    print(change_To_Euro(i1))

elif i2=='Pound':
    print(change_To_Pound(i1))

elif i2=='Yen':
    print(change_To_Yen(i1))

else:
    print('Enter a valid currency')
    



