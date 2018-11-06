import os, sys
import mock
import pytest
from io import StringIO

import materials_list

def test_select_option_1():
    with pytest.raises(Exception) as excinfo:
        # No options
        option_dict = {}
        input_str = ""
        materials_list.select_option(option_dict, input_str)
    assert materials_list.EMPTY_OPTION_DICT in str(excinfo.value)

def test_select_option_2():
    with pytest.raises(Exception) as excinfo:
        # No options
        option_dict = None
        input_str = ""
        materials_list.select_option(option_dict, input_str)
    assert materials_list.EMPTY_OPTION_DICT in str(excinfo.value)
    
def test_select_option_3():
    with pytest.raises(Exception) as excinfo:
        option_dict = {'1': 'test'}
        input_str = None
        materials_list.select_option(option_dict, input_str)
    assert materials_list.EMPTY_OPTION_STR in str(excinfo.value)

def test_select_option_4():
    with pytest.raises(Exception) as excinfo:
        option_dict = {'1': 'test'}
        input_str = ""
        materials_list.select_option(option_dict, input_str)
    assert materials_list.EMPTY_OPTION_STR in str(excinfo.value)

def test_select_option_5():
    with pytest.raises(Exception) as excinfo:
        option_dict = {'1': 'test'}
        input_str = "\n"
        materials_list.select_option(option_dict, input_str)
    assert materials_list.EMPTY_OPTION_STR in str(excinfo.value)

def test_select_option_6():
    with pytest.raises(Exception) as excinfo:
        option_dict = {'1': 'test'}
        input_str = "test"
        acceptable = ( None, "a" )
        materials_list.select_option(option_dict, input_str, acceptable)
    assert materials_list.INVALID_ACCEP_VAL in str(excinfo.value)

def test_select_option_7():
    with pytest.raises(Exception) as excinfo:
        option_dict = {'1': 'test'}
        input_str = "test"
        acceptable = ( "\r", "a" )
        materials_list.select_option(option_dict, input_str, acceptable)
    assert materials_list.INVALID_ACCEP_VAL in str(excinfo.value)
        
def test_select_option_8(capsys):
        
        o_id='1'
        o_desc='test'
        t_id='2'
        t_desc='test2'
        input_str='input:'
        input_value = ['3', '1', 'a', 'b']

        o_line=o_id+". "+o_desc+'\n'
        t_line=t_id+". "+t_desc+'\n'
        bad_input=input_str+" "+materials_list.INVALID_SEL_STR+'\n'

        def mock_input():
            return input_value.pop(0)
        materials_list.input = mock_input
        option_dict = { o_id : o_desc, t_id : t_desc }
        acceptable = ("a", "b")
        # Invalid input, followed by valid
        materials_list.select_option(option_dict, input_str, acceptable)
        capture = capsys.readouterr()
        assert capture.out == o_line+t_line+bad_input+input_str+" "
        # Valid additional input one
        materials_list.select_option(option_dict, input_str, acceptable)
        capture = capsys.readouterr()
        assert capture.out == o_line+t_line+input_str+" "
        # Valid additional input two
        materials_list.select_option(option_dict, input_str, acceptable)
        capture = capsys.readouterr()
        assert capture.out == o_line+t_line+input_str+" "
