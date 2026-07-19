import re

def fix_header():
    path = "src/components/Header.tsx"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace <a href="/"> with <Link href="/">
    content = re.sub(r'<a([^>]+href="/".*?)>', r'<Link\1>', content)
    content = re.sub(r'</a(.*?)>', lambda m: '</Link>' if m.string.rfind('<Link', 0, m.start()) > m.string.rfind('</Link>', 0, m.start()) else m.group(0), content) # this is flaky, let's do a simple regex for the specific lines
    
    # Better: just replace all local links manually
    # Let's just find <a href="/">...</a> and replace
    content = content.replace('<a className="flex items-center gap-3 group shrink-0" href="/">', '<Link className="flex items-center gap-3 group shrink-0" href="/">')
    content = content.replace('<a className="hidden lg:flex items-center justify-center w-8 h-8 rounded-full bg-slate-900 text-white hover:scale-105 transition-transform" href="/">', '<Link className="hidden lg:flex items-center justify-center w-8 h-8 rounded-full bg-slate-900 text-white hover:scale-105 transition-transform" href="/">')
    content = content.replace('<a href="/"\n          className="mobile-nav-link', '<Link href="/"\n          className="mobile-nav-link')
    content = content.replace('Home\n        </a>', 'Home\n        </Link>')
    content = content.replace('          </a>\n\n          {/* GitHub */}', '          </Link>\n\n          {/* GitHub */}')
    content = content.replace('          </a>\n\n          <nav', '          </Link>\n\n          <nav')

    # 2. Fix unescaped quotes
    content = content.replace("Let's talk", "Let&apos;s talk")
    content = content.replace("don't", "don&apos;t")
    content = content.replace("Don't", "Don&apos;t")
    content = content.replace("Rishvin's", "Rishvin&apos;s")

    # 3. Bind {time}
    content = content.replace('<span id="liveClock" className="font-mono text-[11px] text-slate-400 tabular-nums"></span>', 
                              '<span id="liveClock" className="font-mono text-[11px] text-slate-400 tabular-nums">{time}</span>')
    
    # 4. Bind availTyper
    content = content.replace('<span id="availTyper" className="text-[11px] font-semibold whitespace-nowrap"></span>',
                              '<span id="availTyper" className="text-[11px] font-semibold whitespace-nowrap">Available for Opportunities</span>')
    
    # 5. utilityBar scroll
    content = content.replace('id="utilityBar"\n      className="fixed',
                              'id="utilityBar"\n      className={`fixed ${scrolled ? \'-translate-y-full\' : \'\'}')
    content = content.replace('shadow-md">\n      <div className="container',
                              'shadow-md`}>\n      <div className="container')
                              
    # 6. siteHeader scroll offset
    # Wait, siteHeader has `style={{ top: "2.25rem" }}` when utility bar is visible, but if scrolled, it should move up.
    # Actually, in original `index.html`: `siteHeader.style.top = '0';`
    content = content.replace('style={{ top: "2.25rem" }}', 'style={{ top: scrolled ? "0" : "2.25rem" }}')
    
    # 7. mainNav scroll styling
    content = content.replace('id="mainNav"\n          className="mx-auto max-w-[1100px] rounded-full px-4 py-2 flex items-center justify-between transition-all duration-300 bg-white/80 backdrop-blur-xl border border-white/40 shadow-lg"',
                              'id="mainNav"\n          className={`mx-auto max-w-[1100px] rounded-full px-4 py-2 flex items-center justify-between transition-all duration-300 backdrop-blur-xl border border-white/40 ${scrolled ? \'bg-white/90 shadow-xl shadow-slate-200/30\' : \'bg-white/80 shadow-lg\'}`}')
                              
    # 8. mobileMenuBtn toggle
    content = content.replace('id="mobileMenuBtn"\n          className="md:hidden', 
                              'id="mobileMenuBtn"\n          onClick={() => setMenuOpen(!menuOpen)}\n          className="md:hidden')
                              
    # 9. mobileMenu visibility
    content = content.replace('id="mobileMenu"\n        className="absolute top-full left-3 right-3 mt-2 p-4 bg-white/97 backdrop-blur-2xl rounded-3xl shadow-2xl shadow-slate-300/20 border border-white/40 flex flex-col gap-1 origin-top scale-95 opacity-0 invisible transition-all duration-300"',
                              'id="mobileMenu"\n        className={`absolute top-full left-3 right-3 mt-2 p-4 bg-white/97 backdrop-blur-2xl rounded-3xl shadow-2xl shadow-slate-300/20 border border-white/40 flex flex-col gap-1 origin-top transition-all duration-300 ${menuOpen ? \'opacity-100 visible scale-100 translate-y-0\' : \'opacity-0 invisible scale-95\'}`}')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Header fixed!")

if __name__ == "__main__":
    fix_header()
