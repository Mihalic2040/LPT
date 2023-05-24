import os
import tarfile

def bootstrap_rootfs(arch):
    print("Cleaning rootfs")
    os.system("sudo rm -r ./rootfs/*")
    print("ROOTFS cleaned")

    print("Stating creating rootfs")
    
    os.system('sudo debootstrap --arch='+ arch +' stable ./rootfs/ http://deb.debian.org/debian/')
    print("ROOTFS created")
    print("Creating perms")
    os.system("sudo chmod +x ./rootfs/root")
    print("prems seted")

def build_scripts():


    print("Starting build a scripts")
    os.system("chmod +x ./scripts/*")
    os.system("cp -r ./scripts ./rootfs/.")
    print("scripts builded")

    print("Running build")
    os.system("sudo chroot ./rootfs /scripts/build.sh")

def create_tar_gz(folder_path, output_path):
    os.system("tar -czf "+ output_path +" -C "+ folder_path +" .")
# Specify the folder path and output path for the archive
folder_path = "./rootfs"
output_path = "./build/archive.tar.gz"




if __name__ == "__main__":

    print("Star building...")
    # Create the tar.gz archive

    bootstrap_rootfs('amd64') # amd64 or armhf
    build_scripts()
    create_tar_gz(folder_path, output_path)

    print("Archive created successfully!")
