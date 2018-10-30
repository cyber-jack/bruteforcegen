import sys, itertools

def bruteForce(length): #Generates a brute force word list
    charset = input('Enter character set without any spaces or enter 1 for default -->')
    if (charset == '1'):
        charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&()*+,-./:;<=>?@[\]^_`{|}~ '
    file = open('wordlist.txt', 'w')
    print ('This will take a while...')
    dict = itertools.product(charset, repeat=length) #Length is the length of your result.
    for i in dict: 
        file.write(''.join(i) + '\n')
    print ('Done!')
    file.close()

def modFile(oldDic): #Modifies already existing wordlist
    chars = [str(x) for x in input('Please enter letter(s) separated by a comma -->').split(',')]
    old = open(oldDic, 'r')
    oldList = []
    for line in old.readlines():
        oldList.append(line.rstrip())
    old.close()
    file = open('newDictionary.txt', 'w')
    for x in oldList:
        file.write(x+'\n')
        for y in chars:
            file.write(x+y+'\n')
    file.close()
    

def help():
    print("\nWelcome to Python dictionary generator.\nPlease use responsibly and in a lawful matter")
    print("Usage:\n-b specifies length of new brute force dictionary\n-m edits existing dictionary")
    sys.exit('[+] Exiting...\n')

def main():
    #Handles arguments
    if(len(sys.argv) < 2):
        print('\n[+] Missing argument')
        help()
    elif (sys.argv[1] == '--help' or sys.argv[1] == '-h'):
        help()
    if(sys.argv[1] == '-b' and len(sys.argv) < 3):
        length = input('Enter length -->')
        bruteForce(int(length))
    elif(sys.argv[1] == '-m' and len(sys.argv) < 3):
        oldDic = input('Please enter dictionary path -->')
        modFile(oldDic)
    elif(sys.argv[1] == '-m' and len(sys.argv) == 3):
        oldDic = sys.argv[2]
        modFile(oldDic)
    else:
        length = sys.argv[2]
        bruteForce(int(length))
    

if __name__ == '__main__':
    main()
