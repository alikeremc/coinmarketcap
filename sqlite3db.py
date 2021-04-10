import sqlite3


def vt_baglan():
    con = sqlite3.connect('personel.db')
    return con


def tablo_dusur():
    con = vt_baglan()
    cursor = con.cursor()
    cursor.execute('drop table employees')
    con.commit()
    cursor.close()
    con.close()


def tablo_olustur():
    con = vt_baglan()
    cursor = con.cursor()
    cursor.execute(
        'create table employees(ID INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, position TEXT)')
    con.commit()
    cursor.close()
    con.close()


def tablo_insert():
    con = vt_baglan()
    cursor = con.cursor()
    cursor.execute("insert into employees values(1,'Ali Cevik',3000,'Bilgi İslem','Sef')")
    con.commit()
    cursor.close()
    con.close()


def tablo_insert2():
    con = vt_baglan()
    cursor = con.cursor()

    cursor.execute('insert into employees values(?,?,?,?,?)', (2, 'Aziz Sancar', 5000, 'Lab', 'DNA'))
    con.commit()
    cursor.close()
    con.close()


def tablo_select():
    con = vt_baglan()
    cursor = con.cursor()

    cursor.execute('select * from employees order by id')
    data = cursor.fetchall()

    print(data)
    print(data[0])
    print(data[0][1])

    cursor.close()
    con.close()

def tablo_update():
    con=vt_baglan()
    cursor=con.cursor()

    cursor.execute("update employees set salary=? where ID=?",(6000,1))
    con.commit()
    cursor.close()
    con.close()

def tablo_delete():
    con=vt_baglan()
    cursor=con.cursor()

    cursor.execute("delete from employees where ID=?",(1,))
    con.commit()
    cursor.close()
    con.close()

def kayit_sayisi():
    con = vt_baglan()
    cursor = con.cursor()

    cursor.execute('select count(*) from employees')
    data = cursor.fetchone()

    cursor.close()
    con.close()

    return data[0]





sayi = kayit_sayisi()
print('Kayıt sayısı:', sayi)

#tablo_dusur()
#tablo_olustur()
#tablo_insert()
#tablo_insert2()
#tablo_select()
#tablo_update()
#tablo_delete()

