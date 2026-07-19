import re
import os

def convert_html_to_jsx(html_str):
    # Use next/link
    html_str = re.sub(r'<a(.*?)href="([^"]+)\.html(\?[^"]*)?"(.*?)>', r'<Link\1href="/\2\3"\4>', html_str)
    html_str = re.sub(r'<a(.*?)href="index\.html"(.*?)>', r'<Link\1href="/"\2>', html_str)
    html_str = re.sub(r'href="/index"', r'href="/"', html_str)
    
    # external links shouldn't use Link unless we want them to, but for now we'll leave `<Link href="http..."` which NextJS warns about, so let's revert http links to <a>
    html_str = re.sub(r'<Link(.*?)href="(http.*?)"(.*?)>', r'<a\1href="\2"\3>', html_str)
    html_str = re.sub(r'</a(.*?)>', r'</Link\1>', html_str)
    html_str = re.sub(r'</Link(.*?)>', lambda m: '</a>' if '<a' in m.group(0) else '</a>', html_str) # Simple hack, we will just manually fix closing tags in JSX
    # Actually wait, `</Link>` replacing `</a>` everywhere is dangerous. Let's do it carefully.
    
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

def main():
    legacy_path = "legacy/index.html"
    out_file = "src/components/Header.tsx"
    
    with open(legacy_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    start_idx = content.find('<div id="utilityBar"')
    end_idx = content.find('</header>') + 9
    
    header_html = content[start_idx:end_idx]
    
    # We will use normal <a> tags for now to avoid the Link vs a mismatch.
    # The developer can change to <Link> later if needed.
    
    html_str = header_html
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

    empty_tags = ['img', 'br', 'hr', 'input', 'meta', 'link', 'path', 'rect', 'circle', 'line', 'polygon', 'polyline']
    for tag in empty_tags:
        html_str = re.sub(rf'<{tag}([^>]*?)(?<!/)>', rf'<{tag}\1 />', html_str, flags=re.IGNORECASE)

    # Some SVG empty tags might have closing tags in html like <path d="..."></path>
    # The regex above converts <path d="..."> to <path d="..." />
    # So we need to remove the closing tags if they exist.
    for tag in empty_tags:
        html_str = re.sub(rf'</{tag}>', '', html_str, flags=re.IGNORECASE)

    html_str = re.sub(r'<!--(.*?)-->', r'{/* \1 */}', html_str, flags=re.DOTALL)
    
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
    
    html_str = re.sub(r'style="([^"]*)"', style_replacer, html_str)
    
    # Fix local links
    html_str = html_str.replace('href="index.html"', 'href="/"')
    html_str = html_str.replace('href="About_page.html"', 'href="/about"')
    html_str = html_str.replace('href="Portfolio_page.html"', 'href="/portfolio"')
    html_str = html_str.replace('href="IDE.html"', 'href="/ide"')
    html_str = html_str.replace('href="Services_page.html"', 'href="/services"')
    html_str = html_str.replace('href="Resume_page.html"', 'href="/resume"')
    html_str = html_str.replace('href="Skills_page.html"', 'href="/skills"')
    html_str = html_str.replace('href="Awards_page.html"', 'href="/awards"')
    html_str = html_str.replace('href="Blog_page.html"', 'href="/blog"')
    html_str = html_str.replace('href="FAQ_page.html"', 'href="/faq"')
    html_str = html_str.replace('href="Contact_page.html"', 'href="/contact"')
    html_str = html_str.replace('href="Case_study_page.html"', 'href="/case-study"')
    
    # Add client side logic
    template = f"""'use client';
import React, {{ useEffect, useState }} from 'react';
import Link from 'next/link';

export default function Header() {{
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [time, setTime] = useState("");

  useEffect(() => {{
    const handleScroll = () => {{
      setScrolled(window.scrollY > 20);
    }};
    window.addEventListener('scroll', handleScroll);
    
    const updateTime = () => {{
      const options: Intl.DateTimeFormatOptions = {{ timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit', second: '2-digit' }};
      setTime(new Intl.DateTimeFormat('en-US', options).format(new Date()) + " IST");
    }};
    updateTime();
    const timer = setInterval(updateTime, 1000);
    
    return () => {{
      window.removeEventListener('scroll', handleScroll);
      clearInterval(timer);
    }};
  }}, []);

  return (
    <>
      {html_str}
    </>
  );
}}
"""
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(template)
        
    print(f"Successfully created {out_file}")

if __name__ == "__main__":
    main()
