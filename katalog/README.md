# Tugas 2 PBP - Semester Ganjil 2022/2023

#### Link aplikasi heroku: http://tugas2-pbp-syadza.herokuapp.com/katalog/

#### Jawaban Pertanyaan

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py,
   models.py, dan berkas html;<br/>
   Jawab:<br/>
   ![chart](https://github.com/syadzaarrana/PBP-Tugas-2/blob/main/flowchart.png?raw=true)<br/>
   Bagan ini menggambarkan alur pemrosesan *client http request*. *Request* akan diteruskan oleh `urls.py` ke `views.py`, kemudian fungsi pada `views.py` akan memrosesnya dengan menggunakan template HTML dan objek dari `models.py`. Implementasi hubungan `urls.py`, `views.py`, `models.py`, dan template HTML dijelaskan lebih lanjut pada jawaban pertanyaan nomor 3.

2. Jelaskan kenapa menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?<br/>
   Jawab:<br/>
   *Virtual environment* atau lingkungan virtual berfungsi untuk memisahkan pengaturan dan *package* yang diunduh (di-*install*) pada setiap proyek Django sehingga    perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Penggunaan *virtual environment* penting untuk memastikan proyek Django tidak          mengalami konflik dengan proyek lainnya, selain itu proyek yang berbeda juga dapat menggunakan versi Django yang berbeda jika menggunakan *virtual environment*.    Meskipun demikian, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*, akan tetapi akan rentan terhadap konflik. Oleh    karena itu, setiap proyek Django sebaiknya memiliki *virtual environment* sendiri.
   
3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.<br/>
   Jawab:<br/>
   Hal pertama yang harus dilakukan adalah menghubungkan `models.py` dengan `views.py`, `models.py` berisi *class object* dengan atribut elemen kolom-kolom tabel yang akan ditampilkan dan `views.py` berisi fungsi yang akan melakukan pengambilan data dari `models.py` dan dikembalikan ke dalam sebuah *file template* HTML. Objek pada `models.py` diakses/diambil dari `views.py` dan disimpan pada suatu variabel dalam bentuk *QuerySet* dengan *method .objects.all()* yang tersedia pada Django. Kemudian, `views.py` dihubungkan dengan *template* berupa sebuah *file* HTML pada direktori bernama "templates" dengan menggunakan fungsi yang ada pada *django.shortcuts*, yaitu *render()* -> *render(request, template_name, context=None, content_type=None, status=None, using=None)*. Fungsi ini akan mengaplikasikan parameter *context* yang diberikan pada template dan mengembalikan objek HttpResponse. Disini, *template_name* adalah nama *file* HTML pada direktori bernama "templates" dan *context*-nya berisi nama, *student id* (NPM) dan *QuerySet* dari objek pada `models.py` yang sudah didefinisikan sebelumnya.
   
   Dalam direktori aplikasi, ada juga `urls.py` yang berfungsi untuk melakukan *routing* terhadap fungsi pada `views.py` sehingga halaman HTML dapat ditampilkan pada *browser* internet. Fungsi yang digunakan adalah fungsi yang ada pada *django.urls*, yaitu *path()* -> *path(route, view, kwargs=None, name=None)* dengan *route* *string* kosong, *view* nama fungsi pada `views.py` dan *name* berupa *string* dari nama fungsi pada `views.py`. Aplikasi ini juga harus didaftarkan pada `urls.py` dalam folder proyek Django dengan menggunakan fungsi *path()* juga dengan '/[nama_aplikasi]' dan menggunakan *include([nama_aplikasi].urls)* parameter *include()* tersebut me-*refer* `urls.py` pada direktori aplikasi.
   
   Pada *file* HTML, atribut-atribut dari objek yang disimpan dalam *QuerySet* diakses dengan menggunakan *for loop* untuk mengisi tabel. Sintaksnya sedikit mirip dengan sintaks *for loop* biasa pada python, yaitu {% for [elemen_*QuerySet*] in [*QuerySet*] %} dan {{[elemen_*QuerySet*].[nama_atribut]}} yang dibungkus dengan *tag* th HTML (*header cell* pada tabel HTML).
   
   Pada *template source code* yang diberikan, semua *dependencies, procfile, dpl.yml* sudah dibuat dan konfigurasi `settings.py` sudah disesuaikan, sehingga langkah *deployment* aplikasi ke heroku yang masih perlu dilakukan hanyalah memasukkan nama aplikasi yang sudah dibuat dan *API key* akun heroku ke *repository secret* (simpan juga keduanya pada suatu file teks) dan menjalankan ulang *deployment* yang sebelumnya gagal pada bagian *Actions* di *repository*.
