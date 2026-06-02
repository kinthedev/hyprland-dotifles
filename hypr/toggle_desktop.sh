#!/bin/bash

# Lấy ID của workspace hiện tại
CURRENT_WORKSPACE=$(hyprctl monitors -j | jq '.[] | select(.focused == true) | .activeWorkspace.id')

# Kiểm tra xem có cửa sổ nào trong special workspace "desktop" không
HAS_MINIMIZED=$(hyprctl clients -j | jq "[.[] | select(.workspace.name == \"special:desktop\")] | length")

if [ "$HAS_MINIMIZED" -gt 0 ]; then
    # Nếu đang ẩn -> Mang tất cả cửa sổ quay lại workspace hiện tại
    hyprctl clients -j | jq -r '.[] | select(.workspace.name == "special:desktop") | .address' | while read -r addr; do
        hyprctl dispatch movetoworkspace "$CURRENT_WORKSPACE,address:$addr"
    done
else
    # Nếu đang hiện -> Đưa TẤT CẢ cửa sổ của workspace hiện tại vào special workspace
    hyprctl clients -j | jq -r ".[] | select(.workspace.id == $CURRENT_WORKSPACE) | .address" | while read -r addr; do
        hyprctl dispatch movetoworkspacesilent "special:desktop,address:$addr"
    done
fi
