"""Behavior checks for the priority-filter specification; no extra packages."""
import copy
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import equipment_request_app as app


class PriorityFilterTests(unittest.TestCase):
    def setUp(self):
        self.requests = [
            {"equipment": "Camera", "requester": "Alex", "priority": "Low"},
            {"equipment": "Laptop", "requester": "Gavin", "priority": "High"},
            {"equipment": "Projector", "requester": "Sam", "priority": "Medium"},
            {"equipment": "Microphone", "requester": "Hayes", "priority": "High"},
        ]

    def capture(self, function, *args, inputs=()):
        output = io.StringIO()
        with patch("builtins.input", side_effect=inputs), redirect_stdout(output):
            function(*args)
        return output.getvalue()

    def test_ac1_high_first(self):
        output = self.capture(app.filter_requests, self.requests, inputs=["Back"])
        self.assertIn("High Equipment Requests", output)
        self.assertIn("Equipment: Laptop", output)
        self.assertNotIn("Equipment: Camera", output)
        self.assertNotIn("Equipment: Projector", output)

    def test_ac2_exact_priority_and_fields(self):
        for priority in ["High", "Medium", "Low"]:
            with self.subTest(priority=priority):
                output = self.capture(app.filter_requests, self.requests, inputs=[priority, "Back"])
                selected_output = output.split(f"{priority} Equipment Requests")[-1]
                for request in self.requests:
                    if request["priority"] == priority:
                        self.assertIn(f"Equipment: {request['equipment']}", selected_output)
                        self.assertIn(f"Requested by: {request['requester']}", selected_output)
                        self.assertIn(f"Priority: {priority}", selected_output)
                    else:
                        self.assertNotIn(f"Equipment: {request['equipment']}", selected_output)

    def test_ac3_original_order(self):
        for priority in ["All", "High", "Medium", "Low"]:
            output = self.capture(app.view_requests, self.requests, priority)
            positions = [output.index("Equipment: " + r["equipment"]) for r in self.requests
                         if priority == "All" or r["priority"] == priority]
            self.assertEqual(positions, sorted(positions))

    def test_ac4_view_names_and_counts(self):
        for priority, count in [("All", 4), ("High", 2), ("Medium", 1), ("Low", 1)]:
            output = self.capture(app.view_requests, self.requests, priority)
            self.assertIn(f"{priority} Equipment Requests", output)
            self.assertIn(f"Matching requests: {count}", output)

    def test_ac5_empty_and_no_match_can_continue(self):
        for requests in [[], self.requests[:1]]:
            output = self.capture(app.filter_requests, requests, inputs=["All", "Back"])
            self.assertIn("Matching requests: 0", output)
            self.assertIn("No requests found for High.", output)
            self.assertIn("All Equipment Requests", output)

    def test_ac6_normalization_and_invalid_filter(self):
        output = self.capture(app.filter_requests, self.requests,
                              inputs=["urgent", " medium ", " low ", " all ", " back "])
        self.assertIn("Invalid filter. Enter All, High, Medium, Low, or Back.", output)
        for priority in ["Medium", "Low", "All"]:
            self.assertIn(f"{priority} Equipment Requests", output)

    def test_ac7_data_preserved(self):
        original = copy.deepcopy(self.requests)
        self.capture(app.filter_requests, self.requests,
                     inputs=["All", "Low", "High", "Medium", "Back"])
        self.assertEqual(self.requests, original)

    def test_ac7_main_add_back_and_exit(self):
        output = self.capture(app.main, inputs=["1", "Laptop", "Gavin", "high",
                                               "2", "All", "Back", "3"])
        self.assertIn("Equipment request added successfully.", output)
        self.assertIn("Equipment: Laptop", output)
        self.assertEqual(output.count("Equipment Request Application"), 3)
        self.assertIn("Goodbye!", output)


if __name__ == "__main__":
    unittest.main()
