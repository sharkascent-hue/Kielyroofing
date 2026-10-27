# Kiely Roofing & Construction website

Static multi-page site for kielyroofing.ie. No build step needed to host it: upload the folder as-is (Vercel, Netlify, any web host).

- Pages keep the same addresses as the old site (`/roof-repairs`, `/contact-us`, `/gallery` …) so Google rankings carry over. `vercel.json` serves them without a trailing slash.
- Extra pages/tools: `/roof-health-check` (repair-or-replace quiz), a 4-step quote wizard on every page (sends to WhatsApp or email), "Do we cover your area?" checker, live opening-hours badge, gallery and review filters, before/after sliders, sticky Call / WhatsApp / Quote bar on phones.
- Phone, email and form settings are at the top of `assets/site.js`. Area-checker towns are in `assets/tools.js`.
- Forms: paste a free Web3Forms access key into `formKey` in `assets/site.js` to receive enquiries by email. Until then, forms open the visitor's email app pre-filled. The quote wizard sends via WhatsApp (+353 87 359 2163) or email.
- To change page text, edit `build.py` and run `python3 build.py` (also regenerates `sitemap.xml` and `robots.txt`).
- The lightning intro plays once per visit on the home page (add `?intro` to the URL to replay it).
