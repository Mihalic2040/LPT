# LPT
LightPentestToolkit - android tool Wow

# Deps
    debootstap
    wget
    openssl
    python3
    tar
    chroot
    qemu-user-static // for enter other architecture chroot
    qemu-user-static-binfmt

# Build
    mkdir build
    mkdir rootfs
    sudo python3 build.py

# Install (Auto mayby)
    mkdir /data/LPT
    cd /data/LPT
    cp /storage/emulated/0/Downloads/rootfs.tar .
    tar -xf rootfs.tar
    rm rootfs.tar



# Enter
# WARN Do not rm -rf * in mounted system you can kill exsisting os
    ./scripts/mount.sh #mount filesystem
    chroot . /bin/bash --rcfile ./scripts/env.sh # enter chroot with enviroment variable

    # after work witch chrot unmount system
    ./scripts/mount.sh -u