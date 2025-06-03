import os
import subprocess


class BSh:
    def __init__(self):
        self.cwd = os.getcwd()
    
    def run_shell(self):
        print("Welcome to BSh (Black Shell)")
        while True:
            cmd = input(f"bsh:{self.cwd}$ ").strip()

            if cmd == "exit":
                print("Shutting down BSh...")
                break

            elif cmd == "help":
                print("Available commands: exit, help, ls, cd <dir>, pwd, mkdir <name>, rm <file>, run <script>, git clone <repo>")

            elif cmd == "ls":
                print("\n".join(os.listdir(self.cwd)))

            elif cmd == "pwd":
                print(self.cwd)

            elif cmd.startswith("cd "):
                new_dir = cmd[3:].strip()
                target_path = os.path.abspath(os.path.join(self.cwd, new_dir))

                if os.path.exists(target_path) and os.path.isdir(target_path):
                    self.cwd = target_path
                    os.chdir(target_path)
                else:
                    print("Directory not found.")

            elif cmd.startswith("mkdir "):
                dir_name = cmd.split(" ", 1)[1]
                os.makedirs(os.path.join(self.cwd, dir_name), exist_ok=True)

            elif cmd.startswith("rm "):
                file_name = cmd.split(" ", 1)[1]
                path = os.path.join(self.cwd, file_name)
                if os.path.exists(path):
                    os.remove(path) if os.path.isfile(path) else os.rmdir(path)
                else:
                    print("File or directory not found.")

            elif cmd.startswith("run "):  
                script_name = cmd.split(" ", 1)[1]
                script_path = os.path.join(self.cwd, script_name)

                if os.path.exists(script_path):
                    if script_name.endswith(".py"):
                        subprocess.run(["python", script_path])
                    elif script_name.endswith(".sh"):
                        subprocess.run(["bash", script_path])
                    elif os.access(script_path, os.X_OK):
                        subprocess.run(script_path, shell=True)
                    else:
                        print("Unsupported file format.")
                else:
                    print("File not found in current directory.")

            elif cmd.startswith("git clone "):
                repo_url = cmd.split(" ", 2)[2]
                repo_name = repo_url.split("/")[-1].replace(".git", "")
                target_dir = f"user/downloads/{repo_name}"

                if not os.path.exists(target_dir):
                    os.system(f"git clone {repo_url} {target_dir}")
                    print(f"Repository cloned into {target_dir}")
                else:
                    print("Repository already exists.")

            else:
                print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    shell = BSh()
    shell.run_shell()