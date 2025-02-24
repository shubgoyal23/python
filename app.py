import json


def main():
    videos_list = load_videoList()
    print(videos_list)
    while True:
        pass

def load_videoList():
    try:
        with open("data.txt", 'r') as file:
            list = json.loads(file)
            return list                
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    main()