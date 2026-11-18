# TicketManager Class

from ticket import Ticket
from technician import Technician
from enums import Priority, TicketStatus


class TicketManager:

    def __init__(self):
        self._tickets: dict[str, Ticket] = {}
        self._next_ticket_number = 1

    def generate_ticket_id(self) -> str:
        ticket_id = f"T{self._next_ticket_number:03d}"
        self._next_ticket_number += 1
        return ticket_id

    def add_ticket(self, ticket: Ticket) -> None:
        self._tickets[ticket.ticket_id] = ticket

    def get_ticket(self, ticket_id: str) -> Ticket | None:
        return self._tickets.get(ticket_id)

    def get_all_tickets(self) -> list[Ticket]:
        return list(self._tickets.values())

    def update_priority(
        self,
        ticket_id: str,
        priority: Priority
    ) -> bool:

        ticket = self.get_ticket(ticket_id)

        if ticket is None:
            return False

        ticket.update_priority(priority)
        return True

    def update_status(
        self,
        ticket_id: str,
        status: TicketStatus
    ) -> bool:

        ticket = self.get_ticket(ticket_id)

        if ticket is None:
            return False

        ticket.update_status(status)
        return True

    def assign_technician(
        self,
        ticket_id: str,
        technician: Technician
    ) -> bool:

        ticket = self.get_ticket(ticket_id)

        if ticket is None:
            return False

        ticket.assign_technician(technician)
        return True