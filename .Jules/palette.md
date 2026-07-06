## 2026-07-06 - Auto-update calendar and enter-to-submit
**Learning:** Desktop users expect modern web-like interactions in desktop GUIs, like auto-updating content on dropdown selection and submitting forms with the Enter key.
**Action:** Bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to entry fields, updating function signatures to accept an optional `event=None` parameter.