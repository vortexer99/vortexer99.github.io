# Yi Zhuang Personal Website

Personal academic website for <https://vortexer99.github.io/>.

This branch migrates the site from Academic Pages/Jekyll to HugoBlox Academic CV.

## Local Preview

Install Hugo Extended and Node.js, then install dependencies:

```powershell
pnpm install
```

On Windows, Hugo's Tailwind transform needs the Node `.JS` shim to be found
before the `.CMD` shim. Start the local preview with:

```powershell
$repo = (Get-Location).Path
$env:PATH = "$repo\node_modules\.bin;$env:PATH"
$env:PATHEXT = ".JS;.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JSE;.WSF;.WSH;.MSC;.CPL"
hugo server --disableFastRender
```

Then open <http://127.0.0.1:1313/>.

## Deployment

The site deploys to GitHub Pages through `.github/workflows/deploy.yml`.

Legacy static paths are preserved under `static/`:

- `/files/...`
- `/images/...`
- `/assets/images/gallery/...`
