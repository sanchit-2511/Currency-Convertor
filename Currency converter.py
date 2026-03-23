curr_data = open('CurrencyData.txt')
lines = curr_data.readlines()

currencyDict = {}
for line in lines:
	data = line.split("\t") 
	currencyDict[data[0]] = data[1]
'''Here the "split('\t')" divides text wherever it sees "\t".
e.g.,text="apple\tbanaa\torange"
result=text.split('\t') & print(result)
Output: ['apple','banana','orange'] '''
	
amount = int(input("Enter the amount you want to convert:-\n")) 
#Here the data contains no. of lines separated by 'enter' and by splitting '\n', it will create list of character separated by ','.
print("Enter the name of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Enter one of these above values you want to convert into:- \n")
print(f"Your {amount} INR is equal to {amount *float(currencyDict[currency])} in {currency}")