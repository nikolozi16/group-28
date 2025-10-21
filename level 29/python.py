# 1)მოცემულია სტრინგი "PythonProgramming".
# ამოიღე პირველი 6 სიმბოლო და დაბეჭდე გამოიყენეთ slicing
name=["PythonProgramming"]
print(name[0][0:6:])

# 2)მოცემულია სია numbers = [10, 20, 30, 40, 50, 60, 70].
# ამოიღე მხოლოდ შუა 3 ელემენტი და დაბეჭდე გამოიყენეთ slicing (მინუს ინდექსებითაც)
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[2:-2:])
# 3)მოცემულია სტრინგი "HelloWorld".
# დაბეჭდეთ Hello ტერმინალში slicing ის გამოყენებით (მინუს ინდექსებითაც)
str=["Helloworld"]
print(str[0][-10:-5:])
# 3)მოცემულია სია letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'].
# დაბეჭდე ყოველ პირველი მესამე მეხუთე ელემენტები გამოიყენეთ indexing (მინუს ინდექსებითაც)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-7::2])
# 4)მოცემულია სტრინგი "Information".
# ამოიღე "forma" ნაწყვეტი slicing-ით (მინუს ინდექსებითაც)
info=["Information"]
print(info[0][-9:7:])
# 5)
# მოცემულია სტრინგი "abcdefghijklmno".
# შექმენი სამი სხვადასხვა სლაისი:
anbani=["abcdefghijklmno"]
print(anbani[0][0:1:])
print(anbani[0][1:2:] + anbani[0][0:1:] + anbani[0][3:4:])
print(anbani[0][3:4:]+ anbani[0][-1::] + anbani[0][6:7:])

