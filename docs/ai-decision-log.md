# AI Decision Log

## Exercise 6 — Matching-request count
The initial feature request asked for a faster way to focus on requests using priorities. During clarification, I selected exact-priority matching, chose High as the initial view, and selected a matching-request count as my specification improvement. The count makes it easier to see how many requests need attention without counting the displayed records manually. The specification now requires a visible count for every view, including zero (AC4), and the automated checks verify it.

AI assistance was used to draft the specification, implement the Python feature, and run the checks. My recorded choices came from the clarification answers in this conversation.

## Exercise 7 — Accept additional regression coverage
The requirements-reviewer found no implementation gaps. Its most useful recommendation was to preserve additional checks as permanent tests: reopening View requests should reset to High, and blank-name rejection and invalid-priority retry should remain intact. These behaviors were required by Functional Rule 2 and the validation constraint, but the original suite did not retain those checks. I chose Accept in the review-decision question. Three regression tests were added, bringing the suite from 8 passing tests to 11. The application code did not need to change.
