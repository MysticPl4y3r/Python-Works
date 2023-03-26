fhandler=None

try:
    fhandler=open('ttt.txt','r')
    print(fhandler.readlines())
except IOError:
    print("Error opening file")
finally:
    if fhandler:
        fhandler.close()
    else:
        print("file does not exist")