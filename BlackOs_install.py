import os

repo_url = "https://github.com/SashaVoden/BlackOs"
install_dir = "BlackOs"

os.makedirs(install_dir, exist_ok=True)

os.system(f"curl -L {repo_url}/archive/main.zip -o blackos.zip")
os.system("unzip blackos.zip -d BlackOs")
os.system("rm blackos.zip")

os.chdir(install_dir)
print("BlackOs installation complete!")