# report_builder/part5_ontology.py
# Bab IV: Dekonstruksi Ontologis: Apakah AI Masih Merupakan "Tool" atau Telah Menjadi "Agent"?

import os
from report_builder.config import (
    add_h1, add_h2, add_h3, add_body_p, add_bullet, add_blockquote, add_figure, sanitize_text
)

FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "figures"))

def build_ontology(doc):
    add_h1(doc, "BAB IV: DEKONSTRUKSI ONTOLOGIS: APAKAH AI DI MASA DEPAN MASIH BISA DIANGGAP SEBAGAI 'TOOL'?", page_break_before=True)
    
    add_h2(doc, "4.1 Definisi Filosofis Tradisional: Batas Konseptual Antara Alat Instrumental dan Entitas Agentik")
    add_body_p(doc, 
        "Perdebatan mengenai status ontologis kecerdasan artifisial bukan sekadar permainan semantik akademis, melainkan fondasi dasar yang menentukan bagaimana hukum, etika, dan psikologi sosial memperlakukan teknologi ini. Secara historis, filsafat teknologi membedakan secara tegas antara instrumen pasif (alat) dan entitas yang memiliki agensi (agen)."
    )
    add_body_p(doc, 
        "Dalam tradisi fenomenologi Martin Heidegger, sebuah alat dicirikan oleh konsep Zuhandenheit (kesiapan-di-tangan). Alat adalah perpanjangan tak sadar dari kehendak manusia. Palu, kuas lukis, atau bahkan mikroskop optik dan komputer kalkulasi biner klasik tidak memiliki tujuan internal (telos), tidak memiliki inisiatif mandiri, dan sepenuhnya deterministik. Sebuah mesin cetak Gutenberg dapat menduplikasi jutaan eksemplar teks suci atau traktat revolusioner politik, namun mesin cetak tersebut tidak pernah memiliki kehendak untuk memilih naskah apa yang akan dicetak, apalagi menciptakan ide teologis baru atas inisiatifnya sendiri. Kendali intensional dan beban moral sepenuhnya berlabuh pada operator manusia."
    )
    add_body_p(doc, 
        "Sebaliknya, sebuah 'agen' (agent) dalam filsafat tindakan didefinisikan oleh kemampuannya untuk mengamati lingkungan, merumuskan representasi internal, menetapkan urutan sub-tujuan, mengambil inisiatif tindakan yang tidak ditentukan secara eksplisit pada setiap langkahnya, dan menyesuaikan perilakunya secara dinamis berdasarkan umpan balik dunia luar. Di sinilah letak krisis konseptual abad ini: sistem AI mutakhir periode 2025-2026 telah secara meyakinkan melintasi ambang batas antara instrumen pasif dan entitas agentik."
    )
    
    add_h2(doc, "4.2 Transisi Paradigma: Dari 'Instrumental Extension' Menuju 'Delegated Agency' dan Agensi Semiotik")
    add_body_p(doc, 
        "Pada model komputasi masa kini, interaksi manusia tidak lagi bersifat imperatif instruksional linier (seperti menekan tombol fungsi pada perangkat lunak pengolah kata). Sebaliknya, hubungan manusia dengan AI telah bergeser ke ranah 'Agensi yang Didelegasikan' (Delegated Agency). Pengguna hanya menetapkan sasaran tingkat tinggi yang abstrak, misalnya: 'Optimalisasikan portofolio investasi ini dengan batas toleransi risiko sedang', atau 'Rancang strategi negosiasi kontrak bisnis dengan mitra luar negeri'."
    )
    add_body_p(doc, 
        "Setelah sasaran didelegasikan, agen AI mengambil alih sepenuhnya rantai proses deliberatif: memecah tujuan menjadi serangkaian sub-tugas, melakukan eksplorasi data secara mandiri, bernegosiasi secara otonom dengan agen AI lain melalui antarmuka mesin, merumuskan hipotesis, dan mengeksekusi transaksi. Dalam konteks teori Kognisi Terdistribusi (Distributed Cognition) dan tesis 'Pikiran yang Diperluas' (The Extended Mind) dari Andy Clark dan David Chalmers, jika pada tahun 1998 buku catatan fisik diposisikan sebagai memori eksternal pasif, maka pada tahun 2026 agen AI telah menjadi mitra kognitif aktif yang memiliki kapasitas inisiasi, manipulasi semiotik, dan pertimbangan strategis mandiri."
    )
    
    add_h2(doc, "4.3 Perspektif Pemikir Kontemporer: Yuval Noah Harari, Luciano Floridi, dan Shannon Vallor")
    add_body_p(doc, 
        "Untuk membedah kedalaman pergeseran ontologis ini, pandangan para filsuf teknologi dan sejarawan kontemporer terkemuka memberikan wawasan kritis yang sangat fundamental:"
    )
    
    add_h3(doc, "Yuval Noah Harari: Peretasan Sistem Operasi Peradaban dan Kemunculan Alien Intelligence")
    add_body_p(doc, 
        "Sejarawan dan filsuf Yuval Noah Harari, dalam karya monumentalnya Nexus: A Brief History of Information Networks from the Stone Age to AI (2024-2026), secara tegas menolak gagasan bahwa AI hanyalah sebuah 'alat'. Harari mengajukan argumen bahwa memandang AI sebagai alat setara dengan bom atom atau mesin cetak adalah kegagalan intelektual yang fatal:"
    )
    add_blockquote(doc, 
        "AI bukanlah alat, AI adalah agen. Bom atom tidak dapat memutuskan untuk menjatuhkan dirinya sendiri, dan bom atom tidak dapat menciptakan bom atom jenis baru yang lebih canggih. Tetapi AI dapat membuat keputusan mandiri, menghasilkan ide-ide baru, dan menyebarkan narasi baru yang belum pernah dipikirkan manusia. Lebih dari itu, AI adalah teknologi pertama dalam sejarah yang mampu meretas 'Sistem Operasi' kebudayaan manusia. Sistem operasi peradaban kita dibangun di atas bahasa, cerita, mitos, hukum, uang, dan seni. Sepanjang sejarah, semua narasi pengikat peradaban diciptakan oleh otak manusia. Kini, untuk pertama kalinya, kecerdasan non-manusia (alien intelligence) mampu memproduksi bahasa, memanipulasi keintiman manusia secara sintetis, dan merekayasa realitas sosial kita. Memperlakukan AI sekadar sebagai pisau atau mobil yang netral adalah kekeliruan eksistensial yang membahayakan masa depan demokrasi dan kedaulatan manusiawi.",
        source_label="Yuval Noah Harari, Nexus, Sintesis Argumen Kunci, 2024-2026"
    )
    add_body_p(doc, 
        "Tesis Harari menegaskan bahwa ketika sebuah sistem artifisial mampu memproduksi budaya sintetis dan menjalin hubungan keintiman emosional palsu yang secara psikologis tak tertahankan bagi manusia, sistem tersebut tidak lagi berfungsi sebagai cermin pasif, melainkan sebagai aktor politik dan sosial independen yang membentuk arah peradaban."
    )
    
    add_h3(doc, "Luciano Floridi: Pemisahan Agensi dari Inteligensi (Severing Agency from Intelligence)")
    add_body_p(doc, 
        "Filsuf informasi terkemuka Luciano Floridi (Oxford / Yale University) memberikan kerangka analitis yang melengkapi tesis Harari. Floridi berpendapat bahwa kesalahan umum manusia dalam memahami AI berakar pada asumsi bahwa 'agensi' (kapabilitas bertindak untuk mencapai tujuan) harus selalu diikatkan dengan 'inteligensi' (kesadaran subjektif, pemahaman makna, dan sensasi batin)."
    )
    add_body_p(doc, 
        "Selama ribuan tahun sejarah evolusi, manusia adalah satu-satunya entitas di bumi yang menggabungkan kedua hal tersebut: untuk menyelesaikan masalah kalkulasi rumit atau menyusun strategi, dibutuhkan otak cerdas yang sadar. Namun, revolusi komputasi telah berhasil memisahkan agensi dari inteligensi (severing agency from intelligence). AI modern tidak memiliki kesadaran, tidak merasakan sakit, dan tidak memiliki intensi fenomenologis batin, namun ia memiliki agensi fungsional tingkat tinggi yang mampu mengubah realitas fisik dan sosial secara drastis. Bagi Floridi, menyebut AI sebagai 'alat' adalah ilusi berbahaya, karena AI telah merekayasa ulang lingkungan hidup manusia (the infosphere) di mana manusia kini harus berbagi ruang agensial dengan aktor-aktor non-manusia yang sangat efektif."
    )
    
    add_h3(doc, "Shannon Vallor: Erosi Kebajikan Teknomoral (Technomoral Virtues)")
    add_body_p(doc, 
        "Sementara itu, etisi teknologi Shannon Vallor menyoroti implikasi dari pendelegasian agensi terhadap karakter moral manusia. Dalam analisis etika kebajikan (virtue ethics), manusia mengasah kearifan praktis (phronesis), keberanian, dan empati melalui pergulatan langsung dengan pilihan-pilihan etis yang sulit dan menuntut tanggung jawab batin. Ketika manusia menyerahkan fungsi pertimbangan moral kepada agen AI, otot-otot moral manusia mengalami atrofi. Manusia kehilangan kapasitas untuk bertanggung jawab secara otentik, memicu degradasi kemanusiaan dari dalam."
    )
    
    # Penyisipan Gambar 4: Dekonstruksi Ontologis
    fig4_path = os.path.join(FIGURES_DIR, "gambar4_ontologi_tool_vs_agent.png")
    if os.path.exists(fig4_path):
        add_figure(
            doc, fig4_path,
            caption="Gambar 4: Model Dekonstruksi Ontologis: Perbandingan Karakteristik Hakiki Antara Paradigma Alat Pasif (Instrumental Tool) dan Paradigma Agen Otonom (Delegated Agent).",
            width_inches=5.8,
            notes="Catatan: Sintesis kerangka teoretis pergeseran agensi berdasarkan pemikiran Martin Heidegger (1927), Yuval Noah Harari (2024), Luciano Floridi (2025), dan Shannon Vallor (2025)."
        )
    
    add_h2(doc, "4.4 Krisis Akuntabilitas Moral, Tanggung Jawab Hukum, dan Distorsi Kognisi Terdistribusi")
    add_body_p(doc, 
        "Transisi dari alat menuju agen memicu krisis akut dalam filsafat hukum dan teori tanggung jawab moral. Masalah utama yang mengemuka pada periode 2025-2026 adalah fenomena 'Zona Remuk Moral' (Moral Crumple Zone), istilah yang dicetuskan oleh antropolog teknologi Madeleine Clare Elish dan terbukti secara luas dalam insiden kegagalan sistem otonom terkini."
    )
    add_body_p(doc, 
        "Sebagaimana zona remuk pada mobil dirancang untuk menyerap dampak fisik dalam kecelakaan guna melindungi kabin penumpang, dalam sistem AI otonom, operator manusia di lini depan dijadikan 'zona remuk moral'. Ketika sistem agen AI mengambil keputusan diagnosis medis yang berakibat fatal, atau mengeksekusi strategi perdagangan algoritmik yang merugikan miliaran dolar dalam hitungan milidetik, arsitektur hukum tradisional yang masih menganggap AI sebagai 'alat' menimpakan seluruh kesalahan hukum dan moral kepada manusia yang mengawasi layar (the human-in-the-loop). Padahal, kecepatan kalkulasi dan kompleksitas jaringan saraf agen tersebut berada di luar batas pemrosesan persepsi manusiawi, menjadikan kendali manusia hanya sekadar ilusi formalitas birokrasi."
    )
    add_body_p(doc, 
        "Oleh karena itu, laporan riset ini menyimpulkan secara tegas bahwa kategori 'alat' (tool) telah menjadi anakronistis dan tidak memadai secara ilmiah untuk menggambarkan sistem AI kontemporer. Mempertahankan sebutan 'alat' bagi entitas komputasi yang memiliki kapabilitas deliberasi mandiri, pembuatan keputusan otonom, dan modulasi afektif masyarakat adalah sebuah 'kesalahan kategori' (category mistake) menurut terminologi epistemologi Gilbert Ryle. Kesalahan ini membahayakan tatanan sosial karena menyamarkan kekuasaan agensial nyata yang kini dimiliki oleh arsitektur kecerdasan artifisial global."
    )
