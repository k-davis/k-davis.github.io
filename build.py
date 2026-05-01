import os
import shutil
from pathlib import Path

shutil.rmtree('build')
shutil.copytree('src', 'build')

build_dir = Path('./build')
css_path = Path('./build/styles.css')

for md_file in build_dir.glob('**/*.md'):
    html_filename = md_file.with_suffix('.html')
    relative_css_path = os.path.relpath(css_path, md_file.parent)

    print(f"Converting {md_file} to {html_filename}")
    exit_code = os.system(f"pandoc -M document-css=false --standalone --css {relative_css_path} --to=html --output={html_filename} {md_file}")
    
    if exit_code != 0:
        raise ValueError(f"Error converting {md_file.absolute()} to HTML")
    
    os.remove(md_file)