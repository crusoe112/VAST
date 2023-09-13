import datetime
from hashlib import sha256
from random import randint

global rand_number
rand_number = 0

randomTable = [101,40,47,118,62,77,114,67,49,108,67,92,51,119,109,20,21,108,70,
               40,52,24,31,21,54,59,106,76,120,24,13,76,90,71,119,72,48,52,20,
               12,13,30,37,40,99,78,43,64,62,65,7,101,116,16,121,10,91,68,97,
               94,66,119,49,86,25,25,4,17,100,77,30,23,80,24,27,36,127,101,104,
               91,23,40,122,98,49,68,44,97,118,5,107,24,75,66,68,14,117,13,38,
               62,88,3,122,19,75,16,65,25,50,17,93,2,17,99,31,58,55,26,110,36,
               115,123,36,96,68,46,35,67,83,107,52,101,116,99,107,125,48,20,96,
               80,27,12,106,86,102,111,116,82,66,70,26,62,54,68,11,116,5,67,65,
               3,31,86,51,20,52,38,30,48,85,104,42,61,61,14,110,32,37,124,106,
               23,95,92,66,107,68,107,2,62,42,50,109,93,64,77,103,17,113,106,
               127,0,80,33,115,98,115,102,109,14,52,67,81,81,49,11,75,119,113,
               74,13,4,47,22,109,43,29,102,42,91,16,25,46,27,126,48,9,49,119,
               60,74,113,83,121,34,26,22,113,53,30,5,91,38,26,46,16,96,3]
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
        c = 48 + randint(0, 122-48) # 0 to z
        if c >= 58 and c <= 64:
            c += 7 # skip non-alphanumeric characters
        elif c >= 91 and c <= 96:
            c += 6 # skip non-alphanumeric characters
        session_key += chr(c)

    random_number = randint(0, 255)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H")
    session_str = f"{random_number},{username},{int(isLoggedIn)},{current_time},{session_key}"
    encoded = encode_session(rand_number, session_str)
    return encoded

def check_session(session_str):
    fields = session_str.split(',')

    if len(fields) != 5:
        return (None, False)

    username = fields[1]
    if datetime.datetime.strptime(fields[3], "%Y-%m-%d-%H") > datetime.datetime.now():
        return (username, False)
    elif datetime.datetime.strptime(fields[3], "%Y-%m-%d-%H") < datetime.datetime.now() - datetime.timedelta(hours=3):
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