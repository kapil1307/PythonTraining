chartest = input(" Enter value :")
temp = ''
change = False
for i in range(len(chartest)):
    if (chartest[i] != "$" and change == False ):
        temp = temp + chartest[i]
    else:
        temp = temp + "$"
        change = True
print(temp)
