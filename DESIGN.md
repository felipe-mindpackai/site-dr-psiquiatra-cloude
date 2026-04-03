# Design System Strategy: Editorial Compassion

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Digital Sanctuary."** In the context of psychiatric care, the interface must do more than function—it must reassure. We move beyond the "cold clinic" aesthetic by adopting a high-end editorial approach. 

This system breaks the traditional medical template through **intentional asymmetry** and **breathable white space**. By utilizing a sophisticated serif for displays and a technical sans-serif for utility, we create a dialogue between authority and accessibility. Layouts should feel like a premium journal: wide margins, overlapping imagery, and a radical departure from rigid borders in favor of soft tonal transitions.

## 2. Colors
Our palette is anchored in deep, authoritative blues and high-foundation neutrals to evoke trust and clarity.

### The Palette (Material Convention)
*   **Primary Focus:** `primary` (#00307e) and `primary_container` (#1a47a1) serve as our anchors for action and importance.
*   **Surface Foundation:** `surface` (#f8f9fb) provides a cool, clean base that reduces eye strain.
*   **Warmth & Contrast:** `tertiary` (#5f2300) is used sparingly for human-centric highlights and urgent guidance.

### Visual Rules
*   **The "No-Line" Rule:** 1px solid borders are strictly prohibited for sectioning. Structural boundaries must be defined solely by background color shifts—e.g., a `surface-container-low` section resting against a `surface` background.
*   **Surface Hierarchy & Nesting:** Treat the UI as layers of fine paper. Use `surface-container-lowest` for floating cards to create a "lifted" feel, and `surface-container-high` for recessed utility areas. 
*   **The "Glass & Gradient" Rule:** To avoid a flat, "out-of-the-box" look, apply subtle gradients (e.g., `primary` to `primary_container`) on hero buttons. For floating navigation or modals, use `surface` with 80% opacity and a `24px` backdrop blur to create a "frosted glass" effect.

## 3. Typography
The typographic system relies on the interplay between **Newsreader** (an elegant, authoritative serif) and **Manrope** (a modern, highly legible sans-serif).

*   **Display & Headline (Newsreader):** Used for primary messaging. The variable weight of Newsreader conveys a "human touch" and professional heritage. Large scales (`display-lg` at 3.5rem) should be used with generous leading to establish an editorial feel.
*   **Title & Body (Manrope):** Used for all functional and informational text. Manrope’s geometric clarity ensures accessibility in complex medical descriptions.
*   **The Identity Balance:** The serif provides the "Compassion" (Warmth), while the sans-serif provides the "Clinic" (Precision).

## 4. Elevation & Depth
In "The Digital Sanctuary," depth is psychological. We avoid heavy shadows in favor of **Tonal Layering**.

*   **The Layering Principle:** Place `surface-container-lowest` (pure white) cards onto a `surface-container-low` background. This creates a soft, natural lift without the "dirty" look of traditional drop shadows.
*   **Ambient Shadows:** If a floating element (like a FAB or Menu) requires a shadow, use a `12%` opacity version of `on-surface` with a `40px` blur and `12px` Y-offset. This mimics natural light through a window rather than a digital effect.
*   **The "Ghost Border" Fallback:** If a container requires a boundary for accessibility, use the `outline-variant` token at **15% opacity**. High-contrast, 100% opaque borders are forbidden.

## 5. Components

### Buttons
*   **Primary:** Solid `primary` fill, `on-primary` text. Use `xl` (0.75rem) roundedness. Add a subtle 10% vertical gradient to give a "molded" look.
*   **Secondary:** `surface-container-lowest` fill with a `ghost border`. 
*   **Tertiary:** Text-only using `primary` color, strictly for low-emphasis navigation.

### Cards & Sections
*   **Clinic Cards:** Use `surface-container-lowest` with no border. Use vertical padding (80px–120px) to separate content blocks. 
*   **Medical Lists:** Forbid divider lines. Use `surface-container-low` background shifts or `body-md` spacing to denote list item boundaries.

### Input Fields
*   **Text Inputs:** Filled style using `surface-container-high`. Labels should be `label-md` in `on-surface-variant`. On focus, the bottom border should animate to `primary` with a 2px thickness; avoid full-box outlines.

### Specialized Components
*   **The "Bio-Overlap":** Design professional profiles where the image overlaps two background tiers (`surface` and `primary_container`) to break the grid and add depth.
*   **Sanctuary Accordions:** Use for FAQs. Use a subtle `surface-container-low` fill on the active state rather than a border.

## 6. Do's and Don'ts

### Do
*   **DO** use asymmetric layouts where text is weighted to one side and imagery to the other, leaving "white space to breathe."
*   **DO** use `newsreader` for quotes or patient testimonials to emphasize the human story.
*   **DO** ensure a minimum of 4.5:1 contrast ratio for all `body-md` text against its surface background.

### Don't
*   **DON'T** use 100% black (#000000). Always use `on-surface` (#191c1e) for text to maintain a premium, softer feel.
*   **DON'T** use sharp corners. Stick to the `lg` (0.5rem) and `xl` (0.75rem) scale to keep the interface feeling approachable and "soft."
*   **DON'T** use standard "Blue/Gray" medical grids. If the layout feels too "stiff," increase the line-height of the typography and offset the imagery.