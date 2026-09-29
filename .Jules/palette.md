## 2026-09-29 - Modern Auto-submission Patterns
**Learning:** Tkinter interfaces in this application benefit from modern web-like auto-submission patterns to update the UI instantly without explicit submit buttons.
**Action:** Consistently bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to text entries using lambda wrappers (e.g., `lambda e: get_day()`) to avoid altering function signatures and breaking mock configurations.
