# Inline Validation Checklist

_50 questions._

01 — What input requires inline validation?
02 — For every input, do we have exact validation requirements?
03 — What happens when a user jumps between empty fields?
04 — What happens when a user jumps between incomplete fields?
05 — What happens when a user jumps between invalid fields?
06 — What happens when a user jumps between valid fields?
07 — What happens when a user refreshes the page?
08 — What happens when a user opens the page in another tab?
09 — What happens if a user changes correct input?
10 — What happens if a user changes incorrect input?
11 — What input fields are likely to fail more often? 
12 — Can we break these fields into smaller ones to simplify validation?
13 — For these fields, can we show input hints above them (under labels)?
14 — Do we want to allow customers to proceed despite failed validation in these (or any other) fields?
15 — If yes, do we ask users to confirm their input is correct?
16 — For every input, do we set a minimum threshold of characters for validation to be triggered?
17 — For every input, do we start validating only once that threshold is reached?
18 — If there is an error, do we show it immediately as we detect it?
19 — Or do we use only late validation (user has left the field, on blur)?
20 — Do we avoid premature validation (on input focus)?
21 — Do we avoid immediate validation (as a user starts typing)?
22 — How do we minimize negative inline validation?
23 — How do we maximize positive inline validation?
24 — Do we never trigger new errors while the user fills in a form?
25 — When editing a field that was valid, do we validate on blur?
26 — When editing a field that was invalid, do we validate immediately during data entry?
27 — Can we test a "validate" button for complex input fields (passport number, IBAN, VAT, SMS code etc.)?
28 — Can we use auto-suggestions or popular input to help fix mistakes faster?
29 — How do we display error messages?
30 — Do we announce error messages to screen readers?
31 — Are error messages focusable?
32 — Do we change the border/background of an invalid input field?
33 — Do we display error messages above the input field?
34 — Do we complement text messages with warning icons?
35 — Does every error message drive a user towards fixing the error?
36 — Do error messages change based on a user’s specific errors?
37 — Does every error message remain visible until the error is fixed?
38 — Do error messages disappear only when input is validated?
39 — Can we avoid disabled "submit" buttons (and validate on submit)?
40 — If not, can we explain why they are disabled and how to fix it?
41 — Also, can we make disabled buttons focusable and provide help on tap/click/tab?
42 — If yes, can we show a tooltip linking to the error at the top?
43 — Can we guide users to errors when they submit?
44 — When should we guide users to the error summary at the top instead?
45 — Or do we auto-scroll the user to the label of the first error?
46 — In the error summary, do we display each error as a line on its own?
47 — Do we have server-side validation as well?
48 — Do we indicate failed validation in the browser tab's title (e.g. error count and emoji)?
49 — Do we monitor error rates to track how often users experience errors?
50 — Do we maintain and refine the wording of error messages over time?
