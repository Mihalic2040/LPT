echo "-------------HELLO FROM CHROOT-------------"


echo "-------------Instaling depnds-------------"

adduser _apt --force-badname

apt-get update -y
apt-get upgrade -y
apt-get install neofetch -y

mkdir /soft

neofetch

apt-get install git micro python3 pip nmap aircrack-ng net-tools -y






echo "-------------Starting install GITHUB software-------------"
# # AppleDos
apt install -y bluez libpcap-dev libev-dev libnl-3-dev libnl-genl-3-dev libnl-route-3-dev cmake libbluetooth-dev
mkdir -p tools
cd tools
    git clone https://github.com/Mihalic2040/AppleJuice-Dos.git
    cd AppleJuice-Dos
       pip install -r requirements.txt --break-system-packages
    cd ..
cd ..

# # WIFITE2
# cd /tmp
# git clone https://github.com/derv82/wifite2.git
# cd wifite2
# python3 setup.py install
# cd /tmp
# rm -rf wifite2

# # WIFITE2 : reaver-wps
# cd /tmp
# apt -y install build-essential libpcap-dev aircrack-ng pixiewps
# git clone https://github.com/t6x/reaver-wps-fork-t6x
# cd reaver-wps-fork-t6x
# cd src
# chmod +x configure
# ./configure
# make -j 8
# make install
# cd /tmp
# rm -rf reaver-wps-fork-t6x

# # WIFITE2 : bully

# cd /tmp
# git clone https://github.com/aanarchyy/bully
# cd bully/src
# make -j 8
# make install
# cd /tmp
# rm -rf bully

# Fluxion




echo "-------------GOOD HACKING BY CHROOT-------------"
