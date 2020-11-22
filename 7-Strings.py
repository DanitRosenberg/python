
message = 'Hello World'
print(message)
message2 = 'Hello Bobby\'s World'
print(message2)
message3 = """Hello
Bobby\'s
World"""
print(message3)
print(len(message3))
print(message3[0])
print(message3[0:5])
# From index number 6 to the end 
print(message3[6:])

print(message.lower())
print(message.upper())
print(message.count('Hello'))
#return the index
print(message.find('l'))

newMessage = message.replace('World','Universe')
print(newMessage)


a = 'Hello'
b = 'Danit'
message = '{},{}. Welcome!'.format(a,b)
print(message)

message = f'{a},{b.upper()}. Welcome!'

print(message)

#Show all the functions and the methods you available to 
print(dir(message))
#Here you can see help about the sting variable 
# print(help(str))
# print(help(str.lower))
