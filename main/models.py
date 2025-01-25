from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django_ckeditor_5.fields import CKEditor5Field



class MyShortUuid(models.Model):
    uuid = ShortUUIDField(
        primary_key=True,
        editable=False,
        max_length=12,
        alphabet = 'abcdefghijklmnopqrstuvwxz123456789',
    )
    
    class Meta:
        abstract  = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class BaseModel(MyShortUuid):
    created = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class InformationLevel(models.TextChoices):
    HIGH = 'HIGH'
    MIDDLE = 'MIDDLE'
    NO = 'NO'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Continets(models.TextChoices):
    Afrika = 'Afrika'
    Amerika = 'Amerika'
    Asia = 'Asia'
    Europa = 'Europa'
    Oceania = 'Oceania'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class State(BaseModel):
    continent = models.CharField(max_length=200, choices=Continets, null=True)
    title = models.CharField(max_length=200)
    president = models.CharField(max_length=250)
    about = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    flag = models.ImageField(blank=True, upload_to='flags')
    anthem = models.TextField(default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    emblem = models.ImageField(upload_to='emblems/', blank=True)
    language = models.CharField(max_length=200)
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10, default=450.54)
    people = models.PositiveIntegerField(default=40000000)
    capital = models.CharField(max_length=200, default='Option')    
    gdp = models.DecimalField(decimal_places=2, max_digits=15, default=0.0, verbose_name='Umumiy ichki mahsulot (GDP)')
    unemployment_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name=' Ishsizlik darajasi')
    inflation_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Inflyatsiya darajasi') 
    poverty_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Qashshoqlik darajasi')
    literacy_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Savodxonlik darajasi')
    life_expectancy = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Hayot davomiyligi')
    population_growth_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Aholi o'sish darajasi")
    urban_population_percentage = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Shahar aholisi foizi')
    birth_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Tug'ilish darajasi")
    death_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="O'lim darajasi")
    changed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Region(BaseModel):
    title = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, related_name='region')
    governor = models.CharField(max_length=250)
    about = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    total_area_km2 = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    population_density = models.DecimalField(decimal_places=2, max_digits=10, default=0.0, verbose_name='aholi zichligi')  
    people = models.PositiveIntegerField(default=2500000)
    gdp = models.DecimalField(decimal_places=2, max_digits=15, default=0.0, verbose_name='yalpi ichki mahsulot')  
    unemployment_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='ishga joylashish darajasi') 
    literacy_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='savodxonlik darajasi')
    median_income = models.DecimalField(decimal_places=2, max_digits=15, default=0.0, verbose_name="o'rtacha daromad")
    changed_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class District(BaseModel):
    title = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='district')
    governor = models.CharField(max_length=250)
    about = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10, default=45.58)
    people = models.PositiveIntegerField(default=25000)
    total_budget = models.DecimalField(decimal_places=2, max_digits=15, default=0.0, verbose_name='Tuman byudjeti')
    poverty_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Qashshoqlik darajasi (%)') 
    literacy_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Savodxonlik darajasi (%)")
    unemployment_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Ishsizlik darajasi (%)")
    healthcare_facilities = models.PositiveIntegerField(default=0, verbose_name="Tibbiyot muassasalari soni")
    educational_institutions = models.PositiveIntegerField(default=0, verbose_name="Ta'lim muassasalari soni")
    industrial_units = models.PositiveIntegerField(default=0, verbose_name="Sanoat korxonalari soni")
    average_income_per_person = models.DecimalField(decimal_places=2, max_digits=10, default=0.0, verbose_name="Aholi boshiga o'rtacha daromad") 
    birth_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Tug'ilish ko'rsatkichi")
    death_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="O'lim ko'rsatkichi")
    change_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MFY(BaseModel):
    title = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='MFY')
    chairman = models.CharField(max_length=250)
    about = CKEditor5Field(config_name='extends', default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. ')
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10, default=15.75)
    people = models.PositiveIntegerField(default=8500)
    total_budget = models.DecimalField(decimal_places=2, max_digits=15, default=0.0, verbose_name="MFY byudjeti")
    poverty_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Qashshoqlik darajasi (%)")
    literacy_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Savodxonlik darajasi (%)")
    unemployment_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Ishsizlik darajasi (%)")
    healthcare_facilities = models.PositiveIntegerField(default=0, verbose_name="Tibbiyot muassasalari soni")
    educational_institutions = models.PositiveIntegerField(default=0, verbose_name="Ta'lim muassasalari soni")
    industrial_units = models.PositiveIntegerField(default=0, verbose_name="Sanoat korxonalari soni")
    average_income_per_person = models.DecimalField(decimal_places=2, max_digits=10, default=0.0, verbose_name="Aholi boshiga o'rtacha daromad")
    birth_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Tug'ilish ko'rsatkichi")
    death_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="O'lim ko'rsatkichi")
    change_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Neighborhood(BaseModel):   
    title = models.CharField(max_length=200)
    elder = models.CharField(max_length=250, default='Jhon Doe')
    MFY = models.ForeignKey(MFY, on_delete=models.SET_NULL, null=True, related_name='neighborhood')
    about = CKEditor5Field(config_name='extends', default = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. ')
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=15, default=4.65)
    people = models.PositiveIntegerField(default=530)
    population_density = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Aholi zichligi (kishi/km²)")
    unemployment_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name="Ishsizlik darajasi (%)")
    avg_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="O'rtacha daromad (so'm)")
    young_population = models.PositiveIntegerField(default=0, verbose_name="Kichik yoshdagi aholi (0-14)")
    working_population = models.PositiveIntegerField(default=0, verbose_name="Ishchi yoshdagi aholi (15-64)")
    elderly_population = models.PositiveIntegerField(default=0, verbose_name="Keksaygan yoshdagi aholi (65+)")
    education_high = models.PositiveIntegerField(default=0, verbose_name="Oliy ta'lim olganlar")
    education_middle = models.PositiveIntegerField(default=0, verbose_name="O'rta ta'lim olganlar")
    no_education = models.PositiveIntegerField(default=0, verbose_name="Ta'lim olmaganlar")
    change_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class House(BaseModel):
    house_boss = models.CharField(max_length=200)
    house_number= models.PositiveIntegerField()
    a_b = models.CharField(max_length=200, choices={ 'A':'A', 'B':'B'})
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='house')
    status = models.CharField(max_length=200, choices={'POORER':'POORER', 'MIDDLE':'MIDDLE','RICH':'RICH'})
    people = models.PositiveIntegerField(blank=True, default=5)
    area_kv_m = models.DecimalField(decimal_places=2, max_digits=15, default=415.5)
    education_high = models.PositiveIntegerField(default=0, verbose_name="Oliy ta'lim olganlar")
    education_middle = models.PositiveIntegerField(default=0, verbose_name="O'rta ta'lim olganlar")
    no_education = models.PositiveIntegerField(default=0, verbose_name="Ta'lim olmaganlar")
    electricity_available = models.BooleanField(default=False, verbose_name="Elektr energiyasi mavjudligi")
    water_available = models.BooleanField(default=False, verbose_name="Suv ta'minoti mavjudligi")
    gas_available = models.BooleanField(default=False, verbose_name="Gaz ta'minoti mavjudligi")
    change_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.house_number} {self.a_b}"

    class Meta:
        ordering = ['house_number', 'a_b']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Status(models.TextChoices):
    KINDERGARTEN = 'Kindergarten'
    SCHOOLBOY = 'Schoolboy'
    STUDENT = 'Student'
    WORKER = 'Worker'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Human(BaseModel):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    email = models.EmailField(default='example@mail.ru')
    BIO = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    status = models.CharField(max_length=200, choices=Status.choices)
    information = models.CharField(max_length=200, choices=InformationLevel.choices, default=InformationLevel.NO)
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, related_name='human')
    working_hours_per_week = models.PositiveIntegerField(default=0, verbose_name="Haftalik ish soatlari")
    gender_distribution = models.CharField(max_length=50, choices={'MALE':'MALE', 'FEMALE':'FEMALE'}, verbose_name="Jins")
    living_space_per_person = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Uyda har bir a'zoga to'g'ri keladigan maydon (m²)")
    change_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']


   