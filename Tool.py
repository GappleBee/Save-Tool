print("Welcome to the Save Tool!\n")

def write():
  while True:
    info = input('Enter the data you want to put into the new text file: (Type "/exit fileInput" to stop writing to the new text file) ')
    if info != "/exit fileInput":
      file.write(info + "\n")
    else:
      print("\n")
      break

while True:
  print("1) Create a new text file")
  print("2) Add to the end of a new text file")
  print("3) Read from a text file")
  print("4) Find a row(s) in a text file")
  selection = int(input('Enter a selection: (Enter "5" to exit) '))
  print("\n")
  
  if selection == 1:
    name = input("Enter the name for the new text file: ")
    name += ".txt"
    file = open(name, "w")
    write()
    file.close()

  elif selection == 2:
    name2 = input("Enter the name of the text file you would like to add data to the end to: ")
    name2 += ".txt"
    file = open(name2, "a")
    write()
    file.close()

  elif selection == 3:
    name3 = input("Enter the name of the text file you would like to read from: ")
    name3 += ".txt"
    file = open(name3, "r")
    print(file.read())
    file.close()
  
  elif selection == 4:
    name4 = input("Enter the name of the text file you would like to find things from: ")
    name4 += ".txt"
    file = open(name4, "r")
    find = input("Enter the data you would like to find from this file: ")
    for row in file:
      if find in row:
        print('Found row from "' + find + '":')
        print(row)
    file.close()

  elif selection == 5:
    print("See you later!")
    break
  
  else:
    print('Invalid selection! Type "5" if you would like to exit')
