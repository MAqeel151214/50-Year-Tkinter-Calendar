## 2024-05-24 - Auto-updating Tkinter Inputs
**Learning:** Users expect dropdowns in modern apps to update content automatically upon selection without requiring a separate "Update" button click. Similarly, text inputs should submit on Enter key press.
**Action:** Bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to entry fields, ensuring the target functions accept an `event=None` argument.