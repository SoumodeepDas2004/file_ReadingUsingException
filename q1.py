def readfile(filename):
    with open(filename,'r') as f:
        print(f"\n{filename} file opened\n")
        print(f.read())
    

if __name__=='__main__':
    n=input("write file name with extension\n")
    try:
        readfile(n)
    except:
        print("file not found \nENTER CORRECT NAME\n")
        exit()
    else:
        print("\nfile found\n")
    finally:
        print("Program Executed \n  & Thank you\n")
