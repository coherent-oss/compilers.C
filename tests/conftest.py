import pytest


@pytest.fixture
def disable_macos_customization(monkeypatch):
    from compilers.common.platform import macos

    monkeypatch.setattr(macos, 'customize_compiler', lambda config_vars: None)
