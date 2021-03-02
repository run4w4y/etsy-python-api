from dataclasses import dataclass


@dataclass
class Pagination:
    effective_limit: int
    effective_offset: int 
    next_offset: int 
    effective_page: int 
    next_page: int 
