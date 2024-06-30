import os

# Đường dẫn đến thư mục Startup
startup = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
print(f"🚀 {startup}")

# Đường dẫn đến file nghia.ahk
nghia_ahk = os.path.join(os.getcwd(), "nghia.ahk")
print(f"🚀 {nghia_ahk}")

# Tạo liên kết tượng trưng
try:
    os.symlink(nghia_ahk, os.path.join(startup, "nghia.ahk"))
    print(f"Tạo liên kết tượng trưng thành công: {os.path.join(startup, 'nghia.ahk')}")
except FileExistsError:
    print("Liên kết tượng trưng đã tồn tại")
except OSError as e:
    print(f"Lỗi khi tạo liên kết tượng trưng: {e}")
