# ServiceRequestTicket Class

from ticket import Ticket
from enums import Priority


class ServiceRequestTicket(Ticket):

    def __init__(
        self,
        ticket_id: str,
        title: str,
        description: str,
        priority: Priority,
        request_type: str
    ):
        super().__init__(
            ticket_id,
            title,
            description,
            priority
        )

        self._request_type = request_type

    @property
    def request_type(self) -> str:
        return self._request_type

    def get_ticket_type(self) -> str:
        return "Service Request"

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
            f"Request Type: {self._request_type}\n"
            f"Technician: {technician}\n"
            f"Created: {self._created_at}"
        )