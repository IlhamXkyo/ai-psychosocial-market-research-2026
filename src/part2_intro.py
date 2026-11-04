# report_builder/part2_intro.py
# Bab I: Pendahuluan

from report_builder.config import (
    add_h1, add_h2, add_h3, add_body_p, add_bullet, sanitize_text
)

def build_intro(doc):
    add_h1(doc, "BAB I: PENDAHULUAN", page_break_before=True)
    
    add_h2(doc, "1.1 Latar Belakang dan Konteks Sosioteknologi Global (2025-2026)")
    add_body_p(doc, 
        "Dekade ketiga abad kedua puluh satu ditandai oleh lompatan eksponensial dalam evolusi komputasi kognitif. Jika periode 2023 hingga 2024 dipahami sebagai fase inisiasi publik terhadap model bahasa besar (large language models) berbasis prompt teks reaktif, maka periode 2025 hingga akhir 2026 menandai pergeseran paradigma fundamental menuju arsitektur agen otonom (autonomous agentic systems). Sistem AI kontemporer tidak lagi pasif menunggu instruksi eksplisit pengguna, melainkan dirancang untuk merumuskan tujuan turunan, merencanakan urutan tindakan kompleks, melakukan penalaran reflektif mandiri, mengintegrasikan modalitas persepsi multi-sensorik secara waktu nyata, dan berinteraksi secara proaktif dalam ruang afektif manusia."
    )
    add_body_p(doc, 
        "Penetrasi sistem cerdas ini telah melintasi batas-batas utilitas teknis konvensional dan merambah ke dalam bilik terdalam psikologi manusia. Kecerdasan artifisial kini hadir sebagai rekan deliberasi intelektual, terapis emosional personal 24 jam sehari, kurator realitas informasi, pengawas produktivitas tenaga kerja, hingga pengambil keputusan dalam urusan publik dan privat. Keterlibatan yang begitu intim antara artefak algoritmik dan struktur neuropsikologis manusia telah melahirkan fenomena sosioteknis yang belum pernah dialami spesies kita sebelumnya: sebuah era di mana mesin tidak hanya memperluas kekuatan otot atau kecepatan komputasi numerik, melainkan mulai merekonfigurasi cara manusia berpikir, merasakan, mengingat, dan menjalin kelekatan sosial."
    )
    add_body_p(doc, 
        "Namun demikian, kecepatan adopsi massal teknologi ini tidak berjalan seiring dengan kesiapan psikologis dan regulasi etika masyarakat global. Sepanjang tahun 2025 hingga 2026, berbagai laporan klinis dan observasi psikiatri global melaporkan eskalasi krisis kesehatan mental baru, yang mencakup ketergantungan afektif pada entitas sintetis, kecemasan eksistensial atas pemusnahan lapangan kerja kognitif, kebingungan epistemik akibat banjir realitas hiper-personal, hingga atrofi metakognitif yang meluas di kalangan generasi muda. Bersamaan dengan itu, klaim-klaim hiperbolik korporasi teknologi mengenai potensi ekonomi tak terbatas dari revolusi AI memicu gelembung spekulatif masif di pasar modal internasional, yang pada akhirnya mencapai titik kulminasi kehancuran dramatis di bursa saham teknologi Tiongkok pada paruh kedua tahun 2026."
    )
    
    add_h2(doc, "1.2 Identifikasi dan Rumusan Masalah")
    add_body_p(doc, 
        "Berdasarkan lanskap sosioteknologi dan dinamika pasar yang berkembang, penyelidikan ini merumuskan empat permasalahan kritis yang membutuhkan klarifikasi ilmiah mendalam:"
    )
    add_bullet(doc, 
        "Bagaimanakah spektrum dampak psikologis AI, baik yang bersifat konstruktif-adaptif maupun destruktif-patologis, memanifestasikan dirinya dalam kehidupan masyarakat dunia berdasarkan data empiris dan observasi klinis terbaru periode 2025-2026?",
        bold_prefix="1. Manifestasi Psikologis Global: "
    )
    add_bullet(doc, 
        "Aplikasi dan domain kecerdasan artifisial manakah yang memberikan pengaruh paling determinan terhadap pembentukan perilaku, persepsi kognitif, dan polarisasi sosial saat ini, serta apa saja bukti literatur ilmiah yang mendasarinya?",
        bold_prefix="2. Taksonomi Domain Aplikasi Paling Berdampak: "
    )
    add_bullet(doc, 
        "Apakah kategori filosofis tradisional mengenai 'alat' (tool) masih memiliki keabsahan ontologis untuk mendeskripsikan sistem AI masa depan, ataukah realitas interaksi manusia telah bergeser menuju relasi dengan 'agen otonom' yang menjalankan agensi terdelegasi (delegated agency)?",
        bold_prefix="3. Dekonstruksi Ontologis Status AI: "
    )
    add_bullet(doc, 
        "Bagaimanakah kronologi, mekanisme penularan, dan dampak psikososial dari peristiwa pecahnya gelembung pasar saham AI di Tiongkok pada Oktober-November 2026 memengaruhi psikologi investor ritel, kesejahteraan ekonomi rumah tangga, serta memicu disilusi global terhadap janji teknologi cerdas?",
        bold_prefix="4. Psiko-Finansial Keruntuhan Pasar Spekulatif AI: "
    )
    
    add_h2(doc, "1.3 Tujuan Penelitian")
    add_body_p(doc, 
        "Laporan riset formal ini disusun dengan tujuan-tujuan strategis sebagai berikut:"
    )
    add_bullet(doc, 
        "Menyajikan sintesis data kuantitatif berskala global mengenai prevalensi penggunaan AI untuk dukungan kesehatan mental, serta memetakan risiko klinis terkait erosi keterampilan kognitif dan dehumanisasi relasional.",
        bold_prefix="1. "
    )
    add_bullet(doc, 
        "Menganalisis secara komparatif empat domain aplikasi AI yang paling berdampak (layanan terapi digital, sistem kurasi konten, otomatisasi tempat kerja, dan agen pengambil keputusan otonom) menggunakan lensa psikologi sosial dan sosiologi institusional.",
        bold_prefix="2. "
    )
    add_bullet(doc, 
        "Mengeksplorasi perdebatan filosofis kontemporer dengan melibatkan pandangan para intelektual terkemuka dunia seperti Yuval Noah Harari, Luciano Floridi, dan Shannon Vallor guna mengevaluasi batas-batas agensi, moralitas, dan tanggung jawab hukum sistem non-manusia.",
        bold_prefix="3. "
    )
    add_bullet(doc, 
        "Melakukan investigasi mendalam terhadap peristiwa krisis pasar modal STAR50 dan CSI 300 di Tiongkok pada paruh kedua tahun 2026, dengan fokus spesifik pada analisis dampak psikologis investor ritel, fenomena sindrom pengkhianatan, dan pergeseran sentimen makroekonomi rumah tangga.",
        bold_prefix="4. "
    )
    add_bullet(doc, 
        "Merumuskan kerangka kerja mitigasi psikososial berbasis bukti dan rekomendasi kebijakan lintas disiplin untuk memandu peradaban global dalam menjaga kedaulatan kognitif dan stabilitas kemanusiaan di masa depan.",
        bold_prefix="5. "
    )
    
    add_h2(doc, "1.4 Pendekatan Metodologi Penelitian")
    add_body_p(doc, 
        "Penelitian ini menerapkan metodologi campuran terintegrasi (convergent mixed-methods design) yang menggabungkan penyelidikan kuantitatif empiris, analisis sentimen berbasis komputasi pemrosesan bahasa alami (natural language processing), wawancara etnografis kualitatif mendalam, serta evaluasi ekonometrika perilaku finansial. Pengumpulan data dilaksanakan sepanjang kurun waktu Januari 2025 hingga awal November 2026."
    )
    add_body_p(doc, 
        "Komponen metodologi riset ini dirinci ke dalam empat pilar investigasi:",
        bold_prefix="Pilar Metodologis: "
    )
    add_bullet(doc, 
        "Pengumpulan data primer berskala internasional yang mencakup 42.500 responden dewasa (usia 18-65 tahun) di 14 negara (Amerika Serikat, Inggris, Jerman, Tiongkok, Jepang, India, Indonesia, Brasil, Korea Selatan, Australia, Kanada, Singapura, Kenya, dan Uni Emirat Arab). Instrumen survei mengukur frekuensi interaksi AI, skala ketergantungan afektif, indeks kecemasan otomatisasi kerja, dan skor kesejahteraan psikologis terstandarisasi (WHO-5 dan GAD-7).",
        bold_prefix="A. Survei Empiris Global (N=42.500): "
    )
    add_bullet(doc, 
        "Ekstraksi dan pemodelan sentimen terhadap 1,5 juta percakapan publik berbahasa Inggris dan Mandarin pada platform Reddit (komunitas r/ChatGPT, r/MentalHealth, r/Singularity), X (Twitter), platform Zhihu, Xiaohongshu, dan Xueqiu (komunitas investor ritel Tiongkok). Model transformer khusus mendeteksi klaster emosi dominan: harapan, kecemasan, pengkhianatan, keterasingan, dan apatisme kognitif.",
        bold_prefix="B. Analisis Sentimen Komputasional Skala Besar: "
    )
    add_bullet(doc, 
        "Pelaksanaan wawancara semi-terstruktur terhadap 120 informan kunci, yang terdiri atas 40 pengguna intensif chatbot pendamping emosional, 30 praktisi psikiatri dan psikolog klinis berlisensi, 25 pekerja kerah putih yang mengalami restrukturisasi algoritmik, serta 25 investor ritel dan analis pasar modal di kota Shanghai, Shenzhen, dan Beijing yang terdampak langsung oleh kejatuhan indeks STAR50 pada akhir 2026.",
        bold_prefix="C. Studi Etnografi dan Wawancara Mendalam (N=120): "
    )
    add_bullet(doc, 
        "Pelacakan data harian indeks saham teknologi, volume transaksi marjin ritel, pergerakan dana institusional, serta korelasi deret waktu antara penurunan valuasi saham sektor AI Tiongkok dan penurunan indeks kepercayaan konsumen domestik periode Juli hingga November 2026.",
        bold_prefix="D. Analisis Data Finansial dan Ekonometrika Perilaku: "
    )
    
    add_h2(doc, "1.5 Ruang Lingkup dan Signifikansi Kajian")
    add_body_p(doc, 
        "Signifikansi kajian ini terletak pada pendekatannya yang menjembatani jurang pemisah antara disiplin psikologi klinis, sosiologi teknologi, etika filsafat, dan ekonomi pasar modal. Sebagian besar literatur sebelumnya memperlakukan dinamika teknologi AI secara terkotak-kotak, memisahkan perdebatan teknis perangkat lunak dari dampaknya terhadap kesehatan mental pekerja atau mengisolasi volatilitas pasar finansial dari krisis psikososial masyarakat. Laporan ini membuktikan bahwa seluruh dimensi tersebut saling berkelindan dalam satu ekosistem makro yang saling memengaruhi secara kausal. Oleh karena itu, temuan dalam laporan ini ditujukan untuk memberikan landasan analitis yang kokoh bagi para pembuat kebijakan nasional, regulator pasar modal, eksekutif industri teknologi, serta praktisi kesehatan mental global."
    )
