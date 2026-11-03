# پروژه ماشین‌حساب اندروید

این پروژه با Python و Kivy ساخته شده است.

- `main.py`: کد برنامه و رابط کاربری
- `buildozer.spec`: تنظیمات ساخت APK
- `.github/workflows/build-apk.yml`: ساخت خودکار APK در GitHub Actions

## اجرای آزمایشی روی کامپیوتر
در محیط Linux یا محیطی که Kivy در آن نصب شده:
```bash
python -m pip install "kivy==2.3.1"
python main.py
```

## ساخت APK
Buildozer در Linux/Ubuntu اجرا می‌شود. برای ساخت آنلاین:
1. در GitHub یک مخزن جدید بساز.
2. فایل‌های این پروژه را در مخزن بارگذاری کن.
3. وارد تب Actions شو و workflow با نام Build Android APK را اجرا کن.
4. پس از پایان موفق، از بخش Artifacts فایل `calculator-apk` را دریافت کن.

ساخت APK به اینترنت برای دریافت Android SDK/NDK و ابزارهای ساخت نیاز دارد.
این ZIP پروژهٔ آمادهٔ ساخت است، نه خود فایل APK.
