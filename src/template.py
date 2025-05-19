from shlex import join
from textwrap import dedent

cabecalho = dedent("""\
                   ## ESTUDO TÉCNICO PRELIMINAR (RESOLUÇÃO CNJ Nº 468/2022)
                   PROCESSO ADMINISTRATIVO SEI Nº XXXXXX-XX.2025.6.07.8100 UNIDADE DEMANDANTE: COXX - Coordenadoria de XX
                   ## EQUIPE DE PLANEJAMENTO:
                   Integ. Demandante: Fulano Ciclano (Mat. XXXX); Integ. Técnico:  Fulano Ciclano (Mat. XXXX); Integ. Administrativo: Fulano Ciclano (Mat. XXXX)
                   CÓDIGOS CATMAT E CATSER GRUPO 1: 26140; 27669; 22110; 27120. GRUPO 2: 26387 GRUPO 3: 621479
                    """)

objetivo_objetos = dedent("""\
    # 1. DESCRIÇÃO DETALHADA DO OBJETIVO, COM ESPECIFICAÇÃO DOS REQUISITOS NECESSÁRIOS:
    
    ## 1.1 DESCRIÇÃO DETALHADA DO OBJETIVO, COM ESPECIFICAÇÃO DOS REQUISITOS NECESSÁRIOS:
    
    1.1 Estes Estudos Técnicos Preliminares têm por objetivo verificar a viabilidade de contratação e fornecer uma base detalhada e fundamentada para {Objetivo da Contratação}.
    1.2 O que se pretende, portanto, é a contratação dos seguintes objetos, com seus nomes, descrição e quantidades:
    | Item    | Descrição             | Quantidade   |
    |---------|-----------------------|--------------|
    | {Item 1}| {Descrição do Item 1} | {n}          |
    | {Item 2}| {Descrição do Item 2} | {n}          |
    | {Item 3}| {Descrição do Item 3} | {n}          |
    """)

problema_necessidade = dedent("""\
## 1.2. NÃO FUNCIONAIS

### 1.2.1. REQUISITOS DE NEGÓCIO:

1.2.1.1.  {Requisitos de negócio}

### 1.2.2. REQUISITOS DE GARANTIA E MANUTENÇÃO:

1.2.2.1. {Requisitos de Garantia e Manutenção, se houver}

### 1.2.3. REQUISITOS DE SEGURANÇA DA INFORMAÇÃO

1.2.3.1. {Requisitos de Segurança da Informação}

### 1.2.4. REQUISITOS TECNOLÓGICOS E DE ARQUITETURA:

1.2.4.1. {Requisitos Tecnológicos e de Arquitetura}

### 1.2.5. REQUISITOS LEGAIS:

1.2.5.1.  {Requisitos legais}

### 1.2.6 REQUISITOS DE CAPACITAÇÃO

1.2.6.1. {Requisitos de Capacitação}

### 1.2.7. REQUISITOS AMBIENTAIS

1.2.7.1. {Requisitos Ambientais}

### 1.2.8. REQUISITOS CULTURAIS

1.2.8.1. {Requisitos Culturais}

### 1.2.9. REQUISITOS SOCIAIS

1.2.9.1. {Requisitos Sociais}

### 1.2.10. REQUISITOS TEMPORAIS

1.2.10.1. {Requisitos Temporais}

## 1.3. REQUISITOS FUNCIONAIS

### 1.3.1. {Requisitos Funcionais}
1.3.1.1. {Requisito Funcional 1}
1.3.1.2. {Requisisto Funcional 2}

    """)

alinhamento = dedent('''\
## 1.4. ALINHAMENTO DA CONTRATAÇÃO COM O PLANEJAMENTO INSTITUCIONAL
1.4.1. A contratação estará alinhada com os seguintes normativos:

| Normativo   | Relação             |
|-------------|---------------------|
| Normativo 1 | Relação/alinhamento |
''')

necessidade_beneficios = dedent(
'''\
# 2. JUSTIFICATIVA CONTENDO: NECESSIDADE DA AQUISIÇÃO, OBJETIVOS ESPERADOS E RESULTADOS QUE SE PRETENDE ALCANÇAR COM A AQUISIÇÃO:

## 2.1. NECESSIDADE DA AQUISIÇÃO

2.1.1. {Necessidades da Contratação}.

## 2.2. BENEFÍCIOS DIRETOS E INDIRETOS DA CONTRATAÇÃO
2.2.1. {Benefícios Diretos}
2.2.2. {Benefícios Indiretos}
''')

levantamento_de_mercado = dedent('''\
# 3. LEVANTAMENTO DE MERCADO (IDENTIFICAÇÃO DAS DIVERSAS SOLUÇÕES DISPONÍVEIS NO MERCADO E CONTRATAÇÕES SIMILARES REALIZADAS POR OUTROS ÓRGÃOS PÚBLICOS) E JUSTIFICATIVA PARA ESCOLHA DO OBJETO QUE SE ALMEJA CONTRATAR (RAZÃO DA ESCOLHA DA SOLUÇÃO EM CONTRATAÇÃO COM OUTRAS DISPONÍVEIS NO MERCADO):

## 3.1. SOLUÇÕES DE MERCADO
3.1.1. {Soluções de mercado}

| Solução 1 | Descrição |
|-----------|-----------|
| Solução 2 | Descrição |

## 3.2. CONTRATAÇÕES SIMILARES DE OUTROS ÓRGÃOS
3.2.1. Foram, então, levantadas outras contratações públicas similares:

{Outras Contratações Públicas}

| Contratação Pública | Descrição   | Valor total |
|---------------------|-------------|-------------|
| Contratação 1       | Descrição 1 | Valor 1     |

## 3.3 SOLUÇÃO ESCOLHIDA E JUSTIFICATIVA
3.3.1. A Solução escolhida é {Solução Escolhida}. A razão para a escolha é {Solução de mercado melhor}.

''')

