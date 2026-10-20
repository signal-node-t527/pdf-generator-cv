# Technical Documentation

This document provides a detailed overview of the project's architecture, configuration, and development workflows.

## 🏗️ Project Architecture

The project follows a standard Astro structure, emphasizing component modularity and centralized configuration.

### Directory Structure

- `src/assets/`: Local images and branding assets.
- `src/components/`: Reusable Astro components (Hero, Services, Contact, etc.).
- `src/config/`: Business logic and site-wide metadata constants.
- `src/layouts/`: Base HTML templates (Layout.astro).
- `src/pages/`: Route definitions (index.astro).
- `src/styles/`: Global CSS and Tailwind theme definitions.

## ⚙️ Content Management (Centralized Config)

Almost all content displayed on the website can be modified in a single file: **`src/config/site.ts`**.

### What you can update there:
- **SITE:** Name, tagline, description, and canonical URL.
- **BUSINESS:** Legal name, service area, and location.
- **CONTACT:** Phone numbers (WhatsApp and Display), email address.
- **SOCIAL:** Links to Instagram, Facebook, and YouTube.
- **MAP:** Latitude, Longitude, and Zoom level for the service area map.
- **FEATURED_VIDEOS:** YouTube video IDs for the portfolio section.

## 🎨 Styling & Theming

The project uses **Tailwind CSS v4** with a CSS-first configuration approach.

### Theme Variables
Custom design tokens (colors, fonts, shadows) are defined in `src/styles/global.css` using the `@theme` block:

```css
@theme {
  --color-primary: hsl(152 45% 28%);
  --color-accent: hsl(36 60% 50%);
  --font-heading: "Saira Stencil One", system-ui, sans-serif;
  /* ... */
}
```

### Typography
- **Headings:** "Saira Stencil One" (Stencil-style font for industrial/professional feel).
- **Body:** "Inter" (Clean, readable sans-serif).

## 🔍 Search Engine Optimization (SEO)

SEO is handled primarily in `src/layouts/Layout.astro`.

- **Meta Tags:** Automatic generation of `<title>`, `<meta description>`, and canonical URLs.
- **Social Sharing:** Open Graph and Twitter Card tags are pre-populated.
- **Local SEO:** Geo-tags and JSON-LD `LocalBusiness` structured data are included to help with Google Maps and local search rankings.
- **Robots:** `public/robots.txt` and meta robots tags are configured.

## 🚀 Components Overview

| Component | Description |
| :--- | :--- |
| `Header.astro` | Sticky navigation with scroll-aware background changes. |
| `Hero.astro` | Main landing section with background image, CTA, and service area map. |
| `Services.astro` | Grid of core business offerings (Poda, Tala, etc.). |
| `FeaturedWorks.astro` | YouTube video gallery of past projects. |
| `AboutUs.astro` | Company history and value proposition. |
| `FAQ.astro` | Accordion-style frequently asked questions. |
| `Contact.astro` | Direct contact form/links and location info. |
| `WhatsAppButton.astro` | Floating action button for immediate contact. |

## 📦 Build & Deployment

The site is optimized for static hosting.

1. **Build Command:** `npm run build`
2. **Output:** The compiled site will be in the `dist/` folder.
3. **Optimizations:**
   - Images are processed and optimized via `astro:assets`.
   - CSS is minified by Tailwind/Vite.
   - JS is bundled and tree-shaken.

## 🛠️ Future Improvements

- [ ] Add a blog section using Astro Content Collections.
- [ ] Implement a real contact form backend (e.g., Formspree or Netlify Forms).
- [ ] Add a full image gallery with lightbox.
