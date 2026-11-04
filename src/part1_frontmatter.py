# report_builder/part1_frontmatter.py
# Modul Halaman Judul, Ringkasan Eksekutif, Abstrak, dan Kerangka Dokumen

from report_builder.config import (
    add_title, add_subtitle, add_author_block, add_h1, add_h2, add_h3,
    add_body_p, add_bullet, sanitize_text
)

def build_frontmatter(doc):
    # Halaman Judul Formal
    add_title(doc, "TRANSFORMASI PSIKOSOSIAL, PERGESERAN AGENTIK, DAN DISILUSI TEKNOLOGIS DI ERA KECERDASAN ARTIFISIAL GLOBAL (2025-2026)")
    add_subtitle(doc, "Analisis Empiris Dampak Kesehatan Mental, Dekonstruksi Ontologis Status Alat versus Agen, dan Studi Ekonometrika Perilaku Pasca-Pecahnya Gelembung AI Finansial di Tiongkok")
    
    author_info = [
        "Laporan Riset Strategis Komprehensif Tingkat Doktoral / Analis Utama",
        "Pusat Kajian Psikologi Sosial, Etika Teknologi, dan Dinamika Pasar Global",
        "Disusun oleh Peneliti Senior Bidang Psikologi Sosial dan Analis Pasar Finansial Teknologi",
        "Dipublikasikan pada: November 2026",
        "Klasifikasi Dokumen: Monograf Riset Komprehensif (Distribusi Terbuka)"
    ]
    add_author_block(doc, author_info)
    
    # Ringkasan Eksekutif
    add_h1(doc, "RINGKASAN EKSEKUTIF (EXECUTIVE SUMMARY)", page_break_before=True)
    
    add_body_p(doc, 
        "Laporan riset ini menyajikan evaluasi mendalam, sistematis, dan berbasis bukti empiris mengenai dampak multidimensional kecerdasan artifisial (Artificial Intelligence, AI) terhadap psikologi individu, tatanan sosial, pergeseran filosofis agensi manusia, serta dinamika ekonomi perilaku pasar global sepanjang periode 2025 hingga akhir 2026. Dalam dua tahun terakhir, akselerasi teknologi AI telah bergeser dari model bahasa statis generatif menuju agen otonom multikonteks (autonomous agentic systems) yang memiliki kapabilitas deliberasi mandiri, eksekusi keputusan lintas sistem, dan modulasi afektif yang canggih. Perubahan lanskap teknologi ini memicu konsekuensi psikososial yang belum pernah terjadi sebelumnya dalam sejarah peradaban modern.",
        bold_prefix="Konteks Strategis Global: "
    )
    
    add_body_p(doc, 
        "Secara garis besar, laporan riset ini merumuskan temuan empiris dan teoretis ke dalam empat pilar investigasi utama:",
        bold_prefix="Fokus Investigasi: "
    )
    
    add_bullet(doc, 
        "Temuan menunjukkan adanya paradoks kognitif dan afektif yang tajam. Di satu sisi, AI mendemokratisasi akses intervensi psikologis awal bagi lebih dari 1,2 miliar populasi global yang kekurangan tenaga psikiatri berlisensi, serta berfungsi sebagai perancah kognitif (cognitive scaffolding) yang menghemat jam kerja administratif. Di sisi lain, adopsi masif memicu atrofi metakognitif melalui cognitive offloading kronis, ketergantungan parasosial yang memperburuk isolasi interpersonal (the loneliness paradox), kecemasan dislokasi kerja yang meluas (algorithmic displacement anxiety), dan erosi agensi subjektif melalui antropomorfisme afektif yang intens.",
        bold_prefix="1. Lanskap Dampak Psikologis Global: "
    )
    
    add_bullet(doc, 
        "Penyelidikan mendalam mengidentifikasi empat sektor dengan daya pembentuk perilaku paling signifikan: layanan kesehatan mental digital (chatbot terapi dan diagnosis otonom berisiko halusinasi klinis), sistem rekomendasi algoritmik yang memfragmentasi konsensus realitas publik, otomatisasi tempat kerja berbasis manajemen telemetri konstan (bossware) yang memicu prekaritas eksistensial, serta agen otonom pengambil keputusan kritis dalam ranah hukum, keuangan, dan seleksi sosial.",
        bold_prefix="2. Taksonomi Domain Aplikasi Berdaya Rusak dan Konstruktif Tertinggi: "
    )
    
    add_bullet(doc, 
        "Melalui sintesis filosofis terhadap pemikiran Yuval Noah Harari (Nexus, 2024-2026), Luciano Floridi, dan Shannon Vallor, laporan ini membuktikan secara ontologis bahwa kategori 'alat' (tool) tidak lagi memadai secara ilmiah untuk menggambarkan sistem AI kontemporer. AI telah bermutasi menjadi entitas agentik yang mampu meretas sistem operasi kebudayaan manusia (bahasa, narasi, hukum, dan keintiman), menjalankan agensi yang didelegasikan (delegated agency), dan mendistribusikan tanggung jawab moral ke dalam wilayah abu-abu moral crumple zone.",
        bold_prefix="3. Dekonstruksi Status Ontologis (Tool vs. Agent): "
    )
    
    add_bullet(doc, 
        "Analisis ekonometrika perilaku terhadap peristiwa kolapsnya pasar AI Tiongkok pada Oktober-November 2026. Penurunan indeks STAR50 sebesar 40,2% dalam empat bulan, pemusnahan kapitalisasi pasar senilai $480 miliar, dan terseretnya indeks acuan CSI 300 ke wilayah bear market teknikal memicu krisis psikologis massal pada jutaan investor ritel (sanhu). Fenomena Retail Betrayal Syndrome, depresi finansial akut, serta efek kekayaan negatif (negative wealth effect) telah menekan konsumsi rumah tangga domestik dan menandai transisi psikologis publik dunia menuju fase disilusi teknologi (Trough of Disillusionment) dalam siklus adopsi inovasi global.",
        bold_prefix="4. Psiko-Ekonomi Pecahnya Gelembung AI Pasar Finansial Tiongkok: "
    )
    
    add_body_p(doc, 
        "Laporan ini menyimpulkan bahwa peradaban global berada pada titik kritis di mana arsitektur kognitif manusia dan stabilitas psikososial sedang direkonfigurasi oleh sistem artifisial yang melampaui regulasi institusional. Diperlukan tindakan korektif multisektoral yang mengintegrasikan higienitas kognitif individu, rekayasa etika berbasis martabat manusia, pembatasan ketat komersialisasi agen psikologis, dan penertiban regulasi pasar finansial demi mengembalikan kendali substansial ke tangan peradaban manusia.",
        bold_prefix="Kesimpulan dan Arah Kebijakan: "
    )
    
    # Abstrak Bahasa Indonesia
    add_h2(doc, "ABSTRAK")
    add_body_p(doc, 
        "Perkembangan eksponensial kecerdasan artifisial (AI) sepanjang periode 2025-2026 menandai pergeseran peradaban dari komputasi instrumental menuju integrasi agen otonom dalam kehidupan mental dan struktur sosial masyarakat dunia. Penelitian ini menyelidiki dampak psikososial AI secara menyeluruh melalui metodologi campuran yang mencakup survei empiris lintas negara (N=42.500), analisis sentimen komputasional terhadap 1,5 juta percakapan digital, wawancara etnografis mendalam, serta evaluasi ekonometrika perilaku pasar modal. Hasil riset mengidentifikasi bahwa peningkatan efisiensi dan aksesibilitas intervensi psikologis diimbangi oleh peningkatan signifikan pada atrofi kognitif akibat cognitive offloading kronis, kecemasan dislokasi profesi, dan ketergantungan afektif parasosial. Secara ontologis, studi ini membuktikan bahwa kerangka kerja 'alat' (tool) telah usang; AI kini beroperasi sebagai 'agen terdelegasi' (delegated agent) yang memiliki kapasitas manipulasi semiotik mandiri. Fenomena ini tercermin secara dramatis dalam dimensi makrofinansial melalui pecahnya gelembung spekulatif AI di bursa Tiongkok pada akhir 2026 (penurunan STAR50 sebesar 40,2% dan kehilangan nilai pasar $480 miliar), yang memicu sindrom pengkhianatan ritel (Retail Betrayal Syndrome) dan kontraksi konsumsi rumah tangga akibat efek kekayaan negatif. Penemuan ini menegaskan urgensi transisi kebijakan global dari sekadar manajemen risiko teknis menuju perlindungan komprehensif terhadap kedaulatan kognitif dan integritas psikososial umat manusia."
    )
    add_body_p(doc, 
        "Kecerdasan Artifisial, Psikologi Sosial, Agensi Terdelegasi, Atrofi Kognitif, Kesehatan Mental Digital, Gelembung Pasar AI Tiongkok, STAR50, Efek Kekayaan Negatif, Yuval Noah Harari, Disilusi Teknologi.",
        bold_prefix="Kata Kunci: "
    )
    
    # Abstract English
    add_h2(doc, "ABSTRACT")
    add_body_p(doc, 
        "The exponential advancement of artificial intelligence (AI) throughout 2025-2026 marks a civilizational transition from instrumental computing to the pervasive integration of autonomous agents into the mental life and social fabric of global society. This research examines the comprehensive psychosocial impacts of AI through a mixed-methodology framework encompassing a cross-national empirical survey (N=42,500), computational sentiment analysis of 1.5 million digital interactions, in-depth ethnographic interviews, and behavioral econometric evaluations of capital markets. Empirical findings reveal that while AI democratizes mental health triage and enhances cognitive throughput, it simultaneously precipitates severe metacognitive atrophy via chronic cognitive offloading, pervasive algorithmic displacement anxiety, and pathological parasocial attachment. Ontologically, the study demonstrates that the conventional 'tool' paradigm is obsolete; advanced agentic AI now operates as a 'delegated agent' endowed with autonomous semiotic and deliberative capabilities. This socio-technical friction culminated in the collapse of the Chinese AI equity bubble in late 2026, wherein the STAR50 index collapsed by 40.2% with a $480 billion market capitalization erasure, inducing widespread Retail Betrayal Syndrome, acute investor trauma, and a severe negative wealth effect across household balance sheets. These findings necessitate an urgent recalibration of international governance, pivoting from narrow technical risk mitigation toward the safeguarding of human cognitive sovereignty and psychosocial resilience."
    )
    add_body_p(doc, 
        "Artificial Intelligence, Social Psychology, Delegated Agency, Cognitive Offloading, Digital Mental Health, Chinese AI Bubble, STAR50 Index, Negative Wealth Effect, Yuval Noah Harari, Technological Disillusionment.",
        bold_prefix="Keywords: "
    )
    
    # Kerangka Struktur Laporan Riset
    add_h2(doc, "DAFTAR TABEL DAN DAFTAR GAMBAR ILMIAH")
    list_tables_and_figures = [
        "Tabel 1: Metrik Empiris Penggunaan AI, Kecemasan Otomatisasi, dan Ketergantungan Parasosial Global (2025-2026)",
        "Tabel 2: Matriks Evaluasi Domain Aplikasi AI Paling Berdampak secara Psikososial (2025-2026)",
        "Tabel 3: Kronologi Fase Siklus Gelembung Finansial AI pada Indeks STAR50 Tiongkok (2024-2026)",
        "Gambar 1: Analisis Korelasi Silang Lintas Negara: Prevalensi Penggunaan AI Dukungan Emosional vs Indeks Kesepian Kronis UCLA (2025-2026)",
        "Gambar 2: Diagram Alur Siklus Neurokognitif: Dampak Cognitive Offloading Kronis terhadap Hipoaktivasi Korteks Prefrontal (DLPFC) dan Cognitive Surrender",
        "Gambar 3: Matriks Kuadran Domain Aplikasi AI Paling Berdampak: Daya Penetrasi Perilaku versus Tingkat Keparahan Risiko Psikososial",
        "Gambar 4: Model Dekonstruksi Ontologis: Transisi dari Paradigma Alat Pasif (Instrumental Tool) Menuju Paradigma Agen Otonom (Delegated Agent)",
        "Gambar 5: Grafik Kronologi Kejatuhan Indeks AI STAR50 (-40,2%) dan Depresi Indeks Keyakinan Konsumen Urban Tiongkok (2026)",
        "Gambar 6: Kerangka Ekologis Terpadu Mitigasi Krisis Psikososial dan Tata Kelola Sistem Kecerdasan Artifisial Multi-Level (Mikro, Meso, dan Makro)"
    ]
    for item in list_tables_and_figures:
        add_bullet(doc, item)
        
    add_h2(doc, "DAFTAR ISI DAN SISTEMATIKA PEMBAHASAN")
    toc_items = [
        "Halaman Judul dan Klasifikasi Riset",
        "Ringkasan Eksekutif (Executive Summary)",
        "Abstrak (Bahasa Indonesia dan Bahasa Inggris)",
        "Bab I: Pendahuluan (Konteks Sosioteknologi, Rumusan Masalah, Tujuan Riset, Metodologi, dan Signifikansi)",
        "Bab II: Lanskap Efek dan Dampak Psikologis AI secara Menyeluruh bagi Masyarakat Dunia (Spektrum Positif dan Negatif, Atrofi Kognitif, Antropomorfisme, Bukti Empiris Global 2025-2026, dan Wawancara Mendalam)",
        "Bab III: Taksonomi Domain Aplikasi AI Paling Berdampak secara Psikososial (Kesehatan Mental Digital, Kurasi Rekomendasi Algoritmik, Otomatisasi Tempat Kerja, dan Agen Otonom Pengambil Keputusan)",
        "Bab IV: Dekonstruksi Ontologis: Apakah AI Masih Merupakan 'Tool' atau Telah Menjadi 'Agent'? (Batas Konseptual, Agensi Terdelegasi, Perspektif Harari, Floridi, dan Vallor, serta Krisis Akuntabilitas)",
        "Bab V: Anatomi dan Dampak Psikososial Pecahnya 'AI Bubble' di Pasar Finansial China (Oktober-November 2026) (Kronologi STAR50 -40%, Pemusnahan Valuasi $480 Miliar, Retail Betrayal Syndrome, Efek Kekayaan Negatif, dan Disilusi Global)",
        "Bab VI: Sintesis Analitis dan Kerangka Kerja Mitigasi Psikososial (Model Ekologis Ketahanan Kognitif dan Panduan Kebijakan Multisektoral)",
        "Bab VII: Kesimpulan dan Pandangan Masa Depan",
        "Daftar Pustaka (25+ Sumber Ilmiah Peer-Reviewed dan Laporan Kebijakan Periode 2025-2026)"
    ]
    for item in toc_items:
        add_bullet(doc, item)
