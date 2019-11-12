def main():
    # file = open("lco.txt", "a+")
    # for i in range(20):
    #     file.write("Python course going on\n")
    # file.close()
    file = open("lco.txt", "r")
    if file.mode == 'r':
        filecontent = file.read()
        print(filecontent)



if __name__ == "__main__":
    main()


