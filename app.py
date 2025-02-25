import sqlite3
import os

conn = sqlite3.connect("data.db")
cur = conn.cursor()

cur.execute("""
    Create Table if not exists videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )        
""")

def main():
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
                list_data()
            case "2":
                AddData()
            case "3":
                updateData()
            case "4":
                deleteData()
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

    conn.close()

def list_data():
    cur.execute("SELECT * from videos")
    list = cur.fetchall()
    if len(list) == 0:
        print("NO records")
        return
    for data in list:
        print(f"ID: {data[0]}, Name: {data[1]}, Time: {data[2]}")
    
def AddData():
    print("Enter name and Time")
    name = input("Enter name: ")
    time = input("Enter time: ")
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def updateData():
    id = input("Enter ID of Video to be updated: ")
    name = input("Enter name: ")
    time = input("Enter time: ")
    cur.execute("""
        UPDATE videos
        set name = ?, time = ?
        where id = ?        
        """, (name, time, id))
    conn.commit()


def deleteData():
    print("Enter id then, name and Time")
    id = input("Enter ID of Video to be Deleted: ")
    cur.execute("delete from videos where id = ?", (id, )) # if only one value we have to put tralling comma
    conn.commit()

if __name__ == "__main__":
    main()
