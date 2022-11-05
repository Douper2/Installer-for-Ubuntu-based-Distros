import os
import time

os.system("sudo apt update && sudo apt upgrade -y")
time.sleep(1)
os.system("sudo apt-get install git steam flatpak gnome-software-plugin-flatpak -y && latpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
time.sleep(1)
os.system("git clone https://github.com/sourav2k/spotify-adblock-linux.git && cd spotify-adblock-linux")
time.sleep(1)
os.system("chmod a+x spot.sh")
os.system("./spot.sh")
time.sleep(1)
os.system("flatpak install flathub com.mattjakeman.ExtensionManager && flatpak install flathub com.obsproject.Studio")
os.system("flatpak install flathub com.heroicgameslauncher.hgl && flatpak install flathub com.mojang.Minecraft")
os.system("flatpak install flathub com.brave.Browser && sudo apt-get purge firefox")
os.system("rm /snap/bin/firefox && rm .mozila/firefox")
os.system("sudo apt install virtualbox")
os.system("flatpak install flathub net.lutris.Lutris && flatpak install flathub com.snes9x.Snes9x")
os.system("sudo apt update && sudo apt upgrade -y")