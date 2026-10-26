# Web Forms Checklist

_70 questions._

01 — What’s the absolute minimum user input we need for new customers to get started?
02 — When is the right time and place to ask users to verify critical input (email, password, permissions)?
03 — For each piece of data, what’s the best form element to collect it fast and accurately?
04 — For sensitive data input (e.g. phone number), do we explain why we need it?
05 — Are there any form elements which need hints (e.g. password requirements, username)?
06 — Do we have an attribute profile for each input in our form — required/optional, allowed characters, min/max length, prefilling enabled/disabled, masking/validation/auto-formatting needed, accessible tooltip, dependencies on other elements, detection by IP.
07 — Do we always prioritize actionable copy: instead of “Password”, “Choose password”?
08 — Do we always prefer tap-friendly components, i.e. large buttons, toggles, and sliders?
09 — Do text boxes appear as text boxes (good padding, bordered).
10 — Have we adjusted the width of each box to give users a hint of the expected length of input?
11 — Do we use proper labels, associated with input fields?
12 — Do we use letter case for the microcopy on labels?
13 — Do we highlight required or optional fields, or both (preferably either optional or both)?
14 — How do we style placeholders, and is the microcopy helpful?
15 — Will labels be top-aligned or right-aligned (preferably the former)?
16 — Will we be using floating labels? If so, check if they are still announced to screen readers?
17 — Do inputs have :focus and :active styles?
18 — For each input, do we need to enable/disable autocorrect, spell-checking and autocapitalization?
19 — Do we use HTML5’s pattern to restrict input with in-browser validation?
20 — Are there any inputs where we need to provide a reasonable default value?
21 — Do we make use of autofill with the autocomplete attribute?
22 — Do we always display the right keyboard on mobile (inputmode)?
23 — Do we use autofocus to bring focus to the first input element on page load?
24 — Do we lay out fields in a single column (preferably yes)?
25 — Do we lay out field groups in multiple pages (one-thing-per-page pattern)?
26 — Do we show at most 7–8 input fields at a time on desktop, 3–4 on mobile?
27 — Are radio buttons actually round (preferably yes)?
28 — For radio buttons, are there any where a fallback input is required (e.g. “I’d rather not say” for gender, age etc.)?
29 — Are checkboxes square, with enough padding and large font size (18px+)?
30 — For checkboxes used as filters, do we track incompatibility of options or low result count to prevent users from landing on pages with no results?
31 — Do we avoid <select>-dropdowns as much as possible, and use steppers (<10 options) or datalist with autocomplete (>10 options) instead?
32 — For autocomplete, do we surface frequent hits at the top of autosuggestions?
33 — For a country selector autocomplete, do we need to display some countries as frequently used? Do they also appear in the alphabetical list?
34 — How do we design the country selector, and what height should it have (6–7 rows)?
35 — For our autocomplete, do we also accept abbreviations (GB, UK, DE, NL, CH etc.)?
36 — For our autocomplete, do we also accept alternative manual input?
37 — Do we display the results count for categories with autocomplete?
38 — Is autocomplete keyboard-accessible, and forgiving of minor typos and errors?
39 — Do we use a localization based on user-provided country or ZIP/postal code (placeholders, masks, input field(s) width, formatting, spelling, currency, legal requirements)?
40 — Can we ask for a full name instead of first, middle and last names?
41 — Do we avoid “Address Line 2” and use more contextual labels instead (“Apartment, suite, unit, floor”)?
42 — Can we use an address look-up widget (Loqate, Algolia Place, Google Place Autocomplete) to speed up location input?
43 — For date and time input, do we display input boxes or widgets with steppers for quick jumps?
44 — Do we provide autoformatting for phone number, birthday, amounts, numbers, dates, postal codes?
45 — For credit card input, can we avoid selection of the credit card type before input?
46 — As a label for the name on a credit card, do we use “Name on card”?
47 — As a label for security code, can we use “Security code” instead of “CVC” etc.?
48 — As a label for expiry date, can we use a single input field with auto-masking?
49 — Can we use Payment Request API, Apple Pay, Google Pay to avoid lengthy input altogether?
50 — For inline validation, can we define a threshold per input field, after which we start validating input?
51 — Can we not validate the input yet unless the threshold is reached?
52 — Do we show success only if the user has moved to the next field?
53 — When editing a field that was valid, do we validate after full data entry? (Reward early)
54 — When editing a field that was invalid, do we validate during data entry? (Punish late)
55 — Do our error messages drive users to a clear path on how to fix the error?
56 — On submit, do we scroll the user to the first error and focus on it?
57 — …or display the error above the submit button (focused)?
58 — If there are a few errors, do we additionally display a summary of errors at the top of the page?
59 — Do we display the error message just above the input field (not covered by keyboard on mobile)?
60 — Do we show the number of errors in the tab title as a prefix?
61 — Can we not disable submit buttons until all fields are filled in (easier to highlight and explain errors)?
62 — Do we display confirmation boxes only for absolutely critical situations (e.g. deleting email list entirely)? Can we use undos to help users quickly restore data instead?
63 — Do we move users to the next input field automatically after successful input?
64 — Do we persist the data on refresh?
65 — Have we tabbed through the entire form (incl. date picker and autocomplete)? Is the tab order predictable and reasonable?
66 — Have we tested the form on desktop, tablet, mobile? Where do error messages appear? Do labels always appear in full?
67 — For lengthy forms, do we need to first explain to users how much time the form will require, what documents they need to be prepared, and if they can save input and continue later?
68 — Do we have an input budget in place (max number of input fields per step)?
69 — Do we track the tap count (min number of taps needed to successfully complete the form)?
70 — Have we considered what happens when the form is loading (skeleton screen, loading indicator)?
