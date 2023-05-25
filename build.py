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
    print("Creting user")
    os.system("""sudo chroot ./rootfs useradd -m -s /bin/bash -c "LPT" -U lpt""")
    os.system("sudo chroot ./rootfs passwd lpt")


    print("Starting build a scripts")
    os.system("chmod +x ./scripts/*")
    os.system("cp -r ./scripts ./rootfs/.")
    print("scripts builded")

    print("Running build")
    os.system("sudo chroot ./rootfs /scripts/build.sh")

def create_tar_gz(folder_path, output_path):
    os.system("tar -cf "+ output_path +" -C "+ folder_path +" .")
# Specify the folder path and output path for the archive
folder_path = "./rootfs"
output_path = "./build/archive.tar"


# def create_img(rootfs_path, output_path, size_gb):
#     os.system("fallocate -l " + str(size_gb) + "G " + output_path)
#     os.system("sudo mkfs.ext4 " + output_path)
#     os.system("sudo mkdir -p /mnt/tmp")
#     os.system("sudo mount " + output_path + " /mnt/tmp")
#     os.system("sudo cp -a " + rootfs_path + "/. /mnt/tmp")
#     os.system("sudo umount /mnt/tmp")
#     os.system("sudo rmdir /mnt/tmp")

if __name__ == "__main__":
    rootfs_path = "./rootfs"
    output_img_path = "./build/rootfs.img"
    image_size_gb = 3

    print("Star building...")
    # Create the tar.gz archive

    bootstrap_rootfs('amd64') # amd64 or armhf
    build_scripts()
    create_tar_gz(folder_path, output_path)

    print("Archive created successfully!")
