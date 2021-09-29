file = open("alphab.txt", "r")

data = file.read().replace(" ","")


number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)