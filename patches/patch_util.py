import re
import sys

def apply_patch(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"[-] File {file_path} tidak ditemukan.")
        return

    pattern = r"int\s+__system_property_get\s*\([^)]*\)\s*\{"
    replacement = """int __system_property_get(const char *name, char *value) {
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
        new_content = re.sub(pattern, replacement, content, count=1)
        with open(file_path, "w") as f:
            f.write(new_content)
        print("[+] Python Patcher: Berhasil menyisipkan spoofing properti C-level!")
    else:
        print("[-] Python Patcher: Signature __system_property_get tidak ditemukan.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "src/api-impl-jni/util.c"
    apply_patch(target)
