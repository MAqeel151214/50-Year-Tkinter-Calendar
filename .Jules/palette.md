## 2024-09-04 - Desktop App UX Patterns
**Learning:** For Tkinter desktop applications, web-like interaction patterns (such as auto-submitting dropdowns and `<Return>` key submission for text fields) are often absent but significantly improve keyboard accessibility and user flow by minimizing required mouse clicks.
**Action:** When working on Tkinter UI components, immediately look for opportunities to bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to entry fields that correspond to a primary action button.
