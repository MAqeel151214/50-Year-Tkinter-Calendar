## 2026-06-20 - Modernize Tkinter Inputs
**Learning:** Traditional Tkinter interfaces require manual button clicks for form submission and updates, which feels archaic compared to web standards. Binding <<ComboboxSelected>> for auto-updates and <Return> for submission provides a much smoother, modern UX.
**Action:** Always modify Tkinter function signatures to accept event=None so they can easily be bound to keyboard and interaction events without breaking programmatic calls.
