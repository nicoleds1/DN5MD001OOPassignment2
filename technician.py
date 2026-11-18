# Technician Class
class Technician:

    def __init__(self, technician_id: str, name: str, specialism: str):
        self._technician_id = technician_id
        self._name = name
        self._specialism = specialism

    @property
    def technician_id(self) -> str:
        return self._technician_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def specialism(self) -> str:
        return self._specialism

    def __str__(self) -> str:
        return (
            f"{self._technician_id} - "
            f"{self._name} ({self._specialism})"
        )