"""Shared type names for phrases."""

# key -> (what just happened, as told to the AI; things EMO can say offline)
type Lines = dict[str, tuple[str, list[str]]]

# What EMO does in reply to a chat message: (say, emotion, action).
type Reply = tuple[str, str, str]
