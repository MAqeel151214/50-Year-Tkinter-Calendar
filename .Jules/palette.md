## 2024-05-23 - Reactive Tkinter Interfaces
**Learning:** Tkinter forms feel static and require unnecessary button clicks by default. Adding event bindings (`<<ComboboxSelected>>` for dropdowns, `<Return>` for text inputs) significantly reduces interaction friction and mimics modern, reactive web UX.
**Action:** Always bind auto-update and form-submit events to Tkinter inputs where immediate feedback or natural keyboard flow is expected, ensuring the handler accepts an `event=None` argument.
