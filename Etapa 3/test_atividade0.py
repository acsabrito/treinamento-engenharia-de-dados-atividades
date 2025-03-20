# Testes Unitários
import pytest
from utils import fibonacci

def test_fibonacci_base_cases():
		assert fibonacci(0) == 1
		assert fibonacci(1) == 1
		assert fibonacci(2) == 1
		assert fibonacci(3) == 2
		assert fibonacci(4) == 3
		assert fibonacci(5) == 5
	
def test_fibonacci_large_number():
		assert fibonacci(10) == 55
		assert fibonacci(15) == 610
		
def test_fibonacci_invalid_input():
		with pytest.raises(ValueError,  match="O valor de n deve ser um inteiro não negativo."):
			fibonacci(-1)
		with pytest.raises(ValueError, match="O valor de n deve ser um inteiro não negativo."):
			fibonacci(2.5)
		with pytest.raises(ValueError, match="O valor de n deve ser um inteiro não negativo."):
			fibonacci("string")