from django.db import models
# Create your models here.


class PractiseModel(models.Model):
     Model_name = models.CharField(max_length=255)
     email = models.EmailField()
     ID = models.AutoField(primary_key=True)
     big_integer_value = models.BigIntegerField()
     binary_value = models.BinaryField()
     boolean_value = models.BooleanField()
   #   comma_separated_field = models.CharField(
   #      validators=[comma_separated_field],
   #      max_length=255
   #  )
     Todey_Date = models.DateField()
     Today_date_time = models.DateTimeField()
     decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
     Module_duration = models.DurationField()
     file_Up= models.FileField(upload_to='files/')
     file_path_field = models.FilePathField(path='/path/to/files/')
     slug_field = models.SlugField()
     small_Int = models.SmallIntegerField()
     positive_big_integer_field = models.PositiveBigIntegerField()
   #   foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
     Address = models.GenericIPAddressField()
   #   image = models.ImageField(upload_to='images/')
     json_field = models.JSONField()
   #   Relationship_manyToMany = models.ManyToManyField(OtherModel)
   #   Relationship_oneto_one= models.OneToOneField(OtherModel, on_delete=models.CASCADE)
     positive_big_integer_field = models.PositiveBigIntegerField()
     Description = models.TextField()
     url = models.URLField()
     