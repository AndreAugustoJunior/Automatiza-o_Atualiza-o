import os
import subprocess
import shutil

def run(cmd):
	print(f"\n Executando: {''.join(cmd)}\n")
	try:
		subprocess.run(cmd, check=True)
	except Exception as e:
		print(f" Erro ao executar {cmd}: {e}")

def exists(cmd):
	return shutil.which(cmd)

print("\n======Atualizador 2000====\n")

print("Detectando gerenciador de pacotes..")


if exists("apt"):
    print("➡ Sistema baseado em APT (Debian/Ubuntu).")
    run(["apt", "update"])
    run(["apt", "upgrade", "-y"])
    run(["apt", "full-upgrade", "-y"])
    run(["apt", "autoremove", "-y"])

elif exists("pacman"):
    print("➡ Sistema baseado em Pacman (Arch/Manjaro).")
    run(["pacman", "-Syu", "--noconfirm"])

elif exists("dnf"):
    print("➡ Sistema baseado em DNF (Fedora/RHEL).")
    run(["dnf", "upgrade", "-y"])

elif exists("zypper"):
    print("➡ Sistema baseado em Zypper (OpenSUSE).")
    run(["zypper", "refresh"])
    run(["zypper", "update", "-y"])

else:
    print("⚠ Nenhum gerenciador de pacotes principal detectado.")

# --- Flatpak ---
print("\n===== FLATPAK =====")
if exists("flatpak"):
    run(["flatpak", "update", "-y"])
else:
    print("Flatpak não instalado.")

# --- Snap ---
print("\n===== SNAP =====")
if exists("snap"):
    run(["snap", "refresh"])
else:
    print("Snap não instalado.")

# --- Final ---
print("\n===== FINALIZADO =====")
print("✔ Todas as atualizações foram executadas.\n")
