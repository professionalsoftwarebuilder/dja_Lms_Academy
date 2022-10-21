# from django.db import models
#
#
# def CheckForNone(theStr):
#     if theStr is None:
#         return ''
#     else:
#         return theStr + ' '
#
#
# CNTHOEDANIGHEID_CHS = (
#     ('W', 'Bedrijf'),
#     ('H', 'Deskundige'),
# )
#
#
# # Acties die ondernomen moeten worden aangaande contact
# class Action(models.Model):
#     aci_Name = models.CharField('Naam', max_length=85)
#     aci_Descr = models.TextField('Omschrijving', blank=True, null=True)
#     aci_Status = models.CharField('Status', max_length=1, choices=ACTIESTATUS_CHS, blank=True, null=True, default='O')
#
#     def __str__(self):
#         return self.aci_Naam
#
#     class Meta:
#         verbose_name_plural = 'Acties'
#         #verbose_name = 'Activiteit, Project, Lezing, enz.'
#
#
#
# class Group(models.Model):
#     grp_GroupNm = models.CharField('Groep', max_length=45)
#     grp_Website = models.CharField('Website', help_text='Plak hier de url van website', max_length=240, blank=True, null=True)
#     grp_Notes = models.TextField('Notities', blank=True, null=True)
#     grp_Type = models.CharField('Type groep', max_length=1, choices=GROEP_CHS, blank=True, null=True, default='O')
#
#     def __str__(self):
#         return CheckForNone(self.grp_GroupNm)
#
#     class Meta:
#         verbose_name_plural = 'Organisaties, Instanties, Bedrijven, enz.'
#         verbose_name = 'Groep'
#
#
# class Contact(models.Model):
#     cnt_Groups = models.ManyToManyField(Group, blank=True, verbose_name='Groep(en)', help_text='Groepen waaronder dit contact valt; ')
#     cnt_Actions = models.ManyToManyField(Action, blank=True, verbose_name='Acties', help_text='Acties (open) te nemen mbt dit contact; ', related_query_name='acties_related')
#     cnt_FirstNm = models.CharField('Voornaam', max_length=45)
#     cnt_LastNm = models.CharField('Achternaam', max_length=65)
#     cnt_Insertion = models.CharField('Tussenvoegsel', max_length=15, blank=True, null=True)
#     cnt_Initials = models.CharField('Voorletters', max_length=10, blank=True, null=True)
#     cnt_Notes = models.TextField('Notities', blank=True, null=True)
#     cnt_Type = models.CharField('Type contact', max_length=1, choices=CNTHOEDANIGHEID_CHS, blank=True, null=True, default='W')
#
#     def __str__(self):
#         return CheckForNone(self.cnt_FirstNm) + CheckForNone(self.cnt_Initials) + CheckForNone(self.cnt_LastNm)
#
#     class Meta:
#         verbose_name_plural = 'Contacten'
#         ordering = ("cnt_AchterNm", "cnt_VoorNm")
#
#
