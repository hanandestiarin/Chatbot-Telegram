import telebot
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database='harga')

# cek database sudah bisa diakses atau belum
print(mydb)
# memberi input ke sql
sql = mydb.cursor()

api = '1805788621:AAG6FAFBNcvkL6wi6reK1l2r-AC_BQbW-Xg'
bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    nama = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    bot.reply_to(
        message, 'Selamat Datang Di Rental Mobil.\nHalo {} {}\n'.format(nama, nama_akhir))


@bot.message_handler(commands=['harga'])
def harga(message):
    bot.reply_to(
        message, 'Untuk melihat detail harga : '
        '\nPrice List All In /Allin'
        '\nPrice List Mobil Supir /Mblsupir'
        '\nPrice List Lepas Kunci /LpKunci'
        '\nPrice List Wedding Package /wedding')


@bot.message_handler(commands=['sop'])
def harga(message):
    bot.reply_to(
        message, 'Untuk melihat Syarat Dan Ketentuan Yang Berlaku : '
        '\n\nSyarat Dan Ketentuan All In /sop_allin'
        '\n\nSyarat Dan Ketentuan Mobil Supir /sop_mblsupir'
        '\n\nSyarat Dan Ketentuan Lepas Kunci /sop_Lpkunci'
        '\n\nSyarat Dan Ketentuan Wedding Package /sop_wedding')


@bot.message_handler(commands=['Allin'])
def detailharga(message):
    chat_id = message.chat.id
    # input sql
    sql.execute(
        "select*from all_in")
    hasil_sql = sql.fetchall()
    # print(hasil_sql)
    # pesan  yang dikirim oleh bot
    for x in hasil_sql:
        nama_kendaran = x[0]
        type_kendaran = x[1]
        thn_pembuatan = x[2]
        warna = x[3]
        harga_dlm = x[4]
        pesan = "Price List All In : \n\nNama Kendaran : %s\nType Kendaran : %s\nTahun Pembuatan : %s\nWarna kendaran : %s\nHarga Dalam Kota : %s\nDurasi : Per hari/tanggal Cut Off Jam 23:59" % (
            nama_kendaran, type_kendaran, thn_pembuatan, warna, harga_dlm)
        bot.send_message(chat_id, pesan)


@bot.message_handler(commands=['Mblsupir'])
def detailharga(message):
    chat_id = message.chat.id
    # input sql
    sql.execute(
        "select*from mbl_spr")
    hasil_sql = sql.fetchall()
    # print(hasil_sql)
    # pesan  yang dikirim oleh bot
    for x in hasil_sql:
        nama_kendaran = x[0]
        type_kendaran = x[1]
        thn_pembuatan = x[2]
        warna = x[3]
        harga_dlm = x[4]
        harga_luar = x[5]
        pesan = "Price List Mobil Supir : \n\nNama Kendaran : %s\nType Kendaran : %s\nTahun Pembuatan : %s\nWarna kendaran : %s\nHarga Dalam Kota: %s\nHarga Luar Kota : %s\nDurasi : Per hari/tanggal Cut Off Jam 23:59" % (
            nama_kendaran, type_kendaran, thn_pembuatan, warna, harga_dlm, harga_luar)
        bot.send_message(chat_id, pesan)


@bot.message_handler(commands=['LpKunci'])
def detailharga(message):
    chat_id = message.chat.id
    # input sql
    sql.execute(
        "select*from lepas_kunci")
    hasil_sql = sql.fetchall()
    # print(hasil_sql)
    # pesan  yang dikirim oleh bot
    for x in hasil_sql:
        nama_kendaran = x[0]
        type_kendaran = x[1]
        thn_pembuatan = x[2]
        warna = x[3]
        harga_dlm = x[4]
        harga_luar = x[5]
        pesan = "Price List Lepas Kunci : \n\nNama Kendaran : %s\nType Kendaran : %s\nTahun Pembuatan : %s\nWarna kendaran : %s\nHarga Dalam Kota: %s\nHarga Luar Kota : %s\nDurasi : Per hari/tanggal Cut Off Jam 23:59\n" % (
            nama_kendaran, type_kendaran, thn_pembuatan, warna, harga_dlm, harga_luar)
        bot.send_message(chat_id, pesan)


