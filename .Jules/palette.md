## 2024-05-24 - Auto-update on selection
**Learning:** Users expect modern interfaces to react instantly to dropdown changes and "Enter" key presses, rather than having to manually click "Submit" buttons for minor UI updates.
**Action:** Always bind `<<ComboboxSelected>>` for Tkinter comboboxes and `<Return>` for entry fields to trigger updates automatically.