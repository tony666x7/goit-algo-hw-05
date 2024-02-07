contacts = {}  # Словник для зберігання контактів (ім'я: номер телефону)

def input_error(func):
    # Декоратор для обробки ValueError
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Будь ласка, введіть коректні дані.\n\
В форматі \"Команда\" \"Им'я\" \"номер\"\n"
        
    return inner

def handle_error(func):
    # Декоратор для обробки помилок при видаленні
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не існує.\
Будь ласка введіть існуючий контакт.\n"
        except ValueError:
            return "Контакт не існує.\
Будь ласка введіть існуючий контакт.\n"

    return wrapper

def parse_input(user_input):
     # Функція для розбору введеного користувачем рядка на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
     # Додає контакт у словник
    name, phone = args
    contacts[name] = phone
    return f"Контакт {name} додано\n"
    
@input_error   
def change_contact(args, contacts):
    # Змінює номер телефону для існуючого контакту
    name, phone = args
    contacts[name] = phone
    return f"Контакт {name} змінено\n"
    
def show_contact():
     # Виводить усі збережені контакти
    if contacts:
        result = "Всі збережені контакти: \n"
        for name, phone in contacts.items():     
            result += f"{name}: {phone}\n"
        return result
    else:
        return "Немає збережених контактів\n"

@handle_error    
def delete_contact(args, contacts):
    # Видаляє вказанний контакт
    name, = args
    phone = contacts.pop(name)
    return f"Контакт {name} видалено\n"
    
def main():
    
    # Основний цикл функції
    print("Вітаю! Я віртуальний помічник\n\
          \n\t\t Меню\
          \nКоманда \t\t-> \tДія\n\
          \nHello \t\t\t-> \tПривітання\
          \nadd 'name', 'phone' \t-> \tДодати контакт до списку\
          \nchange 'name', 'pnone' \t-> \tЗамінити контакту зі списку\
          \ndelete 'name' \t\t-> \tВидалити контакт зі списку\
          \nall \t\t\t-> \tВивести всі збережені контакти\
          \nexit/close \t\t-> \tЗавершення роботи помічника\n")
    
    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До зустрічі!\n")
            break
        elif command == "hello":
            print("Як я можу допомогти?\n")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_contact())
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print("Невірна команда.\n")

if __name__ == "__main__":
    main()