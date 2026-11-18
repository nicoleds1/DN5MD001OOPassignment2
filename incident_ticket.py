# IncidentTicket Class

from ticket import Ticket
from enums import Priority


class IncidentTicket(Ticket):

    def __init__(
        self,
        ticket_id: str,
        title: str,
        description: str,
        priority: Priority,
        affected_system: str
    ):
        super().__init__(
            ticket_id,
            title,
            description,
            priority
        )

        self._affected_system = affected_system

    @property
    def affected_system(self) -> str:
        return self._affected_system

    def get_ticket_type(self) -> str:
        return "Incident"

    def display_details(self) -> str:
        technician = (
            str(self._assigned_technician)
            if self._assigned_technician
            else "Unassigned"
        )

        return (
            f"Ticket ID: {self._ticket_id}\n"
            f"Type: {self.get_ticket_type()}\n"
            f"Title: {self._title}\n"
            f"Description: {self._description}\n"
            f"Priority: {self._priority.value}\n"
            f"Status: {self._status.value}\n"
            f"Affected System: {self._affected_system}\n"
            f"Technician: {technician}\n"
            f"Created: {self._created_at}"
        )