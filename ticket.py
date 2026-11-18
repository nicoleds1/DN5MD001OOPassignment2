# Ticket Class

from abc import ABC, abstractmethod
from datetime import datetime

from enums import Priority, TicketStatus
from technician import Technician


class Ticket(ABC):

    def __init__(
        self,
        ticket_id: str,
        title: str,
        description: str,
        priority: Priority
    ):
        self._ticket_id = ticket_id
        self._title = title
        self._description = description
        self._priority = priority
        self._status = TicketStatus.OPEN
        self._assigned_technician = None
        self._created_at = datetime.now()

    @property
    def ticket_id(self) -> str:
        return self._ticket_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def priority(self) -> Priority:
        return self._priority

    @property
    def status(self) -> TicketStatus:
        return self._status

    @property
    def assigned_technician(self) -> Technician | None:
        return self._assigned_technician

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def update_priority(self, priority: Priority) -> None:
        self._priority = priority

    def update_status(self, status: TicketStatus) -> None:
        self._status = status

    def assign_technician(self, technician: Technician) -> None:
        self._assigned_technician = technician

    @abstractmethod
    def get_ticket_type(self) -> str:
        pass

    @abstractmethod
    def display_details(self) -> str:
        pass