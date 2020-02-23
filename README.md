# tugas si adarsh
1. install ya mongodbnya, kalo belum download, download anjing disini https://www.mongodb.com/download-center/community?jmp=docs, jangan lupa pilih .msi
2. run installernya ya, next2 aja lah sampe kelar
3. terus buka jupyter notebook, terus buka tuh data di C:\Users\<users>\<folder>\Data acquistion system\Notebooks, yg judulnya MongoDB connection and storage.ipynb
4. run aja biasa itu notebook, kalo belum ke install pymongo, ketika !pip install pymongo di jupyter, tungguin, kalo error internet kalian busuk
5. terus buka folder ini C:\Program Files\MongoDB\Server\4.2\bin, run yg mongo.exe lah
6. cek kopasan dari mba windy di grup yak, buat ngecek isi db
7. abis itu lu pade baru jalanin script.py di folder data acquistion system, jangan lupa ada beberapa yg diedit yaitu :
> ganti batch size, start, skiprowsnya kalo mau iseng2
>> ga diganti juga ga apa2 lah, udah gw ganti discriptna, bangke emang ada yg typo
8. abis itu udah deh cek db.posadressnya



list command buat di mongo.exe
1. show dbs = buat nampilin db yg kalian punya
2. use <nama db> = buat milih db yg kalian mau cek
3. show collectons = buat nampilin semua table yg ada di db
4. db.adresses.find().pretty() = ngecek isi table, kalo ada isinya selamat, anda berhasil
