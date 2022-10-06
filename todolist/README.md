# Tugas 4 PBP - Semester Ganjil 2022/2023

#### Link aplikasi heroku: https://pbp-tugas-deploy.herokuapp.com/todolist/
#### Test users: user_test1 (password: test1todolist) & user_test2 (password: test2todolist)

#### Jawaban Pertanyaan

1. Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?<br/>
   Jawab:<br/>
   csrf adalah singkatan dari Cross-Site Request Forgery. `{% csrf_token %}` adalah implementasi pencegahan Cross-Site Request Forgery attack oleh Django. Cross-Site Request Forgery attack adalah serangan eksploitasi website dimana perintah *unauthorized* dilakukan oleh pengguna yang dipercaya aplikasi web. Tag `{% csrf_token %}` membuat sebuah token pada *server-side* saat me-*render* halaman dan memastikan keberadaan token ini pada setiap *request* yang masuk. *Request* yang tidak memiliki token ini tidak akan dieksekusi.

2. Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.<br/>
   Jawab:<br/>
   Ya, kita dapat membuat `<form>` secara manual. Caranya adalah dengan membungkusnya dalam tag `<form></form>` kemudian menggunakan `<table></table>`, `<tr></tr>`, `<th></th>`, dan `<td></td>` sebagaimana membuat tabel biasa (jika formatnya ingin seperti tabel) dan membuat button submit sendiri (*input type submit*). Jika dibutuhkan, juga dapat digunakan for loop dan conditional. Contoh pembuatan `<form>` secara manual ada pada form login aplikasi ini (`login.html`). Template form ini terhubung pada suatu fungsi pada `views.py` yang mengembalikan `HttpResponse`.

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.<br/>
   Jawab:<br/>
   Pertama, *user* memasukkan *address* (*http://host/path*) dan mengirimkan `HTTP Request` ke *address* tersebut (dari browser ke server). Server menerima `HTTP Request` dan mencari fungsi yang meng-*handle* path tersebut pada `views.py`. Kemudian, akan di-*generate* halaman HTML Form yang akan dikirim kembali ke browser dan ditampilkan. Selanjutnya, pengguna mengisi form tersebut dan browser mengirimkan lagi `HTTP Request`, *method* (POST, dll), dan argumen ke url tujuan berdasarkan format HTML Form. Server akan menerima `HTTP Request` yang dikirimkan dan mencari fungsi yang meng-*handle* path tersebut pada `views.py`. Terakhir, setelah *handling* `HTTP Request` (dapat berupa menyimpan data pada *database* dll) server akan kembali mengirimkan halaman HTML sebagai *response* ke browser untuk ditampilkan.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.<br/>
   Jawab:<br/>
   Hal pertama yang harus dilakukan adalah membuat aplikasi todolist menggunakan *command* `python manage.py startapp`. Kemudian, buat objek Task pada `models.py` dengan atribut elemen kolom-kolom tabel yang akan ditampilkan dan *template* untuk penyajian di *web browser* dengan HTML. Selanjutnya, kita harus menghubungkan `models.py` dengan `views.py`, `views.py` berisi fungsi yang akan melakukan pengambilan data dari `models.py` dan dikembalikan ke dalam sebuah *file template* HTML. Objek pada `models.py` diakses/diambil dari `views.py` dan disimpan pada suatu variabel dalam bentuk *QuerySet* dengan *method .objects.filter(user=request.user).order_by('is_finished')* (filter data *user* tersebut dan urutkan berdasarkan status penyelesaian *task*) yang tersedia pada Django. Kemudian, `views.py` dihubungkan dengan *template* berupa sebuah *file* HTML pada direktori bernama "templates" dengan menggunakan fungsi yang ada pada *django.shortcuts*, yaitu *render()* -> *render(request, template_name, context=None, content_type=None, status=None, using=None)*. Fungsi ini akan mengaplikasikan parameter *context* yang diberikan pada template dan mengembalikan objek HttpResponse. Disini, *template_name* adalah nama *file* HTML pada direktori bernama "templates" dan *context*-nya berisi *QuerySet* dari objek pada `models.py` yang sudah didefinisikan sebelumnya.
   
   Pada aplikasi ini, ada fitur registrasi akun, login, logout, membuat *task* baru, meng-*update* status penyelesaian *task*, dan menghapus *task* sehingga untuk semua fitur harus dibuat fungsi yang meng-*handle*-nya dan dimasukkan juga path urlnya di `urls.py` aplikasi ini. Halaman *todolist* juga hanya dapat ditampikan setelah *user login* sehingga digunakan *decorator* `@login_required(login_url='/todolist/login/')` yang berfungsi memastikan hal itu. Fitur registrasi akun, login, dan membuat *task* baru juga memiliki format HTML-nya masing-masing berupa form.
   
   Dalam direktori aplikasi, ada juga `urls.py` yang berfungsi untuk melakukan *routing* terhadap fungsi pada `views.py` sehingga halaman HTML dapat ditampilkan pada *browser* internet. Fungsi yang digunakan adalah fungsi yang ada pada *django.urls*, yaitu *path()* -> *path(route, view, kwargs=None, name=None)* dengan *route* *string* kosong, *view* nama fungsi pada `views.py` dan *name* berupa *string* dari nama fungsi pada `views.py`. Aplikasi ini juga harus didaftarkan pada `urls.py` dalam folder proyek Django dengan menggunakan fungsi *path()* juga dengan '/[nama_aplikasi]' dan menggunakan *include([nama_aplikasi].urls)* parameter *include()* tersebut me-*refer* `urls.py` pada direktori aplikasi. Karena *repository* ini sudah memiliki *deployment*, kita hanya perlu menjalankan kembali *failed jobs* pada *Actions* di *repository* untuk menyertakan aplikasi baru ini (todolist).


# Tugas 5 PBP - Semester Ganjil 2022/2023

#### Jawaban Pertanyaan

1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style? <br/>
Jawab:<br/>
- Inline style: terletak di dalam tag (pros:priority tertinggi dan lebih spesifik, cons:bisa *redundant* dan lebih sulit di-*maintain* karena kurang terorganisir)<br/>
- Internal style: terletak di dalam file yang sama, namun pendefinisiannya menggunakan selector dan pada bagian sendiri, tidak dalam masing-masing tag, tetapi dalam tag style (pros:lebih terorganisir dan tidak perlu mengunggah beberapa file, cons:file size menjadi besar)<br/>
- External style: terletak pada file terpisah, pendefinisiannya menggunakan selector, dan harus di-*load* untuk digunakan (pros:lebih terorganisir dan mudah di-*maintain*, cons:prioritas terendah, harus mengunggah file terpisah)<br/>

2. Jelaskan tag HTML5 yang kamu ketahui.<br/>
Jawab:<br/>
- a tag: sebagai *hyperlink*
- article tag: untuk membuat format artikel
- form tag: untuk membuat formulir, ada atribut action, method, dll
- blockquote tag: format mengutip
- button: membuat button, ada atribut action dll
- footer tag: format footer pada suatu dokumen
- head tag: bagian head, seperti title
- header tag: untuk membuat header dokumen atau section
- hgroup tag: kumpulan header
- label tag: Untuk membuat label, seperti username label diatas input field pada form
- li tag: membuat list
- link tag: menghubungkan dokumen dengan dokumen external, seperti untuk me-*load* external css
- nav tag: berisi link-link navigasi halaman
- picture tag: format gambar
- section tag: membagi-bagi halaman, seperti header dan footer
- svg tag: untuk menggunakan Scalable Vector Graphics
- dll

3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.<br/>
Jawab:<br/>
- Element Selector: berdasarkan tag, seperti div, p, h1, dll
- Id Selector: berdasarkan atribut id yang ada pada tag, di depannya menggunakan #
- Class Selector: berdasarkan atribut class yang ada pada tag, di depannya mengunakan .
- Universal Selector: seluruh dokumen, menggunakan *
- Group Selector: menggabungkan beberapa selector (jenis apapun), dipisahkan koma
- Attribute Selector: berdasarkan atribut seperti href, di dalam []

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.<br/>
Jawab:<br/>
Saya menggunakan bootstrap dengan styling external css dan inline css. Setiap task menggunakan class card pada bootstrap (menggunakan for loop), dengan 3 kolom/card perbaris. Halaman-halaman form juga menggunakan satu card yang ada di tengah. Untuk mem-format usercreationfor pada register, saya menggunakan crispy form bootstrap.
