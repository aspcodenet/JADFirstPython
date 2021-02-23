print("Vad heter du?")
namn = input()

print("Hur gammal är du?")
age =  int(input())

print("Hej ", namn)

if age > 48:
    print("Gamling")   
    print("hehe")   
else:
    print("Ungdom")   

for i in range(1,age):
    print("Varv ", i)
