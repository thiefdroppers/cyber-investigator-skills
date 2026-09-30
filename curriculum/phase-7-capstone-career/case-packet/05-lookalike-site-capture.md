# Artifact B: the lookalike site (captured)

> SYNTHETIC TRAINING MATERIAL. All organizations, people, domains and IPs are fictional.

Source: the client's IT contractor captured these pages on 17 March 2026 at 13:05 UTC from an isolated, sandboxed browser that the contractor's firm uses for this purpose. The capture is the authorized collection for this case. You do not need to visit the site, and the engagement letter forbids it.

## B1: `https://castellan-hardwood.example/about`

Page head (excerpt):

```html
<title>About Us | Castellan Hardwood Supply</title>
<meta name="description" content="Family-owned hardwood lumber yard supplying cabinetmakers and furniture builders since 1986.">
<link rel="icon" href="/favicon.ico">
<link rel="stylesheet" href="https://castellanhardwood.example/css/site.css?v=2024.1">
<img class="logo" src="https://castellanhardwood.example/img/logo.png" alt="Castellan Hardwood Supply">
```

Rendered text:

> **About Castellan Hardwood Supply**
>
> Castellan Hardwood Supply has milled and supplied North American hardwoods to cabinetmakers, millwork shops and furniture builders since 1986. We are a family-owned business, now in our third generation, operating from our yard and kiln facility at 1400 Ferrule Road in Wrenmoor Crossing.
>
> We stock white oak, red oak, hard and soft maple, cherry, walnut and ash in 4/4 through 12/4, with custom milling to your cut list. Most orders within our delivery region ship within five business days.
>
> **Banking update**
>
> Following our annual audit, Castellan Hardwood Supply has moved to a new banking partner as of March 2026. Existing customers will receive updated remittance instructions from our Accounts Receivable team. Please contact ar@castellan-hardwood.example with any questions.
>
> **Our team**
>
> Graham Castellan, President
> Tobias Venn, Yard and Kiln Manager
> Dana Whitlock, Accounts Receivable Manager
>
> **Contact**
>
> Orders: orders@castellan-hardwood.example
> Accounts: ar@castellan-hardwood.example
> Phone: 555-0148 (Monday to Friday, 7:00 to 16:00)
>
> © 2024 Castellan Hardwood Supply Inc.

## B2: `https://castellan-hardwood.example/privacy`

Rendered text (complete):

> **Privacy policy**
>
> Castellan Hardwood Supply collects only the information needed to process your orders and payments. We do not sell your information to third parties. Marrowline Freight Services respects your privacy and will only use your contact details to respond to your enquiry. For questions about this policy, contact ar@castellan-hardwood.example.

## B3: other paths requested during the capture

| Path | Status | Notes |
|---|---|---|
| `/` | 200 | Home page. Same layout as the real site; the hero image is hotlinked from `castellanhardwood.example`. |
| `/contact` | 200 | Contact form. The form posts to `/assets/php/contact.php`. |
| `/remittance` | 404 | No page at the path shown in the phishing email's link text. |
| `/favicon.ico` | 200 | Byte-identical to the real site's favicon (see the hash in `06-lookup-results.md`). |
