# report_builder/config.py
# Modul konfigurasi dan helper format dokumen Word (.docx)
# Mengikuti standar APA akademis hitam-putih tanpa dekorasi warna

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def sanitize_text(text: str) -> str:
    """
    Membersihkan teks dari karakter yang dilarang (em dash dan en dash).
    Sesuai aturan: Dilarang menggunakan em dash maupun en dash.
    Ganti dengan titik, koma, titik dua, tanda kurung, atau tanda hubung standar.
    """
    if not text:
        return ""
    # Ganti em dash (\u2014) dengan koma atau tanda kurung
    clean = text.replace('\u2014', ', ')
    # Ganti en dash (\u2013) dengan tanda hubung ASCII standar (-)
    clean = clean.replace('\u2013', '-')
    # Pastikan tidak ada yang terlewat
    if '\u2014' in clean or '\u2013' in clean:
        raise ValueError("Teks masih mengandung karakter terlarang em-dash atau en-dash!")
    return clean

def add_page_number_to_run(run):
    """Menambahkan dynamic field PAGE Word pada footer."""
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = 'PAGE'
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)

def create_base_document() -> docx.Document:
    """Inisialisasi dokumen Word dengan format standar akademis."""
    doc = docx.Document()
    section = doc.sections[0]
    
    # Pengaturan ukuran halaman A4
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    
    # Margin 1 inci (2.54 cm) pada semua sisi
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    
    # Footer nomor halaman
    footer = section.footer
    footer_p = footer.paragraphs[0]
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Halaman ")
    run_f.font.name = "Times New Roman"
    run_f.font.size = Pt(10)
    run_f.font.color.rgb = RGBColor(0, 0, 0)
    
    num_run = footer_p.add_run()
    num_run.font.name = "Times New Roman"
    num_run.font.size = Pt(10)
    num_run.font.color.rgb = RGBColor(0, 0, 0)
    add_page_number_to_run(num_run)
    
    # Header minimalis kosong atau penanda dokumen riset
    header = section.header
    header_p = header.paragraphs[0]
    header_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_h = header_p.add_run("Laporan Riset Psikososial dan Pasar AI Global (2025-2026)")
    run_h.font.name = "Times New Roman"
    run_h.font.size = Pt(9)
    run_h.font.color.rgb = RGBColor(80, 80, 80)
    
    return doc

def add_title(doc, text: str):
    clean = sanitize_text(text)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.line_spacing = 1.3
    run = p.add_run(clean)
    run.font.name = "Times New Roman"
    run.font.size = Pt(18)
    run.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_subtitle(doc, text: str):
    clean = sanitize_text(text)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(14)
    p.paragraph_format.line_spacing = 1.2
    run = p.add_run(clean)
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.italic = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_author_block(doc, lines: list):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(24)
    p.paragraph_format.line_spacing = 1.3
    for i, line in enumerate(lines):
        clean = sanitize_text(line)
        run = p.add_run(clean)
        run.font.name = "Times New Roman"
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0, 0, 0)
        if i < len(lines) - 1:
            p.add_run("\n")
    return p

