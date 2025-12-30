# Palette's Journal

## 2025-01-20 - Respecting Motion Preferences
**Learning:** Infinite animations like falling snow can be distracting or nauseating for users with vestibular disorders.
**Action:** Always wrap non-essential decorative animations in `@media (prefers-reduced-motion: no-preference)` or disable them in `(prefers-reduced-motion: reduce)`.

## 2025-01-20 - avoiding Dead-Ends
**Learning:** Single-page reveal apps often leave users at a "success" state with no way to reset, forcing a browser refresh.
**Action:** Always provide a "Reset" or "Play Again" button to allow users to re-experience the flow without leaving the app context.
