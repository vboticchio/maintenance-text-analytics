# maintenance-text-analytics
NLP aplicado a ordens de manutenção para cálculo de criticidade operacional

#  Problema
Ordens de manutenção contêm informação textual rica, mas pouco explorada.

# Solução
Aplicação de NLP + TF-IDF + SVM para identificar termos críticos e calcular índice de criticidade baseado no tempo de parada.

#  Fórmula do Índice
Criticidade = Peso TF-IDF × Tempo Médio de Parada

#  Tecnologias
- Python
- Pandas
- Scikit-learn
- NLTK
- Matplotlib

#  Aplicações
- Priorização de manutenção
- Identificação de falhas críticas
- Base para sistemas inteligentes de manutenção
