# 2) კომენტარების სახით თავიდან ახსენით რა არის conditional statement, რა დანიშუნლება გააჩნიათ და როგორი სახის განცხადებები გვაქვს.
#  Conditional statement ეს არის პროგრამირების კონსტრუქცია რომელიც განსაზღვრავს,
# #  თუ რომელი კოდი უნდა შესრულდეს მოცემული პირობის მიხედვით.


# 3) for ციკლის მეშვეობით გამოიტანეთ "hello world" 50-ჯერ.
for i in range(51):
    print("hello world")

# 4) while ციკლის მეშვეობით გამოიტანეთ რიცხვები 3-დან 17-ის ჩათვლით.
num = 3
while num <= 17:
    print(num)
    num += 1

# 5) მომხმარებელს შემოატანინეთ პაროლი, შემდეგ კი შედეგი შეინახეთ ცვლადში.
#  შექმენით პირობა თუ ის უდრის "1234"-ს დაბეჭდეთ "Password is correct",
#  სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect".
password = 1234
paroli = input("your password ")
if paroli == password:
    print("password is correct")
else:
    print("password is incorrect")

# 6) შექმენით ცვლადი სადაც შეინახავთ მომხმარებლის მიერ შემოყვანილი ცხოველის სახეობას.
#  თუ სახეობა უდრის "ძაღლი" დაბეჟდე "woaf! woaf!", სხვა შემთხვევაში "შენ არ გყავს ძაღლი"
dog = "dog" 
animals = input("Your favorite animal ")
if animals == dog:
    print("woaf! woaf!")
else:
    print("shen ar gyavs dzagli")

# 7) უყურეთ შემდეგ ვიდეო წყაროსს:

# -- https://youtu.be/FvMPfrgGeKs --