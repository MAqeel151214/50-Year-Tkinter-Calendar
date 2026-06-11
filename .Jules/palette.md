## 2024-06-11 - Auto-updating forms and inputs
**Learning:** Users shouldn't need to click buttons for simple inputs like dropdowns or single text entries, but Tkinter doesn't do this by default.
**Action:** Always bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to text inputs, ensuring target functions accept an `event=None` parameter.
