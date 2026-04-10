mes = int(input("Ingrese numero del mes: "))
year = int(input("Ingrese año: "))

no_bisiesto=(year % 4 != 0 or (year%100==0 and year%400!=0))

if(mes==2):
    if no_bisiesto:
         print("Tiene 28 dias")
    else:
         print("Tiene 29 dias")
        
elif(mes in (4,6,9,11)):
    print("Tiene 30 dias")
else:
    print("Tiene 31 dias")
    