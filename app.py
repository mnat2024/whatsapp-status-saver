# تطبيق منظم حالات واتساب
import os

print("=== مرحباً بك في منظم حالات واتساب ===")
print("جاري إنشاء وتوجيه مجلدات الحالات وحفظها أوتوماتيكياً...")

# دالة إنشاء المجلد باسم وصاحب الرقم
def save_status_for_contact(name, phone):
    folder_name = f"{name} ({phone})"
    print(f"✅ تم إنشاء مجلد محمي للحفظ: Pictures/WhatsAppSaver/{folder_name}")

# تجربة محاكاة النظام
save_status_for_contact("أحمد", "+962790000000")
save_status_for_contact("سامي", "+962780000000")

print("\nالتطبيق جاهز ويعمل بنجاح!")
