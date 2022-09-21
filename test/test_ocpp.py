import pytest
import requests
from test_base import Base

class TestOcpp(Base):
    #It is recommended to download the Python Test Explorer on VSCode for easier testing 
    #Make sure the test methods start with test_ 

    #Just example test
    def test_unit(self):
        assert 1 == 1 