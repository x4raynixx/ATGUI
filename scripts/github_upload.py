# 3-Numbers-Check-Verification
# Later, Enter Branch
# Later, Do you want to pull the newest files from github branch?
# Later, Are you sure you want to upload the code to the github branch with --force tag

# 
import atgui
import os
import sys
import signal
import time
import random
import platform

def signalHandler(sig, frame):
    print("Ctrl + C clicked, exiting...")
    sys.exit(0)

ATGUI = atgui.Manager()

def number_verify(old_number):
    numbers = []

    for _ in range(3): # idk desync :sob:
        numbers.append(str(random.randint(1, 99)))

    chosen_num = random.choice(numbers)

    # 3-Numbers-Check-Verification
    first_num_check = ATGUI.show_gui(
        gui_name="box",
        able_to_select=True,
        able_to_escape=True,
        title=f"Number #{old_number}", # smart fr
        description=f"Choose Number: {chosen_num}",
        color="red",
        options=numbers,
    )

    if numbers[first_num_check] != chosen_num:
        print("> Wrong number, canceling!")
        sys.exit(0)

    return old_number + 1

def clear_screen():
    if (platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

def main():
    signal.signal(signal.SIGINT, signalHandler) # for non big error ctrl + cexit fr
    
    branch: str
    wanna_pull_files: bool
    upload_with_force_flag: bool
    commit_message: str
    number = 1
    for _ in range(3):
        number = number_verify(number)
        time.sleep(0.1)
        clear_screen()

    clear_screen()
    time.sleep(1)
    
    branch = str(input("> Branch: "))
    pull_files_branch = ATGUI.show_gui(
        gui_name="box",
        able_to_select=True,
        able_to_escape=True,
        title=f"Branch",
        description=f"Do you want to pull newest files from this github branch?",
        color="yellow",
        options=["Yes", "No"],
    )

    time.sleep(0.3)
    clear_screen()

    match pull_files_branch:
        case 0: # Yes
            wanna_pull_files = True
        case 1: # No
            wanna_pull_files = False

    time.sleep(0.3)
    clear_screen()

    force_flag = ATGUI.show_gui(
        gui_name="box",
        able_to_select=True,
        able_to_escape=True,
        title=f"Force",
        description=f"Do you want to use the --force flag?",
        color="red",
        options=["Yes", "No"],
    )

    time.sleep(0.3)
    clear_screen()

    commit_message = str(input("> Commit message: "))

    match force_flag:
        case 0:
            upload_with_force_flag = True
        case 1:
            upload_with_force_flag = False
    
    if upload_with_force_flag == None or wanna_pull_files == None or branch == None or commit_message == None:
        print("Something went wrong, exiting...")
        sys.exit(0)
    
    # > python scripts/github_upload.py
    if wanna_pull_files == True:
        os.system(f"git pull origin {branch}")

    os.system(f"git add .")
    os.system(f'git commit -m "{commit_message}"')
    os.system(f"git push origin {branch} {"--force" if upload_with_force_flag == True else ""}")

if __name__ == "__main__":
    main()