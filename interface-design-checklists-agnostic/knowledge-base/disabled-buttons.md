# Disabled Buttons Checklist

_36 questions._

01 — Do we need the button to be disabled by default (e.g. item is unavailable)?
02 — If not, can we keep it enabled and validate user input on submit?
03 — If not, can we rely on default values to keep the button enabled?
04 — When should the button become disabled (e.g. prevent double bookings)?
05 — Do we want to gray out any part of the interface along with the disabled button?
06 — Do we want to use a skeleton screen animation as well as the disabled button?
07 — Do we want to use a loading spinner for the UI to indicate that the system is busy?
08 — Do we want to use a progress indicator on the button to indicate progress?
09 — Should the wording on the button be different when it’s disabled?
10 — Does it have sufficient color contrast in the disabled state?
11 — Do we want to add a note under the button explaining why it is disabled?
12 — Do we want to use a tooltip explaining why the button is disabled?
13 — Do we keep the disabled button focusable?
14 — What happens when a user hovers or taps on the disabled button?
15 — What happens when a user tries to activate or focus on the disabled button?
16 — Do we change the cursor to not-allowed to indicate that the action isn’t allowed?
17 — Do we prevent the click via JavaScript by using aria-disabled?
18 — Do we use ARIA live regions to announce dynamic content?
19 — Do we avoid pointer-events: none as it doesn’t prevent focus/keyboard navigation?
20 — Do we guide users towards error messages when they tap/click/tab to the disabled button?
21 — When do we enable a disabled button?
22 — Can we add a link that sends all user input to support if they are locked out?
23 — In that case, do we ask users for their consent to be contacted?
24 — Do we use inline validation (positive or negative)?
25 — When and how do we show error messages?
26 — Do we include an option to continue even if inline validation fails?
27 — Do we need to update the state of the button after every user input?
28 — How will the button change while updating its state?
29 — Do we change the label of the button (“Updating…”) while it’s updating?
30 — Do we change the colors of the button while it’s updating?
31 — Do we want to add a loading spinner while the button is updating?
32 — Should we stop listening to click/tap after the first click/tap?
33 — Do we not stop listening to click/tap for undo buttons and steppers?
33 — Can we make the disabled button sticky on narrow screens?
34 — Do we track how many people who can’t proceed and abandon the flow altogether?
35 — If applicable, can we test if a design without disabled buttons performs better?