@bot.message_handler(commands=['wedding'])
def harga(message):
    bot.reply_to(
        message, 'Price List Wedding Package : \n\n'
        'Jenis Kendaraan : Alphard G \nType Kendaran : Facelift \nTahun Pembuatan : 2019 \nWarna Kendaraan : Hitam \n12 Jam All In : Rp. 2.900.000 \n12 Jam : Rp. 2.600.000\nAll In (Driver + BBM + Tol + Parkir).\n\n'
        'Jenis Kendaraan : Alphard G \nType Kendaran : Transformer \nTahun Pembuatan : 2017 Up \nWarna Kendaraan : Hitam, Putih \n12 Jam All In : Rp. 2.800.000 \n12 Jam : Rp. 2.500.000\nAll In (Driver + BBM + Tol + Parkir).\n\n'
        'Jenis Kendaraan : Mecedez-Benz \nType Kendaran : E250 \nTahun Pembuatan : 2018 Up \nWarna Kendaraan : Hitam \n12 Jam All In : Rp. 4.000.000 \n12 Jam : Rp. 3.500.000\nAll In (Driver + BBM + Tol + Parkir).\n\n'
        'Jenis Kendaraan : Mecedez-Benz \nType Kendaran : E300 AMG \nTahun Pembuatan : 2018 \nWarna Kendaraan : Hitam, Putih \n12 Jam All In : Rp. 3.500.000 \n12 Jam : Rp. 3.000.000\nAll In (Driver + BBM + Tol + Parkir).\n\n'
        'Jenis Kendaraan : Mecedez-Benz \nType Kendaran : S400 \nTahun Pembuatan : 2018 \nWarna Kendaraan : Hitam \nDari 05.00 - 22.59 : Rp. 14.000.000 \n12 Jam : Rp. 10.500.000\nAll In (Driver + BBM + Tol + Parkir).\n\n'
        'Jenis Kendaraan : Mecedez-Benz \nType Kendaran : S450 \nTahun Pembuatan : 2018 \nWarna Kendaraan : Hitam \nDari 05.00 - 22.59 : Rp. 16.500.000 \n12 Jam : Rp. 12.500.000\nAll In (Driver + BBM + Tol + Parkir).\n\n'
        'Jenis Kendaraan : CR-V Turbo \nType Kendaran : Prestige \nTahun Pembuatan : 2019 \nWarna Kendaraan : Hitam \nHarga Dalam Kota : Rp. 2.500.000 \nHarga Luar Kota : Rp. 2.300.000\nAll In (Driver + BBM + Tol + Parkir).\n\n'
        'Jenis Kendaraan : Toyota Camry \nType Kendaran : 2.5 V A/T \nTahun Pembuatan : 2019 \nWarna Kendaraan : Hitam \nHarga Dalam Kota : Rp. 2.100.000 \nHarga Luar Kota : Rp. 1.800.000\nAll In (Driver + BBM + Tol + Parkir).\n\n')


@bot.message_handler(commands=['sop_allin'])
def detailharga(message):
    chat_id = message.chat.id
    # input sql
    sql.execute(
        "select*from sop_allin")
    hasil_sql = sql.fetchall()
    # print(hasil_sql)
    # pesan  yang dikirim oleh bot
    for x in hasil_sql:
        ke1 = x[0]
        ke2 = x[1]
        ke3 = x[2]
        ke4 = x[3]
        ke5 = x[4]
        ke6 = x[5]
        ke7 = x[6]
        ke8 = x[7]
        ke9 = x[8]
        pesan = "Syarat Dan Ketentuan All In: \n\n1. %s\n\n2. %s\n\n3. %s\n\n4. %s\n\n5. %s\n\n6. %s\n\n7. %s\n\n8. %s\n\n9. %s" % (
            ke1, ke2, ke3, ke4, ke5, ke6, ke7, ke8, ke9)
        bot.send_message(chat_id, pesan)


@bot.message_handler(commands=['sop_mblsupir'])
def detailharga(message):
    chat_id = message.chat.id
    # input sql
    sql.execute(
        "select*from sop_ms")
    hasil_sql = sql.fetchall()
    # print(hasil_sql)
    # pesan  yang dikirim oleh bot
    for x in hasil_sql:
        ke1 = x[0]
        ke2 = x[1]
        ke3 = x[2]
        ke4 = x[3]
        ke5 = x[4]
        ke6 = x[5]
        ke7 = x[6]
        ke8 = x[7]
        ke9 = x[8]
        pesan = "Syarat Dan Ketentuan Mobil Supir: \n\n1. %s\n\n2. %s\n\n3. %s\n\n4. %s\n\n5. %s\n\n6. %s\n\n7. %s\n\n8. %s\n\n9. %s" % (
            ke1, ke2, ke3, ke4, ke5, ke6, ke7, ke8, ke9)
        bot.send_message(chat_id, pesan)


@bot.message_handler(commands=['sop_Lpkunci'])
def detailharga(message):
    chat_id = message.chat.id
    # input sql
    sql.execute(
        "select*from sop_lk")
    hasil_sql = sql.fetchall()
    # print(hasil_sql)
    # pesan  yang dikirim oleh bot
    for x in hasil_sql:
        ke1 = x[0]
        ke2 = x[1]
        ke3 = x[2]
        ke4 = x[3]
        ke5 = x[4]
        ke6 = x[5]
        ke7 = x[6]
        ke8 = x[7]
        ke9 = x[8]
        pesan = "Syarat Dan Ketentuan Lepas Kunci: \n\n1. %s\n\n2. %s\n\n3. %s\n\n4. %s\n\n5. %s\n\n6. %s\n\n7. %s\n\n8. %s\n\n9. %s" % (
            ke1, ke2, ke3, ke4, ke5, ke6, ke7, ke8, ke9)
        bot.send_message(chat_id, pesan)


@bot.message_handler(commands=['sop_wedding'])
def detailharga(message):
    chat_id = message.chat.id
    # input sql
    sql.execute(
        "select*from sop_wedding")
    hasil_sql = sql.fetchall()
    # print(hasil_sql)
    # pesan  yang dikirim oleh bot
    for x in hasil_sql:
        ke1 = x[0]
        ke2 = x[1]
        ke3 = x[2]
        ke4 = x[3]
        ke5 = x[4]
        ke6 = x[5]
        ke7 = x[6]
        ke8 = x[7]
        pesan = "Syarat Dan Ketentuan Wedding Package: \n\n1. %s\n\n2. %s\n\n3. %s\n\n4. %s\n\n5. %s\n\n6. %s\n\n7. %s\n\n8. %s\n\n" % (
            ke1, ke2, ke3, ke4, ke5, ke6, ke7, ke8)
        bot.send_message(chat_id, pesan)
    # memperbagus balasan bot
    # menghilangkan koma


print('bot start running')
bot.polling()
