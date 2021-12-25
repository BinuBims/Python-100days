# print([n+n for n in range(1,5)])

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name)<5]
print(short_names)

capilatalized_name = [name.upper() for name in names]
print(capilatalized_name)