import re

filepath = "src/app/resume/page.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add import statement
import_statement = "import ResumeViewer from '@/components/ResumeViewer';\n"
if "ResumeViewer" not in content:
    content = import_statement + content

# 2. Find the start of the dynamic resume section
start_marker = '<div id="resume-loading"'
end_marker = '</div>\n          </div>\n        </div>\n      </section>'

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker) + len('</div>\n          </div>')
    
    new_jsx = """
          </div>
          <ResumeViewer />
"""
    # Wait, the structure in page.tsx is:
    # <div className="flex items-center justify-between border-b border-slate-100 pb-4">
    #   <div>
    #     <h2>...</h2>
    #     <p>...</p>
    #   </div>
    #   <div id="resume-loading">...</div>
    # </div>
    # <div id="resume-tabs">...</div>
    # <div id="resume-viewer-container">...</div>
    
    # Let's just use regex to replace everything from <div id="resume-loading" to the end of the container.
    content = re.sub(r'<div id="resume-loading".*?id="resume-viewer-container".*?</div>\s*</div>', '<ResumeViewer />\n        </div>', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected ResumeViewer into resume page.")
