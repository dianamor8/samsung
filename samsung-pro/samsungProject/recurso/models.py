from distutils.command.upload import upload
from unicodedata import category
from django.db import models

# Create your models here.


class Grade(models.Model):
    """Model definition for Grade."""
    SCHOOL_GRADES_CHOICES = [
        ('1EGB', '1ro. EGB'),
        ('2EGB', '2do. EGB'),
        ('3EGB', '3ro. EGB'),
        ('4EGB', '4to. EGB'),
        ('5EGB', '5to. EGB'),
        ('6EGB', '6to. EGB'),
        ('7EGB', '7mo. EGB'),    
    ]
    school_grade = models.CharField("schoolgrade", max_length=100, choices=SCHOOL_GRADES_CHOICES)
    
    class Meta:
        """Meta definition for Grade."""

        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'

    def __str__(self):
        """Unicode representation of Grade."""
        return self.school_grade

    # def save(self):
    #     """Save method for Grade."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for Grade."""
        return ('')

    # TODO: Define custom methods here


class LearningArea(models.Model):
    """Model definition for LearningArea."""
    LEARNING_AREAS_CHOICES = [
        ('MAT', 'Matemáticas'),
        ('LEN', 'Lenguaje'),
        ('ING', 'Inglés'),        
    ]
    area = models.CharField("area", max_length=100, choices=LEARNING_AREAS_CHOICES)
    # TODO: Define fields here

    class Meta:
        """Meta definition for LearningArea."""

        verbose_name = 'LearningArea'
        verbose_name_plural = 'LearningAreas'

    def __str__(self):
        return self.area

    # def save(self):
    #     """Save method for LearningArea."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for LearningArea."""
        return ('')

    # TODO: Define custom methods here


class Resource(models.Model):
    # TODO: Define fields here
    name = models.CharField('name',max_length=250)
    description = models.CharField('description',max_length=250)
    instruction = models.CharField('instruction',max_length=250)
    pub_date = models.DateTimeField('date_published', auto_now=True, auto_now_add=False)
    link =models.CharField(max_length=250)
    status=models.BooleanField('published', default=False)
    image= models.ImageField(blank=True, upload_to='resource_images')
    school_grades = models.ManyToManyField(Grade, verbose_name='grades')   
    learning_areas = models.ManyToManyField(LearningArea, verbose_name='areas')
    
    class Meta:
        """Meta definition for Resource."""
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'

    def __str__(self):
        return self.name

    # def save(self):
    #     """Save method for Resource."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for Resource."""
        return ('')

    # TODO: Define custom methods here


