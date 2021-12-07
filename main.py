patskani = ['a', 'ā', 'e', 'ē', 'i', 'ī', 'o', 'u', 'ū']
teikums = input("Ievadiet tekstu: ")
count = 0
for letter in teikums:
    if letter in patskani:
        count += 1
print(count)