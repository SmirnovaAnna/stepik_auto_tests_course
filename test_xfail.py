from email.policy import strict
import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    """Checks the success of the test  

    :return: None
    """
    assert True


@pytest.mark.xfail
def test_not_succeed():
    """
    Checks the not success of the test 

    :return: None
    """
    assert False


@pytest.mark.skip
def test_skipped():
    """Checks the skip of the test 
        
    :return: None
    """
    assert False