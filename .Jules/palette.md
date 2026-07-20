## 2024-05-24 - Auto-update and enter-to-submit
**Learning:** Users of Tkinter desktop apps expect modern web-like behaviors: dropdowns that auto-submit when changed and text fields that submit on Enter, reducing unnecessary clicks on utility buttons.
**Action:** Bind <<ComboboxSelected>> to dropdowns and <Return> to entry fields, modifying target functions to accept optional event=None arguments.