justificativa_parcelamento = dedent('''\
# 4. JUSTIFICATIVAS PARA O PARCELAMENTO OU NÃO DO OBJETO, DE ACORDO COM A LEI DE LICITAÇÕES E CONTRATOS, COM DEFINIÇÃO E DOCUMENTAÇÃO DO MÉTODO PARA AVALIAR SE O OBJETO É DIVISÍVEL, COM BASE NAS PARTICULARIDADES DO MERCADO FORNECEDOR (DEFINIÇÃO DO TIPO DE LICITAÇÃO/ADJUDICAÇÃO):

4.1. Em função da natureza da contratação, decide-se pelo {parcelamento / não parcelamento do objeto}, uma vez que é {tecnicamente inviável/tecnicamente viável}, em função da seguinte justificativa {justificativa de parcelamento}.
''')

justificativa_economicidade = dedent('''\
# 5. JUSTIFICATIVA ECONÔMICA DA CONTRATAÇÃO
5.1. {Justificativa da economicidade}
''')

quantidade_calculo = dedent('''\
# 6. ESTIMATIVA DAS QUANTIDADES, ACOMPANHADAS DAS MEMÓRIAS DE CÁLCULO E DOS DOCUMENTOS QUE LHE DÃO SUPORTE (DEFINIÇÃO E DOCUMENTAÇÃO DO MÉTODO UTILIZADO PARA REALIZAR A ESTIMATIVA DE QUANTIDADES, BEM COMO A RELAÇÃO ENTRE A DEMANDA E O QUANTITATIVO ESTIMADO):

## 6.1. Quantitativos da contratação e suas memórias de cálculo
                            
| Item   | Quantitativo           | Memória de Cálculo           | Total           |
|--------|------------------------|------------------------------|-----------------|
| Item 1 | Quantitativo do item 1 | Memória de Cálculo do Item 1 | Total do Item 1 |

## 6.2. Total da Contratação
6.2.1. A contratação perfazerá o total de {total da contratação}.

''')

impacto_ambiental = dedent('''\
# 7. IMPACTO AMBIENTAL DA CONTRATAÇÃO
7.1. {Impactos ambientais}
''')

risk_management = dedent('''\
# 8. GESTÃO DE RISCO
8.1. {Gestão de Riscos}
                         
| Risco   | Possibilidade de Ocorrência | Impactos na Instituição | Ações de Mitigação |
|---------|-----------------------------|-------------------------|--------------------|
| Risco 1 | Baixo (XX%)                 | Baixo (XX%)             | Ação 1; Ação 2     |
| Risco 2 | Alto (XX%)                  | Médio (XX%)             | Ação 1; Ação 2     |
''')

final = dedent('''\
# 9. A CLASSIFICAÇÃO ORÇAMENTÁRIA COM A INDICAÇÃO DA FONTE DE RECURSO DO ORÇAMENTO DO ÓRGÃO PREVISTO PARA ATENDER A NECESSIDADE DA CONTRATAÇÃO (SE NECESSÁRIO, A EQUIPE DEVERÁ DILIGENCIAR À SEPEO PARA ESCLARECIMENTOS):

- 16.1.  Segundo informações da SEPEO, a presente demanda classifica-se na Ação XXXX: PO SEG0 - Segurança da Informação, na natureza de despesa  3390.40  -  Serviços  de  Tecnologia  da  Informação  e  Comunicação  -  PJ,  no  subitem  07  -  Manutenção  Corretiva  /  Adaptativa  e Sustentação de Softwares.

# 10. DECLARAÇÃO DE VIABILIDADE DA CONTRATAÇÃO

- 17.1. A  Equipe  de  Planejamento  da  Contratação,  com  fundamento  na  Resolução  CNJ  nº  468/2022,  e  após  concluir  os  estudos  técnicos  preliminares  aqui apresentados, declara ser viável a contratação pretendida.

## EQUIPE DE PLANEJAMENTO DA CONTRATAÇÃO

| Integrante Demandante                          | Integrante Técnico                     | Integrante Administrativo         |
|------------------------------------------------|----------------------------------------|-----------------------------------|
''')
corpo_etp = [cabecalho, 
             objetivo_objetos, 
             problema_necessidade, 
             alinhamento, 
             necessidade_beneficios, 
             levantamento_de_mercado, 
             justificativa_parcelamento,
             justificativa_economicidade,
             quantidade_calculo,
             impacto_ambiental,
             risk_management,
             final]
template = str.join("# PROJETO ETP {NOME DO PROJETO} \n \n", [i+" \n" for i in corpo_etp])
