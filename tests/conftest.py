import pytest


@pytest.fixture
def disable_macos_customization(monkeypatch):
    from compilers.common.platform import macos

    monkeypatch.setattr(macos, 'customize_compiler', lambda config_vars: None)


# from pytest-dev/pytest#363
@pytest.fixture(scope="session")
def monkeysession():
    from _pytest.monkeypatch import MonkeyPatch

    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()


@pytest.fixture(scope="module")
def suppress_path_mangle(monkeysession):
    """
    Disable the path mangling in the compiler. Workaround for pypa/distutils#169.
    """
    from compilers.C import base

    monkeysession.setattr(base.Compiler, '_make_relative', staticmethod(lambda x: x))
