## 2026-05-07 - Add Keyboard Support and Auto-update
**Learning:** Users expect seamless interaction with forms without always needing to click a button. In this Tkinter app, having to click 'Show Calendar' after every dropdown change or 'Find Day of Week' after typing a date was causing friction.
**Action:** Bind `<<ComboboxSelected>>` to dropdowns to trigger updates automatically, and bind `<Return>` to text fields so users can press Enter to submit forms. Remember to add `event=None` to function signatures so they can be called both programmatically and via events.
