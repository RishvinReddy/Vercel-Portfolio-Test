import re
import os

filepath = "src/app/page.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add import statement at the top
import_statement = "import { TECH_STACK, SERVICES, FEATURED_PROJECTS } from '../data/portfolio';\n"
if "import { TECH_STACK" not in content:
    content = import_statement + content

# 2. Replace Services
services_start_marker = '<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
services_end_marker = '{/*  Bottom CTA row  */}'

if services_start_marker in content and services_end_marker in content:
    start_idx = content.find(services_start_marker) + len(services_start_marker)
    end_idx = content.find(services_end_marker)
    
    new_services_jsx = """
        {SERVICES.map((service, index) => (
          <div key={index} className={`group relative bg-white/5 rounded-3xl p-8 border border-white/10 ${service.colorClasses.borderHover} transition-all duration-500 hover:-translate-y-2 overflow-hidden backdrop-blur-md`}>
            <div className={`absolute inset-0 bg-gradient-to-br from-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500`}></div>
            <div className="relative z-10 flex flex-col h-full">
              <div className={`w-14 h-14 rounded-2xl bg-gradient-to-br ${service.colorClasses.bgGradient} flex items-center justify-center shadow-lg mb-6 group-hover:scale-110 transition-transform duration-500`}>
                <svg className={`w-7 h-7 ${service.colorClasses.iconText}`} fill="none" stroke="currentColor" viewBox="0 0 24 24" dangerouslySetInnerHTML={{ __html: service.iconPath }}></svg>
              </div>
              <h3 className={`text-xl font-bold text-white mb-3 transition-colors ${service.colorClasses.groupHoverText}`}>{service.title}</h3>
              <p className="text-slate-400 text-sm leading-relaxed mb-6 flex-grow">{service.description}</p>
            </div>
          </div>
        ))}
      </div>
      
      """
    content = content[:start_idx] + "\n" + new_services_jsx + content[end_idx:]


# 3. Replace Marquee
marquee_start_marker = '<div id="tech-marquee-v2"'
marquee_end_marker = '{/*  Set 2 — identical duplicate for seamless loop  */}'

if marquee_start_marker in content:
    start_idx = content.find(marquee_start_marker)
    start_idx = content.find('>', start_idx) + 1
    
    set2_end_idx = content.find('Smart Contracts', start_idx)
    set2_end_idx = content.find('</span>', set2_end_idx) + 7
    
    new_marquee_jsx = """
        {/* Set 1 */}
        {TECH_STACK.map((tech, i) => (
          <span key={`tech-1-${i}`} className="tech-chip" style={{ flexShrink: "0", whiteSpace: "nowrap", padding: "7px 16px", fontSize: "12px" }}>
            <svg style={{ width: "14px", height: "14px", color: tech.color, flexShrink: "0" }} fill="none" stroke="currentColor" viewBox="0 0 24 24" dangerouslySetInnerHTML={{ __html: tech.iconPath }}></svg>
            {tech.name}
          </span>
        ))}
        {/* Set 2 - duplicate for seamless loop */}
        {TECH_STACK.map((tech, i) => (
          <span key={`tech-2-${i}`} className="tech-chip" style={{ flexShrink: "0", whiteSpace: "nowrap", padding: "7px 16px", fontSize: "12px" }}>
            <svg style={{ width: "14px", height: "14px", color: tech.color, flexShrink: "0" }} fill="none" stroke="currentColor" viewBox="0 0 24 24" dangerouslySetInnerHTML={{ __html: tech.iconPath }}></svg>
            {tech.name}
          </span>
        ))}
"""
    content = content[:start_idx] + "\n" + new_marquee_jsx + "\n      " + content[set2_end_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Refactored page.tsx successfully.")
