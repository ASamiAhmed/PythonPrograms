my_library = {
    "fiction":{
        "A":"comedy",
        "B":"graphic novel",
        "C":"science fiction",
        "D":"historical fiction",
    },
    "non_fiction":{
        "E":"history and geography",
        "F":"arts",
        "G":"science and technology",
        "H":"others",}
}
user_input =input('''Which type do you want to select? 
Press 1: Fiction
Press 2: Non_fiction
Press 0: Exit... 
 ''')

if (user_input == "1"):
    category_select=input('''Which category do you want?
     comedy
     graphic novel
     science fiction
     historical fiction
   ''' ).lower() 
    for k,v in my_library["fiction"].items():
        if v==category_select:
            print(k)
elif (user_input == "2"):
    category_select=input('''Which category do you want?
     history and geography
     arts
     science and technology
     others
     ''').lower()
    for k,v in my_library["non_fiction"].items():
        if v==category_select:
            print(k)
else:
    exit()       