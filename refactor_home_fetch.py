import os

filepath = "src/app/page.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Import getGithubProjects
import_statement = "import { getGithubProjects } from '@/lib/github';\n"
if "getGithubProjects" not in content:
    content = import_statement + content

# 2. Change Home to async
if "export default function Home() {" in content:
    content = content.replace("export default function Home() {", "export default async function Home() {\n  const dynamicProjects = await getGithubProjects();\n  const displayProjects = dynamicProjects.length > 0 ? dynamicProjects : FEATURED_PROJECTS;\n")

# 3. Replace FEATURED_PROJECTS mapping with displayProjects mapping
if "FEATURED_PROJECTS.length > 0" in content:
    content = content.replace("FEATURED_PROJECTS.length > 0", "displayProjects.length > 0")
    content = content.replace("FEATURED_PROJECTS.map", "displayProjects.map")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Refactored page.tsx to use server-side GitHub fetch.")
