num = 1
string = '1'
num2 = int(string)
print(num + num2)

words = 'words ' * 3
print(words)

word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num) #等价于字符串'bang！' * 4
print(total)

name = 'My Name is Mike'
print(name[0])
'M'
print(name[-4])
'M'
print(name[11:14]) #from 11th to 14th,14ht one is excluded
'Mik'
print(name[11:15]) #from 11th to 15th, 15th one is excluded
'Mike'
print(name[5:])
'me is Mike'
print(name[:5])
'My Na'

word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends)

url = 'http://ww1.site.cn/14d2e8ejwlexjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
print(file_name)

phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[5:8],'*' *4)
print(hiding_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(search + ' is at ' + str(num_a.find(search)) +
      ' to ' + str(num_a.find(search) + len(search))+ ' of num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to ' + str(num_b.find(search)
      +  len(search)) +' of num_b')

print('{} a word she can get what she {} for.'.format('With','came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition
        = 'With',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('With','came'))
