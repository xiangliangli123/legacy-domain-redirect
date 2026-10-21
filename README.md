# Old academic website redirects

This separate Pages project redirects `www.xiangliang.li` to the new free GitHub Pages website. Keep the main website repository free of a custom domain.

1. Run `python3 build_redirects.py --target https://VERIFIED-ACCOUNT.github.io`.
2. Publish `docs` from `main` in GitHub Pages.
3. Set the project custom domain to `www.xiangliang.li` before changing DNS.
4. Point the old domain to GitHub Pages and wait for its HTTPS certificate.
5. Check the old homepage, `/home`, and `/research` over HTTPS.

These pages use an immediate meta refresh and canonical links. They are not HTTP 301 responses. GitHub Pages does not provide arbitrary server-side redirect rules.

The redirect works only while the old domain is active. Its automatic renewal is off. Do not renew it or add paid services without the owner's instruction.
