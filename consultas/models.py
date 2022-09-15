from django.db import models

# O modelo (models) trata-se de uma classe que estende models.Model
# Este modelo já possui divérsos recursos para o uso de banco de dados e 
#    interface, como o atributo id, que cria um identificador único para o
#    registro e objects, que trata do módulo manage que nos possibilita criar
#    comandos de consulta no banco de dados

# Documentação para selecionar os fields 
#  https://docs.djangoproject.com/en/4.1/ref/models/fields/
class Medico(models.Model):
    # Charfield: este tipo de atributo cria no banco de dados um campo de texto(VARCHAR)
    #  -É obrigatorio a parametrização do maximo de caracteres, para isso utilizamos o max_lenght.

    #Nome
    nome = models.CharField(
        max_length=255
        )

    # Por padrão não são aceitas informações nulas, para que não seja obrigatório o uso de determinado atributo é utilizado o parâmetro null para que no banco de dados seja um NOT NULL e blank para permitir informações em branco na interface

    #CPF
    cpf = models.CharField(
        max_length=11,
        null=True,
        blank=True
    )

    #CRM
    crm = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    #Datefield: tipo de atributo que representa uma data
    #DATA DE NASCIMENTO
    data_nascimento = models.DateField()

    #CIDADE
    cidade = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    # EmailField: é o tipo que representa a estrutura de um e-mail.
    # Para o banco de dados é simplesmente um texto e para a interface é um componente com validação de e-mail.
    #E-MAIL
    email = models.EmailField(
        null=True,
        blank=True
    )
