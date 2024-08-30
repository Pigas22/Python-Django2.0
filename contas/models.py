from django.db import models as m

# Create your models here.

class Categoria(m.Model):
    var_nome = m.CharField(max_length= 100)
    var_descricao = m.CharField(max_length= 350)
    dt_criacao = m.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.var_nome


class Transacao(m.Model):
    data = m.DateTimeField(auto_now= True)
    descricao = m.CharField(max_length= 350)
    valor = m.DecimalField(max_digits= 7, decimal_places= 2)
    categoria = m.ForeignKey(Categoria, on_delete= m.CASCADE)
    observacoes = m.TextField(null= True, blank= True)

    class Meta:
        verbose_name_plural = "Transacoes"

    def __str__(self):
        return self.descricao
