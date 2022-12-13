
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

# Constance settings

defEmailBody = """
Geachte heer/mevrouw {0},

Dit is een afspraakbevestiging van Stichting Duurzaam Woerden, wij hebben u op {1} ingeplanned voor een bezoek met een van onze energiecoaches.
Tijdens dit coachgesprek zal er een zgn "woningtour" plaatsvinden waarbij u samen met de energiecoach('s) door de woning gaat om vast te stellen waar eventueel besparingen te verwezelijken zijn en wat de staat is van de isolatie van het huis.
Het coachgesprek wordt gevoerd door {2}, hierbij kan eventueel een extra "collega energiecoach" (in opleiding) aanwezig zijn.

Wij hopen u hierbij voldoende geinformeerd te hebben, en zien u graag bij het komende coachgesprek.

Mocht u verhinderd zijn op de aangegeven datum, dan kunt u dat doorgeven via het volgende e-mail adres:
energiecoach@duurzaamwoerden.nl
(U kunt desgewenst deze e-mail beantwoorden)

Met vriendelijke groet,

Stichting Duurzaam Woerden.
"""

CONSTANCE_CONFIG = {
    'BEVESTIGINGSMAIL_BODY': (defEmailBody, 'E-mail bevestiging body', str),
    'SITE_TITLE': ('ProfSoft Academy', 'Titel van de website', str),
    'SITE_BACKGROUNDCOLOR': ('#b9d0ed', 'Achtergrondkleur van de website', str),

}