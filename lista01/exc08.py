num1=int(input("digite um numero--> "))
num2=int(input("digite outro numero--> "))

while num2<num1:
	num1=int(input("digite um numero--> "))
	num2=int(input("digite outro numero--> "))
else:
	for i in range(num1,num2,1):
		lista = []
		lista.append(i)
		
		for i in lista:
			
		    print(i)
			temperature = float(input("Please enter temperature in fahrenheit:"))
            celsius = (temperature - 32) * 5 / 9
    print("Temperature in celsius: " , celsius)
		
    

# for i in range(n1, n2, 1):
#     print(i)
#     temperature = float(input("Please enter temperature in fahrenheit:"))
#     celsius = (temperature - 32) * 5 / 9
#     print("Temperature in celsius: " , celsius)