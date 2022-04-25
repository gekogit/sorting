import os

def save (filename,content):
    if os.path.isfile(filename):
        with open(filename, 'w') as fopen:
            while True:
                answer=str(input(f"File  {filename} already exist . Overwride this file? Y/N: "))
                if answer=='Y':
                    #with open(filename, 'w') as fopen:
                    fopen.write(content)
                    break
                elif answer=='N':
                    print(f"File {filename} wasn't save ")
                    break
                else:
                    print ("Incorrect answer. Try again")
    else:
        with open(filename, 'w') as fopen:
            print (f"Save to file {filename}")
            fopen.write(content)
