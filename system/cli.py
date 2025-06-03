import system.bsh as bsh

def start_cli():

    print("Welcome to BlackOs CLI")
    shell = bsh.BSh()
    shell.run_shell()

if __name__ == "__main__":
    start_cli()