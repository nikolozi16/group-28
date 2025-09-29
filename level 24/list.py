# # 1)შექმენი სია 7 რიცხვით.
# # დაბეჭდე პირველი და ბოლო ელემენტების ნამრავლი ისე, რომ ორივეჯერ უარყოფითი ინდექსი გამოიყენო.
# # დაბეჭდე მესამე ელემენტი მარცხნიდან და მესამე ელემენტი მარჯვნიდან (უარყოფითიინდექსის გამოყენებით).
# num =[1,2,3,4,5,6,7]
# print(num[-7]*num[-1])
# print(num[2])
# print(num[-5])

# # 2)შექმენი სია "apple", "banana", "cherry", "grape", "kiwi", "orange".
# # დაბეჭდე შუა 2 ელემენტი (ორივე(დადებითი და უარყოფითი)) ინდექსით.

# product = ["apple", "banana", "cherry", "grape", "kiwi", "orange"]
# print(product[2])
# print(product[3])
# print(product[-3])
# print(product[-4])

# # 3)
# # შექმენი [3,4,5,6,7,1,2,9,8,11]
# # მომხმარებელს შემოატანინე ერთი ინდექსი(რიცხვი) 0 დან 10 მდე.
# # თუ მომხმარებლის ინდექსი დადებითია → დაბეჭდე ის ელემენტი
# # თუ უარყოფით რიცხვი ან  10 ზე მეტი მაღალირიცხვი შემოიყვანა დაბეჭდეთ --> "you entered negative or more than 10  number "

# number =[3,4,5,6,7,1,2,9,8,10]
# momxmarebeli = int(input("please enter 0, 10 numbers: "))
# if momxmarebeli in number:
#     print(momxmarebeli)
# else:
#     print("you entered negative or more than 10  number ")

# 4)შექმენით სია ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]
# --- მინუს ინდექსების გამოყენებით შეადგინეთ შემდეგი წინადადება და დაბეჭდეთ --> "dog is running in forest very fast"
# --- აასწყვეთ ზემოთ მოცემული წინადადება ოღონდ დადებითი ინდექსებით
# --- დადებით ინდექსების გამოყენებით ააწყვეთ შემდეგი წინადადება ---> "cat is very angry"

# list = ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]
# print(list[-11],list[-9],list[-7],list[-4],list[-6],list[-1],list[-5])
# print(list[0],list[2],list[4],list[7],list[5],list[10],list[6])
# print(list[8],list[2],list[10],list[3])

# # 5)
# # შექმენი სია ცხოველებით: ["dog", "cat", "horse", "cow", "sheep", "goat"].
# # მომხმარებელს შემოიტანინე ინდექსი(რიცხვი)
# # თუ მომხმარებლის მიერ შემოყვანილ ინდექსზე მდგომი ელემენტი არის  "cat", დაბეჭდე "შენ აირჩიე კატა".
# # თუ არის "goat", დაბეჭდე "შენ აირჩიე თხა".
# # სხვა შემთხვევაში დაბეჭდე "სხვა ცხოველი აირჩიე".

# animals = ["dog", "cat", "horse", "cow", "sheep", "goat"]
# archeva = int(input("please enter 0, 5 number: "))

# if 0 <= archeva < len(animals): 
#     print("shen airchie " + animals[archeva])
# else:
#     print("sxva cxoveli airchie")


# # 6)
# # შექმენი სია 6 ქალაქით.
# # მომხმარებელი შემოიტანს ორ ინდექსს(რიცხვს).
# # თუ პირველი ინდექსი ნაკლებია მეორეზე → დაბეჭდე ამ ინდექსებზე მდგომი ორივე ელემენტი.
# # თუ მეორე ნაკლებია პირველზე → დაბეჭდე "შეცვალე ინდექსები ადგილებით"--->ზემოთ თუ დაპრინტე a და b ამ შემთხვევაში დაპრინტე b და a.
# # თუ ინდექსები ერთნაირია → დაბეჭდე "ორივე ერთია" და გამოიტანე ამ ინდექსზე მდგომი ელემენტი ვთქვათ თუ 
# # შემოიყვანა მომხმარებელმა 5 და 5 დაუბეჭდე მე 5 ინდექსზე მდგომი ელემენტი.

# city = ["tbilisi", "gurjaani", "telavi", "signagi", "axalcixe", "axalqalaqi"]

# num1 = int(input("please enter 0, 5-numbers: "))
# num2 = int(input("please enter 0, 5-numbers: "))

# if num1 < num2:
#     print(city[num1], city[num2])
# elif num1 > num2:
#     print("shecvale indexebi adgilebit")
#     print(city[num2], city[num1])
# else:
#     print("orive ertia")
#     print(city[num1])

# # 7)მომხმარებელი შემოიტანს სიტყვას.
# # თუ პირველი ასო "a"-ა → დაბეჭდე "სიტყვა იწყება a-თი".
# # თუ ბოლო ასო "z"-ია → დაბეჭდე "სიტყვა მთავრდება z-ით".
# # სხვაგვარად → დაბეჭდე "სიტყვა არც a-თი იწყება და არც z-ით მთავრდება".

# word = input("შეიყვანე სიტყვა: ")

# if word[0] == "a":
#     print("sityva iwyeba a-ti")
# elif word[-1] == "z":
#     print("sityva mtavrdeba z-ti")
# else:
#     print("sityva arc a-ti iwyeba da arc z-ti mtavrdeba")


# # 8)დავალება 4
# # მომხმარებელი შემოიტანს სიტყვას.
# # თუ პირველი და ბოლო ასო ერთმანეთს ემთხვევა → დაბეჭდე "პირველი და ბოლო ერთნაირია".
# # თუ განსხვავდება → "პირველი და ბოლო განსხვავებულია".

# name = input("შეიყვანე სიტყვა: ")

# if name[0] == name[-1]:
#     print("პირველი და ბოლო ერთნაირია")\
# else:
#     print("პირველი და ბოლო განსხვავებულია")



# 9)შექმენი ცვლადი სადაც შეინახავთ შემდეგ ასოებს ---> "agivorsbgitr"
 
# ----ამ სიიდან შეადგინე სიტყვა "goga, 
# ----ამ სიტყვიდან შეადგინე სიტყვა "saba"
# ----ამ სიტყვიდან შეადგინე სიტყვა "bativar"

# cvladi = ["a","g","i","v","o","r","s","b","g","i","t","r"]

# print(cvladi[1] + cvladi[4] + cvladi[1] + cvladi[0])
# print(cvladi[-6] + cvladi[0] + cvladi[-5] + cvladi[0])
# print(cvladi[-5] + cvladi[0] + cvladi[-2] + cvladi[-3] + cvladi[3] + cvladi[0] + cvladi[-1])



# # 10)შექმენი შემდეგი სტრინგი --> 'giorgi'
# # შენი დავალებააა რომ for დდა while loop ის დახმარებით გამოიტანო ამ სტრინგის თითეული ასო ცალ ცალკე

# name = "giorgi"

# for i in range(len(name)):
#     print(name[i])
# num = 0
# while num < len(name):
#     print(name[num])
#     num += 1


# 11)გადახედეთ რესურსებს!!!!!!!!!!!!!!!!!!!!!