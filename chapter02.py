print("--------------------chapter01--------------------")
# 认识变量，使用变量

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)


print("--------------------chapter02--------------------")
# 字符串
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

favorite_language = ' python '
print(len(favorite_language))
print(len(favorite_language.rstrip()))
print(len(favorite_language.lstrip()))
print(len(favorite_language.strip()))

# 数字
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print(3 ** 2)

print(0.1 + 0.2)
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)