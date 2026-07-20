# SEO Strategy

The portfolio includes a structured SEO implementation powered by Next.js Metadata API.

## Core SEO Elements

| Element | Implementation in Next.js |
|---------|---------------------------|
| **Page Title** | Dynamic via `metadata` object |
| **Meta Description** | Configured in root layout |
| **Open Graph** | Social sharing previews configured in layout |
| **Sitemap** | Generated dynamically or statically |
| **Robots.txt** | Located in `public/` or generated |
| **Google Console**| Verified via meta tag |

## Metadata Implementation
Standard metadata is exported from `src/app/layout.tsx` to ensure search engines can properly index the portfolio contents.
