import os

if __name__ == '__main__':
    print("welcome to RoboSpeaker 2.0 Created by Arsalan")
    while True:
        x = input("Enter what you want to me speak: ")
        if x =="q":
            os.system("espeak -s 130 'bye bye friend'")
            break
        command = f'espeak -s 120 "{x}"'
        os.system(command)








