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

def main():
    legacy_path = "legacy/Portfolio_page.html"
        
    with open(legacy_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    header_end = content.find("</header>")
    if header_end == -1:
        body_start = content.find("<body")
        header_end = content.find(">", body_start) if body_start != -1 else 0
    else:
        header_end += 9

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

    # Re-inject the grid!
    grid_html = """<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-10">
            {projects.map((project, index) => (
              <div key={index} className="group flex flex-col bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-2">
                <div className="relative h-48 bg-slate-100 overflow-hidden">
                  <div className="absolute inset-0 bg-gradient-to-tr from-slate-200 to-slate-100 group-hover:scale-105 transition-transform duration-700"></div>
                  <div className="absolute top-4 right-4 flex gap-2">
                    {project.repoUrl && (
                      <a href={project.repoUrl} target="_blank" rel="noopener noreferrer" className="w-8 h-8 rounded-full bg-white/90 backdrop-blur shadow-sm flex items-center justify-center text-slate-700 hover:text-primary hover:scale-110 transition-all">
                        <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
                      </a>
                    )}
                  </div>
                </div>
                
                <div className="p-6 sm:p-8 flex-1 flex flex-col">
                  <div className="flex flex-wrap gap-2 mb-4">
                    {project.tags.map((tag, i) => (
                      <span key={i} className="px-2.5 py-1 rounded-md bg-slate-100 text-slate-600 text-[10px] font-bold uppercase tracking-wider">{tag}</span>
                    ))}
                  </div>
                  
                  <h3 className="text-xl font-bold text-slate-900 mb-3 group-hover:text-primary transition-colors">{project.title}</h3>
                  <p className="text-slate-500 text-sm leading-relaxed mb-6 flex-grow">{project.description}</p>
                </div>
              </div>
            ))}
          </div>"""
    
    # We will regex replace <div id="projectsGrid"...></div>
    jsx_content = re.sub(r'<div id="projectsGrid"[^>]*>.*?</div>', grid_html, jsx_content, flags=re.DOTALL)

    out_file = "src/app/portfolio/page.tsx"
    
    template = f"""import React from 'react';
import {{ getGithubProjects }} from '@/lib/github';

export const metadata = {{
  title: 'Portfolio | Rishvin Labs',
}};

export default async function Portfolio() {{
  const projects = await getGithubProjects();

  return (
    <>
      {jsx_content}
    </>
  );
}}
"""
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(template)
        
    print(f"Successfully converted Portfolio_page.html to {out_file}")

if __name__ == "__main__":
    main()
