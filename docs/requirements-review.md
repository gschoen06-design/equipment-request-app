# Exercise 7 Requirements Review

## Scope and evidence
Invocation: `$requirements-reviewer Review the priority-filter feature against docs/priority-filter-spec.md. Do not change files.`

The repository-scoped skill at `.agents/skills/requirements-reviewer/SKILL.md` was initialized using Skill Creator, inspected, validated, and invoked in a separate review session. The session examined the Exercise 6 implementation at revision `8343a06b1901724739ef67bfb9020b93c6a8e649`, its specification, tests, README, and diff. It made no file edits. Its workflow explicitly covers applicability, evidence, reporting, and a read-only boundary.

## Satisfied acceptance criteria

| Criterion | Status | Specification evidence | Implementation evidence | Executed test evidence |
| --- | --- | --- | --- | --- |
| AC1 High first | Satisfied | docs/priority-filter-spec.md:22 | equipment_request_app.py:53 | tests/test_priority_filter.py:26 |
| AC2 Exact matches and fields | Satisfied | docs/priority-filter-spec.md:23 | equipment_request_app.py:35 and :46–48 | tests/test_priority_filter.py:33 |
| AC3 Entry order | Satisfied | docs/priority-filter-spec.md:24 | equipment_request_app.py:34 and :44 | tests/test_priority_filter.py:46 |
| AC4 Labels and counts | Satisfied | docs/priority-filter-spec.md:25 | equipment_request_app.py:38–41 | tests/test_priority_filter.py:53 and :59 |
| AC5 Empty results and continued use | Satisfied | docs/priority-filter-spec.md:26 | equipment_request_app.py:41 and :54–59 | tests/test_priority_filter.py:59 |
| AC6 Normalization and invalid retry | Satisfied | docs/priority-filter-spec.md:27 | equipment_request_app.py:55–61 | tests/test_priority_filter.py:66 |
| AC7 Data preservation and navigation | Satisfied | docs/priority-filter-spec.md:28 | equipment_request_app.py:33–36, :56–57, :76–82 | tests/test_priority_filter.py:73 and :79 |

## Gaps
No implementation gaps found. The original review ran `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v`: 8 tests passed. Supplemental read-only checks for reopening with High, empty views, blank names, and invalid-priority retry also passed.

## Unsupported behavior
None found. The direct helper `view_requests(requests)` defaults to All (equipment_request_app.py:31); the actual menu opens High through filter_requests (equipment_request_app.py:53 and :79), as specified.

## Data or security concerns
None observed within the specified console-app scope. Requests remain in memory (equipment_request_app.py:66). Persistence and login are explicitly out of scope (docs/priority-filter-spec.md:19 and :31). Filtering builds a separate list without modifying stored dictionaries.

## Tests still needed — most important finding
The review identified a nonblocking verification gap: supplemental passing checks were not retained as regression tests. Reopening View must reset to High (docs/priority-filter-spec.md:11; equipment_request_app.py:53), and existing add-request validation must remain intact (docs/priority-filter-spec.md:19; equipment_request_app.py:6–20).

## Student decision and response
Gavin selected **Accept** when asked how to respond. Added `test_reopening_view_resets_to_high`, `test_add_rejects_blank_names`, and `test_add_retries_invalid_priority` in tests/test_priority_filter.py. These turn the supplemental checks into repeatable evidence without changing working application code.

After the response, `python -m unittest discover -s tests -v` passed all **11 tests**. The specification's Verification Results now records both the Exercise 6 baseline and the Exercise 7 result. No blocking missing checks remain from this review.

## Recommendation
The evidence supports acceptance of the feature and the reviewer skill. The accepted testing improvement is complete. Skill structure validation also passed using Skill Creator's quick_validate.py.
