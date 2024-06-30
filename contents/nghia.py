import os
import subprocess
import sys
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Đường dẫn đến thư mục Startup
    startup = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
    print(f"🚀 {startup}")

    nghia_ahk_link = os.path.join(startup, "nghia.ahk")
    print(f"🚀 {nghia_ahk_link}")

    # Đường dẫn đến file nghia.ahk
    nghia_ahk = os.path.join(os.getcwd(), "nghia.ahk")
    print(f"🚀 {nghia_ahk}")

    # Tạo liên kết
    try:
        subprocess.run(['mklink', nghia_ahk_link, nghia_ahk], shell=True, check=True)
        print(f"Tạo liên kết tượng trưng thành công: {nghia_ahk_link}")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi tạo liên kết tượng trưng: {e}")
    except FileExistsError:
        print("Liên kết tượng trưng đã tồn tại")
    except OSError as e:
        print(f"Lỗi hệ thống khi tạo liên kết tượng trưng: {e}")
else:
    # Chạy lại script với quyền quản trị
    print("Chạy lại script với quyền quản trị")
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
