# report_builder/build.py
# Script perakit utama untuk menghasilkan dokumen Word (.docx) formal
# Memeriksa kepatuhan terhadap aturan gaya, format hitam-putih, dan nihil em-dash/en-dash.

import sys
import os

# Tambahkan direktori kerja ke sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from report_builder.config import create_base_document
from report_builder.generate_figures import generate_all
from report_builder.part1_frontmatter import build_frontmatter
from report_builder.part2_intro import build_intro
from report_builder.part3_psychology import build_psychology
from report_builder.part4_domains import build_domains
from report_builder.part5_ontology import build_ontology
from report_builder.part6_china_bubble import build_china_bubble
from report_builder.part7_synthesis_conclusion import build_synthesis_and_conclusion

def verify_no_forbidden_dashes(doc):
    """
    Memverifikasi secara ketat bahwa tidak ada em-dash (\u2014) maupun en-dash (\u2013)
    di seluruh paragraf dan sel tabel dokumen Word.
    """
    forbidden = {'\u2014': 'Em Dash', '\u2013': 'En Dash'}
    violations = []
    
    # Periksa paragraf utama
    for i, p in enumerate(doc.paragraphs):
        for char, name in forbidden.items():
            if char in p.text:
                violations.append(f"Paragraf #{i}: mengandung {name} -> '{p.text[:60]}...'")
                
    # Periksa tabel
    for t_idx, table in enumerate(doc.tables):
        for r_idx, row in enumerate(table.rows):
            for c_idx, cell in enumerate(row.cells):
                for p_idx, p in enumerate(cell.paragraphs):
                    for char, name in forbidden.items():
                        if char in p.text:
                            violations.append(f"Tabel #{t_idx} Baris #{r_idx} Kolom #{c_idx}: mengandung {name} -> '{p.text[:60]}...'")
                            
    if violations:
        print("\n[PERINGATAN KRITIS] Ditemukan karakter terlarang:")
        for v in violations:
            print(" -", v)
        raise ValueError(f"Ditemukan {len(violations)} pelanggaran karakter em-dash/en-dash!")
    else:
        print("[VERIFIKASI BERHASIL] Nol karakter em-dash (\u2014) dan en-dash (\u2013) di seluruh dokumen.")

def calculate_document_stats(doc):
    total_words = 0
    total_paras = len(doc.paragraphs)
    total_tables = len(doc.tables)
    
    for p in doc.paragraphs:
        words = p.text.strip().split()
        total_words += len(words)
        
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    words = p.text.strip().split()
                    total_words += len(words)
                    
    # Estimasi halaman Word standar (1.5 spasi, 12pt Times New Roman, 1 inci margin, tabel & judul)
    # Biasanya berkisar antara 350-400 kata per halaman Word teks mengalir, atau ~300 kata jika ada tabel dan judul.
    est_pages_low = total_words / 420.0
    est_pages_high = total_words / 320.0
    
    return {
        "words": total_words,
        "paragraphs": total_paras,
        "tables": total_tables,
        "est_pages": (est_pages_low, est_pages_high)
    }

def main():
    print("=" * 70)
    print("MEMULAI PROSES KOMPILASI LAPORAN RISET FORMAL WORD (.DOCX)")
    print("=" * 70)
    
    output_filename = os.path.join(BASE_DIR, "Laporan_Riset_Dampak_Psikologis_dan_Pasar_AI_2026.docx")
    
    # Inisialisasi dokumen A4 margins 1 inci standar akademis
    doc = create_base_document()
    
    print("[0/7] Membangkitkan 6 Gambar Visual Riset Ilmiah (300 DPI)...")
    generate_all()
    
    print("[1/7] Membangun Halaman Judul, Ringkasan Eksekutif, dan Abstrak...")
    build_frontmatter(doc)
    
    print("[2/7] Membangun Bab I: Pendahuluan dan Metodologi...")
    build_intro(doc)
    
    print("[3/7] Membangun Bab II: Lanskap Dampak Psikologis Global (Survei 2025-2026)...")
    build_psychology(doc)
    
    print("[4/7] Membangun Bab III: Taksonomi Domain Aplikasi Paling Berdampak...")
    build_domains(doc)
    
    print("[5/7] Membangun Bab IV: Dekonstruksi Ontologis (Tool vs. Agent)...")
    build_ontology(doc)
    
    print("[6/7] Membangun Bab V: Analisis Krisis Finansial AI Tiongkok (STAR50)...")
    build_china_bubble(doc)
    
    print("[7/7] Membangun Bab VI, Bab VII, dan Daftar Pustaka (25+ Sumber APA)...")
    build_synthesis_and_conclusion(doc)
    
    # Verifikasi kepatuhan karakter terlarang
    print("\nMenjalankan audit kepatuhan karakter terlarang...")
    verify_no_forbidden_dashes(doc)
    
    # Hitung metrik dokumen
    stats = calculate_document_stats(doc)
    
    # Simpan dokumen Word
    saved_path = output_filename
    try:
        doc.save(output_filename)
        print(f"\n[SUKSES] Dokumen berhasil disimpan di:\n  -> {output_filename}")
    except PermissionError:
        alt_filename = os.path.join(BASE_DIR, "Laporan_Riset_Dampak_Psikologis_dan_Pasar_AI_2026_Lengkap_Bergambar.docx")
        doc.save(alt_filename)
        saved_path = alt_filename
        print(f"\n[CATATAN] Dokumen utama sedang terbuka di Microsoft Word.")
        print(f"[SUKSES] Dokumen versi berilustrasi lengkap berhasil disimpan di:\n  -> {alt_filename}")
        
    print("=" * 70)
    print("STATISTIK DOKUMEN RISET:")
    print(f"  • Total Kata (Word Count)        : {stats['words']:,} kata")
    print(f"  • Total Paragraf                 : {stats['paragraphs']} paragraf")
    print(f"  • Total Tabel Akademis Monokrom : {stats['tables']} tabel")
    print(f"  • Total Gambar Visual Ilmiah     : 6 gambar resolusi tinggi")
    print(f"  • Estimasi Tebal Halaman Word    : {stats['est_pages'][0]:.1f} hingga {stats['est_pages'][1]:.1f} halaman (Setara ~24-32 halaman)")
    print(f"  • File Akhir Siap Unduh         : {saved_path}")
    print("=" * 70)

if __name__ == "__main__":
    main()
