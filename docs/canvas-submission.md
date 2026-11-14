# Canvas Submission Guide

## Exercise 6
- Merged pull request: https://github.com/gschoen06-design/equipment-request-app/pull/1
- Screenshot: [Completed priority filter](screenshots/exercise-6-priority-filter.png). Download the PNG from GitHub and attach it to Canvas.
- AI Decision Log entry: use the Exercise 6 entry in [ai-decision-log.md](ai-decision-log.md). Read it to confirm it reflects your decisions before submitting.

## Exercise 7
The Exercise 7 pull request contains `.agents/skills/requirements-reviewer/SKILL.md`, its metadata, the review report, and the accepted testing improvement. Use the merged Exercise 7 pull-request link supplied with this submission.

Most important finding: The feature met the specification, but the permanent suite lacked regression checks for resetting the view to High when reopened and preserving original add-request validation.

Decision: Accept. Functional Rule 2 requires the High reset, and the Constraints section requires preserving validation. Three tests were added for reopening with High, rejecting blank equipment/requester names, and retrying invalid priority input. All 11 tests pass. The application code was already correct and did not need changes.

Full evidence is in [requirements-review.md](requirements-review.md). AI assistance was used to create the code, specification, skill, review, tests, and these submission notes; the business choices and Accept decision were selected by Gavin in the conversation.

## Before submitting
Open both merged pull requests, check the screenshot, and review the decision entries. Submit the requested links and evidence in Canvas. These files do not submit anything to Canvas automatically.
