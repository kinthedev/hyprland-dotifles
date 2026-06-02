# Hyprland dotfiles

This repository contains my Hyprland configuration and related dotfiles. The layout is designed so you can copy or symlink files to your home directory on an Arch Linux system running Hyprland.

## What goes where

- Copy the hidden folders and files `.icons`, `.themes`, and the file `.zshrc` into your home directory root: `/home/use/`.
- Copy the remaining dotfiles and folders into the `.config` directory under that same home: `/home/use/.config/`.

Quick copy (example)

- Replace `/home/use` with your actual home path if different.

```bash
# copy icons and themes and .zshrc to home
cp -r icons /home/use/.icons
cp -r themes /home/use/.themes
cp .zshrc /home/use/.zshrc

# copy configuration folders to ~/.config (creates hypr, waybar, wofi, etc.)
mkdir -p /home/use/.config
cp -r hypr /home/use/.config/hypr
cp -r waybar /home/use/.config/waybar
cp -r wofi /home/use/.config/wofi
```

Or create symlinks so updates in this repo reflect immediately:

```bash
ln -sT $(pwd)/hypr /home/use/.config/hypr
ln -sT $(pwd)/waybar /home/use/.config/waybar
ln -sT $(pwd)/wofi /home/use/.config/wofi
ln -sT $(pwd)/icons /home/use/.icons
ln -sT $(pwd)/themes /home/use/.themes
ln -sT $(pwd)/.zshrc /home/use/.zshrc
```

## Notes for Arch (Hyprland)

- Install Hyprland and common utilities (example):

```bash
sudo pacman -Syu hyprland waybar wofi kitty wl-clipboard grim slurp mako hyprpaper swaync nwg-look 
```

- If you use a compositor-specific wallpaper daemon (e.g. `hyprpaper`) or notification daemon (`mako`), install and enable them.
- After copying or symlinking, restart your session or reload Hyprland for configuration to take effect.

## Files and purpose

- `hypr/` — main Hyprland config files (`hyprland.conf`, `hyprlock.conf`, `monitors.conf`, `monitors.lua`). Customize monitor layouts and keybindings here.
- `waybar/` — Waybar configuration and style for the top bar.
- `wofi/` — Wofi launcher config and styles.
- `fastfetch/` — fastfetch config and ascii logos used by the terminal status script.
- `kitty/` — Kitty terminal config.
- `swaync/` — Notification center styles and settings.
- `images/`, `wallpapers/` — wallpapers and images referenced by the configs.
- `scripts/` and `hypr/scripts/` — helper scripts to manage monitors, toggle desktop, and other utilities.

## Customization tips

- Edit `hypr/hyprland.conf` to adapt keybindings and workspace rules to your hardware.
- Update absolute paths in configs (wallpapers, scripts) if you copied the repo to a different folder.
- For monitor-specific layouts, inspect `hypr/monitors.conf` and `hypr/monitors.lua` and adapt per your displays.

## Troubleshooting

- If Hyprland fails to start, move the config out of the way and try a minimal config to debug:

```bash
mv /home/use/.config/hypr /home/use/.config/hypr.backup
mkdir -p /home/use/.config/hypr && printf "# minimal" > /home/use/.config/hypr/hyprland.conf
```

- Use `journalctl` or the TTY logs to inspect errors from Hyprland and related services.

## Want me to automate this?

- I can add a small installer script that creates backups, copies or symlinks files, and optionally installs required packages on Arch. Tell me if you'd like that.

---

Last updated: 2026-06-02
