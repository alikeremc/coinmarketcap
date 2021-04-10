import requests
import json
from tkinter import *
import sqlite3

con = sqlite3.connect('coin.db')
cursor = con.cursor()

def db_doldur():
    # Tabloyu düşürüyoruz.
    cursor.execute("DROP TABLE coin")
    con.commit()

    # Tabloyu oluşturuyoruz (Yoksa)
    cursor.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT, "
                   "amount INTEGER, price REAL)")
    con.commit()

    cursor.execute("insert into coin values (1, 'BTC', 3, 45000)")
    con.commit()

    cursor.execute("insert into coin values (?,?,?,?)", (2, 'ADA', 300, 1.20))
    con.commit()

    cursor.execute("insert into coin values (3, 'LTC', 48, 185)")
    con.commit()


def rgb_color(rgb):
    return '#%02x%02x%02x' % rgb

def font_color_pl(para):
    if para > 0:
        return "green"
    elif para == 0:
        return "grey"
    else:
        return "red"


def turkish_formatla(para):
    binlik_ayrac = ","
    ondalik_ayrac = "."

    currency = "{:,.2f}".format(para)

    if binlik_ayrac == '.':
        tamsayi_kisim = currency.split('.')[0]
        ondalik_kisim = currency.split('.')[1]

        yeni_tamsayi_kisim = tamsayi_kisim.replace(',', '.')
        currency = yeni_tamsayi_kisim + ondalik_ayrac + ondalik_kisim + " TL"
    else:
        currency = '$' + currency

    return currency


def center_window(w=300, h=200):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency"
                               "/listings/latest?start=1&limit=10&convert=USD&"
                               "CMC_PRO_API_KEY=f1e4d2c9-ca98-4890-8b29-70ee91a81a86")

    result = json.loads(api_request.content)


    # print(result)

    # total count
    # print("Total count:", result["status"]["total_count"])

    # sepet = [
    #     {
    #         "sembol": "BTC",
    #         "miktar": 3,
    #         "fiyat": 60000
    #     },
    #     {
    #         "sembol": "ADA",
    #         "miktar": 300,
    #         "fiyat": 1.20
    #     },
    #     {
    #         "sembol": "LTC",
    #         "miktar": 48,
    #         "fiyat": 185
    #     }
    #
    # ]

    cursor.execute("SELECT * from coin order by id")
    sepet = cursor.fetchall()



    # print('----------------------')

    portfoy_karzarar = 0

    all_amount_paid = 0

    satir_no = 1

    for i in range(10):
        for coin in sepet:
            if result["data"][i]["symbol"] == coin[1]:
                yuvarlak_current = round(result["data"][i]["quote"]["USD"]["price"], 2)
                coin_basina_karzarar = yuvarlak_current - coin[3]
                toplam_maliyet = coin[2] * coin[3]
                toplam_karzarar = coin_basina_karzarar * coin[2]
                portfoy_karzarar = portfoy_karzarar + toplam_karzarar

                name = Label(window, text=coin[1], bg='#d1d1cf', fg='black',
                             borderwidth=2, relief='groove', padx=2, pady=2,
                             font='Lato 12')
                name.grid(row=satir_no, column=0, sticky=N+S+W+E)

                price = Label(window, text=turkish_formatla(coin[3]), fg='black',
                              bg='#d1d1cf',
                              borderwidth = 2, relief = 'groove', padx = 2, pady = 2,
                              font='Lato 12')
                price.grid(row=satir_no, column=1, sticky=N+S+W+E)

                no_coins = Label(window, text=coin[2], bg='#d1d1cf', fg='black',
                                 borderwidth=2, relief='groove', padx=2, pady=2,
                                 font='Lato 12')
                no_coins.grid(row=satir_no, column=2, sticky=N+S+W+E)

                amount_paid = Label(window, text=turkish_formatla(toplam_maliyet), fg='black',
                                    bg='#d1d1cf',
                                    borderwidth=2, relief='groove', padx=2, pady=2,
                                    font='Lato 12')
                amount_paid.grid(row=satir_no, column=3, sticky=N+S+W+E)

                all_amount_paid = all_amount_paid + toplam_maliyet



                current_val = Label(window, text=turkish_formatla(yuvarlak_current),
                                    bg='#d1d1cf', fg='black',
                                    borderwidth=2, relief='groove', padx=2, pady=2,
                                    font='Lato 12')
                current_val.grid(row=satir_no, column=4, sticky=N+S+W+E)

                pl_coin = Label(window, text=turkish_formatla(coin_basina_karzarar),
                                fg=font_color_pl(coin_basina_karzarar),
                                bg='#d1d1cf',
                                borderwidth=2, relief='groove', padx=2, pady=2,
                                font='Lato 12')
                pl_coin.grid(row=satir_no, column=5, sticky=N+S+W+E)

                total_pl = Label(window, text=turkish_formatla(toplam_karzarar),
                                 bg='#d1d1cf', fg=font_color_pl(toplam_karzarar),
                                 borderwidth=2, relief='groove', padx=2, pady=2,
                                 font='Lato 12', anchor='e')
                total_pl.grid(row=satir_no, column=6, sticky=E+W)

                satir_no = satir_no + 1

    all_amount_paid_label = Label(window, text=turkish_formatla(all_amount_paid),
                         bg='#d1d1cf', fg='black',
                         borderwidth=2, relief='groove', padx=2, pady=2,
                         font='Lato 12')
    all_amount_paid_label.grid(row=satir_no, column=3, sticky=N + S + W + E)

    portfolio_pl = Label(window, text=turkish_formatla(portfoy_karzarar),
                     bg='#d1d1cf', fg=font_color_pl(portfoy_karzarar),
                     borderwidth=2, relief='groove', padx=2, pady=2,
                     font='Lato 12', anchor='e')
    portfolio_pl.grid(row=satir_no, column=6, sticky=N + S + W + E)

    update_button = Button(window, text="Update",
                         bg='blue', fg='white',
                         borderwidth=2, relief='groove', padx=2, pady=2,
                         font='Lato 12 bold', command=my_portfolio)
    update_button.grid(row=satir_no+1, column=6, sticky=N + S + W + E)




