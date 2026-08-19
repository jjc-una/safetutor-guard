"""Core gateway interfaces.

Everything here is a stub on day 1. The signatures are the contract; the six
weeks of work is making the bodies real. Deciding the shape of the interface
before writing any detection logic is deliberate: it keeps the detectors
swappable and the evaluation harness stable.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Action(str, Enum):
    ALLOW = "ALLOW"
    SANITIZE = "SANITIZE"
    BLOCK = "BLOCK"


class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


@dataclass(frozen=True)
class Signal:
    """One piece of evidence produced by a detector."""

    rule_id: str
    category: str
    severity: Severity
    weight: float
    evidence: str


@dataclass
class Verdict:
    """The result of one validation pass."""

    action: Action
    risk_score: float
    signals: list[Signal] = field(default_factory=list)
    payload: str = ""
    elapsed_ms: float = 0.0

    @property
    def blocked(self) -> bool:
        return self.action is Action.BLOCK


def validate_input(user_prompt: str, *, source: str = "student") -> Verdict:
    """Score an inbound prompt for adversarial intent. (Week 2)"""
    raise NotImplementedError("Week 2, day 6")


def sanitize_output(llm_response: str) -> Verdict:
    """Scan and redact an outbound response before it reaches the student. (Week 3)"""
    raise NotImplementedError("Week 3, day 11")


def authorize_tool_call(tool_name: str, arguments: dict, *, provenance: str) -> Verdict:
    """Decide whether a tool invocation is permitted. (Week 6)"""
    raise NotImplementedError("Week 6, day 26")
