#!/usr/bin/env python3
"""Build static redirects for the old academic website. No network access."""
import argparse
from html import escape
from pathlib import Path
from urllib.parse import urlsplit

parser = argparse.ArgumentParser()
parser.add_argument('--target', required=True, help='Verified new HTTPS homepage')
args = parser.parse_args()
target = args.target.rstrip('/')
parts = urlsplit(target)
if parts.scheme != 'https' or not parts.hostname or parts.query or parts.fragment:
    parser.error('Use an HTTPS website address without a query or fragment.')
root = Path(__file__).resolve().parent / 'docs'

for path, destination in {
    'index.html': target + '/',
    'home/index.html': target + '/',
    'research/index.html': target + '/research/',
    '404.html': target + '/',
}.items():
    page = root / path
    page.parent.mkdir(parents=True, exist_ok=True)
    url = escape(destination, quote=True)
    page.write_text(f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Xiangliang Li — New website</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0;url={url}">
</head><body><main>
<h1>Xiangliang Li</h1><p>This website has moved.</p>
<p><a href="{url}">Open the new website</a></p>
</main></body></html>''')
(root / 'CNAME').write_text('www.xiangliang.li\n')
(root / '.nojekyll').write_text('')
(root / 'robots.txt').write_text('User-agent: *\nAllow: /\n')
print('Built redirects to', target)
