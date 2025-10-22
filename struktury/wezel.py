from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Wezel:
    wartosc: Any
    nastepny: Optional["Wezel"] = None
    poprzedni: Optional["Wezel"] = None
