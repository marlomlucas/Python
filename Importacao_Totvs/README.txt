Migração de sistema.
Sistema desenvolvido para facilitar a importação de dados no sistema Totvs
Dados exportados do sistema legado (sistema antigo) em arquivos .CSV
Usuário tinha que pesquisar no arquivo “CTRL + F” copiar e colar a linha com os dados do cliente em outro arquivo CSV separado.
Isso causava muitos erros de mesclagem, formatação e atraso na importação.

Solução foi desenvolver esta ferramenta que permite pesquisar os clientes pela Razão social, CNPJ, COD ou filtrar vários registros por determinados critérios.
Registro a ser importado é exibido no modo “Tabela” pois o layout de importação fornecido pela Totvs, segue o modelo de colunas e linhas como o Excel.
Além das validações básicas de entrada de dados, sistema também verifica se arquivo já existe, se está vazio e oferece a opção de limpeza caso contrário.
