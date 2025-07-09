print("=" *41)
print("Kalkulator Serba Guna Dua Angka")
print("=" *41)

def Kalkulator () :
    Angka1 = float(input("Masukan Angka Pertama: "))
    Angka2 = float(input("Masukan Angka Kedua: "))
    
    print("1.Tambah")
    print("2.Kurang")
    print("3.Kali")
    print("4.Bagi")
    operasi = input("Masukan Pilihan: ")
    
    if operasi == '1' :
        hasil = Angka1 + Angka2
        print (f"{Angka1} + {Angka2} = {hasil} ")
    elif operasi == '2' :
        hasil = Angka1 - Angka2 
        print (f"{Angka1} - {Angka2} = {hasil}")  
    elif operasi == '3' :
        hasil = Angka1 * Angka2 
        print (f"{Angka1} x {Angka2} = {hasil}")  
    elif operasi == '4' :
        hasil = Angka1 / Angka2 
        print (f"{Angka1} : {Angka2} = {hasil}")          
Kalkulator()        
    
    
    