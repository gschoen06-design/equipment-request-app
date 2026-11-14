# Priority Filter Specification

## Goal
Help managers focus on equipment requests by priority without losing requests.

## User Need
As a manager, I need to view one exact priority or all requests and see how many match.

## Functional Rules
1. Keep the existing Add and Exit menu options; rename View all requests to View requests.
2. Each time View requests opens, display High requests first. Offer All, High, Medium, Low, and Back.
3. Match the selected priority exactly. All includes every request.
4. Accept filter words without regard to case or surrounding spaces. Reject other choices with a helpful message and ask again.
5. Display the selected view, matching count, and each matching request's equipment, requester, and priority in original entry order.
6. If nothing matches, show a count of zero and an explicit message naming the view. Allow another selection or Back.
7. Never remove or modify stored requests when filtering. Back returns to the main menu.

## Constraints
Use beginner-friendly Python functions, lists, dictionaries, loops, and conditionals. No login, database, or additional runtime packages. Preserve add-request validation. Requests remain in memory for the current run only, as in the starter.

## Acceptance Criteria
- AC1: Opening View requests with mixed-priority data displays only High requests before asking for a filter.
- AC2: Selecting High, Medium, or Low displays only that exact priority, with correct equipment, requester, and priority values.
- AC3: Selecting All displays all requests in original entry order; filtered views also preserve relative entry order.
- AC4: Every view displays its name and the correct matching count, including zero.
- AC5: An empty list or a priority with no matches displays a clear no-results message and still permits another selection or Back.
- AC6: Input such as ` medium ` is accepted; an invalid filter displays guidance and does not exit the view.
- AC7: Filtering repeatedly leaves the original list and request dictionaries unchanged. Back returns to the main menu, Add still works, and Exit closes the program.

## Out of Scope
Editing, deleting, sorting, multiple simultaneous priorities, threshold matching, login, database storage, and saving requests between runs.

## Student Decisions and Specification Improvement
Gavin selected exact-priority matching and High as the initial view. For the required specification improvement, he selected a matching-request count. AC4 explicitly makes that improvement observable and testable.

## Implementation Plan
Keep add_request unchanged. Allow view_requests to display one selected priority using a separate matching list. Add a filter-menu function that initially displays High and loops until Back. Verify AC1–AC7 using standard-library unittest and a complete menu interaction.

## Verification Results
Command: `python -m unittest discover -s tests -v` — 8 tests passed in Exercise 6; 11 tests passed after the accepted Exercise 7 regression-coverage improvement.

| Criterion | Result | Observable check |
| --- | --- | --- |
| AC1 | Pass | Mixed data opens with only High requests. |
| AC2 | Pass | High, Medium, Low selections show exact matches and all three fields. |
| AC3 | Pass | All and each filtered view preserve entry order. |
| AC4 | Pass | View labels and counts are checked for all four views, including zero in AC5. |
| AC5 | Pass | Empty data and a missing High priority show zero and a message; All and Back remain usable. |
| AC6 | Pass | Invalid selection is rejected; spaced lowercase inputs work afterward. |
| AC7 | Pass | Deep comparison confirms data preservation; a full menu run adds, views, returns, and exits. |

Verification applies to the tested console interactions. The existing in-memory storage limitation remains unchanged.
