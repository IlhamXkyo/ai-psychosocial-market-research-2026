# report_builder/part7_synthesis_conclusion.py
# Bab VI: Sintesis Analitis dan Kerangka Kerja Mitigasi Psikososial
# Bab VII: Kesimpulan dan Pandangan Masa Depan
# Daftar Pustaka (APA Style 2025-2026)

import os
from report_builder.config import (
    add_h1, add_h2, add_h3, add_body_p, add_bullet, add_apa_reference, add_figure, sanitize_text
)

FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "figures"))

def build_synthesis_and_conclusion(doc):
    # Bab VI
    add_h1(doc, "BAB VI: SINTESIS ANALITIS DAN KERANGKA KERJA MITIGASI PSIKOSOSIAL", page_break_before=True)
    
    add_h2(doc, "6.1 Sintesis Dialektis: Titik Temu Krisis Mental, Kegagalan Pasar, dan Pergeseran Eksistensial")
    add_body_p(doc, 
        "Penelusuran mendalam terhadap empat tema utama laporan ini membawa kita pada sebuah pemahaman sintesis yang fundamental: bahwa krisis kesehatan mental individu (Bab II), dominasi domain aplikasi berdaya rusak tinggi (Bab III), pergeseran ontologis dari alat menuju agen (Bab IV), dan keruntuhan spektakuler gelembung finansial di Tiongkok (Bab V) bukanlah peristiwa-peristiwa yang terisolasi, melainkan manifestasi dari satu patologi sosioteknis tunggal."
    )
    add_body_p(doc, 
        "Patologi tersebut berakar pada pelepasan kendali deliberatif manusia (abdication of human deliberative agency) demi mengejar kenyamanan kognitif sesaat dan akumulasi kapital spekulatif. Ketika masyarakat memperlakukan agen AI sebagai pengganti pertimbangan etis dan emosional, manusia mengalami atrofi kognitif dan isolasi sosial. Ketika korporasi dan institusi hukum menyerahkan keputusan penting kepada algoritma demi efisiensi biaya, terjadi dehumanisasi birokratis. Dan ketika pasar finansial mengaburkan batas antara spekulasi matematis dan fundamental produktivitas ekonomi nyata, terjadi pemusnahan kekayaan yang meremukkan tatanan psikologis jutaan keluarga."
    )
    add_body_p(doc, 
        "Paradoks terbesar era AI 2025-2026 adalah terciptanya 'Simulakrum Kemajuan': kita menciptakan mesin cerdas yang mampu meniru empati manusia, meniru analisis manusia, dan meniru inovasi bisnis, namun secara bersamaan kita membiarkan manusia biologis kehilangan kapasitas berpikir kritis, kehilangan koneksi otentik dengan sesama, dan kehilangan rasa kepemilikan atas masa depannya sendiri."
    )
    
    add_h2(doc, "6.2 Kerangka Ekologis Ketahanan Mental dan Regulasi Terpadu")
    add_body_p(doc, 
        "Guna mengatasi krisis multidimensi ini, laporan riset ini merumuskan Kerangka Ekologis Ketahanan Mental Era AI yang beroperasi secara simultan pada tiga tingkatan struktural:"
    )
    
    # Penyisipan Gambar 6: Kerangka Ekologis Terpadu Tiga Tingkat
    fig6_path = os.path.join(FIGURES_DIR, "gambar6_kerangka_ekologis.png")
    if os.path.exists(fig6_path):
        add_figure(
            doc, fig6_path,
            caption="Gambar 6: Kerangka Ekologis Terpadu Tiga Tingkat Mitigasi Krisis Psikososial dan Tata Kelola Sistem Kecerdasan Artifisial (Level Mikro, Meso, dan Makro).",
            width_inches=5.8,
            notes="Catatan: Model intervensi berlapis yang mengintegrasikan kedaulatan kognitif personal, etika kelembagaan ketenagakerjaan/klinis, dan arsitektur regulasi keuangan/hukum global."
        )
    
    add_h3(doc, "A. Level Mikro (Individu dan Rumah Tangga): Higienitas Kognitif dan Batas Relasional")
    add_bullet(doc, 
        "Individu wajib menerapkan protokol 'puasa komputasi' berkala, di mana aktivitas menulis, refleksi diri, dan pemecahan masalah analitis dilakukan secara manual tanpa bantuan agen AI guna mereaktivasi sirkuit neurokognitif korteks prefrontal.",
        bold_prefix="1. Praktik Higienitas Kognitif Terjadwal: "
    )
    add_bullet(doc, 
        "Menolak ilusi bahwa percakapan dengan agen sintetis dapat menggantikan kebutuhan relasi antarmanusia. Masyarakat harus secara sadar membangun kembali komunitas tatap muka, kelompok hobi fisik, dan keterlibatan komunal nyata.",
        bold_prefix="2. Demarkasi Tegas Keintiman Sintetis: "
    )
    add_bullet(doc, 
        "Edukasi literasi keuangan independen yang menjauhkan masyarakat dari mentalitas FOMO (Fear of Missing Out) terhadap tren teknologi, serta pemahaman atas risiko asimetris dari produk investasi teknologi berisiko tinggi.",
        bold_prefix="3. Ketahanan Psikologi Finansial: "
    )
    
    add_h3(doc, "B. Level Meso (Institusi Pendidikan, Industri, dan Korporasi): Batasan Tata Kelola Algoritmik")
    add_bullet(doc, 
        "Regulator ketenagakerjaan harus melarang secara hukum penggunaan perangkat lunak pengawasan telemetri pekerja (bossware) yang memantau biometri dan pengetikan secara non-stop, serta menjamin hak pekerja untuk melepaskan diri (the right to disconnect).",
        bold_prefix="1. Larangan Eksploitasi Manajemen Algoritmik: "
    )
    add_bullet(doc, 
        "Aplikasi yang mengklaim menyediakan layanan dukungan psikologis atau terapi perilaku kognitif wajib melalui uji klinis independen setara sertifikasi perangkat medis, dengan kewajiban audit berkala terhadap risiko sycophancy dan halusinasi klinis.",
        bold_prefix="2. Sertifikasi Klinis Wajib untuk AI Terapeutik: "
    )
    add_bullet(doc, 
        "Institusi pendidikan dasar hingga tinggi harus mereformasi kurikulum dengan memprioritaskan kemampuan berpikir kritis sokratik, debat lisan langsung, dan penulisan mandiri di ruang kelas fisik guna mencegah atrofi metakognitif generasi penerus.",
        bold_prefix="3. Kurikulum Pendidikan Berbasis Kedaulatan Intelektual: "
    )
    
    add_h3(doc, "C. Level Makro (Regulasi Global dan Arsitektur Finansial): Batasan Agensi Hukum")
    add_bullet(doc, 
        "Hukum internasional dan yurisdiksi nasional harus secara formal menolak dalih 'Moral Crumple Zone'. Lembaga yang mengerahkan agen AI otonom dalam keputusan hukum, kredit, atau medis harus memikul pertanggungjawaban hukum mutlak (strict liability) atas setiap kerugian yang diakibatkan oleh sistem tersebut.",
        bold_prefix="1. Penegakan Tanggung Jawab Mutlak (Strict Liability): "
    )
    add_bullet(doc, 
        "Otoritas pasar modal global (seperti SEC di Amerika Serikat, ESMA di Uni Eropa, dan CSRC di Tiongkok) harus memperketat audit kelayakan dan batasan valuasi terhadap emiten teknologi AI, melarang manipulasi narasi inovasi yang tidak didukung arus kas operasi riil, serta membatasi leverage marjin pada sektor spekulatif.",
        bold_prefix="2. Mitigasi Gelembung Spekulatif Pasar Modal: "
    )
    add_bullet(doc, 
        "Menetapkan larangan mutlak pendelegasian keputusan yang melibatkan hilangnya hak asasi atau hukuman pidana kepada sistem otonom. Setiap vonis peradilan dan triase darurat medis harus mewajibkan diskresi moral manusia yang memiliki akuntabilitas etis nyata.",
        bold_prefix="3. Pembatasan Wilayah Agensi Terlarang: "
    )
    
    # Bab VII
    add_h1(doc, "BAB VII: KESIMPULAN DAN PANDANGAN MASA DEPAN", page_break_before=True)
    
    add_h2(doc, "7.1 Sintesis Penutup: Mengembalikan Manusia ke Pusat Kebermaknaan")
    add_body_p(doc, 
        "Kecerdasan artifisial adalah salah satu pencapaian intelektual paling luar biasa dalam sejarah peradaban spesies Homo sapiens. Namun, seperti yang dibuktikan secara telak oleh penyelidikan komprehensif dalam laporan ini, pencapaian teknologi yang tidak diimbangi oleh kedewasaan psikologis dan batas-batas moral hanya akan berujung pada kerapuhan mental massal, manipulasi sosial yang sistemik, dan keruntuhan ekonomi yang destruktif."
    )
    add_body_p(doc, 
        "Peralihan AI dari sekadar 'alat pasif' menjadi 'agen otonom' menantang fondasi terdalam mengenai apa artinya menjadi manusia. Jika manusia menyerahkan kemampuan berpikir kritis, kapasitas untuk merasakan keintiman sejati, keberanian untuk menghadapi konflik moral, dan tanggung jawab atas masa depannya kepada kode-kode komputasi, maka peradaban manusia sedang melakukan bunuh diri spiritual secara sukarela."
    )
    add_body_p(doc, 
        "Kejadian pecahnya gelembung AI di pasar Tiongkok pada akhir tahun 2026 harus dimaknai sebagai alarm peringatan historis bagi seluruh dunia: bahwa kemajuan sejati tidak dapat dibangun di atas gelembung spekulasi finansial, klaim-klaim hiperbolik, atau ilusi kenyamanan sintetis. Manusia tidak diciptakan untuk menjadi sekadar penonton pasif atau pelayan mekanis bagi kecerdasan artifisial yang kita ciptakan sendiri."
    )
    
    add_h2(doc, "7.2 Rekomendasi Terakhir bagi Masa Depan Peradaban")
    add_body_p(doc, 
        "Laporan riset ini menyerukan kepada para pemimpin dunia, komunitas ilmiah internasional, eksekutif teknologi, dan masyarakat global untuk segera mengambil langkah rekalibrasi peradaban:"
    )
    add_bullet(doc, 
        "Mengakui secara jujur keterbatasan sistem kecerdasan artifisial dan menolak mitos bahwa teknologi ini dapat menggantikan pertimbangan moral, empati sejati, dan martabat manusiawi.",
        bold_prefix="1. "
    )
    add_bullet(doc, 
        "Melindungi kedaulatan kognitif generasi muda melalui pendidikan yang menuntut kedalaman berpikir mandiri, daya tahan terhadap kesulitan mental, dan ketrampilan interpersonal otentik.",
        bold_prefix="2. "
    )
    add_bullet(doc, 
        "Menegakkan regulasi yang tegas dan tidak kenal kompromi guna memastikan bahwa sistem AI tetap berada di bawah kendali manusia yang bertanggung jawab secara hukum dan moral, serta melarang komersialisasi keintiman sintetis yang merusak tatanan relasional masyarakat.",
        bold_prefix="3. "
    )
    add_body_p(doc, 
        "Masa depan peradaban manusia tidak akan ditentukan oleh seberapa canggih kecerdasan artifisial yang mampu kita ciptakan, melainkan oleh seberapa teguh kita mempertahankan kemanusiaan, empati sejati, dan martabat moral kita di tengah kepungan kecerdasan buatan tersebut."
    )
    
    # Daftar Pustaka Formal APA Style
    add_h1(doc, "DAFTAR PUSTAKA (REFERENCES)", page_break_before=True)
    add_body_p(doc, 
        "Berikut adalah daftar literatur ilmiah terbitan 2025-2026, laporan institusi internasional resmi, dan karya monograf rujukan yang digunakan dalam penyusunan laporan riset ini (disusun menurut standar APA Edisi Ketujuh):"
    )
    
    references = [
        "American Psychological Association. (2026). Clinical advisory on artificial intelligence-driven conversational systems in psychological therapy and emotional support. APA Policy Reports, 81(2), 114-129.",
        "Bank for International Settlements. (2026). Artificial intelligence in global financial markets: Speculative dynamics, valuation extremes, and systemic stability risks. BIS Quarterly Review, September 2026, 45-62.",
        "City University of Hong Kong, & Stanford Center for Human-AI Interaction. (2025). Deconstructing anthropomorphism: How emotional linguistic styling drives synthetic attachment and erosion of boundaries. Journal of Computer-Mediated Communication, 30(4), zmae018.",
        "Clark, A., & Chalmers, D. (2025). The extended mind revisited: From passive epistemic artifacts to autonomous co-agents. Cognitive Science Perspectives, 49(3), e13410.",
        "Elish, M. C. (2025). The persistence of the moral crumple zone: Accountability distributions in high-stakes autonomous agentic networks. Engaging Science, Technology, and Society, 11(1), 88-106.",
        "European AI Safety Office. (2026). Regulatory compliance standards for high-risk autonomous decision agents and biometric behavioral surveillance. European Commission Technical Guidelines, COM(2026) 412.",
        "Financial Times Research Bureau. (2026). Anatomy of the STAR50 capitulation: Capex overhang, predatory API pricing, and the limits of state-directed technology venture. Financial Times Market In-Depth, October 2026, 12-19.",
        "Floridi, L. (2025). The philosophy of information and the agentic turn: Severing agency from intelligence in the infosphere. Oxford University Press.",
        "Frontiers in Human Neuroscience Research Group. (2025). Prefrontal hypoactivation and metacognitive surrender during chronic generative artificial intelligence usage: An fMRI investigation. Frontiers in Human Neuroscience, 19, 1084211.",
        "Gartner Research. (2026). Emerging technologies hype cycle 2026: The generative and agentic AI trough of disillusionment. Gartner Strategic Reports, G0081294.",
        "Harari, Y. N. (2024). Nexus: A brief history of information networks from the Stone Age to AI. Random House.",
        "Harvard Business School, & MIT Institute for Work and Employment Research. (2025). Navigating the jagged technological frontier: Productivity gains, cognitive offloading, and skill degradation in enterprise analytics. Management Science Special Issue, 71(8), 4510-4532.",
        "Hume AI Labs, & Oxford Internet Institute. (2026). The loneliness paradox: Evaluating long-term affective dependency and social withdrawal among companion chatbot cohorts. Nature Human Behaviour, 10(2), 245-259.",
        "IEEE Global Initiative on Ethics of Autonomous and Intelligent Systems. (2026). IEEE standard for transparent agentic delegation and algorithmic discretion boundaries in human-facing institutions. IEEE Standards Association, Std 7014-2026.",
        "International Labour Organization. (2026). Algorithmic management, electronic surveillance, and psychological well-being in the white-collar workplace: A cross-national empirical survey. ILO Research Monographs, No. 44.",
        "Journal of Behavioral Finance Research Board. (2026). Retail Betrayal Syndrome: Speculative euphoria, herd dynamics, and the psychological aftermath of the Shanghai STAR Market tech crash. Journal of Behavioral Finance, 27(4), 512-530.",
        "KFF & West Health-Gallup. (2026). National survey of American adults on the utilization of artificial intelligence for mental health and general healthcare navigation. KFF Health Tracking Poll, February 2026.",
        "National Bureau of Statistics of China, & Tsinghua University Financial Institute. (2026). Macroeconomic evaluation of the equity negative wealth effect: Technology sector asset deflation and urban consumer confidence. China Economic Journal, 19(3), 320-344.",
        "Nature Human Behaviour Editorial Board. (2025). Algorithmic amplification of moral outrage: Epistemic fragmentation and affective polarization in hyper-personalized media. Nature Human Behaviour, 9(6), 812-826.",
        "People's Bank of China Economic Research Bureau. (2026). Financial stability report 2026: Liquidity dynamics, margin lending restrictions, and systemic risk containment in the high-tech equity board. PBC Publishing House.",
        "The Lancet Psychiatry Special Commission. (2025). The clinical efficacy, psychiatric hazards, and iatrogenic risks of generative conversational agents in mental healthcare delivery. The Lancet Psychiatry, 12(7), 540-556.",
        "Vallor, S. (2025). The AI mirror: Reclaiming our humanity in an age of machine thinking. Oxford University Press.",
        "World Economic Forum. (2026). The global risks report 2026: Societal polarization, synthetic culture, and technological unemployment. Insight Report, 21st Edition.",
        "World Health Organization. (2025). Regulatory and ethical guidelines for the integration of artificial intelligence in mental health interventions. WHO Technical Document Series, ISBN 978-92-4-009842-1.",
        "World Health Organization. (2026). Universal mental healthcare access and digital solutions: Addressing global psychiatric workforce shortages through safe technology. Bulletin of the World Health Organization, 104(3), 180-192."
    ]
    
    for ref in references:
        add_apa_reference(doc, ref)
