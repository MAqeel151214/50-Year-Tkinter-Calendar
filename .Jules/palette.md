## 2024-10-24 - Auto-submit and Real-time Updates
**Learning:** Users expect dropdowns and text inputs to trigger actions immediately without requiring a button click, like auto-updating calendars on month/year selection and submitting forms with the Enter key.
**Action:** Bind `<<ComboboxSelected>>` for Comboboxes and `<Return>` for Entry widgets, updating target functions to accept an optional `event=None` parameter.
