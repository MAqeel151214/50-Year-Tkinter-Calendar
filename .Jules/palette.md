## 2026-06-30 - Auto-Trigger Interactions
**Learning:** Users expect seamless, web-like interactions where selecting from a dropdown or pressing Enter immediately updates the UI without requiring an extra button click.
**Action:** Bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to text inputs to trigger updates automatically, ensuring target functions accept an `event=None` parameter.
