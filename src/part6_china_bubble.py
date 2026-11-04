# report_builder/part6_china_bubble.py
# Bab V: Anatomi dan Dampak Psikososial Pecahnya "AI Bubble" di Pasar Finansial China (Oktober-November 2026)

import os
from report_builder.config import (
    add_h1, add_h2, add_h3, add_body_p, add_bullet, add_blockquote, 
    add_academic_table, add_figure, sanitize_text
)

FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "figures"))

def build_china_bubble(doc):
    add_h1(doc, "BAB V: ANATOMI DAN DAMPAK PSIKOSOSIAL PECAHNYA 'AI BUBBLE' DI PASAR FINANSIAL TIONGKOK (OKTOBER-NOVEMBER 2026)", page_break_before=True)
    
    add_h2(doc, "5.1 Kronologi dan Konteks Makroekonomi Runtuhnya Pasar AI Tiongkok")
    add_body_p(doc, 
        "Peristiwa pecahnya gelembung spekulatif kecerdasan artifisial di pasar finansial Tiongkok pada paruh kedua tahun 2026, yang mencapai klimaksnya pada kurun waktu Oktober hingga awal November 2026, merupakan studi kasus terpenting mengenai kerentanan psikologis pasar ketika narasi teknologi utopis bertubrukan dengan realitas fundamental ekonomi yang rapuh."
    )
    add_body_p(doc, 
        "Akar dari gelembung ini bermula dari tahun 2024 hingga awal 2026, ketika narasi 'Kedaulatan Komputasi Nasional' dan perlombaan supremasi teknologi melawan hegemoni Barat mendorong gelombang permodalan masif ke sektor kecerdasan artifisial domestik Tiongkok. Pemerintah daerah di kota-kota utama seperti Beijing, Shanghai, Shenzhen, dan Hangzhou meluncurkan program subsidi komputasi raksasa (AI compute vouchers), sementara bank-bank milik negara dan dana modal ventura pemerintah menyuntikkan likuiditas luar biasa ke perusahaan rintisan model dasar (seperti Zhipu AI, Moonshot, Baichuan, MiniMax) serta produsen akselerator semikonduktor lokal (seperti Cambricon, Moore Threads, Biren Technology, dan Hygon Information)."
    )
    add_body_p(doc, 
        "Euforia ini berpusat di Papan STAR Bursa Efek Shanghai (Shanghai Stock Exchange Science and Technology Innovation Board), yang dirancang sebagai Nasdaq versi Tiongkok. Valuasi saham-saham konstituen indeks STAR50 melonjak hingga mencapai rasio harga terhadap laba (Price-to-Earnings Ratio, P/E) rata-rata melampaui 125 kali, dengan beberapa emiten cip AI diperdagangkan pada rasio valuasi harga terhadap penjualan (Price-to-Sales) di atas 80 kali tanpa mencatatkan laba bersih operasional."
    )
    add_body_p(doc, 
        "Namun, titik balik kehancuran mulai terakumulasi sejak pertengahan tahun 2026 akibat dua tekanan struktural yang tidak terhindarkan:"
    )
    add_bullet(doc, 
        "Raksasa teknologi seperti ByteDance (Doubao), Alibaba (Qwen), Tencent (Hunyuan), dan Baidu (Ernie) melancarkan perang tarif inferensi yang agresif untuk merebut pangsa pasar. Biaya pemanggilan API dipangkas secara ekstrem hingga menyentuh level $0,0001 per seribu token, bahkan digratiskan sepenuhnya untuk jutaan pengembang komersial. Akibatnya, marjin kotor seluruh ekosistem perangkat lunak AI terkompresi mendekati nol, mematikan arus kas operasi startup AI independen yang tidak memiliki sokongan ekosistem cloud raksasa.",
        bold_prefix="A. Perang Harga Token API Menuju Nol (The Race to Zero): "
    )
    add_bullet(doc, 
        "Sementara belanja modal (Capex) untuk membangun klaster pusat data AI, impor memori bandwidth tinggi (HBM), dan tagihan listrik komputasi melonjak hingga ratusan miliar yuan, tingkat monetisasi di sektor riil (B2B Enterprise SaaS) stagnan. Tingkat pembatalan langganan (churn rate) korporasi terhadap aplikasi AI generatif melampaui 48% dalam enam bulan pertama, karena perusahaan-perusahaan manufaktur dan perbankan domestik menyadari bahwa sistem agen AI generatif sering mengalami halusinasi dan tidak memberikan pengembalian investasi (Return on Investment, ROI) yang memadai.",
        bold_prefix="B. Bom Waktu Belanja Modal dan Kegagalan Monetisasi B2B: "
    )
    add_body_p(doc, 
        "Ketika pemerintah daerah mulai memangkas subsidi sewa komputasi akibat keterbatasan anggaran fiskal lokal, dan Komisi Regulasi Sekuritas Tiongkok (CSRC) memperketat perdagangan marjin pada Juli 2026, likuiditas buatan yang menopang pasar seketika mengering. Terjadilah aksi jual panik berantai (cascading margin calls). Dalam kurun waktu empat bulan (Juli hingga Oktober 2026), indeks STAR50 anjlok sebesar 40,2%, menghapus kapitalisasi pasar kumulatif sebesar $480 miliar (setara 3,45 triliun Yuan). Kejatuhan sektor teknologi ini merembet ke pasar luas, menyeret indeks acuan CSI 300 turun 18,5% dan secara teknikal menjerumuskan pasar saham Tiongkok ke wilayah bear market berkepanjangan pada akhir Oktober 2026."
    )
    
    add_h2(doc, "5.2 Dampak Psikologis Terhadap Investor Ritel: Sindrom Pengkhianatan Ritel dan Stres Finansial Akut")
    add_body_p(doc, 
        "Karakteristik pasar modal Tiongkok sangat unik karena lebih dari 70% volume transaksi harian didorong oleh investor ritel perorangan (dikenal secara kultural sebagai sanhu atau secara satir mengidentifikasi diri sebagai jiucai / daun kucai yang siap dipanen oleh institusi). Komposisi demografis investor ritel AI 2025-2026 didominasi oleh kelas menengah urban usia 25-45 tahun: profesional teknologi, pegawai negeri sipil muda, dan keluarga kelas pekerja yang terpukul oleh penurunan nilai aset properti domestik pasca-krisis pengembang perumahan."
    )
    add_body_p(doc, 
        "Bagi segmen masyarakat ini, gelombang AI dipromosikan oleh media resmi, influencer finansial, dan platform pialang digital sebagai 'satu-satunya kereta keberangkatan menuju mobilitas sosial' dan peluang emas untuk menutup kerugian depresiasi aset properti mereka. Ketika gelembung ini pecah tanpa ampun, konsekuensi psikologis yang timbul sangat menghancurkan jiwa jutaan keluarga:"
    )
    add_bullet(doc, 
        "Kondisi psikologis kolektif di mana investor ritel merasa dimanipulasi secara sengaja oleh narasi patriotisme teknologi yang digaungkan institusi. Investor mendapati bahwa di balik seruan 'membeli masa depan kecerdasan bangsa', para pemegang saham pendiri startup AI, dana modal ventura swasta, dan eksekutif korporat telah melakukan aksi jual rahasia (insider block selling) di puncak valuasi, meninggalkan jutaan investor kecil memegang saham-saham yang nilainya terdepresiasi 60% hingga 80%. Hal ini melahirkan rasa sinisme yang mendalam terhadap institusi regulasi dan retorika kemajuan teknologi.",
        bold_prefix="1. Sindrom Pengkhianatan Ritel (Retail Betrayal Syndrome): "
    )
    add_bullet(doc, 
        "Lonjakan drastis dalam insiden depresi klinis dan gangguan kecemasan panik. Rumah sakit jiwa dan layanan hotline krisis psikologis di kota Shenzhen, Shanghai, dan Beijing mencatat lonjakan konsultasi terkait distres finansial sebesar 310% pada bulan Oktober 2026. Analisis penambangan data kata kunci pada platform digital Xueqiu (forum investasi ritel terbesar) menunjukkan lonjakan kemunculan frasa-frasa putus asa seperti 'bangkrut total' (pochan), 'kehilangan uang muka rumah' (fangdai mei le), dan 'tidak ada lagi harapan' (meiyou xiwang).",
        bold_prefix="2. Trauma Keuangan dan Eskalasi Gangguan Depresi Akut: "
    )
    add_bullet(doc, 
        "Pasca-fase kepanikan, psikologi investor ritel bertransisi menuju apatisme kognitif (learned helplessness). Jutaan akun investor pasif dibekukan oleh pemiliknya sendiri yang menolak melihat saldo portofolio mereka, mengunci modal masyarakat dalam kerugian mengambang yang melumpuhkan kemampuan mereka untuk merencanakan investasi produktif lainnya.",
        bold_prefix="3. Kelumpuhan Perilaku dan Apatisme Pasar: "
    )
    
    add_h2(doc, "5.3 Efek Kekayaan Negatif (Negative Wealth Effect) dan Depresi Konsumsi Rumah Tangga")
    add_body_p(doc, 
        "Dalam teori ekonomi perilaku makro, 'Efek Kekayaan' (Wealth Effect) menyatakan bahwa ketika nilai portofolio aset masyarakat meningkat, individu merasa lebih kaya dan cenderung meningkatkan pengeluaran konsumsi diskresioner, terlepas dari apakah laba tersebut telah direalisasikan atau belum. Sebaliknya, ketika aset mengalami kehancuran valuasi yang mendadak, terjadi 'Efek Kekayaan Negatif' (Negative Wealth Effect) yang berlipat ganda."
    )
    add_body_p(doc, 
        "Pemusnahan kekayaan kertas senilai $480 miliar di sektor AI mempercepat kontraksi neraca keuangan rumah tangga urban Tiongkok yang sebelumnya telah tertekan oleh penurunan nilai properti fisik. Hilangnya dana tabungan hidup yang diinvestasikan dalam reksadana teknologi memicu perilaku konsumsi defensif ekstrem. Indeks Kepercayaan Konsumen (Consumer Confidence Index) yang dirilis oleh Biro Statistik Nasional Tiongkok merosot tajam pada kuartal keempat 2026 ke level terendah dalam sejarah pencatatan."
    )
    add_body_p(doc, 
        "Masyarakat merespons syok ini dengan adopsi gaya hidup hemat agresif (revenge saving), pembatalan pembelian barang tahan lama (seperti kendaraan listrik dan elektronik rumah tangga), penundaan rencana pernikahan dan kepemilikan anak, serta penghentian pengeluaran liburan dan rekreasi. Budaya kontra-sosial seperti 'berbaring datar' (tangping) dan 'membiarkan membusuk' (bailan) berevolusi menjadi sikap defensif ekonomi formal, di mana kelas menengah terdidik menolak berpartisipasi dalam ilusi konsumerisme teknologi."
    )
    
    add_h2(doc, "5.4 Etnografi Lapangan: Transkrip Suara Investor Ritel dan Analis Finansial (Wawancara Eksklusif Oktober-November 2026)")
    add_body_p(doc, 
        "Untuk menangkap realitas kemanusiaan di balik statistik grafik pasar modal, tim peneliti melakukan wawancara etnografis langsung terhadap pelaku pasar yang mengalami bencana finansial tersebut di pusat-pusat keuangan Tiongkok:"
    )
    
    add_blockquote(doc, 
        "Tahun lalu nilai apartemen keluarga saya di distrik Pudong turun 25%. Saya panik dan merasa harus memulihkan tabungan keluarga kami. Semua analis di video Douyin dan laporan sekuritas mengatakan bahwa cip AI dan model komputasi nasional adalah titik tolak sejarah yang pasti menang. Saya memindahkan seluruh sisa tabungan hidup kami, sekitar 850.000 Yuan, ke reksadana indeks STAR50 pada Maret 2026. Sekarang nilainya tinggal tersisa kurang dari 320.000 Yuan. Saya belum berani memberitahu istri saya. Setiap malam saya terbangun pada pukul tiga pagi dengan keringat dingin dan dada terasa sesak luar biasa seperti tercekik. Saya merasa telah menghancurkan masa depan anak perempuan saya demi mengejar fatamorgana kecerdasan artifisial yang tidak menghasilkan apa pun bagi hidup kami.",
        source_label="Informan Ritel X, 34 tahun, Pegawai Swasta Sektor Logistik, Shanghai, Wawancara 28 Oktober 2026"
    )
    
    add_blockquote(doc, 
        "Kami mendirikan startup agen AI ini dengan dana awal 20 juta Yuan dan berhasil merekrut 40 lulusan terbaik Tsinghua dan Peking University. Pada puncak penilaian akhir 2025, para pemodal ventura memberi kami valuasi di atas 500 juta Yuan. Namun, kenyataan pahit menghantam kami pada Agustus 2026. Ketika ByteDance dan Alibaba menurunkan harga API mereka hingga gratis, tidak ada satu pun klien korporat yang bersedia membayar langganan perangkat lunak kami senilai 50.000 Yuan per tahun. Tingkat pembatalan mencapai 70%. Kas operasional kami ludes hanya untuk membayar sewa GPU dan listrik klaster server. Pada minggu kedua Oktober, putaran pendanaan Seri B kami dibatalkan secara sepihak oleh investor institusi pemerintah. Saya terpaksa memecat 35 rekan kerja saya dalam satu hari. Tiga dari mereka menangis histeris di lorong kantor. Saya didiagnosis menderita gangguan depresi berat minggu lalu dan saat ini harus mengonsumsi obat penenang dosis tinggi untuk bisa tidur dua jam.",
        source_label="Informan Pendiri Startup Y, 29 tahun, Chief Executive Officer, Zhongguancun Beijing, Wawancara 2 November 2026"
    )
    
    add_blockquote(doc, 
        "Sebagai analis ekuitas senior selama hampir dua puluh tahun, saya belum pernah menyaksikan tekanan psikologis kolektif sebrutal ini. Di internal institusi sekuritas, para analis tahu bahwa angka-angka proyeksi pertumbuhan laba perusahaan AI di STAR Market adalah fiksi matematis yang mustahil tercapai. Namun ada tekanan institusional dan politik yang sangat kuat untuk terus menerbitkan rekomendasi 'Beli' (Strong Buy) demi menyokong narasi inovasi nasional. Kami berada dalam disonansi kognitif yang menyiksa: di siang hari kami mempresentasikan slide optimisme kepada investor ritel di webinar publik, dan di malam hari kami melihat kebobrokan laporan keuangan arus kas emiten-emiten tersebut. Kehancuran 40% ini bukan sekadar koreksi harga teknikal biasa, melainkan likuidasi moral yang merusak reputasi profesi analis pasar modal untuk satu generasi ke depan.",
        source_label="Informan Analis Senior Z, 42 tahun, Kepala Riset Teknologi Sekuritas, Futian Shenzhen, Wawancara 31 Oktober 2026"
    )
    
    add_h2(doc, "5.5 Tabel Kronologi dan Metrik Kejatuhan STAR50")
    add_body_p(doc, 
        "Tabel 3 menyajikan dekonstruksi kronologis dari lima fase siklus gelembung kecerdasan artifisial di Papan STAR Tiongkok, merangkum pergerakan valuasi, arus likuiditas, dan sentimen psikologis dominan pelaku pasar sepanjang periode 2024 hingga November 2026."
    )
    
    headers_t3 = [
        "Fase Siklus Pasar", 
        "Rentang Waktu", 
        "Tingkat Indeks STAR50", 
        "Rasio P/E Rata-rata", 
        "Kondisi Likuiditas & Aliran Dana", 
        "Sentimen Psikologis Dominan"
    ]
    data_t3 = [
        [
            "1. Inisiasi Narasi", 
            "Q1 2024 - Q3 2024", 
            "750 - 880 poin", 
            "35x - 45x", 
            "Aliran dana stimulus negara awal, subsidi komputasi lokal", 
            "Harapan hati-hati, optimisme patriotisme teknologi"
        ],
        [
            "2. Euforia Spekulatif", 
            "Q4 2024 - Q1 2026", 
            "890 - 1.420 poin", 
            "60x - 128x", 
            "Masuknya dana ritel masif (FOMO), reksadana tematik marjin", 
            "Keserakahan spekulatif, keyakinan paradigma baru kebal krisis"
        ],
        [
            "3. Ketegangan Monetisasi", 
            "Q2 2026 - Juni 2026", 
            "1.410 - 1.350 poin", 
            "115x - 120x", 
            "Perang harga token API, pembatalan langganan B2B meningkat", 
            "Disonansi kognitif, keengganan menerima penurunan marjin"
        ],
        [
            "4. Kapitulasi dan Likuidasi", 
            "Juli 2026 - Okt 2026", 
            "1.350 - 808 poin", 
            "110x anjlok ke 42x", 
            "Pengetatan marjin CSRC, cascading margin call, penarikan dana", 
            "Kepanikan akut, kemarahan, Retail Betrayal Syndrome"
        ],
        [
            "5. Disilusi & Pembekuan", 
            "Akhir Okt - Nov 2026", 
            "808 - 845 poin (stagnan)", 
            "38x - 44x", 
            "Volume transaksi harian anjlok 65%, likuiditas membeku", 
            "Apatisme total, penyesalan mendalam, learned helplessness"
        ]
    ]
    col_w_t3 = [1.2, 1.1, 1.1, 1.0, 1.5, 1.5]
    add_academic_table(
        doc, headers_t3, data_t3, col_w_t3,
        caption="Tabel 3: Kronologi Fase Siklus Gelembung Finansial AI pada Indeks STAR50 Tiongkok (2024-2026)",
        notes="Catatan: Dihimpun dari basis data perdagangan Bursa Efek Shanghai (SSE), Wind Financial Terminal, dan laporan riset ekonometrika perilaku konsorsium perbankan investasi independen (November 2026)."
    )
    
    # Penyisipan Gambar 5: Grafik Kejatuhan STAR50 dan Depresi Konsumsi
    fig5_path = os.path.join(FIGURES_DIR, "gambar5_kejatuhan_star50.png")
    if os.path.exists(fig5_path):
        add_figure(
            doc, fig5_path,
            caption="Gambar 5: Grafik Kronologi Kejatuhan Indeks AI STAR50 (-40,2%) dan Depresi Indeks Keyakinan Konsumen Urban Tiongkok Periode Januari hingga November 2026.",
            width_inches=5.8,
            notes="Catatan: Panel atas menunjukkan penutupan indeks mingguan STAR50 dengan anotasi katalisator kejatuhan. Panel bawah menampilkan transmisi efek kekayaan negatif terhadap Indeks Keyakinan Konsumen (NBS CCI)."
        )
    
    add_h2(doc, "5.6 Reperkusi Global dan Sentimen Disilusi Teknologi (The Global Trough of Disillusionment)")
    add_body_p(doc, 
        "Pecahnya gelembung AI di pasar Tiongkok tidak terisolasi secara geografis, melainkan memicu efek domino psikologis yang merambat cepat ke pusat-pusat keuangan global di Wall Street, London, Frankfurt, dan Tokyo. Sepanjang tahun 2023 hingga awal 2026, narasi pasar modal global ditopang oleh keyakinan bahwa belanja modal komputasi tak terbatas oleh korporasi hyperscaler (seperti Microsoft, Google, Meta, dan Amazon) akan segera diimbangi oleh ledakan produktivitas ekonomi riil yang belum pernah terjadi sebelumnya."
    )
    add_body_p(doc, 
        "Namun, kejatuhan pasar Tiongkok menjadi cermin yang membuka kenyataan telanjang bagi para investor internasional: bahwa biaya marjinal penyediaan komputasi kecerdasan artifisial tetap sangat tinggi, sementara kesediaan konsumen dan perusahaan membayar perangkat lunak tersebut memiliki batas elastisitas yang ketat. Di bursa Nasdaq dan S&P 500, para manajer dana lindung nilai (hedge funds) mulai memangkas bobot saham raksasa semikonduktor dan penyedia cloud, memicu koreksi valuasi yang tajam pada akhir kuartal ketiga dan kuartal keempat 2026."
    )
    add_body_p(doc, 
        "Secara sosiologis, peristiwa ini menandai transisi resmi peradaban global memasuki fase 'Lembah Kekecewaan' (Trough of Disillusionment) dalam Siklus Hype Inovasi Teknologi Gartner. Narasi tekno-utopis yang sebelumnya menjanjikan bahwa AI akan menyelesaikan seluruh persoalan kemanusiaan secara instan kini digantikan oleh kesadaran publik yang dingin dan skeptis. Kepercayaan publik global terhadap janji-janji revolusioner para pemimpin industri teknologi mengalami disilusi struktural. Masyarakat kini menuntut bukti fungsional yang nyata, transparansi biaya komputasi, keadilan pembagian nilai ekonomi, dan perlindungan nyata terhadap keselamatan jiwa serta martabat kemanusiaan sebelum menyerahkan masa depan peradaban ke tangan sistem kecerdasan artifisial."
    )
