import pytest
from src.abnt_converter import convert_to_abnt

class TestConverter:
    def test_given_a_name_convert_name_to_abnt_properly(self):
        name = 'Marcela Barella'
        expected = 'BARELLA, Marcela'
        assert convert_to_abnt(name) == expected

    def test_given_a_single_word_name_convert_to_abnt_properly(self):
        name = 'Guimaraes'
        expected = 'GUIMARAES'
        assert convert_to_abnt(name) == expected
    
    @pytest.mark.parametrize('name,expected', [('Marcela Barella Filha', 'FILHA BARELLA, Marcela'),
                                                ('Marcela Barella Neta', 'NETA BARELLA, Marcela'),
                                                ('Marcela Barella Sobrinha', 'SOBRINHA BARELLA, Marcela'),
                                                ('Marcela Barella Junior', 'JUNIOR BARELLA, Marcela')])
    def test_when_reserved_last_name_return_especial_formated_name(self, name, expected):
        assert convert_to_abnt(name) == expected

    @pytest.mark.parametrize('name,expected', [('Marcela Barella dos Santos', 'SANTOS, Marcela Barella'),
                                        ('Marcela Barella das Dores', 'DORES, Marcela Barella'),
                                        ('Marcela Barella da Silva', 'SILVA, Marcela Barella'),
                                        ('Marcela Barella do Carmo', 'CARMO, Marcela Barella')])
    def test_when_name_has_article_do_not_capitalize_and_include_on_formated_name(self, name, expected):
        assert convert_to_abnt(name) == expected
