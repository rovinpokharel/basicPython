try:
    file = open("testfile","w")
    try:
        file.write("Hello")
finally:
    print("     Biraj    ")
    file.close()
except IOError:
    print("Hi Biraj")