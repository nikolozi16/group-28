num_1 = int(input("შემოიყვანე პირველი რიცხვი: "))
num_2 = int(input("შემოიყვანე მეორე რიცხვი: "))
num_3 = int(input("შემოიყვანე მესამე რიცხვი: "))

if num_1 == num_2 == num_3:
    print("სამივე ტოლია")

elif num_1 == num_2:
    print("1 და 2 ტოლია")
elif num_1 == num_3:
    print("1 და 3 ტოლია")
elif num_2 == num_3:
    print("2 და 3 ტოლია")

else:
    print("არცერთი არ არის ტოლია")
