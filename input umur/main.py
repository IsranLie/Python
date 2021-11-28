umur = int(input("Masukan Umur : "))
if(umur >= 0 and umur <= 5):  
    kriteria = "Balita"
else:
    kriteria = "Tidak Diketahui"
if(umur > 5 and umur <= 13): 
    kriteria = "Anak-anak"
if(umur > 13 and umur <= 25): 
    kriteria = "Remaja"
if(umur > 25 and umur <= 35): 
    kriteria = "Dewasa"
if(umur > 35 and umur <= 55): 
    kriteria = "Paruhbaya"
if(umur > 55 and umur <= 100): 
    kriteria = "Lansia"
if(umur > 100): 
    kriteria = "Superior"

status = input("Status Menikah [Y/T]: ")
if status == 'Y' or status == 'y':
    status = "Sudah Menikah"
else:
    status = "Lajang"

print("--------------------------")
print("Umur           : %d Tahun"%(umur))
print("Kriteria Umur  : %s"%(kriteria))
print("Status Menikah :",status)
print()
print("Umur %d tahun dan Kriteria Umur yaitu %s"%(umur,kriteria))
print("dengan Status",status)

