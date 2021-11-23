# Множества
names = ['Иван', 'Анна', 'Игорь', 'Иван' , 'Сергей', 'Анна']
for name in names:
    if names.count(name) == 1:
        print(name)

unique_names = set()
repeated_names = set()
for name in names:
    if name in repeated_names:
        continue
    if name in unique_names:
        repeated_names.add(name)
        unique_names.discard(name)
        continue
    unique_names.add(name)
print(unique_names)  # отличительное свойство множества
print([name for name in names if name in unique_names])

names = {'Иван', 'Анна', 'Игорь', 'Иван', 'Сергей', 'Анна'}
print(names)
