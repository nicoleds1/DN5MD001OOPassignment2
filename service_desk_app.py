# Import the classes needed for the Service Desk application
from ticket_manager import TicketManager
from technician import Technician
from incident_ticket import IncidentTicket
from service_request_ticket import ServiceRequestTicket
from enums import Priority, TicketStatus


# ServiceDeskApp controls the user interaction and menu
class ServiceDeskApp:

    # Set up the application when it first starts
    def __init__(self):

        # Create one TicketManager to manage all tickets
        self.manager = TicketManager()

        # Create technicians that can be assigned to tickets
        self.technicians = [
            Technician("TECH001", "Alex", "Networking"),
            Technician("TECH002", "Sam", "Software"),
            Technician("TECH003", "Jordan", "Hardware")
        ]


    # Display the main menu to the user
    def display_menu(self) -> None:

        print("\n========================================")
        print("     IT SERVICE DESK TICKET SYSTEM")
        print("========================================")
        print("1. Create New Ticket")
        print("2. Display Ticket Information")
        print("3. Update Priority or Status")
        print("4. Assign or Reassign Technician")
        print("5. Close Ticket")
        print("6. Exit")
        print("========================================")


    # Run the application and keep showing the menu until the user exits
    def run(self) -> None:

        while True:

            # Show the main menu
            self.display_menu()

            # Ask the user to select a menu option
            choice = input("Enter option (1-6): ").strip()

            # Call the correct method based on the user's choice
            if choice == "1":
                self.create_new_ticket()

            elif choice == "2":
                self.display_ticket_information()

            elif choice == "3":
                self.update_ticket()

            elif choice == "4":
                self.assign_or_reassign_technician()

            elif choice == "5":
                self.close_ticket()

            elif choice == "6":
                print("\nThank you for using the IT Service Desk.")
                print("Application closed.")
                break

            # Handle invalid menu options
            else:
                print("\nInvalid option.")
                print("Please enter a number between 1 and 6.")


    # Create either an Incident Ticket or Service Request Ticket
    def create_new_ticket(self) -> None:

        print("\n========================================")
        print("          CREATE NEW TICKET")
        print("========================================")
        print("1. Incident Ticket")
        print("2. Service Request Ticket")

        # Ask the user which type of ticket to create
        ticket_type = input("Select ticket type (1-2): ").strip()

        # Check that the user entered a valid ticket type
        if ticket_type not in ["1", "2"]:
            print("\nInvalid ticket type.")
            print("Please select option 1 or 2.")
            return

        # Generate a unique ID for the new ticket
        ticket_id = self.manager.generate_ticket_id()

        # Ask for a title and prevent an empty title
        while True:

            title = input("Enter ticket title: ").strip()

            if title:
                break

            print("Ticket title cannot be empty.")

        # Ask for a description and prevent an empty description
        while True:

            description = input("Enter ticket description: ").strip()

            if description:
                break

            print("Ticket description cannot be empty.")

        # Ask the user to select the ticket priority
        priority = self.select_priority()

        # Create an IncidentTicket if option 1 was selected
        if ticket_type == "1":

            # Ask which system is affected
            while True:

                affected_system = input(
                    "Enter affected system: "
                ).strip()

                if affected_system:
                    break

                print("Affected system cannot be empty.")

            # Create the IncidentTicket object
            ticket = IncidentTicket(
                ticket_id,
                title,
                description,
                priority,
                affected_system
            )

            # Store the ticket in TicketManager
            self.manager.add_ticket(ticket)

            print(
                f"\nIncident Ticket {ticket_id} "
                "successfully created."
            )

        # Create a ServiceRequestTicket if option 2 was selected
        elif ticket_type == "2":

            # Ask the user what type of service is being requested
            while True:

                request_type = input(
                    "Enter request type: "
                ).strip()

                if request_type:
                    break

                print("Request type cannot be empty.")

            # Create the ServiceRequestTicket object
            ticket = ServiceRequestTicket(
                ticket_id,
                title,
                description,
                priority,
                request_type
            )

            # Store the ticket in TicketManager
            self.manager.add_ticket(ticket)

            print(
                f"\nService Request Ticket {ticket_id} "
                "successfully created."
            )

        # Display the information for the newly created ticket
        print("\nTicket Information:")
        print(ticket.display_details())


    # Allow the user to search for a ticket or display all tickets
    def display_ticket_information(self) -> None:

        print("\n========================================")
        print("       DISPLAY TICKET INFORMATION")
        print("========================================")
        print("1. Search for a Ticket")
        print("2. Display All Tickets")

        # Ask the user how they want to view tickets
        choice = input("Enter option (1-2): ").strip()

        # Search for one specific ticket
        if choice == "1":

            # Ask for the ticket ID
            ticket_id = input(
                "Enter Ticket ID: "
            ).strip().upper()

            # Try to find the ticket
            ticket = self.manager.get_ticket(ticket_id)

            # Stop if the ticket does not exist
            if ticket is None:
                print("\nTicket not found.")
                return

            # Display the details of the ticket
            print("\nTicket Information:")
            print(ticket.display_details())

        # Display every ticket stored in TicketManager
        elif choice == "2":

            tickets = self.manager.get_all_tickets()

            # Check whether there are any tickets
            if not tickets:
                print("\nNo tickets currently exist.")
                return

            print("\nAll Tickets:")

            # Go through every ticket in the list
            for ticket in tickets:

                print("\nTicket Information:")

                # Polymorphism happens here because each subclass
                # provides its own version of display_details()
                print(ticket.display_details())

        # Handle an invalid display option
        else:
            print("\nInvalid option.")
            print("Please enter option 1 or 2.")


    # Allow the user to update either the priority or status
    def update_ticket(self) -> None:

        print("\n========================================")
        print("             UPDATE TICKET")
        print("========================================")

        # Ask which ticket should be updated
        ticket_id = input(
            "Enter Ticket ID: "
        ).strip().upper()

        # Find the requested ticket
        ticket = self.manager.get_ticket(ticket_id)

        # Prevent the update if the ticket does not exist
        if ticket is None:
            print("\nTicket not found.")
            return

        print("\n1. Update Priority")
        print("2. Update Status")

        # Ask what should be updated
        choice = input("Enter option (1-2): ").strip()

        # Update the ticket priority
        if choice == "1":

            priority = self.select_priority()

            success = self.manager.update_priority(
                ticket_id,
                priority
            )

            if success:
                print(
                    f"\nTicket {ticket_id} priority "
                    f"successfully updated to {priority.value}."
                )

        # Update the ticket status
        elif choice == "2":

            status = self.select_status()

            success = self.manager.update_status(
                ticket_id,
                status
            )

            if success:
                print(
                    f"\nTicket {ticket_id} status "
                    f"successfully updated to {status.value}."
                )

        # Handle an invalid update option
        else:
            print("\nInvalid option.")
            print("Please enter option 1 or 2.")


    # Assign a technician or replace the currently assigned technician
    def assign_or_reassign_technician(self) -> None:

        print("\n========================================")
        print("      ASSIGN/REASSIGN TECHNICIAN")
        print("========================================")

        # Ask which ticket needs a technician
        ticket_id = input(
            "Enter Ticket ID: "
        ).strip().upper()

        # Find the ticket
        ticket = self.manager.get_ticket(ticket_id)

        # Stop if the ticket does not exist
        if ticket is None:
            print("\nTicket not found.")
            return

        print("\nAvailable Technicians:")

        # Display each technician with a number
        for number, technician in enumerate(
            self.technicians,
            start=1
        ):
            print(f"{number}. {technician}")

        # Ask the user to choose a technician
        technician = self.select_technician()

        # Stop if an invalid technician was selected
        if technician is None:
            print("\nInvalid technician selection.")
            return

        # Check whether the ticket currently has a technician
        if ticket.assigned_technician is None:

            # Assign the selected technician
            success = self.manager.assign_technician(
                ticket_id,
                technician
            )

            if success:
                print(
                    f"\n{technician.name} successfully "
                    f"assigned to ticket {ticket_id}."
                )

        else:

            # Save the old technician so the change can be displayed
            old_technician = ticket.assigned_technician

            # Replace the current technician
            success = self.manager.assign_technician(
                ticket_id,
                technician
            )

            if success:
                print(
                    f"\nTicket {ticket_id} successfully "
                    f"reassigned from {old_technician.name} "
                    f"to {technician.name}."
                )


    # Close an existing ticket
    def close_ticket(self) -> None:

        print("\n========================================")
        print("              CLOSE TICKET")
        print("========================================")

        # Ask which ticket should be closed
        ticket_id = input(
            "Enter Ticket ID: "
        ).strip().upper()

        # Find the ticket
        ticket = self.manager.get_ticket(ticket_id)

        # Stop if the ticket cannot be found
        if ticket is None:
            print("\nTicket not found.")
            return

        # Check whether the ticket is already closed
        if ticket.status == TicketStatus.CLOSED:

            print(
                f"\nTicket {ticket_id} is already closed."
            )

            return

        # Ask for confirmation before changing the status
        print(
            f"\nAre you sure you want to close "
            f"ticket {ticket_id}?"
        )

        print("1. Yes")
        print("2. No")

        choice = input("Enter option (1-2): ").strip()

        # Change the ticket status to CLOSED
        if choice == "1":

            success = self.manager.update_status(
                ticket_id,
                TicketStatus.CLOSED
            )

            if success:
                print(
                    f"\nTicket {ticket_id} "
                    "successfully closed."
                )

        # Leave the ticket unchanged
        elif choice == "2":

            print("\nTicket closure cancelled.")

        # Handle an invalid confirmation option
        else:

            print("\nInvalid option.")
            print("Ticket was not closed.")


    # Ask the user to select a priority
    def select_priority(self) -> Priority:

        # Keep asking until a valid priority is entered
        while True:

            print("\nSelect Priority:")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            print("4. Critical")

            choice = input(
                "Enter priority (1-4): "
            ).strip()

            # Match each number with a Priority enum value
            priorities = {
                "1": Priority.LOW,
                "2": Priority.MEDIUM,
                "3": Priority.HIGH,
                "4": Priority.CRITICAL
            }

            # Return the selected priority if it is valid
            if choice in priorities:
                return priorities[choice]

            # Tell the user if the input was not valid
            print("\nInvalid priority.")
            print("Please enter a number between 1 and 4.")


    # Ask the user to select a ticket status
    def select_status(self) -> TicketStatus:

        # Keep asking until a valid status is entered
        while True:

            print("\nSelect Status:")
            print("1. Open")
            print("2. In Progress")
            print("3. Resolved")
            print("4. Closed")

            choice = input(
                "Enter status (1-4): "
            ).strip()

            # Match each number with a TicketStatus enum value
            statuses = {
                "1": TicketStatus.OPEN,
                "2": TicketStatus.IN_PROGRESS,
                "3": TicketStatus.RESOLVED,
                "4": TicketStatus.CLOSED
            }

            # Return the selected status if it is valid
            if choice in statuses:
                return statuses[choice]

            # Tell the user if the input was not valid
            print("\nInvalid status.")
            print("Please enter a number between 1 and 4.")


    # Ask the user to select a technician from the list
    def select_technician(self) -> Technician | None:

        # Keep asking until a valid number is entered
        while True:

            choice = input(
                "Select technician number: "
            ).strip()

            try:

                # Convert the user's choice into a list position
                # Subtract 1 because Python lists start at position 0
                index = int(choice) - 1

                # Check that the number exists in the technician list
                if 0 <= index < len(self.technicians):
                    return self.technicians[index]

                print("\nInvalid technician number.")
                print("Please select a technician from the list.")

            # ValueError occurs if the user enters text instead of a number
            except ValueError:

                print("\nInvalid input.")
                print("Please enter a number.")