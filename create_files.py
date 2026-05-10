with open('test.txt', 'a') as file:
    files=file.writelines(['hello there2','\nhows it going'])
    print(files)
