## 2024-05-20 - Auto-updating and Keyboard Navigation in Tkinter
**Learning:** Users expect Tkinter apps to behave like modern web apps, where dropdown selections auto-update content and form fields can be submitted with the Enter key without needing explicit button clicks.
**Action:** Always bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to inputs that have an obvious primary action.
