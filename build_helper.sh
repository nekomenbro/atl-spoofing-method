#!/bin/bash
# Helper script automation for ATL Spoofing Method
echo "[*] Menjalankan helper build ATL..."
makepkg -od --noconfirm
python3 patches/patch_util.py src/android_translation_layer/src/api-impl-jni/util.c
makepkg -efi --noconfirm
