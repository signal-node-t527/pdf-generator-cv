# Portfolio Variant Configuration Documentation

This document describes how to configure and use real-time site variants for the AI Engineer Portfolio.

## 🚀 Overview

The portfolio supports dynamic variants loaded from a remote GitHub repository. By visiting a specific URL or using query parameters, the site fetches a JSON configuration file and updates content and styles in real-time.

**GitHub Repository:** `https://github.com/signal-node-t527/rawconfiglist`

---

## 🛠 Configuration Schema

Each variant is a JSON file named `{variantId}.json`. The structure follows the `PortfolioVariant` interface:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` | **Required.** The unique identifier for the variant (should match filename). |
| `heroBadgeGreeting` | `object` | Dictionary with `en` and `es` keys for the top badge greeting. |
| `heroBadgeRole` | `object` | Dictionary with `en` and `es` keys for the role description in the badge. |
| `heroHeadingPre` | `object` | Dictionary for the text *before* the highlight in the main heading. |
| `heroHeadingHighlight`| `object` | Dictionary for the animated/gradient text in the main heading. |
| `heroHeadingPost` | `object` | Dictionary for the text *after* the highlight in the main heading. |
| `heroSubheading` | `object` | Dictionary for the paragraph text below the main heading. |
| `aboutSubtitle` | `object` | Dictionary for the primary description in the "About Me" section. |
| `aboutExperience` | `object` | Dictionary for the experience description in the "About Me" section. |
| `customProjects` | `string[]`| Optional list of project IDs to display (e.g., `["agent-system", "nlp-classifier"]`). |
| `primaryColor` | `string` | Optional CSS color value or HSL components (e.g., `"280 65% 45%"`). |

### Example JSON (`full-config-test.json`)

```json
{
  "id": "full-config-test",
  "heroBadgeGreeting": {
    "en": "Hello from CLI",
    "es": "Hola desde CLI"
  },
  "heroHeadingPre": {
    "en": "Welcome to ",
    "es": "Bienvenidos al "
  },
  "heroHeadingHighlight": {
    "en": "future",
    "es": "futuro"
  },
  "heroHeadingPost": {
    "en": " of AI",
    "es": " de la IA"
  },
  "aboutSubtitle": {
    "en": "This is a custom about me description.",
    "es": "Esta es una descripción personalizada sobre mí."
  },
  "customProjects": ["nlp-classifier", "vision-qa"],
  "primaryColor": "300 80% 60%"
}
```

---

## 🏗 How to Generate New Variants

An automation script is provided in the `portfolio/` folder.

### CLI Usage
```bash
python generate_variant.py [OPTIONS]
```

### Available Flags
| Flag | Description |
| :--- | :--- |
| `--id` | Unique identifier (default: random 8-char UUID) |
| `--greeting-en` / `-es` | Badge greeting text |
| `--role-en` / `-es` | Badge role description |
| `--heading-pre-en` / `-es`| Main heading prefix |
| `--highlight-en` / `-es` | Main heading highlight word |
| `--heading-post-en` / `-es`| Main heading suffix |
| `--subheading-en` / `-es` | Paragraph below heading |
| `--about-en` / `-es` | "About Me" subtitle |
| `--exp-en` / `-es` | "About Me" experience body |
| `--cv-link` | Public URL for CV download |
| `--projects` | List of project IDs (space separated) |
| `--color` | Primary color HSL (e.g. "210 60% 35%") |

**Example:**
```bash
python generate_variant.py --id my-variant --highlight-en "revolutionary" --projects agent-system --color "280 65% 45%"
```

---

## 🌐 Accessing Variants

Once you push your JSON files to the `master` branch of your GitHub repo, they can be accessed via:

1.  **URL Path:** `https://your-portfolio.com/variantId`
2.  **Query Parameter:** `https://your-portfolio.com/?v=variantId`

### Note on Styling
The `primaryColor` field updates the `--primary` CSS variable. For best results with Tailwind's HSL system, provide the value as space-separated HSL components (e.g., `"210 60% 35%"`) without the `hsl()` wrapper.
