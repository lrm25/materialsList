import pytest

import materials_list

def test_select_option():
    with pytest.raises(Exception) as excinfo:
        # No options
        option_dict = {}
        input_str = ""
        materials_list.select_option(option_dict, input_str)
    assert materials_list.EMPTY_OPTION_DICT in str(excinfo.value)
    
