# Yi Zhuang Personal Website

Personal academic website for <https://vortexer99.github.io/>.

This branch migrates the site from Academic Pages/Jekyll to HugoBlox Academic CV.

## Local Preview

Install Hugo Extended and Node.js, then run:

```bash
pnpm install
hugo server
```

## Deployment

The site deploys to GitHub Pages through `.github/workflows/deploy.yml`.

Legacy static paths are preserved under `static/`:

- `/files/...`
- `/images/...`
- `/assets/images/gallery/...`
