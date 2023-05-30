#!/system/bin/sh

MOUNT_DIR="/data/LPT"
MOUNTED=false

# Function to unmount the filesystem
unmount_filesystem() {
  umount "$MOUNT_DIR/dev/pts"
  umount "$MOUNT_DIR/dev"
  umount "$MOUNT_DIR/proc"
  umount "$MOUNT_DIR/sys"
  echo "Filesystem unmounted"
}

# Check if -u flag is provided to unmount the filesystem
if [ "$1" == "-u" ]; then
  unmount_filesystem
  exit 0
fi

echo "Mounting filesystem for LPT ROOTFS"

cd "$MOUNT_DIR"

# Mount the necessary directories
mount --bind /dev dev/
mount --bind /dev/pts dev/pts/
mount --bind /proc proc/
mount --bind /sys sys/

MOUNTED=true


echo "System mounted"
echo "Happy Hacking!!!"

# Trap the script exit and unmount the filesystem if it was mounted

# Function to cleanup and unmount the filesystem
