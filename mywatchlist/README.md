# Tugas 3 PBP - Semester Ganjil 2022/2023

#### Link aplikasi heroku: https://pbp-tugas-deploy.herokuapp.com/mywatchlist/

#### Jawaban Pertanyaan

1. Jelaskan perbedaan antara JSON, XML, dan HTML!<br/>
   Jawab:<br/>
   HTML (Hyper Text Markup Language) adalah adalah standar *markup language* dokumen yang didesain untuk menampilkan sesuatu pada *web browser*. XML (eXtensible Markup Language) adalah *markup language* yang didesain menjadi *self-descriptive* dan digunakan untuk menyimpan dan memindahkan data. Dokumen XML membentuk struktur seperti tree yang dimulai dari root, lalu branch, hingga berakhir pada leaves. Dokumen XML harus mengandung sebuah root element yang merupakan parent dari elemen lainnya. Meskipun sama-sama merupakan *markup language*, keduanya memiliki fokus yang berbeda. XML lebih berfokus pada penyimpanan dan transfer data sedangkan HTML lebih berfokus pada presentasi data. XML hanyalah informasi yang dibungkus di dalam tag, sehingga masih perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut. JSON (JavaScript Object Notation) adalah format file yang didesain menjadi *self-describing*, sehingga JSON sangat mudah untuk dimengerti. JSON digunakan untuk menyimpan dan mentransmisi data. Salah satu perbedaan utama JSON dan XML adalah XML memiliki lebih banyak fungsionalitas karena merupakan *markup language*, sedangkan JSON hanyalah sebuah *data-interchange format*. Meskipun demikian JSON juga memiliki kelebihan, yaitu lebih mudah diimplementasikan dan diakses daripada XML, juga lebih cepat.
   
2. Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah *platform*?<br/>
   Jawab:<br/>
   Dalam pengembangan *platform*, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Sebuah *platform* pasti berinteraksi dengan pengguna dan data, *data delivery* adalah cara *platform* mengirimkan data tersebut. Data yang dikirimkan bisa bermacam-macam bentuknya. Contoh format data yang umum digunakan adalah HTML, XML, dan JSON.
   
3. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.<br/>
   Jawab:<br/>
   Hal pertama yang harus dilakukan adalah membuat aplikasi mywatchlist menggunakan *command* `python manage.py startapp`. Kemudian, buat objek MyWatchList pada `models.py` dengan atribut elemen kolom-kolom tabel yang akan ditampilkan, data awal watchlist dalam format JSON, dan *template* untuk penyajian di *web browser* dengan HTML. Selanjutnya, kita harus menghubungkan `models.py` dengan `views.py`, `views.py` berisi fungsi yang akan melakukan pengambilan data dari `models.py` dan dikembalikan ke dalam sebuah *file template* HTML. Objek pada `models.py` diakses/diambil dari `views.py` dan disimpan pada suatu variabel dalam bentuk *QuerySet* dengan *method .objects.all()* yang tersedia pada Django. Kemudian, `views.py` dihubungkan dengan *template* berupa sebuah *file* HTML pada direktori bernama "templates" dengan menggunakan fungsi yang ada pada *django.shortcuts*, yaitu *render()* -> *render(request, template_name, context=None, content_type=None, status=None, using=None)*. Fungsi ini akan mengaplikasikan parameter *context* yang diberikan pada template dan mengembalikan objek HttpResponse. Disini, *template_name* adalah nama *file* HTML pada direktori bernama "templates" dan *context*-nya berisi nama, *student id* (NPM) dan *QuerySet* dari objek pada `models.py` yang sudah didefinisikan sebelumnya. Data delivery dengan XML dan JSON diimplementasikan menggunakan *serialzers*.
   
   Dalam direktori aplikasi, ada juga `urls.py` yang berfungsi untuk melakukan *routing* terhadap fungsi pada `views.py` sehingga halaman HTML dapat ditampilkan pada *browser* internet. Fungsi yang digunakan adalah fungsi yang ada pada *django.urls*, yaitu *path()* -> *path(route, view, kwargs=None, name=None)* dengan *route* *string* kosong, *view* nama fungsi pada `views.py` dan *name* berupa *string* dari nama fungsi pada `views.py`. Aplikasi ini juga harus didaftarkan pada `urls.py` dalam folder proyek Django dengan menggunakan fungsi *path()* juga dengan '/[nama_aplikasi]' dan menggunakan *include([nama_aplikasi].urls)* parameter *include()* tersebut me-*refer* `urls.py` pada direktori aplikasi.
   
   Pada *file* HTML, atribut-atribut dari objek yang disimpan dalam *QuerySet* diakses dengan menggunakan *for loop* untuk mengisi tabel. Sintaksnya sedikit mirip dengan sintaks *for loop* biasa pada python, yaitu {% for [elemen_*QuerySet*] in [*QuerySet*] %} dan {{[elemen_*QuerySet*].[nama_atribut]}} yang dibungkus dengan *tag* th HTML (*header cell* pada tabel HTML).
   
   Pada *template source code* yang diberikan, semua *dependencies dan dpl.yml* sudah dibuat dan konfigurasi `settings.py` sudah disesuaikan, sehingga langkah *deployment* aplikasi ke heroku yang masih perlu dilakukan hanyalah memodifikasi sedikit *procfile* untuk me-*load* data awal dan memasukkan nama aplikasi yang sudah dibuat dan *API key* akun heroku ke *repository secret* (simpan juga keduanya pada suatu file teks). Kemudian *deployment* yang sebelumnya gagal pada bagian *Actions* di *repository* dijalankan ulang.

#### Screenshot Postman
![postman-1](https://github.com/syadzaarrana/Tugas-PBP/blob/main/postman/1.png?raw=true)<br/>
![postman-2](https://github.com/syadzaarrana/Tugas-PBP/blob/main/postman/2.png?raw=true)<br/>
![postman-3](https://github.com/syadzaarrana/Tugas-PBP/blob/main/postman/3.png?raw=true)<br/>
![postman-4](https://github.com/syadzaarrana/Tugas-PBP/blob/main/postman/4.png?raw=true)<br/>
![postman-5](https://github.com/syadzaarrana/Tugas-PBP/blob/main/postman/5.png?raw=true)<br/>
![postman-6](https://github.com/syadzaarrana/Tugas-PBP/blob/main/postman/6.png?raw=true)<br/>
