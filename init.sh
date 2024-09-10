echo "Installing/updating pacman"
pkexec bash -c "
    pacman -Syu --noconfirm &&
    pacman -S --noconfirm xfce4-terminal &&
    pacman -S --noconfirm gparted &&
    yay -S --noconfirm gnome-disk-utility &&
"
python main.py