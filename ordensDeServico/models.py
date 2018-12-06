from django.db import models

class OportunidadesRecente(models.Model):
    op_id = models.AutoField(primary_key=True)
    op_nome = models.CharField(max_length=30)
    op_descricao = models.TextField()
    op_data = models.DateField()
    op_dapartamento = models.CharField(max_length=50)

    def __str__(self):
        return self.op_nome + ' ' + self.op_dapartamento

class OrdensServico(models.Model):
    os_numero = models.AutoField(primary_key=True)
    os_nome = models.CharField(max_length=30)
    os_recursos = models.PositiveIntegerField()
    os_descricao = models.TextField()

    def __str__(self):
        return str(self.os_numero) + ' ' + self.os_nome

class Funcionario(models.Model):
    func_id = models.AutoField(primary_key=True)
    func_nome = models.CharField(max_length=30)
    func_funcao= models.CharField(max_length=30)
    func_status = models.BooleanField(default=False)

    def __str__(self):
        return self.func_nome
