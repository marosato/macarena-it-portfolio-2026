"""Valida referencias locales y empaqueta los archivos necesarios del portafolio."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from zipfile import ZipFile, ZIP_DEFLATED
import sys

root = Path(__file__).resolve().parents[1]
pages = list(root.glob('*.html')) + list((root / 'en').glob('*.html'))
class Document(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids, self.refs = set(), []
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'Duplicate ID: ' + attrs['id']
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs: self.refs.append(attrs[key])
        if 'srcset' in attrs:
            self.refs.extend(item.strip().split()[0] for item in attrs['srcset'].split(','))

docs = {p: Document(p.read_text(encoding='utf-8')) for p in pages}
files = set(pages) | {root/'main.css', root/'script.js', root/'README.md', root/'AGENTS.md', root/'tools/build.py', root/'tools/courses.json'}
checked = 0
for page, doc in docs.items():
    for ref in doc.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc: continue
        target = (page.parent / unquote(url.path)).resolve() if url.path else page
        assert target.is_relative_to(root), f'Outside project: {ref}'
        assert target.is_file(), f'Missing file: {target}'
        if url.fragment:
            assert unquote(url.fragment) in docs[target].ids, f'Missing anchor: {ref}'
        files.add(target)
        checked += 1
destination = Path(sys.argv[1])
with ZipFile(destination, 'w', ZIP_DEFLATED) as archive:
    for file in sorted(files): archive.write(file, 'Macarena-Rosato-Portfolio/' + file.relative_to(root).as_posix())
print(f'Validated {checked} local references across {len(pages)} pages. Packaged {len(files)} files: {destination}')
