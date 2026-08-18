import re

def apply_patch():
    file_path = "src/api-impl-jni/util.c"
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except Exception as e:
        print(f"[-] Gagal membaca file: {e}")
        return

    # Regex ini mengabaikan tipe data dan spasi, langsung mengincar nama fungsinya
    pattern = r"(__system_property_get\s*\([^)]*\)\s*\{)"
    
    spoof_logic = """
    if (name != NULL) {
        if (strcmp(name, "ro.product.model") == 0) { strcpy(value, "Pixel 6"); return 7; }
        if (strcmp(name, "ro.product.brand") == 0) { strcpy(value, "google"); return 6; }
        if (strcmp(name, "ro.product.manufacturer") == 0) { strcpy(value, "Google"); return 6; }
        if (strcmp(name, "ro.product.device") == 0) { strcpy(value, "raven"); return 5; }
        if (strcmp(name, "ro.build.tags") == 0) { strcpy(value, "release-keys"); return 12; }
        if (strcmp(name, "ro.build.fingerprint") == 0) { 
            strcpy(value, "google/raven/raven:12/SP1A.210812.016/7701450:user/release-keys"); 
            return 56; 
        }
    }
"""
    
    if re.search(pattern, content):
        # Menyisipkan modifikasi spoofing langsung setelah kurung kurawal buka "{"
        new_content = re.sub(pattern, r"\1" + spoof_logic, content, count=1)
        with open(file_path, "w") as f:
            f.write(new_content)
        print("[+] Python Patcher: SUPER HOOK berhasil disisipkan permanen ke util.c!")
    else:
        print("[-] Python Patcher: Fungsi tetap tidak ditemukan!")

if __name__ == "__main__":
    apply_patch()
