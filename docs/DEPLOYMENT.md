# Deployment Strategy

The portfolio is deployed on **Vercel** for optimal Next.js performance and CI/CD integration.

## Deployment Architecture

```mermaid
flowchart LR
    DEV[Developer]
    DEV --> GIT[Local Git]
    GIT --> GH[GitHub Main Branch]
    GH --> VERCEL[Vercel Build Pipeline]
    VERCEL --> VALIDATE[Lint & Type Check]
    VALIDATE --> BUILD[Next.js Build]
    BUILD --> HOST[Vercel Edge Network]
    HOST --> DOMAIN[Custom Domain]
```

## Vercel Workflow
1. Push changes to the `main` branch.
2. Vercel automatically intercepts the webhook.
3. Vercel runs `npm run build`.
4. If successful, the new build is deployed to production.
