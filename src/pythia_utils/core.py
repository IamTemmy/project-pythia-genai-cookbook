from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class GenerationResult:
    prompt: str
    output: str
    meta: Dict[str, Any]

def count_tokens(text: str) -> int:
    return len(text.split())

def pretty_print(title: str):
    print(f"\n=== {title} ===\n")
