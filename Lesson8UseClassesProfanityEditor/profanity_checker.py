def read_text():
    quotes = open("/Users/subha/Desktop/UdacityFullStackWebDevelopment/Lesson8UseClassesProfanityEditor/profanity.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text() 
