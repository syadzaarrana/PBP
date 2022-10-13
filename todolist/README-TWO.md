# Tugas 6 PBP - Semester Ganjil 2022/2023

#### Link aplikasi heroku: https://pbp-tugas-deploy.herokuapp.com/todolist/
#### Test users: user_test1 (password: test1todolist) & user_test2 (password: test2todolist)

#### Jawaban Pertanyaan
1. Jelaskan perbedaan antara *asynchronous programming* dengan *synchronous programming*.<br/>
   Jawab:<br/>
   *Asynchronous programming* adalah pendekatan *programming* yang setiap eksekusi pekerjaannya dilakukan secara *independennt*, tidak terikat dengan proses/pekerjaan lainnya. *Synchronous programming* adalah pendekatan *programming* yang proses/pekerjaannya saling terikat. Jadi, perbedaan utama *asynchronous programming* dengan *synchronous programming* adalah dalam mengeksekusi pekerjaanya, *asynchronous programming* tidak bergantung pada pekerjaan lain atau dapat dibilang tidak perlu menunggu pekerjaan lain diproses sedangkan *synchronous programming* pekerjaan satu dengan yang lainnya saling terikat.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma *Event-Driven Programming*. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.<br/>
   Jawab:<br/>
   *Event-Driven Programming* adalah paradigma dimana *flow* program bergantung pada suatu *event*, contohnya *user actions*. Program akan selalu menunggu *event* apapun yang masuk dan bekerja sesuai dengan *event* tersebut. Contoh penerapannya pada tugas ini adalah pada saat AJAX meng-*update* halaman sesuai dengan *user actions* seperti menambahkan *task*

3. Jelaskan penerapan *asynchronous programming* pada AJAX.<br/>
   Jawab:<br/>
   Pada tugas ini, dapat dilihat pada bagian script ada *async function*, ini adalah contoh *asynchronous programming* pada AJAX, *function* yang meng-*update* halaman dijalankan secara *asynchronous* tanpa perlu *reload* seluruh halaman. Proses ini berjalan secara *independent* tanpa menunggu atau bergantung pada proses/*event* lain yang terjadi.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.<br/>
   Jawab:<br/>
   Pertama, membuat fungsi baru pada yang mengembalikan JSONResponse kemudian dihubungkan pada url todolist/json. Isi dari *div row* sekarang adalah *output* dari fungsi asinkronus loadCards(), fungsi yang secara asinkronus akan meng-*update* bagian halaman tersebut dengan fetch() url JSONResponse sebelumnya kemudian *looping* hasilnya untuk ditampilkan. Lalu, memindahkan *form* pembuatan *task* baru pada html yang sama untuk dijadikan Bootstrap Modal. Tombol yang tadinya menggunakan *form action* sekarang diganti menjadi format *trigger* modal seperti yang ada pada dokumentasi Bootstrap dan *form*-nya dimasukkan ke *modal-body*. Lalu tombol *Create Task* sekarang tidak menjadi tipe submit lagi karena di*return false* dan diubah menjadi terhubung ke fungsi addTask() pada *script* yang memanggil lagi fungsi addTask() pada *views*, kemudian akan otomatis menjalankan loadCards() *script* di akhirnya.