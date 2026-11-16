"""Remove all metadata from a PDF in place (needs PyMuPDF).

Usage: python3 strip_pdf_metadata.py file.pdf
Empties the document info, drops XMP metadata and pdfTeX's PTEX.* keys,
then checks that every page's text is unchanged.
"""
import os
import sys

import fitz

path = sys.argv[1]
tmp = path + ".tmp"

doc = fitz.open(path)
info = doc.xref_get_key(-1, "Info")
if info[0] == "xref":
    doc.update_object(int(info[1].split()[0]), "<<>>")
doc.del_xml_metadata()
for xref in range(1, doc.xref_length()):
    try:
        keys = doc.xref_get_keys(xref)
    except Exception:
        continue
    for key in keys:
        if key.startswith("PTEX") or key == "Metadata":
            doc.xref_set_key(xref, key, "null")
doc.save(tmp, garbage=4, deflate=True, use_objstms=1, no_new_id=True)

before, after = fitz.open(path), fitz.open(tmp)
assert before.page_count == after.page_count
assert all(before[i].get_text() == after[i].get_text() for i in range(before.page_count))
before.close()
after.close()
doc.close()
os.replace(tmp, path)
