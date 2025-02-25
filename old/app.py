import json
import os


def main():
    videos_list = load_videoList()
    print("*" * 50)
    print("1. List Data")
    print("2. Add Data")
    print("3. Update Data")
    print("4. Remove Data")
    print("5. Exit")
    print("*" * 50)
    while True:
        userinput = input("Enter your Choise: ")
        match userinput:
            case "1":
                list_data(videos_list)
            case "2":
                name = input("Enter name: ")
                time = input("Enter time: ")
                d = {"name":name, "time":time}
                videos_list = AddData(d, videos_list)
            case "3":
                videos_list = update(videos_list)
            case "4":
                videos_list = deleteData(videos_list)
            case "5" | "exit":
                print("Closing Program....")
                break
            case "clear":
                os.system('clear')
            case "cls":
                os.system('cls')
            case "help":
                print("*" * 50)
                print("1. List Data")
                print("2. Add Data")
                print("3. Update Data")
                print("4. Remove Data")
                print("5. Exit")
                print("*" * 50)
            case _:
                print("Invalid input")

def load_videoList():
    try:
        with open("data.txt", 'r') as file:
            list = json.load(file)
            data = []
            for k, v in enumerate(list, start=1):
                data.append(v)
            return list                
    except FileNotFoundError:
        return []
    
def list_data(videos):
    print()
    print("*" * 50)
    for k, v in enumerate(videos, start=1):
        print(f"{k}. Name: {v["name"]}, time: {v["time"]}")
    print("*" * 50)
    print()

def saveDate(list):
    try:
       with open("data.txt", 'w') as file:
            json.dump(list, file)
    except:
        print("something went wrong saving data")
    
    
def AddData(data, list):
    list.append(data)
    saveDate(list)
    return list

def update(list):
    print()
    print("*" * 50)
    try:
        i = int(input("Enter Id: "))
        name = input("Enter name: ")
        time = input("Enter time: ")
        d = {"name":name, "time":time}
        list[i-1] = d
        saveDate(list)
    except:
        print("Wrong agrument")
    print("*" * 50)
    print() 
    return list  
  
def deleteData(list):
    try:
        i = int(input("Enter id: "))  
        list.pop(i-1)
        saveDate(list)
    except:
        print("something went wrong")
    finally:
        return list


if __name__ == "__main__":
    main()