import os
import tarfile
from libs.log4py import *



architecture = "arm64" # amd64 or armhf, arm64


folder_path = "./rootfs"
bundle_path = "./build"



def prepare():
    

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        Warning(f"Folder created: {folder_path}")
    else:
        Log(f"Folder already exists: {folder_path}")

    if not os.path.exists(bundle_path):
        os.makedirs(bundle_path)
        Warning(f"Folder created: {bundle_path}")
    else:
        Log(f"Folder already exists: {bundle_path}")


def bootstrap_rootfs(arch):
    Warning("Cleaning ROOTFS")
    os.system("sudo rm -r ./rootfs/*")
    Log("ROOTFS Cleaned")

    Log("Stating creating ROOTFS")
    
    os.system('sudo debootstrap --arch='+ arch +' stable ./rootfs/ http://deb.debian.org/debian/')
    Log("ROOTFS created")
    Log("Creating perms")
    os.system("sudo chmod +x ./rootfs/root")
    Log("Perms created")

def build_scripts():

    Log("Starting build a scripts")
    os.system("chmod +x ./scripts/*")
    os.system("cp -r ./scripts ./rootfs/.")
    print("Scripts builded")

    Warning("Running build")
    os.system("sudo chroot ./rootfs /scripts/build.sh")

def create_tar_gz(folder_path, output_path):

    Log("Creating ROOTFS bundle")
    os.system("tar -cf "+ output_path +" -C "+ folder_path +" .")
    Log("Bundle created")

# Specify the folder path and output path for the archive


# def create_img(rootfs_path, output_path, size_gb):
#     os.system("fallocate -l " + str(size_gb) + "G " + output_path)
#     os.system("sudo mkfs.ext4 " + output_path)
#     os.system("sudo mkdir -p /mnt/tmp")
#     os.system("sudo mount " + output_path + " /mnt/tmp")
#     os.system("sudo cp -a " + rootfs_path + "/. /mnt/tmp")
#     os.system("sudo umount /mnt/tmp")
#     os.system("sudo rmdir /mnt/tmp")

logo = """
 (    (            
 )\ ) )\ )  *   )  
(()/((()/(` )  /(  
 /(_))/(_))( )(_)) 
(_)) (_)) (_(_())  
| |  | _ \|_   _|  
| |__|  _/  | |    
|____|_|    |_|    
"""

if __name__ == "__main__":
    Log("Star building...")
    prepare()
    # Create the tar.gz archive

    output_path = bundle_path + "/rootfs.tar"

    bootstrap_rootfs(architecture) # amd64 or armhf, arm64
    build_scripts()
    create_tar_gz(folder_path, output_path)

    Log("BUILD DONE: Happy hacking!")

    Log(logo)

    Warning("To enter chroot: chroot . /bin/bash --rcfile ./scripts/env.sh")
