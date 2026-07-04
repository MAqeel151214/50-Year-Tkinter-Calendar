## 2026-07-04 - Auto-updating dropdowns & Enter to submit
**Learning:** Tkinter forms that rely solely on "Submit/Update" buttons interrupt flow. Auto-updating on dropdown selection (`<<ComboboxSelected>>`) and enabling `<Return>` key submission for text fields significantly reduces user friction and modernizes the feel without needing web dependencies.
**Action:** Always bind `<<ComboboxSelected>>` for interconnected filtering options or immediate visual updates, and bind `<Return>` to primary actions on relevant entry fields.
