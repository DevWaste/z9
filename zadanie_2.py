
pets = {
    1: {
        "Имя": "Мухтар",
        "Вид питомца": "Собака",
        "Возраст питомца": 9,
        "Имя владельца": "Павел"
    },
    2: {
        "Имя": "Каа",
        "Вид питомца": "желторотый питон",
        "Возраст питомца": 19,
        "Имя владельца": "Саша"
    }
}
# данные для теста

def create():
    last = max(pets.keys()) if pets else 0
    new_id = last + 1
    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца питомца: ")
    pets[new_id] = {
        "Имя": pet_name,
        "Вид питомца": pet_type,
        "Возраст питомца": pet_age,
        "Имя владельца": owner_name
    }

def read(ID):
    pet = get_pet(ID)
    if pet:
        pet_info = f'Это {pet["Вид питомца"]} по кличке "{pet["Имя"]}". Возраст питомца: {pet["Возраст питомца"]} {get_suffix(pet["Возраст питомца"])}. Имя владельца: {pet["Имя владельца"]}'
        print(pet_info)
    else:
        print("Питомец с таким ID не найден.")

def update(ID):
    pet = get_pet(ID)
    if pet:
        print(f"Обновление данных для {pet['Имя']}. Оставьте поле пустым, если не хотите изменять.")
        pet['Вид питомца'] = input(f"Вид питомца ({pet['Вид питомца']}): ") or pet['Вид питомца']
        new_age = input(f"Возраст питомца ({pet['Возраст питомца']}): ")
        pet['Возраст питомца'] = int(new_age) if new_age else pet['Возраст питомца']
        pet['Имя владельца'] = input(f"Имя владельца ({pet['Имя владельца']}): ") or pet['Имя владельца']
    else:
        print("Питомец с таким ID не найден.")

def delete(ID):
    if ID in pets:
        del pets[ID]
        print(f"Запись о питомце с ID {ID} удалена.")
    else:
        print("Питомец с таким ID не найден.")

def get_pet(ID):
    return pets.get(ID, False)

def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

def pets_list():
    for ID, pet in pets.items():
        print(f'ID: {ID}, Имя: {pet["Имя"]}, Вид: {pet["Вид питомца"]}, Возраст: {pet["Возраст питомца"]} {get_suffix(pet["Возраст питомца"])}, Владелец: {pet["Имя владельца"]}')

def main():
    while True:
        command = input("Введите команду (create, read, update, delete, list, stop): ").lower()
        if command == "stop":
            print("Программа завершена.")
            break
        elif command == "create":
            create()
        elif command == "read":
            ID = int(input("Введите ID питомца: "))
            read(ID)
        elif command == "update":
            ID = int(input("Введите ID питомца: "))
            update(ID)
        elif command == "delete":
            ID = int(input("Введите ID питомца: "))
            delete(ID)
        elif command == "list":
            pets_list()
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()
