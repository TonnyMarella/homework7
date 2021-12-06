def greetings():
    myName = "Артём"
    name = str(input("Укажите ваше Имя, если хотите пропустить нажмите Enter\n"))
    if name == '':
        print("Приветствую", myName)
    else:
        print("Приветствую", name)

greetings()