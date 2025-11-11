from typing import Optional, Dict, List, Tuple
from dataclasses import dataclass, field
from pydantic import BaseModel, ConfigDict
import json


class RegistrationInput(BaseModel):
    fixed: str
    moving: str
    level: Optional[float] = None
    polygons: List[List[float]]
    model_config = ConfigDict(extra="forbid")
