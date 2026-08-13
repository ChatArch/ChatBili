"Typed environment configuration for ChatBili."

from chatenv import BaseEnvConfig


class ChatBiliConfig(BaseEnvConfig):
    "ChatBili ChatEnv configuration placeholder."

    _title = "ChatBili Configuration"
    _aliases = ["chatbili"]
    _storage_dir = "ChatBili"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")


__all__ = ["ChatBiliConfig"]
