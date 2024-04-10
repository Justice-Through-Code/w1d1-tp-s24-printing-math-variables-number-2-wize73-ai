from unittest.mock import patch
from grade_calculator import calculate_average_grade

def test_calculate_average_grade():
    with patch('builtins.input', side_effect=['John Doe', '85', '90', '92']):
        assert calculate_average_grade() == ('John Doe', 89)

    with patch('builtins.input', side_effect=['Jane Smith', '75', '80', '85']):
        assert calculate_average_grade() == ('Jane Smith', 80)

    with patch('builtins.input', side_effect=['Alice Johnson', '60', '70', '65']):
        assert calculate_average_grade() == ('Alice Johnson', 65)