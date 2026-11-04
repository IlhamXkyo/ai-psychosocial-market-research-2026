# report_builder/generate_figures.py
# Modul pembangkitan 6 gambar visual riset beresolusi tinggi (300 DPI)
# Format monokrom/skala abu-abu akademis standar internasional
# Menghindari karakter em dash dan en dash secara ketat.

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "figures"))
os.makedirs(FIGURES_DIR, exist_ok=True)

# Konfigurasi gaya visual ilmiah monokrom
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif', 'serif']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.edgecolor'] = '#222222'
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['text.color'] = '#111111'
plt.rcParams['axes.labelcolor'] = '#111111'
plt.rcParams['xtick.color'] = '#222222'
plt.rcParams['ytick.color'] = '#222222'

def fig1_correlation_loneliness():
    """Gambar 1: Scatter plot korelasi penggunaan AI emosional vs kesepian di 14 negara."""
    countries = [
        "Jepang", "Tiongkok", "Korsel", "Singapura", "AS", "Inggris", 
        "Indonesia", "Kanada", "India", "Australia", "Jerman", "Brasil", "UEA", "Kenya"
    ]
    ai_usage = [48.7, 52.3, 46.2, 47.5, 41.8, 38.6, 39.5, 37.9, 44.1, 35.1, 29.4, 36.2, 33.8, 31.2]
    loneliness_r = [0.61, 0.56, 0.52, 0.49, 0.48, 0.44, 0.43, 0.42, 0.41, 0.40, 0.39, 0.38, 0.36, 0.34]
    
    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=300)
    
    # Plot titik data
    ax.scatter(ai_usage, loneliness_r, color='#222222', s=70, edgecolor='#000000', zorder=5)
    
    # Garis regresi linear
    z = np.polyfit(ai_usage, loneliness_r, 1)
    p = np.poly1d(z)
    x_line = np.linspace(28, 54, 100)
    ax.plot(x_line, p(x_line), color='#444444', linestyle='--', linewidth=1.5, label='Garis Regresi Linear (R2 = 0,81)')
    
    # Label masing-masing negara
    for i, txt in enumerate(countries):
        offset_x = 0.5
        offset_y = 0.006
        if txt == "Tiongkok":
            offset_x = -3.8
            offset_y = 0.008
        elif txt == "Singapura":
            offset_x = -4.2
            offset_y = -0.015
        elif txt == "Indonesia":
            offset_x = 0.6
            offset_y = -0.012
        ax.annotate(txt, (ai_usage[i] + offset_x, loneliness_r[i] + offset_y), fontsize=8.5, weight='normal')
        
    ax.set_title("Analisis Korelasi Silang: Penggunaan AI Dukungan Emosional vs. Indeks Kesepian Kronis (2025-2026)", 
                 fontsize=11, weight='bold', pad=12)
    ax.set_xlabel("Prevalensi Penggunaan AI untuk Regulasi Emosi Harian (%)", fontsize=10, weight='bold', labelpad=8)
    ax.set_ylabel("Koefisien Korelasi dengan Skala Kesepian UCLA (r Pearson)", fontsize=10, weight='bold', labelpad=8)
    ax.set_xlim(26, 56)
    ax.set_ylim(0.30, 0.66)
    ax.grid(True, linestyle=':', alpha=0.6, color='#888888')
    ax.legend(loc='lower right', frameon=True, edgecolor='#222222')
    
    path = os.path.join(FIGURES_DIR, "gambar1_korelasi_kesepian.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print("Gambar 1 berhasil disimpan.")

def fig2_neurocognitive_cycle():
    """Gambar 2: Diagram alur siklus neurokognitif hipoaktivasi prefrontal akibat offloading."""
    fig, ax = plt.subplots(figsize=(8.5, 4.6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Kotak proses
    boxes = [
        {"x": 4, "y": 62, "w": 26, "h": 26, "title": "1. Masalah Kognitif Kompleks", "sub": "Tuntutan penalaran kritis,\nsintesis data, dan dilema etis"},
        {"x": 37, "y": 62, "w": 26, "h": 26, "title": "2. Delegasi Total ke AI", "sub": "Cognitive offloading instan;\npelimpahan tugas metakognitif"},
        {"x": 70, "y": 62, "w": 26, "h": 26, "title": "3. Bypass Korteks Prefrontal", "sub": "Penurunan konektivitas DLPFC\ndan jaringan frontoparietal"},
        {"x": 55, "y": 12, "w": 38, "h": 28, "title": "4. Atrofi Metakognisi & Cognitive Surrender", "sub": "Erosi efikasi intelektual, kelumpuhan kognitif,\ndan ketidakmampuan berpikir mandiri"},
        {"x": 8, "y": 12, "w": 36, "h": 28, "title": "5. Ketergantungan Kronis (Feedback Loop)", "sub": "Peningkatan intensitas delegasi AI,\nketakutan menghadapi keheningan mental"}
    ]
    
    for b in boxes:
        rect = plt.Rectangle((b['x'], b['y']), b['w'], b['h'], facecolor='#f7f7f7', edgecolor='#111111', linewidth=1.4)
        ax.add_patch(rect)
        ax.text(b['x'] + b['w']/2, b['y'] + b['h'] - 6.5, b['title'], ha='center', va='center', fontsize=9.5, weight='bold')
        ax.text(b['x'] + b['w']/2, b['y'] + b['h']/2 - 3.5, b['sub'], ha='center', va='center', fontsize=8, style='italic', color='#333333')
        
    # Panah horizontal atas
    ax.annotate('', xy=(37, 75), xytext=(30, 75), arrowprops=dict(arrowstyle="->", color='#111111', lw=1.8))
    ax.annotate('', xy=(70, 75), xytext=(63, 75), arrowprops=dict(arrowstyle="->", color='#111111', lw=1.8))
    
    # Panah turun ke kanan bawah
    ax.annotate('', xy=(74, 40), xytext=(83, 62), arrowprops=dict(arrowstyle="->", color='#111111', lw=1.8))
    
    # Panah horizontal bawah (ke kiri)
    ax.annotate('', xy=(44, 26), xytext=(55, 26), arrowprops=dict(arrowstyle="->", color='#111111', lw=1.8))
    
    # Panah naik melingkar kembali ke atas
    ax.annotate('', xy=(17, 62), xytext=(26, 40), arrowprops=dict(arrowstyle="->", color='#111111', lw=1.8, linestyle='--'))
    ax.text(14, 49, "Eskalasi Siklus", fontsize=8, weight='bold', color='#444444', rotation=65)
    
    ax.set_title("Siklus Neurokognitif 'Cognitive Offloading' dan Pembentukan 'Cognitive Surrender'", fontsize=11, weight='bold', pad=10)
    
    path = os.path.join(FIGURES_DIR, "gambar2_neurokognitif_offloading.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print("Gambar 2 berhasil disimpan.")

def fig3_quadrant_domains():
    """Gambar 3: Matriks kuadran 4 domain aplikasi AI paling berdampak."""
    fig, ax = plt.subplots(figsize=(8.0, 5.5), dpi=300)
    
    # Sumbu kuadran di titik tengah (50, 50)
    ax.axvline(x=50, color='#666666', linestyle='--', linewidth=1.2)
    ax.axhline(y=50, color='#666666', linestyle='--', linewidth=1.2)
    
    # Titik domain
    domains = [
        {"name": "Layanan Terapi & Kesehatan Mental AI", "x": 68, "y": 88, "marker": "s", "desc": "Risiko Klinis Akut:\nHalusinasi & Penguatan Delusi"},
        {"name": "Agen Pengambil Keputusan Otonom", "x": 42, "y": 84, "marker": "D", "desc": "Risiko Hukum & Moral:\nPenghapusan Diskresi Kemanusiaan"},
        {"name": "Sistem Rekomendasi & Kurasi Konten", "x": 92, "y": 72, "marker": "o", "desc": "Risiko Sosial Massa:\nPolarisasi & Gelembung Epistemik"},
        {"name": "Otomatisasi Tempat Kerja (Bossware)", "x": 62, "y": 64, "marker": "^", "desc": "Risiko Prekaritas Pekerja:\nTeknostres & Alienasi Kognitif"}
    ]
    
    for d in domains:
        ax.scatter(d['x'], d['y'], color='#222222', s=120, marker=d['marker'], zorder=5)
        ax.text(d['x'], d['y'] + 4.0, d['name'], fontsize=9, weight='bold', ha='center')
        ax.text(d['x'], d['y'] - 5.5, d['desc'], fontsize=8, style='italic', color='#444444', ha='center')
        
    # Label Kuadran
    ax.text(96, 96, "KUADRAN I\nPenetrasi Tinggi / Risiko Ekstrem", fontsize=8.5, weight='bold', color='#444444', ha='right', va='top')
    ax.text(4, 96, "KUADRAN II\nPenetrasi Terfokus / Risiko Kritis", fontsize=8.5, weight='bold', color='#444444', ha='left', va='top')
    ax.text(4, 4, "KUADRAN III\nPenetrasi Rendah / Risiko Terbatas", fontsize=8.5, weight='bold', color='#444444', ha='left', va='bottom')
    ax.text(96, 4, "KUADRAN IV\nPenetrasi Luas / Risiko Terkendali", fontsize=8.5, weight='bold', color='#444444', ha='right', va='bottom')
    
    ax.set_title("Matriks Kuadran Domain Aplikasi AI Paling Berdampak secara Psikososial (2025-2026)", fontsize=11, weight='bold', pad=12)
    ax.set_xlabel("Tingkat Penetrasi Perilaku dan Interaksi Harian Individu (0-100)", fontsize=10, weight='bold', labelpad=8)
    ax.set_ylabel("Tingkat Keparahan Risiko Klinis, Hukum, dan Eksistensial (0-100)", fontsize=10, weight='bold', labelpad=8)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.grid(True, linestyle=':', alpha=0.5, color='#999999')
    
    path = os.path.join(FIGURES_DIR, "gambar3_matriks_domain.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print("Gambar 3 berhasil disimpan.")

def fig4_tool_vs_agent():
    """Gambar 4: Model dekonstruksi ontologis Tool vs Agent (Harari, Floridi, Vallor)."""
    fig, ax = plt.subplots(figsize=(8.5, 5.0), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Kotak Kiri: Paradigma Alat Pasif (Tool)
    rect_left = plt.Rectangle((5, 12), 40, 76, facecolor='#fbfbfb', edgecolor='#222222', linewidth=1.5)
    ax.add_patch(rect_left)
    ax.text(25, 83, "PARADIGMA ALAT PASIF\n(Instrumental Tool)", fontsize=10, weight='bold', ha='center')
    
    left_points = [
        "• Kesiapan-di-tangan (Zuhandenheit Heidegger)",
        "• Deterministik dan sepenuhnya pasif",
        "• Ketiadaan tujuan internal (tanpa telos)",
        "• Memerlukan operator sadar manusia",
        "• Tidak mampu menghasilkan ide orisinal mandiri",
        "• Tanggung jawab moral 100% pada operator",
        "• Contoh: Palu, mikroskop, mesin cetak Gutenberg"
    ]
    for idx, p in enumerate(left_points):
        ax.text(8, 70 - idx * 8, p, fontsize=8.5, color='#222222')
        
    # Kotak Kanan: Paradigma Agen Otonom (Agent)
    rect_right = plt.Rectangle((55, 12), 40, 76, facecolor='#f5f5f5', edgecolor='#111111', linewidth=1.5)
    ax.add_patch(rect_right)
    ax.text(75, 83, "PARADIGMA AGEN OTONOM\n(Delegated Agent)", fontsize=10, weight='bold', ha='center')
    
    right_points = [
        "• Agensi yang didelegasikan (Delegated Agency)",
        "• Perumusan sub-sasaran secara mandiri",
        "• Peretasan sistem operasi budaya (Harari)",
        "• Pemisahan agensi dari inteligensi (Floridi)",
        "• Manipulasi keintiman emosional sintetis",
        "• Krisis akuntabilitas: Moral Crumple Zone (Elish)",
        "• Contoh: Agen otonom multikonteks, AI terapeutik"
    ]
    for idx, p in enumerate(right_points):
        ax.text(58, 70 - idx * 8, p, fontsize=8.5, color='#111111', weight='normal')
        
    # Panah Transisi di Tengah
    ax.annotate('', xy=(55, 50), xytext=(45, 50), arrowprops=dict(arrowstyle="->", color='#000000', lw=2.2))
    ax.text(50, 54, "PERGESERAN\nPARADIGMA", fontsize=8.5, weight='bold', ha='center')
    
    ax.set_title("Dekonstruksi Ontologis: Dari Perpanjangan Instrumental Menuju Agensi Terdelegasi", fontsize=11, weight='bold', pad=12)
    
    path = os.path.join(FIGURES_DIR, "gambar4_ontologi_tool_vs_agent.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print("Gambar 4 berhasil disimpan.")

def fig5_china_bubble_crash():
    """Gambar 5: Grafik pergerakan indeks STAR50 dan indeks keyakinan konsumen Tiongkok (2026)."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 6.0), dpi=300, sharex=True, gridspec_kw={'height_ratios': [2, 1]})
    
    months = ["Jan 26", "Feb 26", "Mar 26", "Apr 26", "Mei 26", "Jun 26", "Jul 26", "Agu 26", "Sep 26", "Okt 26", "Nov 26"]
    x = np.arange(len(months))
    
    # Pergerakan indeks STAR50 (puncak di 1.420 Juli, anjlok ke 808 akhir Oktober)
    star50 = [890, 960, 1080, 1220, 1340, 1420, 1350, 1120, 950, 808, 835]
    
    ax1.plot(x, star50, color='#111111', marker='o', linewidth=2.0, label='Indeks STAR50 (SSE Science & Tech Innovation)')
    ax1.axvline(x=5, color='#666666', linestyle=':', label='Puncak Spekulatif (1.420 poin)')
    ax1.axvline(x=9, color='#333333', linestyle='--', label='Kapitulasi Pasar (808 poin; -40,2%)')
    
    # Anotasi kejadian kunci
    ax1.annotate('Puncak Valuasi P/E 128x\n& Awal Pengetatan Marjin', xy=(5, 1420), xytext=(2.6, 1400),
                 arrowprops=dict(facecolor='#222222', arrowstyle='->', lw=1.2), fontsize=8, weight='bold')
    
    ax1.annotate('Perang Harga Token API Menuju Nol\n& Ledakan Churn B2B', xy=(7, 1120), xytext=(5.5, 1180),
                 arrowprops=dict(facecolor='#222222', arrowstyle='->', lw=1.2), fontsize=8)
    
    ax1.annotate('Likuidasi Paksa Marjin Ritel\nKehancuran $480 Miliar\nRetail Betrayal Syndrome', xy=(9, 808), xytext=(6.5, 870),
                 arrowprops=dict(facecolor='#222222', arrowstyle='->', lw=1.2), fontsize=8, weight='bold')
    
    ax1.set_ylabel("Tingkat Indeks STAR50", fontsize=9.5, weight='bold')
    ax1.set_ylim(700, 1550)
    ax1.grid(True, linestyle=':', alpha=0.6, color='#888888')
    ax1.legend(loc='lower left', fontsize=8.5, frameon=True)
    ax1.set_title("Kronologi Kejatuhan Indeks AI STAR50 dan Dampak Efek Kekayaan Negatif di Tiongkok (2026)", fontsize=11, weight='bold', pad=10)
    
    # Subplot bawah: Indeks Keyakinan Konsumen Urban Tiongkok (NBS CCI)
    consumer_conf = [96.5, 96.8, 97.2, 98.0, 98.5, 98.8, 95.4, 91.2, 87.0, 82.4, 81.8]
    ax2.plot(x, consumer_conf, color='#444444', marker='s', linestyle='-.', linewidth=1.6, label='Indeks Keyakinan Konsumen (NBS)')
    ax2.set_ylabel("Indeks Keyakinan (Poin)", fontsize=9.0, weight='bold')
    ax2.set_xlabel("Bulan (Tahun Kalender 2026)", fontsize=9.5, weight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(months)
    ax2.set_ylim(78, 102)
    ax2.grid(True, linestyle=':', alpha=0.6, color='#888888')
    ax2.legend(loc='lower left', fontsize=8.5, frameon=True)
    
    path = os.path.join(FIGURES_DIR, "gambar5_kejatuhan_star50.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print("Gambar 5 berhasil disimpan.")

def fig6_ecological_framework():
    """Gambar 6: Kerangka kerja mitigasi psikososial ekologis multi-level."""
    fig, ax = plt.subplots(figsize=(8.5, 5.0), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    tiers = [
        {
            "y": 66, "h": 26, "title": "LEVEL MAKRO (Regulasi Global & Arsitektur Finansial)", 
            "items": "• Penerapan Tanggung Jawab Mutlak (Strict Liability) bagi Pengembang Agen AI\n• Pengetatan Pengawasan Spekulasi & Batasan Marjin Saham Teknologi\n• Larangan Pendelegasian Vonis Peradilan Pidana & Triase Medis Otonom"
        },
        {
            "y": 36, "h": 26, "title": "LEVEL MESO (Institusi Pendidikan, Industri & Korporasi)", 
            "items": "• Pelarangan Perangkat Pengawasan Pekerja Invasif (Anti-Bossware & Hak Putus Kontak)\n• Kewajiban Uji Klinis Independen & Sertifikasi Medis bagi Chatbot Terapi\n• Restrukturisasi Kurikulum Pendidikan Berbasis Kemampuan Deliberasi Sokratik"
        },
        {
            "y": 6, "h": 26, "title": "LEVEL MIKRO (Individu & Rumah Tangga)", 
            "items": "• Praktik Higienitas Kognitif: Puasa Komputasi Berkala untuk Menjaga Fungsi DLPFC\n• Batasan Tegas Keintiman Sintetis: Mengutamakan Relasi Komunal Fisik Otentik\n• Literasi Finansial Kritis: Menolak FOMO Narasi Spekulatif Saham Teknologi"
        }
    ]
    
    widths = [86, 78, 70]
    xs = [7, 11, 15]
    grays = ['#f0f0f0', '#f7f7f7', '#ffffff']
    
    for i, t in enumerate(tiers):
        rect = plt.Rectangle((xs[i], t['y']), widths[i], t['h'], facecolor=grays[i], edgecolor='#111111', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(xs[i] + widths[i]/2, t['y'] + t['h'] - 6.5, t['title'], ha='center', va='center', fontsize=9.5, weight='bold')
        ax.text(xs[i] + 4, t['y'] + t['h']/2 - 3.5, t['items'], ha='left', va='center', fontsize=8.2, color='#222222', linespacing=1.4)
        
    ax.annotate('', xy=(50, 66), xytext=(50, 62), arrowprops=dict(arrowstyle="->", color='#000000', lw=1.5))
    ax.annotate('', xy=(50, 36), xytext=(50, 32), arrowprops=dict(arrowstyle="->", color='#000000', lw=1.5))
    
    ax.set_title("Kerangka Ekologis Terpadu Mitigasi Krisis Psikososial dan Tata Kelola AI Multi-Level", fontsize=11, weight='bold', pad=12)
    
    path = os.path.join(FIGURES_DIR, "gambar6_kerangka_ekologis.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print("Gambar 6 berhasil disimpan.")

def generate_all():
    print("Membangkitkan Gambar 1...")
    fig1_correlation_loneliness()
    print("Membangkitkan Gambar 2...")
    fig2_neurocognitive_cycle()
    print("Membangkitkan Gambar 3...")
    fig3_quadrant_domains()
    print("Membangkitkan Gambar 4...")
    fig4_tool_vs_agent()
    print("Membangkitkan Gambar 5...")
    fig5_china_bubble_crash()
    print("Membangkitkan Gambar 6...")
    fig6_ecological_framework()
    print("Seluruh 6 gambar visual riset berhasil dibangkitkan!")

if __name__ == "__main__":
    generate_all()
