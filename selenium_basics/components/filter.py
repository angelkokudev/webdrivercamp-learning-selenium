from components.base import Base

#3. Inheritance
class LeftFilter(Base):
    def __init__(self, driver):
        super().__init__(driver)
#4. Add method
    LOCATOR = "//*"
    def select_option(self, option, visible=False):
        print(Base.BASE_VAR)
        print(LeftFilter.LOCATOR)
        print(option)
        print(visible)