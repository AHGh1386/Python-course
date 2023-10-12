# phone book
phone_book = {
    "John Doe": "09111234562",
    "Jane Smith": "09359876543",
    "Alice Johnson": "09114567894",
    "Bob Thompson": "09357891233",
    "Emily Davis": "09112461358",
    "Michael Wilson": "09351352496",
    "Sarah Anderson": "09115793507",
    "David Clark": "09353575789",
    "Olivia Baker": "09118246850",
    "Daniel Green": "09356808244",
    "Sophia King": "09114682436",
    "William Lee": "09352464681",
    "Mia Miller": "09113575799",
    "Joseph Hill": "09355793576",
    "Grace Adams": "09112461357",
    "Andrew Parker": "09351352465",
    "Elizabeth Stewart": "09115793570",
    "Matthew Turner": "09353575749",
    "Ava Bennett": "09116808234",
    "Anthony Morgan": "09358246820",
    "Chloe Cook": "09112464628",
    "Christopher Reed": "09354682426",
    "Victoria Scott": "09115793574",
    "Ryan Phillips": "09353575795",
    "Ella Young": "09111352466",
    "Benjamin Hall": "09352461359",
}

while True:
    option = input(
        "Please Choose an option (add to add a new number / src to search a number) :").lower()
    if option == "add":
        while True:
            name_to_add = input("Please enter a name: ")
            number_to_add = input("Please enter a number: ")
            if name_to_add != "" and number_to_add.isnumeric():
                phone_book[name_to_add] = number_to_add
                print("Your Contact number successfully Saved!")
                break
            else:
                print("Wrong name or phone number. Please retry!")
                retry = input("Type 'c' to continue or 'e' to exit: ")
                if retry == "e":
                    break
                else:
                    pass
    elif option == "src":
        while True:
            print("You can 'exit' by typing exit")
            name_to_search = input("Please enter a Name to search: ")
            if name_to_search != "" and name_to_search.lower() != "exit":
                result = [f"{key} :  {value}" for key,
                          value in phone_book.items() if name_to_search in key]
                for num in result:
                    print(num)
            elif name_to_search.lower() == "exit":
                break
            else:
                print("Not Found! Try again.")
    else:
        print("Firstly, select an option (add or src)"
