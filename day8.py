import sys

number = int(sys.stdin.readline().strip()) # same as input()but instead it's removing the white space in the end of beginning of each entry
dict1 = {}
for i in range(number):
    name_number = input()
    name_list = name_number.split(' ')
    dict1[name_list[0]] = name_list[1]

search_int = sys.stdin.readline().strip()

while search_int:
    phone_number = dict1.get(search_int)
    if phone_number:
        result = search_int + "=" + phone_number
        print(result)
    else:
        print("Not found")
    search_int = sys.stdin.readline().strip()
    
