from django.db import models

# Create your models here.
class churn(models.Model):	
    GENDER_CHOICES = (
		('Male', 'Homme'),
		('Female', 'Femme')
	)
    SENIOR_CITIZEN_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non')
	)
    PARTNER_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non')
	)
    Dependents_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non')
	)
    Phone_Service_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non')
	)
    Multiple_Lines_CHOICES = (
		('Fiber optic', 'Fibre Optique'),
		('Non', 'Non'),
        ('No phone service', 'Pas de service Téléphonique')
	)
    Internet_Service_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non'),
        ('No phone service', 'Pas de service Téléphonique')
	)
    Online_Security_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non'),
        ('No phone service', 'Pas de service Téléphonique')
	)
    Online_Backup_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non'),
        ('No phone service', 'Pas de service Téléphonique')
	)
    Device_Protection_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non'),
        ('No phone service', 'Pas de service Téléphonique')
	)
    Tech_Support_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non'),
        ('No phone service', 'Pas de service Téléphonique')
	)
    Streaming_TV_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non'),
        ('No phone service', 'Pas de service Téléphonique')
	)
    Streaming_Movies_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non'),
        ('No phone service', 'Pas de service Téléphonique')
	)
    Contract_CHOICES = (
		('Month-to-month', 'Par Mois'),
		('One year', 'Par An'),
        ('Two year', 'Sur 2 ans')
	)
    Paperless_Billing_CHOICES = (
		('Yes', 'Oui'),
		('Non', 'Non')
	)
    Payment_Method_CHOICES = (
		('Bank transfer (automatic)', 'Transfere Banquaire'),
		('Mailed check', 'Non'),
        ('Credit card (automatic)','Carte de credit'),
        ('Electronic check','Cheque Electronique')
	)	

    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    gender=models.CharField(max_length=15,choices=GENDER_CHOICES)
    seniorCitizen=models.CharField(max_length=15,choices=SENIOR_CITIZEN_CHOICES)
    partner=models.CharField(max_length=15,choices=PARTNER_CHOICES)
    dependents=models.CharField(max_length=15,choices=Dependents_CHOICES)
    tenureMonths=models.FloatField(default=0.0)
    phoneService=models.CharField(max_length=30,choices=Phone_Service_CHOICES)
    multipleLines=models.CharField(max_length=30,choices=Multiple_Lines_CHOICES)
    internetService=models.CharField(max_length=30,choices=Internet_Service_CHOICES)    
    onlineSecurity=models.CharField(max_length=30,choices=Online_Security_CHOICES) 
    onlineBackup=models.CharField(max_length=30,choices=Online_Backup_CHOICES)   
    deviceProtection=models.CharField(max_length=30,choices=Device_Protection_CHOICES)   
    techSupport=models.CharField(max_length=30,choices=Tech_Support_CHOICES)    
    streamingTv=models.CharField(max_length=30,choices=Streaming_TV_CHOICES)    
    streamingMovies=models.CharField(max_length=30,choices=Streaming_Movies_CHOICES)    
    contract=models.CharField(max_length=30,choices=Contract_CHOICES)    
    paperlessBilling=models.CharField(max_length=30,choices=Paperless_Billing_CHOICES)
    paymentMethod=models.CharField(max_length=30,choices=Payment_Method_CHOICES)  
    monthlyCharges=models.FloatField(default=0.0) 
    totalCharges=models.FloatField(default=0.0)
	
    def __str__(self):
        return '{}, {}'.format(self.lastname, self.firstname)