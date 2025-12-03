# 1)კომენტარის სახით ჩამოწერე თითეული სიის ფუნქცია რაც ვისწავლეთ და მიუწერეთ გვერდით ახსნა განმარტება
#  თუ რა გადაეცემა თითეულს და რას აკეთებს ის

# 2)შექმენი რიცხვების სია.
# append() ფუნქციით დაამატე მასში რიცხვი 10 ბოლოში.
# დაბეჭდე სია რომ ნახო ჩაემატა თუ არა

# list=[1,2,3,4,5,6,7,8,9]
# list.append(10)
# print(list)
# # 3)შექმენი სახელების სია.
# # append() ფუნქციით დაამატე შენი სახელი სიის ბოლოში
# # დაბეჭდე სია.

# name=["nika","gio","dato","lika","nino","daviti"]
# name.append("salome")
# print(name)

# # 4)შექმენი სია სადაც შეიყვან სახელებს,შენიდავალებაა მომხმარებელს შემოატანინო
# # რაიმე სახელი და შეინახო ცვლადში,შემდეგ ჩაამატე append()ის დახმარებით სიის ბოლოში
# #  მომხმარებლის შემოტანილი სიტყვა ~
# # დაბეჭდე სია რომნახო ჩაემატა თუ არა

# name1=["zaza","giorgi","daviti","mariami"]
# user_name=input("please enter your name: ")
# name1.append(user_name)
# print(name1)


# # 5)შექმენი სია სადაც შეიყვანთ 5 სახეკს
# # .insert() დახმარებით სიაში ჩაამატე მესამე ინდექსზე შენი სახელი

# name2=["shio", "cindela", "seirani", "zuka", "maqsime"]
# name2.insert(3,"nikolozi")
# print(name2)


# # 6)მომხმარებელს შემოატანინე სახელი და რიცხვი(integer 0 იდან 6 ჩათვლით)
# # შენი დავალებაა შექმნა სია მინიმუმ 6 ელემენტიანი
# # insert() დახმარებით დაამატე სიაში მომხმარებლის მიერ შემოტანილი 
# # რიცხვი,მომხმარებლის მიერ შემოტანილ ინდექსზე
# # მაგ:მომხმარებელმა სახელი შემოიტანა საბა და რიცხვი 4 , 
# # შენი დავალებაა რომ საბა დაამატო მეოთხე ინდექსზე(გამოიყენე ცვლადის
# #  სახელები იმიტომ რომ არ იცი მომხმარებელი რა მნშვნელობებს შემოიტანს
# # დაბეჭდე სია რომ ნახო ჩაემატა თუ არა

# name3=["ani","nini","nino","tazo","sandro","saba","gogalo"]
# user_name1 = input("please enter your name: ")
# user = int(input("please enter number 0, 6: "))
# name3.insert(user, user_name1)
# print(name3)


# # 7)შექმენი სია:

# # fruits = ["apple", "banana"]

# # insert() ფუნქციით ჩასვი "orange" 1 ინდექსზე.

# fruits = ["apple", "banana"]
# fruits.insert(1,"orange")
# print(fruits)


# # 8)შექმენი სია:

# # names = ["goga", "saba", "luka"]

# # insert()-ით ჩასვი "irakli" ბოლოს წინა პოზიციაზე ანუ ლუკას წინ

# names = ["goga", "saba", "luka"]
# names.insert(2, "irakli")
# print(names)

# # 9)შექმენი სია:

# # foods = ["bread", "milk", "cheese"]

# # insert() ფუნქციით ჩასვი "water" სიის დასაწყისში.

# foods = ["bread", "milk", "cheese"]
# foods.insert(0,"water")
# print(foods)

# # 10)შექმენი სია:numbers = [5, 10, 15]

# # pop() ფუნქციით წაშალე ბოლო ელემენტი და დაბეჭდე განახლებული სია.

# numbers = [5, 10, 15]
# numbers.pop(2)
# print(numbers)

# # 11)შექმენი სია:

# # fruits = ["apple", "banana", "orange"]


# # pop -ით ამოშალე "banana" და დაბეჭდე დარჩენილი სია.
# fruits = ["apple", "banana", "orange"]
# fruits.pop(1)
# print(fruits)


# # 12)შექმენი სია:

# # names = ["goga", "saba", "luka"]


# # ამოშალე "saba" pop()-ით  — შემდეგ დაბეჭდე სია რომ ნახო ამოიშალა თუ არა

# namess = ["goga", "saba", "luka"]
# namess.pop(1)
# print(namess)

# # 13)შექმენი სია:

# # colors = ["red", "green", "blue" , "yellow" , "black" , "purple"]

# # pop()-ით წაშალე "red" და დაბეჭდე განახლებული სია.

# # შემდეგ სიიდან ასევე ამოშალე yellow
# # დაბეჭდე სია და ნახე შედეგი
# colors = ["red", "green", "blue" , "yellow" , "black" , "purple"]
# colors.pop(0)
# print(colors)
# colors.pop(2)
# print(colors)

# # 14)მომხმარებელს შემოტანინე რიცხვი(0 იდან 4 მდე და შეინახე ცვლადში

# # შექმენი სია tems = ["pen", "pencil", "book", "eraser"] 

# # pop ის დახმარებით სიიდან ამოშალე მომხმარებლის მიერ შემოტანილ რიცხვზე(ინდექსზე) მდგომი ელემენტი

# userr = int(input("please enter number 0, 4: "))

# tems = ["pen", "pencil", "book", "eraser"]

# tems.pop(userr)
# print(tems)

# # 15)შექმენი სია:

# # fruits = ["apple", "banana", "orange"]


# # remove() ფუნქციით სიისდან წაშალე "banana".

# # დაბეჭდე სია ნახე ამოიშალა თუ არა

# fruits = ["apple", "banana", "orange"]
# fruits.remove("banana")
# print(fruits)

# # 16)შექმენი სია:

# # nums = [3, 5, 3, 7]

# # remove()-ით წაშალე 3 და დააკვირდი, მხოლოდ პირველი 3 იანი შაიშლება.

# # დაბეჭდე სია რომ დარწმუნდე
# nums = [3, 5, 3, 7]
# nums.remove(3)
# print(nums)

# # 17)შექმენი სია:

# # colors = ["red", "blue", "green"]


# # remove() ფუნქციით წაშალე "blue" და დაბეჭდე განახლებული სია.
# colors = ["red", "blue", "green"]
# colors.remove("blue")
# print(colors)


# # 18)შექმენი სია:

# # names = ["goga", "saba", "luka"]
# # მომხმარებელს შემოატანინე ამ სამიდან რომელიმე სახელი
# # შეინახე ცვლადში და remove()-ით წაშალე მომხმარებლის შემოტანილი სახელი სიიდან.
# # დაბეჭდე სია რომ გაიგო მართლა ამოიშალა თუ არა

# usser=input("please enter name: goga, saba, luka: ")
# names = ["goga", "saba", "luka"]
# names.remove(usser)
# print(names)

# # 19)შექმენი სია:

# # items = ["pen", "pencil", "book", "pencil"]


# # remove()-ით წაშალე "pencil" და დაბეჭდე დარჩენილი სია.

# items = ["pen", "pencil", "book", "pencil"]
# items.remove("pencil")
# items.remove("pencil")
# print(items)
