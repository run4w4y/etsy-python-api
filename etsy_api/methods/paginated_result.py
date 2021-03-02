from dataclasses import dataclass
from .pagination import Pagination


@dataclass
class PaginatedResult:
    total_count: int
    pagination: Pagination
    results: list
