import math
import random 
import os

def encrypt(message, e, n):
    ciphertext = []
    for char in message:
        number = ord(char)
        cipher_number = pow(number, e, n)
        ciphertext.append(cipher_number)
    return(ciphertext)
       

def decrypt(ciphertext, d, n):
    message = ""
    for number in ciphertext:
        message_number = pow(number, d, n)
        message += chr(message_number)
    return(message)

def is_prime(p):
    if p <= 1:
        return(False)
    else:
        for i in range(2 , int(math.sqrt(p)) + 1):
            if p%i == 0: 
                return(False)
        return(True)

def generate_keys():
    while True:
        candidate = random.randint(1000,2000)
        if is_prime(candidate) == True:
            p = candidate
            break
    while True:
        candidate = random.randint(8000, 16000)
        if is_prime(candidate) == True and candidate != p:
            q = candidate
            break
    n = p*q
    phi = (p-1) * (q-1)
    
    while True:
        candidate_e = random.randint(2, phi)
        if math.gcd(candidate_e, phi) == 1:
            e = candidate_e
            break
    
    d = pow(e, -1, phi)
    return (e,d,n)

def save_keys(username, e, d, n):
    os.makedirs("keys", exist_ok= True)
    with open(f"keys/{username}_public.txt", "w") as pub_file:
        pub_file.write(f"{e},{n}")
    with open(f"keys/{username}_private.txt", "w") as priv_file:
        priv_file.write(f"{d},{n}")
    

def load_public_key(username):
    try:
        with open(f"keys/{username}_public.txt", "r") as f:
            e, n = map(int, f.read().split(","))
            return e, n
    except FileNotFoundError:
        print("Public Key not found.")
        return None, None
    
def load_private_key(username):
    try:
        with open(f"keys/{username}_private.txt", "r") as f:
            d, n = map(int, f.read().split(","))
            return d, n
    except FileNotFoundError:
        print("Private Key not found.")
        return None, None   

def main():
    print("\n--- RSA CLI Tool ---")
    username = input("Enter your username: ").strip()

    while True:
        print("\n --- Your Options ---")
        print("1. Generate RSA keys")
        print("2. Encrypt a message for someone")
        print("3. Decrypt a received message")
        print("4. Quit")

        choice = input("What would you like to do today? ").strip()

        if choice == "1":
            e , d, n = generate_keys()
            save_keys(username, e, d, n)
            print("\n ✅ Keys Generated & Saved!")
            print(f"Share your public key file: keys/{username}_public.txt")
            print("Your private key is generated & saved securely. (not displayed)")

        elif choice == "2":
            recipient = input("Enter recipient username: ").strip()
            e_pub, n_pub = load_public_key(recipient)
            if not e_pub or not n_pub:
                continue
            message = input("Enter message to encrypt: ")
            cipher = encrypt(message, e_pub, n_pub)
            print("\nEncrypted Text (send this to the recipient): ")
            print(','.join(map(str, cipher)))

        elif choice == "3":
            d_priv, n_priv = load_private_key(username)
            if not d_priv or not n_priv:
                continue
            cipher_input = input("Enter ciphertext: ")
            try:
                ciphertext = [int(x.strip()) for x in cipher_input.split(",")]
                decrypted = decrypt(ciphertext, d_priv, n_priv)
                print("\nDecrypted message: ")
                print(decrypted)
            except:
                print("Invalid ciphertext format.")
        
        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()