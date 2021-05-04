import pytest


@pytest.mark.skip()
@pytest.mark.skipif()
@pytest.mark.xfail()
@pytest.mark.parametrize()
@pytest.mark.usefixtures('fixture1', 'fixture2')
@pytest.fixture(autouse=True, name='lue')
