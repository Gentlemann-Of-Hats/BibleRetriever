import requests
import sys

api_url = 'http://labs.bible.org/api/'
bibleBooks =[    'Genesis','Exodus','Leviticus','Numbers','Deuteronomy','Joshua','Judges','Ruth','1 Samuel','2 Samuel', '1 Kings','2 Kings','1 Chronicles','2 Chronicles','Ezra','Nehemiah','Tobit'
             ,'Judith','Esther','1 Maccabees','2 Maccabees','Job','Psalms','Proverbs','Ecclesiastes','Song of Songs','Wisdom','Sirach','Isaiah','Jeremiah','Lamentations','Baruch','Ezekiel',
             'Daniel','Hosea','Joel','Amos','Obadiah','Jonah','Micah','Nahum','Habakkuk','Zephaniah','Haggai','Zechariah','Malachi','The Gospels','Matthew','Mark','Luke','John',
            'Acts of the Apostles','Romans','1 Corinthians','2 Corinthians','Galatians','Ephesians','Philippians','Colossians','1 Thessalonians','2 Thessalonians','1 Timothy','2 Timothy','Titus',
            'Philemon','Hebrews','James','1 Peter','2 Peter','1 John','2 John','3 John','Jude','Revelation']

menuOptions = [1,2,3,4]
def main():
    print('[Main Menu]\n' , '1: return a specific bible passage \n', '2: Retrieve the verse of the day.\n', '3: Retrieve a random verse.\n', '4: Terminate program\n')
    usOption = int(input('Please enter a menu option: '))
    if usOption == 1:
        userPassage = input("Please type a passage, passages, or just a book (Ex. John 3:16): ")
        #Split it into list to check if the book is a proper book of the bible
        bookCheck = userPassage.split()
        if bookCheck[0] == 1 or bookCheck[0] == 2:
            bookCheck = bookCheck[0]+' '+bookCheck[1]
            if bookCheck not in bibleBooks:
                #print(bookCheck)
                wrongBookFunc()
        elif bookCheck[0] not in bibleBooks:
            wrongBookFunc()
        print('Requesting passage ', userPassage, '...')
        userPassage = userPassage.replace(' ', '+')
        #Debugging what went wrong
        #print('Requesting passage ', userPassage, '...')
        response = requests.get(api_url+'?passage='+userPassage+'&formatting=plain')
        print('\n'+response.text+ '\n')
        main()
    if usOption == 2:
        response = requests.get(api_url+'?formatting=plain'+'&passage=votd')
        print('\n'+response.text+ '\n')
        main()
    if usOption == 3:
        response = requests.get(api_url+'?formatting=plain'+'&passage=random')
        print('\n'+response.text+ '\n')
        main()
    if usOption == 4:
        sys.exit(0)
    if usOption not in menuOptions:
        print('\n\nplease select a valid option')
        main()

def wrongBookFunc():
    print('please type a book first')
    main()

if __name__ == "__main__":
    print('Hello, welcome to bible retriever! \n\n')
    main()
