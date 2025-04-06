from django.db import models


class BasicModel(models.Model):
    created_at = models.DateTimeField(verbose_name='criado em',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em',
                                      auto_now=True)
    is_active = models.BooleanField(verbose_name='Ativo?')

    class Meta:
        abstract = True


class Author(BasicModel):
    name = models.CharField(verbose_name='Nome', max_length=100)
    about = models.CharField(verbose_name='Sobre', max_length=250)
    birth = models.DateField(verbose_name='Nascimento', blank=True)
    birthplace = models.CharField(verbose_name='Naturalidade', max_length=50,
                                  blank=True)
    death = models.DateField(verbose_name='Falecimento', blank=True)
    place_of_death = models.CharField(verbose_name='Local de falecimento',
                                      max_length=50, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ('name',)


class Genre(BasicModel):
    name = models.CharField(verbose_name='nome', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ('name',)


class Book(BasicModel):
    title = models.CharField(verbose_name='Título', max_length=100)
    genre = models.ForeignKey(Genre, verbose_name='Gênero',
                              on_delete=models.SET_NULL, null=True)
    synopsis = models.CharField(verbose_name='Sinopse', max_length=500)
    author = models.ManyToManyField(Author, verbose_name='Autor')
    about = models.CharField(verbose_name='Sobre', max_length=250)
    publication = models.DateField(verbose_name='Publicação')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ('title',)
