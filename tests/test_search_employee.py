from utils.base_class import BaseClass
from test_data.test_data import data

# TEST DATA
login_data = data['login']
employee_data = data['search_employee']


class TestSearchEmployee(BaseClass):

    def test_search_employee(self):

        # Test Navigation
        cells, employee_id = self.search_employee(
            login_data['username'],
            login_data['password'],
            employee_data['first_name'],
            employee_data['last_name']
        )
        refreshed_cells = self.get_cells_by_employee_id(employee_id)
        # Test Assertions
        assert refreshed_cells[2].text == employee_data['first_name']
        assert refreshed_cells[3].text == employee_data['last_name']
        assert refreshed_cells[1].text == employee_id
