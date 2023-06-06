#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    #myfile = open("Test.txt","w+")
 
    # Open the file for appending text to the end
    myfile = open("Test.txt","a+")

    # write some lines of data to the file
    for i in range(10):
        myfile.write("Some new text\n")
    
    # close the file when done
    myfile.close()
    
    # Open the file back up and read the contents
    myfile=open("test.txt","r")
    if myfile.mode =="r":
    
       rl= myfile.readlines()
       for line in rl:
           print(line)
    
if __name__ == "__main__":
    main()
