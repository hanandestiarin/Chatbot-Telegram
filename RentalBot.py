import telebot
import mysql.connector
from telebot import types

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
    chat_id = message.chat.id

    custom = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('/start')
    b = types.KeyboardButton('/katalog')
    c = types.KeyboardButton('/harga')
    d = types.KeyboardButton('/sop')

    custom.row(a)
    custom.row(b)
    custom.row(c)
    custom.row(d)

    bot.send_message(
        chat_id, 'Selamat Datang Di Rental Mobil.\n\n'
        'Untuk melihat katalog silakan ketik /katalog\n\n'
        'Untuk melihat daftar harga silakan ketik /harga\n\n'
        'Untuk melihat Syarat Dan Ketentuan Yang Berlaku silakan ketik /sop', reply_markup=custom)


@bot.message_handler(commands=['harga'])
def detailharga(message):
    chat_id = message.chat.id

    custom = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('/Allin')
    b = types.KeyboardButton('/Mblsupir')
    c = types.KeyboardButton('/LpKunci')
    d = types.KeyboardButton('/wedding')
    e = types.KeyboardButton('/start')

    custom.row(a, b)
    custom.row(c, d)
    custom.row(e)

    bot.send_message(chat_id, 'Untuk melihat detail harga : '
                     '\nPrice List All In /Allin'
                     '\nPrice List Mobil Supir /Mblsupir'
                     '\nPrice List Lepas Kunci /LpKunci'
                     '\nPrice List Wedding Package /wedding'
                     '\nUntuk kembali ke menu awal silakan ketik /start', reply_markup=custom)


@bot.message_handler(commands=['katalog'])
def katalog(message):
    chat_id = message.chat.id

    custom = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('/mobil1')
    b = types.KeyboardButton('/mobil2')
    c = types.KeyboardButton('/mobil3')
    d = types.KeyboardButton('/mobil4')
    e = types.KeyboardButton('/mobil5')
    f = types.KeyboardButton('/mobil6')
    g = types.KeyboardButton('/mobil7')
    h = types.KeyboardButton('/mobil8')
    i = types.KeyboardButton('/mobil9')
    j = types.KeyboardButton('/mobil10')
    k = types.KeyboardButton('/mobil11')
    l = types.KeyboardButton('/mobil12')
    m = types.KeyboardButton('/mobil13')
    n = types.KeyboardButton('/mobil14')
    o = types.KeyboardButton('/mobil15')
    p = types.KeyboardButton('/mobil16')
    q = types.KeyboardButton('/start')

    custom.row(a, b, c, d)
    custom.row(e, f, g, h)
    custom.row(i, j, k, l)
    custom.row(m, n, o, p)
    custom.row(q)

    bot.send_message(chat_id, 'Untuk melihat jenis mobil : '
                     '\nAlphard Facelift /mobil1'
                     '\nAlphard Transformer /mobil2'
                     '\nMercy E 250 /mobil3'
                     '\nMercy E 300 /mobil4'
                     '\nMercy S 400 /mobil5'
                     '\nMercy S 450 /mobil6'
                     '\nPajero Sport Dakar /mobil7'
                     '\nFortuner Vrz-Trd /mobil8'
                     '\nElf Long /mobil9'
                     '\nHiace Commuter /mobil10'
                     '\nHyundai H1 /mobil11'
                     '\nCR-V Prestige /mobil12'
                     '\nInnova Reborn /mobil13'
                     '\nXPander Ultimate /mobil14'
                     '\nToyota Voxy /mobil15'
                     '\nCamry /mobil16'
                     '\n\nUntuk kembali ke menu awal silakan ketik /start', reply_markup=custom)


@bot.message_handler(commands=['mobil1'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('1.png', 'rb'))


@bot.message_handler(commands=['mobil2'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('2.png', 'rb'))


@bot.message_handler(commands=['mobil3'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('3.png', 'rb'))


@bot.message_handler(commands=['mobil4'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('4.png', 'rb'))


@bot.message_handler(commands=['mobil5'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('5.png', 'rb'))


@bot.message_handler(commands=['mobil6'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('6.png', 'rb'))


@bot.message_handler(commands=['mobil7'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('7.png', 'rb'))


@bot.message_handler(commands=['mobil8'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('8.png', 'rb'))


@bot.message_handler(commands=['mobil9'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('9.png', 'rb'))


@bot.message_handler(commands=['mobil10'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('10.png', 'rb'))


@bot.message_handler(commands=['mobil11'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('11.png', 'rb'))


@bot.message_handler(commands=['mobil12'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('12.png', 'rb'))


@bot.message_handler(commands=['mobil13'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('13.png', 'rb'))


@bot.message_handler(commands=['mobil14'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('14.png', 'rb'))


@bot.message_handler(commands=['mobil15'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('15.png', 'rb'))


@bot.message_handler(commands=['mobil16'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('16.png', 'rb'))


@bot.message_handler(commands=['sop'])
def sop(message):
    chat_id = message.chat.id

    custom = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('/sop_allin')
    b = types.KeyboardButton('/sop_mblsupir')
    c = types.KeyboardButton('/sop_Lpkunci')
    d = types.KeyboardButton('/sop_wedding')
    e = types.KeyboardButton('/start')

    custom.row(a, b)
    custom.row(c, d)
    custom.row(e)
    bot.send_message(
        chat_id, 'Untuk melihat detail Syarat Dan Ketentuan Yang Berlaku : '
        '\n\nSyarat Dan Ketentuan All In  silakan ketik /sop_allin'
        '\n\nSyarat Dan Ketentuan Mobil Supir silakan ketik /sop_mblsupir'
        '\n\nSyarat Dan Ketentuan Lepas Kunci siakan ketik /sop_Lpkunci'
        '\n\nSyarat Dan Ketentuan Wedding Package silakan ketik /sop_wedding'
        '\n\n Untuk kembali ke menu awal silakan ketik /start', reply_markup=custom)


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
def detailharga(message):
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
def sop(message):
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
def sop(message):
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
def sop(message):
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
def sop(message):
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
