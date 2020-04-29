import pytest
from src.abnt_converter import convert_to_abnt

class TestConverter:
    def test_given_a_name_convert_name_to_abnt_properly(self):
        name = 'Marcela Barella'
        expected = 'BARELLA, Marcela'

        assert convert_to_abnt(name) == expected
    
    @pytest.fixture()
    def test_when_reserved_last_name_return_especial_formated_name(self):
        name = 'Marcela Barella Sobrinha'
        expected = 'SOBRINHA BARELLA, Marcela'

        assert convert_to_abnt(name) == expected

    @pytest.fixture()
    def test_when_name_has_article_do_not_capitalize_and_include_on_formated_name(self):
        name = 'Marcela Barella dos Santos'
        expected = 'SANTOS, Marcela Barella'

        assert convert_to_abnt(name) == expected