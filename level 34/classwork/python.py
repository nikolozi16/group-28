# # 1) შექმენით სია სადაც შეინახავთ სხვადასხვა ქალაქების სახელებს.  
# #    for loop ით დაბეჭდეთ მხოლოდ ის ქალაქები, რომელთა სახელის სიგრძე მეტია 6-ზე.

# city = ["tbilisi", "batumi", "gurjaani", "signagi", "axalcixe", "axalqalaqi", "gori"]
# for i in range(len(city)):
#     if len(city[i]) > 6:
#         print(city[i])

# # 2) შექმენით სია სხვადასხვა სიტყვებით.  
# # -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად იყოფა 15-ზე.
# list = ["tvitmfrinavi", "eleqtrosadgurii","mtversasruti"]
# for i in range(len(list)):
#     if len(list[i]) % 15 == 0:
#         print(list[i])

# # 3) შექმენით სია რიცხვებით.  
# # -> გამოიყენეთ for loop რათა დათვალოთ რამდენი რიცხვია სიაში.  
# # -> არ გამოიყენოთ len() — დაითვალეთ ხელით.
# num = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
# sum = 0
# for i in range(0, len(num)):
#     sum += 1
# print(sum)

# # 4) შექმენით სია სხვადასხვა სიტყვებით.  
# # -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად 5 სიმბოლოა.
# name = ["nikolozi", "giorgi", "sandro", "maqsi","paata"]
# for i in range(len(name)):
#     if len(name[i]) % 5 == 0:
#         print(name[i])

# 5) მომხმარებელს შემოატანინე წინადადება.  
# -> გაიგე რამდენი სიმბოლოა წინადადებაში.  
# -> for ციკლით დათვალე რამდენი აso "a" ან "A" არის ტექსტში.

# user = input("gtxovt shemoiyvanot winanadeba: ")
# print(len(user))
# aso = 0
# for i in range(len(user)):
#     if user[i] == "a" or user[i] == "A":
#         aso+=1
# print(aso)

# 6) <= Boss Level =>
# შექმენით სია სადაც შეინახავთ სხვადასხვა სტრინგებს.
# --> დაპრინტეთ ამ სიიდან ყველაზე გრძელი სტრინგი
string = ["leopardi", "gorila", "niangi", "jirafi"]
grdzeli = ""
for i in range(len(string)):
    if len(string[i]) > len(grdzeli):
        grdzeli = string[i]
print(grdzeli)