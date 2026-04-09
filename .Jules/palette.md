## 2024-05-18 - Auto-update and Enter key submission in Tkinter apps
**Learning:** Desktop applications with Tkinter benefit significantly from modern web-like UX patterns. Users expect dropdowns to update content automatically upon selection rather than requiring an explicit "Show" button click, and they expect text inputs to be submittable via the Enter key.
**Action:** Always consider adding `<<ComboboxSelected>>` bindings for dropdowns and `<Return>` bindings for text inputs in Tkinter interfaces to improve fluidity and reduce required clicks.
