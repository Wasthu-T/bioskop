# from datetime import date

# # create a date object representing March 1, 2023
# start_date = date(2023, 3, 1)

# # extract information such as the year, month, and day
# year = start_date.year
# month = start_date.month
# day = start_date.day

# # get the day of the week (Note: Monday is coded as 0, and Sunday as 6)
# weekday = start_date.weekday()

# # the date can be formatted as a string if needed
# date_str = start_date.strftime('%Y-%m-%d')
# print(date_str)

from datetime import datetime
import locale
# Meminta pengguna untuk memasukkan tanggal dalam format tertentu
locale.setlocale(locale.LC_TIME, 'id_ID')
# Mencoba mengonversi string ke objek datetime
try:
    date_str = input("Masukkan tanggal (format: YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d")
    date_only = date.date()
    day_name = date.strftime("%A")
    print("Tanggal yang dimasukkan (tanpa waktu):", date_only)
    print("Hari dari tanggal yang dimasukkan:", day_name)
except ValueError:
    print("Format tanggal salah. Pastikan format YYYY-MM-DD.")
# while True :
#     hari = str(input("Masukan hari : "))

#     if(hari in ('senin', 'selasa', 'rabu', 'kamis')) :
#         harga = 30000
#     elif hari == 'jumat' :
#         harga = 35000
#     elif(hari in ('sabtu','minggu')) :
#         harga = 40000
#     print(harga)
