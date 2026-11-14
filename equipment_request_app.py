"""A beginner-friendly equipment request application."""


def add_request(requests):
    """Ask for request information and add it to the list."""
    equipment = input("Equipment name: ").strip()
    if equipment == "":
        print("Equipment name cannot be blank.")
        return

    requester = input("Your name: ").strip()
    if requester == "":
        print("Your name cannot be blank.")
        return

    print("Priority options: High, Medium, Low")
    priority = input("Priority: ").strip().title()
    while priority not in ["High", "Medium", "Low"]:
        print("Please enter High, Medium, or Low.")
        priority = input("Priority: ").strip().title()

    request = {
        "equipment": equipment,
        "requester": requester,
        "priority": priority
    }
    requests.append(request)
    print("Equipment request added successfully.")


def view_requests(requests):
    """Display every request in the order it was added."""
    if len(requests) == 0:
        print("No equipment requests have been added.")
        return

    print("\nAll Equipment Requests")
    for number, request in enumerate(requests, start=1):
        print(f"\nRequest {number}")
        print(f"Equipment: {request['equipment']}")
        print(f"Requested by: {request['requester']}")
        print(f"Priority: {request['priority']}")


def main():
    # This list stores requests only while the program is running.
    requests = []

    while True:
        print("\nEquipment Request Application")
        print("1. Add equipment request")
        print("2. View all requests")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_request(requests)
        elif choice == "2":
            view_requests(requests)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

