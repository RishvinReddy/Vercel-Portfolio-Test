import os

filepath = "src/app/page.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Projects Grid
projects_start_marker = '<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 lg:gap-12" id="projectsGrid">'
projects_end_marker = '      </div>\n    </div>\n  </section>'

if projects_start_marker in content and projects_end_marker in content:
    start_idx = content.find(projects_start_marker) + len(projects_start_marker)
    end_idx = content.find(projects_end_marker)
    
    new_projects_jsx = """
        {FEATURED_PROJECTS.length > 0 ? (
          FEATURED_PROJECTS.map((project, index) => (
            <div key={index} className="group flex flex-col bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-2">
              {/* Image Placeholder */}
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
          ))
        ) : (
          <p className="col-span-full text-center text-slate-500 py-10">Fetching projects securely...</p>
        )}
"""
    content = content[:start_idx] + "\n" + new_projects_jsx + content[end_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Refactored projects grid.")
