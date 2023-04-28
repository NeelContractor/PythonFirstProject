import os
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Neel")
    while True:
        x = input("Enter what do you want me speak: ")
        if x=="q":
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)