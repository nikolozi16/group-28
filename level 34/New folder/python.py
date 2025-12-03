# # 1) მომხმარებელს შემოატანინე სიტყვა ანდა ტექსტი.  
# # -> გაიგე ამ სიტყვის/ტექსტის სიგრძე და დაპრინტე 
# # -> for ციკლით დაბეჭდე ამ სიტყვის თითოეული ასო ცალცალკე.
# num = input("shemoiyvanet teqsti: ")
# print(len(num),"sityvis sigrdze")
# for i in range(len(num)):
#     print(num[i])
    

# 2) შექმენით სია სადაც შეინახავთ სტრინგებს.
# for loop ით დაუარეთ სიის თითოეულ ელემენტს:
# 1. დაპრინტეთ რამდენი სიმბოლოსაგან შედგება სიტყვა
# 2. თუ სიტყვის სიგრძე არის: 
# --> კენტი დაპრინტეთ 'კენტია'
# --> ლუწი დაპრინტეთ 'ლუწია'

words = ["pantera", "niangi", "maimuni", "lomi", "mgeli", "spilo"]

for i in range(len(words)):
    word = words[i]
    length = len(word)
    print(word, "-", length)

    if length % 2 == 0:
        print("luwia")
    else:
        print("kentia")
