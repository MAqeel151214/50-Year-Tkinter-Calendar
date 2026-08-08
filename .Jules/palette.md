## 2026-08-08 - Auto-Update Calendar on Selection
**Learning:** Tkinter interfaces can lack fluid interaction; requiring explicit button clicks for dropdowns breaks modern web-like UX expectations.
**Action:** Always bind `<<ComboboxSelected>>` to dropdown menus and `<Return>` to text fields to provide immediate feedback without manual clicks.