window = Tk()
window.title('My Coin Portfolio')
window.iconbitmap('favicon.ico')

window.geometry('840x175')
center_window(840, 175)

name = Label(window, text='Coin Name', bg=rgb_color((0, 0, 128)), fg='white',
             font='Lato 12 bold', borderwidth=2, relief='groove', padx=5, pady=5)
name.grid(row=0, column=0, sticky=N+S+W+E)

price = Label(window, text='Price', bg=rgb_color((0, 0, 128)), fg='white',
              font='Lato 12 bold', borderwidth=2, relief='groove', padx=5, pady=5)
price.grid(row=0, column=1, sticky=N+S+W+E)

no_coins = Label(window, text='Coin Owned', bg=rgb_color((0, 0, 128)), fg='white',
                 font='Lato 12 bold', borderwidth=2, relief='groove', padx=5, pady=5)
no_coins.grid(row=0, column=2, sticky=N+S+W+E)

amount_paid = Label(window, text='Total Amount Paid', bg=rgb_color((0, 0, 128)), fg='white',
                    font='Lato 12 bold', borderwidth=2, relief='groove', padx=5, pady=5)
amount_paid.grid(row=0, column=3, sticky=N+S+W+E)

current_val = Label(window, text='Current Value', bg=rgb_color((0, 0, 128)), fg='white',
                    font='Lato 12 bold', borderwidth=2, relief='groove', padx=5, pady=5)
current_val.grid(row=0, column=4, sticky=N+S+W+E)

pl_coin = Label(window, text='P/L Per Coin', bg=rgb_color((0, 0, 128)), fg='white',
                font='Lato 12 bold', borderwidth=2, relief='groove', padx=5, pady=5)
pl_coin.grid(row=0, column=5, sticky=N+S+W+E)

total_pl = Label(window, text='Total P/L with Coin', bg=rgb_color((0, 0, 128)), fg='white',
                 font='Lato 12 bold', borderwidth=2, relief='groove', padx=5, pady=5)
total_pl.grid(row=0, column=6, sticky=N+S+W+E)

#db_doldur()
my_portfolio()
window.mainloop()

cursor.close()
con.close()



