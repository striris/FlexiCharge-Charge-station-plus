
class Base:
    #If these methods need to be called before and after each tests individually, 
    # use setup_method and teardown_method instead 
    # go to this link https://docs.pytest.org/en/6.2.x/xunit_setup.html if you want to know more
    @classmethod
    def setup_class(cls):
        #This is called before all the tests
        pass

    def teardown_class(self):
        #This is called after all the tests
        pass