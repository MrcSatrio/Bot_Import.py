import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Buat objek ChromeOptions
chrome_options = webdriver.ChromeOptions()

# Tambahkan path ChromeDriver ke options
chrome_options.add_argument(r'--webdriver.chrome.driver=C:\path\to\chromedriver.exe')

# Inisialisasi driver Chrome dengan options
driver = webdriver.Chrome(options=chrome_options)

# Buka halaman login
driver.get('http://52.221.227.139')  # Ganti dengan URL yang sesuai

# Tunggu beberapa detik agar halaman terbuka sepenuhnya (sesuaikan waktu sesuai kebutuhan)
driver.implicitly_wait(5)

# Isi formulir login
username_field = driver.find_element(By.NAME, 'username')  # Ganti dengan nama field sesuai dengan halaman Anda
password_field = driver.find_element(By.NAME, 'password')  # Ganti dengan nama field sesuai dengan halaman Anda

username_field.send_keys('1')
password_field.send_keys('123')

# Temukan elemen tombol submit menggunakan selector CSS
submit_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.w-100.py-2')

# Submit formulir dengan mengklik tombol submit
submit_button.click()

# Tunggu sejenak untuk memberikan waktu agar proses login selesai
driver.implicitly_wait(5)

# Setelah login, langsung arahkan ke URL yang diinginkan
new_url = 'http://52.221.227.139/admin/create_warga'
driver.get(new_url)

# Tunggu sejenak untuk memberikan waktu agar proses menuju ke menu lain selesai
driver.implicitly_wait(5)

# Baca data dari file Excel menggunakan pandas
excel_path = 'C:/Users/marcs/Downloads/Documents/tes.xlsx'
df = pd.read_excel(excel_path)

df = df.iloc[::-1]

# Iterasi melalui setiap baris data dan isi formulir
for index, row in df.iterrows():
    # Ganti dengan nama field dan kolom DataFrame sesuai dengan halaman dan file Excel Anda
    field1 = driver.find_element(By.NAME, 'nama')
    field1.send_keys(row[3])  # Kolom D

    field2 = driver.find_element(By.NAME, 'alamat')
    field2.send_keys(row[4])  # Kolom E

    # Tambahkan langkah-langkah sesuai dengan jumlah kolom dan field pada formulir

    # Jika diperlukan, tambahkan tindakan untuk mengirim formulir
    submit_form_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_form_button.click()

    # Tunggu sejenak setelah mengirim formulir
    driver.implicitly_wait(5)

    # Kembali ke URL baru
    driver.get(new_url)

    # Tunggu sejenak untuk memberikan waktu agar proses menuju ke menu lain selesai
    driver.implicitly_wait(5)

# Tutup browser
driver.quit()

# Tutup browser
driver.quit()
