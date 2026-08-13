from chatbili.config import ChatBiliConfig


def test_placeholder_config_uses_canonical_chatbili_identity():
    assert ChatBiliConfig._title == "ChatBili Configuration"
    assert ChatBiliConfig._aliases == ["chatbili"]
    assert ChatBiliConfig._storage_dir == "ChatBili"


def test_placeholder_config_does_not_define_fake_runtime_fields():
    public_names = [name for name in vars(ChatBiliConfig) if name.isupper()]
    assert public_names == []
