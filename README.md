# Validador de CEP

Projeto de validação de CEP utilizando Python, Pytest e GitFlow.

## Exemplos válidos

18110-000 → Votorantim  
18110000 → Votorantim  
18000-000 → Sorocaba  

## Exemplos inválidos

18110-000 → Sorocaba  
00000-000 → Cidade  
abcde → Sorocaba  