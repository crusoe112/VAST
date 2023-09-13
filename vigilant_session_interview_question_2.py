import datetime
from hashlib import sha256
import random

global rand_number
rand_number = 0

with open('seed', 'r') as file:
    seed = int(file.read().replace('\n', ''))


random.seed(seed)
randomTable = [random.randint(0, 255) for i in range(256)]
# session: "random_number,username,isLoggedIn,year-mon-mday-hour,session_key"


def encode_session(random_number, session_str):
    encoded = f"{random_number:02X}"
    for c in session_str:
        encoded += f"{ord(c) ^ randomTable[random_number % 255]:02X}"
        random_number += 1
    return encoded

def decode_session(encoded):
    index = int(encoded[:2], 16)
    decoded = ''
    for i in range(2, len(encoded), 2):
        decoded += chr(int(encoded[i:i+2], 16) ^ randomTable[index % 255])
        index += 1
    return decoded

def create_session(username, isLoggedIn):
    session_key = ''

    for i in range(51):
        c = 48 + random.randint(0, 122-48) # 0 to z
        if c >= 58 and c <= 64:
            c += 7 # skip non-alphanumeric characters
        elif c >= 91 and c <= 96:
            c += 6 # skip non-alphanumeric characters
        session_key += chr(c)

    random_number = random.randint(0, 255)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    session_str = f"{random_number},{username},{int(isLoggedIn)},{current_time},{session_key}"
    encoded = encode_session(rand_number, session_str)
    return encoded

def check_session(session_str):
    fields = session_str.split(',')

    if len(fields) != 5:
        return (None, False)

    username = fields[1]

    if datetime.datetime.strptime(fields[3], "%Y-%m-%d-%H-%M-%S") > datetime.datetime.now():
        return (username, False)
    elif datetime.datetime.strptime(fields[3], "%Y-%m-%d-%H-%M-%S") < datetime.datetime.now() - datetime.timedelta(hours=3):
        return (username, False)
    elif fields[2] != '1':
        return (username, False)

    return (username, True)

def main():
    choice = int(input("1. Login\n2. Resume Session\n3. Exit\n"))
    if choice == 1:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if username == 'admin' and sha256(password.encode('utf-8')).hexdigest() == '358383a527c67ad80d1476d317bb7b45ad0e7fe3fc5d38d18260aea29f672e40':
            token = create_session(username, True)
            print(f"Session token: {token}")
            print(f"Welcome {username}!")
        else:
            token = create_session(username, False)
            print(f"Session token: {token}")
            print(f"Invalid credentials for {username}!")
    elif choice == 2:
        token = input("Enter session token: ").strip()
        decoded = decode_session(token)
        username, isLoggedIn = check_session(decoded)
        if isLoggedIn:
            print(f"Welcome {username}!")
        else:
            print(f"Invalid session for {username}!")
    else:
        print("Goodbye!")

if __name__ == '__main__':
    main()