def add_h1(doc, text: str, page_break_before: bool = False):
    clean = sanitize_text(text)
    if page_break_before:
        doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.keep_with_next = True
    run = p.add_run(clean)
    run.font.name = "Times New Roman"
    run.font.size = Pt(14)
    run.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_h2(doc, text: str):
    clean = sanitize_text(text)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.keep_with_next = True
    run = p.add_run(clean)
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_h3(doc, text: str):
    clean = sanitize_text(text)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.keep_with_next = True
    run = p.add_run(clean)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.bold = True
    run.italic = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_body_p(doc, text: str, bold_prefix: str = None, space_after: float = 6.0):
    clean_text = sanitize_text(text)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    
    if bold_prefix:
        clean_prefix = sanitize_text(bold_prefix)
        r_pre = p.add_run(clean_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.bold = True
        r_pre.font.color.rgb = RGBColor(0, 0, 0)
        
    r_body = p.add_run(clean_text)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(12)
    r_body.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_blockquote(doc, quote_text: str, source_label: str = None):
    clean_q = sanitize_text(quote_text)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.right_indent = Inches(0.5)
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(6)
    
    r_q = p.add_run('"' + clean_q + '"')
    r_q.font.name = "Times New Roman"
    r_q.font.size = Pt(11)
    r_q.italic = True
    r_q.font.color.rgb = RGBColor(0, 0, 0)
    
    if source_label:
        clean_src = sanitize_text(source_label)
        p_src = doc.add_paragraph()
        p_src.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_src.paragraph_format.left_indent = Inches(0.5)
        p_src.paragraph_format.right_indent = Inches(0.5)
        p_src.paragraph_format.space_before = Pt(0)
        p_src.paragraph_format.space_after = Pt(6)
        r_s = p_src.add_run("(" + clean_src + ")")
        r_s.font.name = "Times New Roman"
        r_s.font.size = Pt(10)
        r_s.font.color.rgb = RGBColor(50, 50, 50)
    return p

def add_bullet(doc, text: str, bold_prefix: str = None):
    clean_text = sanitize_text(text)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.35)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    
    # Simbol bullet standar karakter ASCII atau bullet
    r_bullet = p.add_run("•  ")
    r_bullet.font.name = "Times New Roman"
    r_bullet.font.size = Pt(12)
    r_bullet.font.color.rgb = RGBColor(0, 0, 0)
    
    if bold_prefix:
        clean_prefix = sanitize_text(bold_prefix)
        r_pre = p.add_run(clean_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.bold = True
        r_pre.font.color.rgb = RGBColor(0, 0, 0)
        
    r_body = p.add_run(clean_text)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(12)
    r_body.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_apa_reference(doc, text: str):
    clean_text = sanitize_text(text)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(6)
    
    r = p.add_run(clean_text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def set_cell_border(cell, **kwargs):
    """
    Format border cell Word XML.
    kwargs: top, bottom, left, right, insideH, insideV
    value: dict(sz=8, val='single', color='000000', space='0')
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)
    
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = 'w:{}'.format(edge)
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)
            for key, val in edge_data.items():
                element.set(qn('w:{}'.format(key)), str(val))

def add_academic_table(doc, headers: list, data: list, col_widths: list, caption: str = None, notes: str = None):
    """
    Menambahkan tabel akademis standar hitam-putih APA Style:
    - Garis atas dan bawah tabel berwarna hitam.
    - Garis pemisah di bawah baris header berwarna hitam.
    - Tanpa garis vertikal dan tanpa pewarnaan background (murni monokrom).
    """
    if caption:
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_cap.paragraph_format.space_before = Pt(12)
        p_cap.paragraph_format.space_after = Pt(4)
        p_cap.paragraph_format.keep_with_next = True
        r_c = p_cap.add_run(sanitize_text(caption))
        r_c.font.name = "Times New Roman"
        r_c.font.size = Pt(11)
        r_c.bold = True
        r_c.font.color.rgb = RGBColor(0, 0, 0)
        
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    # Format baris header
    hdr_row = table.rows[0]
    for i, title in enumerate(headers):
        cell = hdr_row.cells[i]
        cell.width = Inches(col_widths[i])
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        run = p.add_run(sanitize_text(title))
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        
        # Garis atas tebal dan garis bawah header
        set_cell_border(cell, 
                        top=dict(val='single', sz=12, color='000000', space=0),
                        bottom=dict(val='single', sz=8, color='000000', space=0),
                        left=dict(val='none'),
                        right=dict(val='none'))
        
    # Format baris data
    for r_idx, row_values in enumerate(data):
        row = table.rows[r_idx + 1]
        is_last_row = (r_idx == len(data) - 1)
        for c_idx, val in enumerate(row_values):
            cell = row.cells[c_idx]
            cell.width = Inches(col_widths[c_idx])
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            run = p.add_run(sanitize_text(str(val)))
            run.font.name = "Times New Roman"
            run.font.size = Pt(10)
            run.font.color.rgb = RGBColor(0, 0, 0)
            
            if is_last_row:
                set_cell_border(cell, 
                                bottom=dict(val='single', sz=12, color='000000', space=0),
                                top=dict(val='none'),
                                left=dict(val='none'),
                                right=dict(val='none'))
            else:
                set_cell_border(cell, 
                                bottom=dict(val='none'),
                                top=dict(val='none'),
                                left=dict(val='none'),
                                right=dict(val='none'))
                
    if notes:
        p_not = doc.add_paragraph()
        p_not.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_not.paragraph_format.space_before = Pt(3)
        p_not.paragraph_format.space_after = Pt(10)
        r_n = p_not.add_run(sanitize_text(notes))
        r_n.font.name = "Times New Roman"
        r_n.font.size = Pt(9)
        r_n.italic = True
        r_n.font.color.rgb = RGBColor(60, 60, 60)
        
    return table

def add_figure(doc, image_path: str, caption: str, width_inches: float = 5.8, notes: str = None):
    """
    Menambahkan gambar ilustrasi akademis ke dalam dokumen Word secara rapi:
    - Gambar diposisikan di tengah (centered) dengan lebar terukur.
    - Keterangan gambar (caption) dicantumkan di bawah gambar sesuai standar APA.
    - Catatan metodologis gambar dicetak dengan font Times New Roman 9pt miring.
    """
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(12)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(image_path, width=Inches(width_inches))
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(4)
    p_cap.paragraph_format.keep_with_next = True
    r_c = p_cap.add_run(sanitize_text(caption))
    r_c.font.name = "Times New Roman"
    r_c.font.size = Pt(10)
    r_c.bold = True
    r_c.font.color.rgb = RGBColor(0, 0, 0)
    
    if notes:
        p_not = doc.add_paragraph()
        p_not.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_not.paragraph_format.space_before = Pt(0)
        p_not.paragraph_format.space_after = Pt(12)
        r_n = p_not.add_run(sanitize_text(notes))
        r_n.font.name = "Times New Roman"
        r_n.font.size = Pt(9)
        r_n.italic = True
        r_n.font.color.rgb = RGBColor(60, 60, 60)

