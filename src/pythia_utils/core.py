from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class GenerationResult:
    prompt: str
    output: str
    meta: Dict[str, Any]

def pretty_print(title: str):
    print(f"\n=== {title} ===\n")
