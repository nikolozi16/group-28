# # 1) შექმენი სია ხილებზე და დაამატე მასში კიდევ 2 ხილი extend() ფუნქციით.
# list = ["vashli", "banani", "msxali", "fortoxali"]
# list1 = ["kivi", "sazamtro"]
# list.extend(list1)
# print(list)

# # 2) შექმენი სია numbers და დაამატე მასში [40, 50] extend()-ით.
# num = [1, 2, 3, 4, 5, 6, 7, 8]
# nums = [40, 50]
# num.extend(nums)
# print(num)

# # 3) შექმენი სია names და შეაბრუნე reverse()-ით.
# names = ["nika", "gio", "salome", "sandro","lika"]
# names.reverse()
# print(names)

# # 4) შექმენი სია სახელად nums და დათვალე რამდენი ცალი 5 არის მასში count()-ით.
# nums = [ 3, 4, 5, 6, 7, 6, 5, 4, 4, 5, 7, 8 , 9, 3 ,4 ,6 ,5,7,3,5,5]

# print(nums.count(5))

# # 5) შექმენი letters = ["a","b","a","c"] და დაბეჭდე რამდენი ცალი "a" არის ჩვენს სიაში.
# letters = ["a", "b", "a", "c"]
# print(letters.count("a"))

# # 6) შექმენი სია სახელად names და იპოვე "saba"-ს ინდექსი index()-ით.
# names = ["nika", "dato", "saba", "gio"]

# print(names.index("saba"))

# # 7) შექმენი list = ["red","green","blue"] და იპოვე რომელ ინდექსზე დგას "blue". გამოიყენე შესაბამისი ფუნქცია.
# list = ["red","green","blue"]
# print(list.index("blue"))

# # 8) შექმენი სია სახელად nums და დამატე მასში extend()-ით [7, 8, 9].
# nums = [1, 2, 3, 4, 5, 6]
# num = [7, 8, 9]
# nums.extend(num)
# print(nums)

# # 9) შექმენი სია სახელად foods და დააბრუნე შებრუნებული სია.
# food = ["kartofili", "xinkali", "mwvadi", "qababi", "kubdari", "xawapuri"]

# food.reverse()

# print(food)


# # 10) შექმენი სია cities და იპოვე რომელ ინდექსზე დგას "tbilisi".

# city = ["gurjaani", "axalcixe", "axalqalaqi","tbilisi", "rustavi", "telavi"]

# print(city.index("tbilisi"))

# # 11) შექმენი animals = ["cat","dog","cat","cow"] და დაითვალე ამ სიაში რამდენი "cat" არის.
# animals = ["cat","dog","cat","cow"]
# print(animals.count("cat"))

# # 12)შექმენი სია fruits = ["apple", "banana"] და append ფუნქციით დაამატე "grape". დაბეჭდე სია.
# fruits = ["apple", "banana"]
# fruits.append("grape")
# print(fruits)

# # 13)შექმენი სია numbers = [1, 2, 3] და extend()-ით დაუმატე [4, 5]. დაბეჭდე სია.
# numbers = [1, 2, 3]
# num = [4,5]
# numbers.extend(num)

# print(numbers)

# # 14)შექმენი სია names = ["goga", "saba"] და insert()-ით ჩასვი "luka" პირველ ინდექსზე. დაბეჭდე სია.
# names = ["goga", "saba"]
# names.insert(0,"luka")

# print(names)

# # 15)შექმენი სია items = ["pen", "pencil", "eraser"] და pop()-ით წაშალე ბოლო ელემენტი; დაბეჭდე განახლებული სია.
# items = ["pen", "pencil", "eraser"]
# items.pop(2)
# print(items)

# # 16)შექმენი სია colors = ["red", "green", "blue"] და remove()-ით წაშალე "green". დაბეჭდე შედეგი.
# colors = ["red", "green", "blue"]
# colors.remove("green")
# print(colors)

# # 17)შექმენი სია foods = ["bread", "milk"]. შეამოწმე სიაში 2 ელემენტია თუ მეტი — თუ ორია,
# #  append()-ით დაამატე "cheese", შემდეგ დაბეჭდე სია, სხვა შემთხვევაში append()-ით დაამატე "meat" და დაბეჭდე სია.
# foods = ["bread", "milk"]
# if len(foods) == 2:
#     foods.append("cheese")
# else:
#     foods.append("meat")

# print(foods)

# # 18)შექმენი სია nums = [10, 20, 30]. მომხმარებელს შემოატანინე მთელი რიცხვი.
# #  თუ რიცხვი nums სიაშია, დაბეჭდე "Already in list", თუ არა — append()-ით დაამატე 40 და დაბეჭდე სია.

# nums = [10, 20, 30]
# user = int(input("please enter number: "))

# if user in nums:
#     print("Already in list")
# else:
#     nums.append(40)

# print(nums)

# # 19)შექმენი სია letters = ["a", "b", "c"]. მომხმარებელს შემოატანინე ასო, 
# # შემდეგ insert()-ით ჩასვი ის სიის შუაში (ცენტრალურ ინდექსზე). დაბეჭდე სია.
# letters = ["a", "b", "c"]
# user = input("gtxovt shemoitanot aso: ")
# letters.insert(1,user)

# print(letters)

# # 20)შექმენი სია values = [1, 2, 3, 4]. მომხმარებელს შემოატანინე ინდექსი.
# #  თუ ინდექსი სიის ფარგლებშია, pop()-ით ამოშალე შესაბამისი ელემენტი; თუ არა, 
# # დაბეჭდე "Index out of range". ბოლოს დაბეჭდე სია.
# values = [1, 2, 3, 4]
# userr = int(input("please enter index: "))
# values.pop(userr)

# print(values)