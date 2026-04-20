## 2024-05-18 - [Add Auto-update to Month/Year Dropdown]
**Learning:** Users naturally expect modern dropdowns to auto-update the content without needing an explicit submit button. The existing Tkinter interface relies on a manual 'Show Calendar' button after making selections.
**Action:** Bind the `<<ComboboxSelected>>` event to the `month_menu` and `year_menu` in `my_calendar_app.py` to call `update_calendar` automatically when a selection is made.

## 2024-05-18 - [Add Enter Key Submission to Day Entry]
**Learning:** Keyboard accessibility is improved when users can press 'Enter' (<Return>) on text entry fields instead of manually clicking a submit button.
**Action:** Bind the `<Return>` event to the `day_entry` field in `my_calendar_app.py` to trigger the `get_day` function directly.
