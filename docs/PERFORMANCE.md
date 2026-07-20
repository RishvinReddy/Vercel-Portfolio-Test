# Performance Strategy

Performance is an important component of the portfolio architecture.

## Performance Pipeline

```mermaid
flowchart LR
    SRC[Next.js Source]
    SRC --> OPT[Build Time Optimization]
    OPT --> HTML[Static HTML Generation]
    OPT --> CSS[Tailwind CSS Purging]
    OPT --> JS[Code Splitting]
    OPT --> IMG[Next/Image Optimization]
    
    HTML --> DEPLOY[Vercel CDN]
    CSS --> DEPLOY
    JS --> DEPLOY
    IMG --> DEPLOY
```

## Key Optimizations
* **Images:** Uses `next/image` for automatic format selection (WebP/AVIF), lazy loading, and responsive sizing.
* **Fonts:** Uses `next/font` to optimize font loading and prevent layout shifts.
* **CSS:** Tailwind CSS ensures only used styles are shipped in the final bundle.
