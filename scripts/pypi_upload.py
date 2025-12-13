import os
import platform
from subprocess import Popen, PIPE
from dotenv import load_dotenv
import atgui

ATGUI = atgui.Manager()

load_dotenv()

token = os.getenv('PYPI_TOKEN')

options = ["No", "Yes"]

def main():
    pyprefix = ""

    if (platform.system() == "Windows"):
        pyprefix = "py"

    elif (platform.system() == "Linux"):
        pyprefix = "python3"

    print(f"Using: {platform.system()}")

    gui = ATGUI.show_gui(
        gui_name="box",
        title="Are you sure?",
        able_to_select=True,
        able_to_escape=True,
        color="red",
        options=options
    )
    
    match gui:
        case 0:
            print("Goodbye then.")
            os._exit(0)

    buildprocess = Popen([pyprefix, "-m", "build"])
    
    exitcode = buildprocess.wait()
    if exitcode != 0:
        print("The build process failed.")
    update_process = Popen([pyprefix, "-m", "pip", "install", "--upgrade", "twine"]) 
    exitcode = update_process.wait()
    if exitcode != 0:
        print("The Update process failed.")
    
    os.environ["TWINE_USERNAME"] = "__token__"
    os.environ["TWINE_PASSWORD"] = token

    upload_process = Popen(
        [pyprefix, "-m", "twine", "upload", "--repository", "pypi", "dist/*"],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE
    )

    exitcode = upload_process.wait()
    if exitcode != 0:
        print("The uploading to PyPi failed!")

if __name__ == "__main__":
    main()