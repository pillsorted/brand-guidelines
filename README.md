# PillSorted Brand Guidelines

> Source: [PillSorted Brand Asset Library](https://www.figma.com/design/Z2nkh8e6JZWs7sRTxkZzQo/PillSorted-Brand-Asset-Library?node-id=0-1) (Figma)
> This file is the single source of truth for all Claude-generated documents across PillSorted projects.

---

## 1. Colors

### Primary

Main brand colour. Which pink sits behind white text depends on the text size: see the rule below the table.

| Token | HEX | Usage |
|-------|-----|-------|
| **Brand** | `#eb1f79` | Links, highlighted headings, accent lines, borders, icons |
| **Action** | `#e1146e` | Filled buttons, badges, tags and selected states with white text on them |

**White text on pink:** Brand `#eb1f79` only behind large text, 24 px and up (or 18.66 px and up at Bold 700). Below that, for button labels, badges and tags, use Action `#e1146e`. White on Brand is 4.2:1, which meets WCAG AA for large text (3:1) but not for normal text (4.5:1). White on Action is 4.6:1.

### Secondary

Purple harmony companion — illustration accents, badges, thumbnail backgrounds.

| Token | HEX | Usage |
|-------|-----|-------|
| **Purple 600** | `#9758a1` | Illustration accents, badges |
| **Purple 500** | `#b377be` | Lighter purple accents |
| **Gradient 400** | `Brand Pink 400 → Purple 500` | Decorative gradients |
| **Gradient 700** | `Purple 700 → Purple 500` | Dark decorative gradients |

### Accent

Subtle tints for backgrounds, tag fills, section washes, highlights — **never used as text**.

| Token | HEX | Usage |
|-------|-----|-------|
| **Brand 50** | `#fef1f8` | Very light pink tint backgrounds |
| **Brand 100** | `#fee5f3` | Light pink tint, tag fills |
| **Purple 200** | `#edddf1` | Light purple tint backgrounds |
| **Gradient 200** | `Scarlet 100 → Purple 200` | Soft gradient washes |

### Text

Typographic hierarchy — body, supporting, captions, disabled.

| Token | HEX | Usage |
|-------|-----|-------|
| **Text** | `#162948` | All headings and body copy — never use pure black |
| **Text Supporting** | `#5c697f` | Descriptions, captions, secondary info |
| **Text Disabled** | `#b2bac7` | Disabled UI elements, placeholder text |

### Neutrals

Structural grays — borders, dividers, component surfaces.

| Token | HEX | Usage |
|-------|-----|-------|
| **Divider** | `#edeef1` | Horizontal rules, section separators |
| **Border** | `#edeef1` | Table borders, card outlines |
| **White** | `#ffffff` | Primary surface color |
| **White Smoke** | `#f6f6f9` | Subtle surface differentiation |

### Backgrounds

Page-level and surface backgrounds. **Web:** prefer Alice Blue or Gradient 200 for tinted backgrounds. **Print:** prefer White Smoke.

| Token | HEX | Usage |
|-------|-----|-------|
| **White Smoke** | `#f6f6f9` | Page background (print preferred), alternating table rows |
| **Alice Blue** | `#f6f6ff` | Info panels, callout boxes, highlighted sections (web preferred) |
| **White** | `#ffffff` | Default document/page background |
| **Gradient 200** | `Scarlet 100 (#fde7e6) → Purple 200 (#edddf1)` | Soft tinted background (web preferred) |
| **Gradient 700** | `Purple 700 → Purple 500` | Hero/feature backgrounds |
| **Gradient Soft Pink** | `#fff0f2 → #fde8f9`, top to bottom | Page background for the whole weight loss consultation flow, from the questionnaire through product selection to checkout. Its two colours are not on the primitive scales |

### Semantic

System feedback colors — success, error, info, warning. Each has a primary fill (icons, text) and a secondary fill (background).

| State | Primary Fill | Secondary Fill | Usage |
|-------|-------------|----------------|-------|
| **Success** | `#19b07b` | `#d3f8e4` | Confirmations, completed states |
| **Error** | `#e84b51` | `#fde7e6` | Validation errors, critical warnings |
| **Info** | `#419ef0` | `#dceffd` | Informational callouts, tips |
| **Warning** | `#f9c74f` | `#fdefc8` | Caution notices, attention required |

### Color Primitives (Full Scales)

Complete 50–950 ramps for building extended palettes. The semantic tokens above should be preferred; use primitives only when a specific shade is needed.

| Family | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 950 |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **Brand Pink** | `#fef1f8` | `#fee5f3` | `#ffcbe9` | `#ffa1d5` | `#ff67b7` | `#fa3a98` | `#eb1f79` | `#cc0a5a` | `#a80c4a` | `#8c0f41` | `#560123` |
| **Shuttle Gray** | `#f6f6f9` | `#edeef1` | `#d6dae1` | `#b2bac7` | `#8895a8` | `#6a788d` | `#5c697f` | `#454e5f` | `#3c4350` | `#353a45` | `#23272e` |
| **Navy** | `#f6f6ff` | `#dceffd` | `#c1e4fc` | `#97d4f9` | `#65bcf5` | `#419ef0` | `#2c81e4` | `#236bd2` | `#2357aa` | `#224b86` | `#162948` |
| **Emerald** | `#edfcf5` | `#d3f8e4` | `#abefce` | `#74e1b3` | `#3ccb94` | `#19b07b` | `#0e9e6e` | `#0a7252` | `#0b5a42` | `#0a4a38` | `#042a20` |
| **Scarlet** | `#fef3f2` | `#fde7e6` | `#fbd1d0` | `#f7abaa` | `#f27a7b` | `#e84b51` | `#d93f4c` | `#b31d2e` | `#961b2c` | `#801b2c` | `#470a13` |
| **Purple** | `#fbf7fc` | `#f6eff8` | `#edddf1` | `#dfc2e5` | `#cc9ed4` | `#b377be` | `#9758a1` | `#7e4685` | `#6a3c6f` | `#58345b` | `#361939` |
| **Amber Gold** | `#fffaeb` | `#fdefc8` | `#fbde8c` | `#f9c74f` | `#f7b128` | `#f18f0f` | `#d56b0a` | `#b1490c` | `#903910` | `#762f11` | `#441604` |

**Brand Pink 650** `#e1146e` sits between 600 and 700. It exists for the **Action** token above and is not part of the regular 50–950 ramp.

---

## 2. Logo

### Lockup Variants

| Variant | Description | When to Use | Min Height |
|---------|-------------|-------------|-----------|
| **Clean** | Heart symbol + "PillSorted" wordmark (no tagline) | Minimal contexts, small sizes | 36 px |
| **Wordmark** | Heart symbol + "PillSorted" + "PERSONAL PHARMACY" tagline | **PREFERRED** — default for most uses | 36 px |
| **Symbol** | Heart icon only | Favicons, app icons, very small spaces | 16 px |
| **Proportional** | Compact horizontal layout | Navigation bars, tight horizontal layouts | 20 px |

### Colour Modes

| Mode | Lockups | Use On |
|------|---------|--------|
| **Default (Pink)** | All (Clean, Wordmark, Symbol, Proportional) | White, PS Accent/Background colours, PS Neutrals, clear uncluttered photographs |
| **Invert (White)** | All (Clean, Wordmark, Symbol, Proportional) | PS Primary or Secondary colours, clear uncluttered photographs |
| **Secondary (Shuttle Gray 600)** | Wordmark, Proportional only | White and White Smoke — document footers, subdued contexts |

### Logo Assets

Logo exports are stored in the `assets/logos/` folder within this repository.

**Default (Pink):**
- `PS-Logo-Pink` — Full logo with tagline
- `PS-Logo-Wordmark-Pink` — Wordmark lockup
- `PS-Logo-Proportional-Pink` — Proportional lockup
- `PS-Logo-Symbol-Pink` — Symbol only

**Invert (White):**
- `PS-Logo-White` — Full logo with tagline
- `PS-Logo-Wordmark-White` — Wordmark lockup
- `PS-Logo-Proportional-White` — Proportional lockup
- `PS-Logo-Symbol-White` — Symbol only

### Clear Space

Always maintain minimum clear space around the logo.

| Context | Exclusion Area |
|---------|---------------|
| **Print & Signage** | Full height of the PillSorted heart symbol on all sides |
| **Digital** | Half the height of the PillSorted heart symbol on all sides |

> These are *minimum* exclusion areas. More space is preferred where possible.

### Logo on Backgrounds

**Acceptable:**

| Background | Logo Colour | Notes |
|-----------|-------------|-------|
| White `#ffffff` | Pink | Default pairing |
| PS Accent or Background colors (e.g. Alice Blue `#f6f6ff`) | Pink | Any brand accent/background token |
| PS Neutrals (e.g. White Smoke `#f6f6f9`) | Pink | Also valid for Shuttle Gray 600 secondary logo |
| PS Primary or Secondary colors (e.g. Brand Pink `#eb1f79`) | White | Cover pages, hero sections |
| Clear, uncluttered photographs | Pink | Photo must not compete with logo |
| Clear, uncluttered photographs | White | Dark or high-contrast photography |

**Unacceptable:**

| Background | Why |
|-----------|-----|
| Any colour outside PS Primary or Secondary palette | White logo only on brand-approved backgrounds |
| Cluttered photographs | Logo gets lost in visual noise |

---

## 3. Typography

**Typeface:** [DM Sans](https://fonts.google.com/specimen/DM+Sans) (Google Fonts — variable, optical size 9–40)
**Webfont:** `https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400;1,9..40,500;1,9..40,600&display=swap`
**Weights:** Regular (400), Medium (500), SemiBold (600)
**Desktop install:** [Download DM Sans from Google Fonts](https://fonts.google.com/specimen/DM+Sans) — install locally to view Word documents with correct formatting.
**Word fallback:** If DM Sans is not installed, use Calibri as the fallback font. Never fall back to Times New Roman or other serif typefaces.

### Headings

| Style | Size | Weight | Line Height | Letter Spacing |
|-------|------|--------|-------------|----------------|
| **H1** | 30px | SemiBold (600) | 140% | 0px |
| **H2** | 24px | SemiBold (600) | Auto | -0.25px |
| **H3** | 20px | SemiBold (600) | Auto | -0.25px |
| **H4** | 18px | SemiBold (600) | Auto | -0.25px |

### Body

| Style | Size | Weight | Line Height | Letter Spacing | Paragraph Spacing |
|-------|------|--------|-------------|----------------|-------------------|
| **Body 16 / Regular** | 16px | Regular (400) | 150% | 0px | 14px |
| **Body 16 / SemiBold** | 16px | SemiBold (600) | 150% | 0px | 0px |
| **Body 16 / Medium** | 16px | Medium (500) | 150% | 0px | 0px |
| **Body 14 / Regular** | 14px | Regular (400) | 150% | 0px | 0px |
| **Body 14 / Medium** | 14px | Medium (500) | 150% | 0px | 0px |

### Body (Print)

| Style | Size | Weight | Line Height | Letter Spacing | Paragraph Spacing |
|-------|------|--------|-------------|----------------|-------------------|
| **Body 12 / SemiBold** | 12px | SemiBold (600) | 150% | 0% | 0px |
| **Body 10 / Regular** | 10px | Regular (400) | 150% | 0% | 10px |
| **Body 10 / SemiBold** | 10px | SemiBold (600) | 150% | 0% | 10px |

### Captions

| Style | Size | Weight | Line Height | Letter Spacing | Case |
|-------|------|--------|-------------|----------------|------|
| **All Caps** | 12px | SemiBold (600) | 12px | 1px | UPPERCASE |

---

## 4. Document Formatting

These rules apply to all Claude-generated documents (audits, reports, briefs, analyses).

**Template:** [`assets/templates/brand-template.docx`](./assets/templates/brand-template.docx) — reference Word document exercising all styles below. Use as a visual reference or starting point for `python-docx` generation.

### Cover Page

Used for formal documents (audits, compliance reports, proposals).

| Element | Specification |
|---------|--------------|
| **Background** | White (`#ffffff`) |
| **Logo** | Pink Wordmark lockup, top-left, 28 px height |
| **Document title** | Text colour (`#162948`), 36 px SemiBold, 120% line-height, vertically centred left |
| **Subtitle** | Text Supporting (`#5c697f`), Body 16 Regular, 150% line-height, below title, 12 px gap |
| **Status badge** | All Caps (12 px SemiBold, 1 px letter-spacing), white text on Action (`#e1146e`) background, 8 px padding, 8 px border-radius |
| **Metadata** | Vertical stack below title block, 24 px gap between items. Labels: 10 px SemiBold, 0.6 px letter-spacing, Text Supporting (`#5c697f`). Values: 12 px Regular, Text colour (`#162948`). 4 px gap between label and value |

### Body Pages (Letterhead)

| Element | Specification |
|---------|--------------|
| **Header** | Pink Wordmark logo, left-aligned, 28 px height, 24 px bottom padding |
| **Content area** | 32 px below header. 56 px right padding |
| **Section gap** | 24 px between sections |
| **Section headings** | H4 style — PillSorted Pink (`#eb1f79`), 18 px SemiBold, -0.25 px letter-spacing |
| **Sub-headings** | Body 12 (print) SemiBold, Text colour (`#162948`) |
| **Body text** | Body 10 (print) Regular, Text colour (`#162948`), 150% line-height, 10 px paragraph spacing |
| **Bullet lists** | Disc style, 15 px left margin, 10 px spacing between items (last item: 0), Body 10 (print) Regular, 150% line-height |
| **Footer** | Date in 9 px Regular, Text Supporting (`#5c697f`), 12 px line-height, 36 px bottom padding |

### Data Tables

| Element | Specification |
|---------|--------------|
| **Container** | White background, 1 px `#edeef1` border, 12 px border-radius, overflow hidden |
| **Header row** | White background |
| **Header text** | Body 10 (print) SemiBold, Text colour (`#162948`) |
| **Body text** | Body 10 (print) Regular, Text colour (`#162948`), 150% line-height |
| **Cell padding** | 10 px horizontal, 8 px vertical |
| **Cell borders** | 1 px solid Divider (`#edeef1`) on all sides |
| **Row striping** | Alternate rows: White (`#ffffff`) → White Smoke (`#f6f6f9`) |
| **Summary/total row** | White Smoke background, same text style as body rows |

### Callout Boxes

Use semantic colours for callout/alert boxes in documents:

| Type | Background | Border/Accent | Text Colour | When to Use |
|------|-----------|---------------|-------------|-------------|
| **Info** | `#dceffd` | `#419ef0` left border | `#162948` | Informational notes, tips |
| **Warning** | `#fdefc8` | `#f9c74f` left border | `#162948` | Caution notices |
| **Error/Critical** | `#fde7e6` | `#e84b51` left border | `#162948` | Critical warnings, compliance issues |
| **Success** | `#d3f8e4` | `#19b07b` left border | `#162948` | Confirmations, positive outcomes |
| **Brand highlight** | `#fef1f8` | `#eb1f79` left border | `#162948` | Key takeaways, executive summary |

### Company Details (for document headers/footers)

| Field | Value |
|-------|-------|
| **Company** | PillSorted Pharmacy |
| **Address** | Carthouse 3, Copley Hill Business Park Cambridge CB22 3GN |
| **Phone** | 03334 050380 |
| **Website** | www.pillsorted.com |
| **Email** | help@pillsorted.com |

---

## 5. CSS Reference

### Font Import

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400;1,9..40,500;1,9..40,600&display=swap');
```

### Design Tokens

```css
:root {
  /* Primary */
  --primary-brand:       #eb1f79;
  --primary-action:      #e1146e;   /* fill behind white text under 24 px */

  /* Secondary */
  --secondary-purple-600: #9758a1;
  --secondary-purple-500: #b377be;

  /* Accent */
  --accent-brand-50:     #fef1f8;
  --accent-brand-100:    #fee5f3;
  --accent-purple-200:   #edddf1;

  /* Text */
  --text:                #162948;
  --text-supporting:     #5c697f;
  --text-disabled:       #b2bac7;

  /* Neutrals */
  --neutrals-divider:    #edeef1;
  --neutrals-border:     #edeef1;
  --neutrals-white:      #ffffff;
  --neutrals-white-smoke: #f6f6f9;

  /* Backgrounds */
  --bg-white-smoke:      #f6f6f9;
  --bg-alice-blue:       #f6f6ff;
  --bg-gradient-soft-pink: linear-gradient(180deg, #fff0f2 0%, #fde8f9 100%);
  --bg-white:            #ffffff;

  /* Semantic — Primary Fills */
  --semantic-success:    #19b07b;
  --semantic-error:      #e84b51;
  --semantic-info:       #419ef0;
  --semantic-warning:    #f9c74f;

  /* Semantic — Secondary Fills (backgrounds) */
  --semantic-success-bg: #d3f8e4;
  --semantic-error-bg:   #fde7e6;
  --semantic-info-bg:    #dceffd;
  --semantic-warning-bg: #fdefc8;

  /* Typography */
  --font-family:         'DM Sans', sans-serif;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
}
```

### Typography Classes

```css
/* Headings */
.h1 { font-family: var(--font-family); font-weight: 600; font-size: 30px; line-height: 1.4; }
.h2 { font-family: var(--font-family); font-weight: 600; font-size: 24px; letter-spacing: -0.25px; }
.h3 { font-family: var(--font-family); font-weight: 600; font-size: 20px; letter-spacing: -0.25px; }
.h4 { font-family: var(--font-family); font-weight: 600; font-size: 18px; letter-spacing: -0.25px; }

/* Body */
.body-16             { font-family: var(--font-family); font-weight: 400; font-size: 16px; line-height: 1.5; }
.body-16-semi        { font-family: var(--font-family); font-weight: 600; font-size: 16px; line-height: 1.5; }
.body-16-medium      { font-family: var(--font-family); font-weight: 500; font-size: 16px; line-height: 1.5; }
.body-14             { font-family: var(--font-family); font-weight: 400; font-size: 14px; line-height: 1.5; }
.body-14-medium      { font-family: var(--font-family); font-weight: 500; font-size: 14px; line-height: 1.5; }

/* Body (Print) */
.body-12-semi        { font-family: var(--font-family); font-weight: 600; font-size: 12px; line-height: 1.5; }
.body-10             { font-family: var(--font-family); font-weight: 400; font-size: 10px; line-height: 1.5; }
.body-10-semi        { font-family: var(--font-family); font-weight: 600; font-size: 10px; line-height: 1.5; }

/* Captions */
.caption-caps        { font-family: var(--font-family); font-weight: 600; font-size: 12px; line-height: 12px; letter-spacing: 1px; text-transform: uppercase; }

/* Paragraph spacing — apply to containers, not inline text */
.body-16 p + p       { margin-top: 14px; }   /* Body 16 Regular paragraph gap */
.body-10 p + p       { margin-top: 10px; }   /* Body 10 (print) paragraph gap */
.body-10-semi p + p  { margin-top: 10px; }   /* Body 10 Semi (print) paragraph gap */

/* List spacing */
.body-10 li + li     { margin-top: 10px; }   /* Print list item gap */
.body-10 li          { margin-left: 15px; }  /* Print list indent */
```

---

## Source

- **Figma:** [PillSorted Brand Asset Library](https://www.figma.com/design/Z2nkh8e6JZWs7sRTxkZzQo/PillSorted-Brand-Asset-Library?node-id=0-1)
- **Jira:** [DES-651](https://pillsorted.atlassian.net/browse/DES-651)
- **Last updated:** 2026-10-09
