
import subprocess
import psutil
script_process = None


def start_script():
    global script_process
    if script_process is None:
        script_process = subprocess.Popen(
            ["cmd", "/c", "start", "/min", "cmd", "/k", "python", "utils/ForwardHandler.py"], shell=True)


def stop_script():
    global script_process
    if script_process:
        python_pid = None
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if 'python.exe' in proc.info['name'] and 'utils/ForwardHandler.py' in proc.cmdline():
                python_pid = proc.info['pid']
                break

        # Terminate the python process and the terminal window
        if python_pid:
            # First terminate the python process
            psutil.Process(python_pid).terminate()

            # Then find and terminate the terminal window
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                if 'cmd.exe' in proc.info['name'] and 'utils/ForwardHandler.py' in proc.cmdline():
                    subprocess.run(
                        ['taskkill', '/PID', str(proc.info['pid']), '/F'])
                    break
        script_process = None
    else:
        print("Script is not running.")

# Main function


def main():
    # start_script()
    # return
    while True:
        user_input = input(
            "Enter 'start' to start the script, 'stop' to stop it, or 'exit' to quit: ")
        if user_input == 'start':
            start_script()
        elif user_input == 'stop':
            stop_script()
        elif user_input == 'exit':
            stop_script()
            break
        else:
            print("Invalid input. Please enter 'start', 'stop', or 'exit'.")


if __name__ == "__main__":
    main()
