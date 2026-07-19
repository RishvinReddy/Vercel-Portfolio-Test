import re
import os

def convert_html_to_jsx(html_str):
    html_str = re.sub(r'<script.*?</script>', '', html_str, flags=re.IGNORECASE | re.DOTALL)
    html_str = re.sub(r'<style.*?</style>', '', html_str, flags=re.IGNORECASE | re.DOTALL)

    html_str = html_str.replace('class="', 'className="')
    html_str = html_str.replace('for="', 'htmlFor="')
    html_str = html_str.replace('tabindex="', 'tabIndex="')
    html_str = html_str.replace('onclick="', 'data-onclick="')
    
    svg_attrs = [
        "stroke-width", "stroke-linecap", "stroke-linejoin",
        "stroke-dasharray", "stroke-dashoffset", "fill-rule", "clip-rule",
        "view-box"
    ]
    for attr in svg_attrs:
        camel = "".join(word.title() if i > 0 else word for i, word in enumerate(attr.split("-")))
        html_str = html_str.replace(f'{attr}=', f'{camel}=')

    empty_tags = ['img', 'br', 'hr', 'input', 'meta', 'link']
    for tag in empty_tags:
        html_str = re.sub(rf'<{tag}([^>]*?)(?<!/)>', rf'<{tag}\1 />', html_str, flags=re.IGNORECASE)

    html_str = re.sub(r'<!--(.*?)-->', r'{/* \1 */}', html_str, flags=re.DOTALL)

    return html_str

def convert_page(legacy_path, out_file, title):
    with open(legacy_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    header_end = content.find("</header>")
    if header_end == -1:
        body_start = content.find("<body")
        header_end = content.find(">", body_start) if body_start != -1 else 0
    else:
        header_end += 9

    footer_start = content.find("</main>")
    if footer_start != -1:
        footer_start += 7
    else:
        footer_start = content.rfind("<footer")
        if footer_start == -1:
            footer_start = content.rfind("</body>")

    main_html = content[header_end:footer_start].strip()

    jsx_content = convert_html_to_jsx(main_html)
    
    def style_replacer(match):
        style_val = match.group(1)
        parts = style_val.split(';')
        rules = []
        for p in parts:
            if ':' in p:
                k, v = p.split(':', 1)
                k = k.strip()
                v = v.strip().replace('"', "'")
                if '-' in k:
                    k = "".join(word.title() if i > 0 else word for i, word in enumerate(k.split("-")))
                rules.append(f'{k}: "{v}"')
        return 'style={{ ' + ', '.join(rules) + ' }}'
    
    jsx_content = re.sub(r'style="([^"]*)"', style_replacer, jsx_content)
    
    component_name = "".join(word.title() for word in title.split())
    
    template = f"""import React from 'react';

export const metadata = {{
  title: '{title} | Rishvin Labs',
}};

export default function {component_name}() {{
  return (
    <>
      {jsx_content}
    </>
  );
}}
"""
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(template)
        
    print(f"Successfully converted {legacy_path} to {out_file}")

def main():
    pages = [
        ("legacy/Blog_page.html", "src/app/blog/page.tsx", "Blog"),
        ("legacy/FAQ_page.html", "src/app/faq/page.tsx", "FAQ")
    ]
    
    for legacy_path, out_file, title in pages:
        if os.path.exists(legacy_path):
            convert_page(legacy_path, out_file, title)

if __name__ == "__main__":
    main()
