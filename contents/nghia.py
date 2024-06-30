import os


startup = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
print(f"🚀 {startup}")


nghia_ahk = os.path.join(os.getcwd(), "nghia.ahk")
print(f"🚀 {nghia_ahk}")


os.symlink(
    
# # print(f"Tạo liên kết 
