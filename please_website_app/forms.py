# -*- coding: utf-8 -*-

from django import forms
from django.utils.safestring import mark_safe


class SendSmsForm(forms.Form):
    phone_cta = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "phone-input",
                "placeholder": "06 07 08 09 10",
            }
        )
    )


class CandidateForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        label="Prénom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Hubert"
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        label="Nom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Bonisseur de La Bath"
            }
        )
    )

    phone = forms.CharField(
        required=True,
        label="Téléphone*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "0 117 117 117"
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label="Email*",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "hubert.dlb@oss.fr",
            }
        )
    )

    linkedin = forms.CharField(
        required=True,
        label="Lien vers votre profil LinkedIn*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "https://linkedin.com/noel-flantier",
            }
        )
    )

    message = forms.CharField(
        required=True,
        label="Votre message*",
        label_suffix="",
        widget=forms.Textarea(
            attrs={
                "class": "long-text-input",
                "placeholder": "Vous êtes bien OSS 117, le meilleur agent français ? Oui. Enfin, le meilleur... C' est pas à moi de le dire. Vous savez, comme je dis souvent...",
            }
        )
    )


class LeadForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre email",
            }
        )
    )

    zip_code = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre code postal",
            }
        )
    )


# APP SECTION

class CityManagerForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        label="Prénom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre prénom"
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        label="Nom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre nom"
            }
        )
    )

    phone = forms.CharField(
        required=True,
        label="Téléphone*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "06 07 08 09 10"
            }
        )
    )

    city = forms.CharField(
        required=True,
        label="Ville*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "La ville où vous souhaitez vous lancer"
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label="Email*",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "vous@mail.com",
            }
        )
    )

    password = forms.CharField(
        required=True,
        label="Mot de Passe*",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={
                "class": "text-input",
                "placeholder": "********",
            }
        )
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label="Email*",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "vous@mail.com",
            }
        )
    )

    password = forms.CharField(
        required=True,
        label="Password*",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={
                "class": "text-input",
                "placeholder": "********",
            }
        )
    )

class DeliveryManForm(forms.Form):

    first_name = forms.CharField(
        required=True,
        label="Prénom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Prénom",
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        label="Nom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Nom",
            }
        )
    )

    phone = forms.CharField(
        required=True,
        label="Téléphone*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "06 07 08 09 10",
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label="Email*",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "livreur@gmail.com",
            }
        )
    )

    auto = forms.ChoiceField(
        required=False,
        label="A-t-il un véhicule motorisé ?",
        label_suffix="",
        choices=(
            (True, 'Oui'),
            (False, 'Non')
        ),
        widget=forms.Select(
            attrs={
                "class": "text-input",
            }
        )
    )

    sent_to_bereglo = forms.ChoiceField(
        required=False,
        label=mark_safe("Est-il inscrit sur BeRéglo ? (<a href='https://bereglo.fr' target='_blank'>Découvrir BeRéglo</a>)"),
        label_suffix="",
        choices=(
            (True, 'Oui'),
            (False, 'Non')
        ),
        widget=forms.Select(
            attrs={
                "class": "text-input",
            }
        )
    )

    siret = forms.CharField(
        required=False,
        label="Son SIRET",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "812 456 457 0001",
            }
        )
    )


class MerchantForm(forms.Form):
    category_choices = (
        ("Restaurant", "Restaurant"),
        ("Fast Food", "Fast Food"),
        ("Bien-Etre & Beauté", "Bien-Etre & Beauté"),
        ("Boulangerie & Petit-Déjeuner", "Boulangerie & Petit-Déjeuner"),
        ("Epicerie de Quartier", "Epicerie de Quartier"),
        ("Epicerie Fine", "Epicerie Fine"),
        ("Course et Marché", "Course et Marché"),
        ("Gourmandises", "Gourmandises"),
        ("Service", "Service"),
    )

    first_name = forms.CharField(
        required=True,
        label="Prénom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Prénom",
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        label="Nom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Nom",
            }
        )
    )

    business_name = forms.CharField(
        required=True,
        label="Nom du Commerce*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Nom",
            }
        )
    )

    business_type = forms.ChoiceField(
        required=True,
        label="Type de commerce*",
        label_suffix="",
        choices=category_choices,
        widget=forms.Select(
            attrs={
                "class": "text-input",
            }
        )
    )

    phone = forms.CharField(
        required=False,
        label="Téléphone",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "06 07 08 09 10",
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label="Email*",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "commerce@gmail.com",
            }
        )
    )

    interested = forms.ChoiceField(
        required=True,
        label="Semble intéressé(e) ?*",
        label_suffix="",
        choices=(
            ('Pas intéressé(e)', 'Pas intéressé(e)'),
            ('Mitigé(e)', 'Mitigé(e)'),
            ('Intéressé(e)', 'Intéressé(e)'),
            ('Très intéressé(e)', 'Très intéressé(e)'),
        ),
        widget=forms.Select(
            attrs={
                "class": "text-input",
            }
        )
    )

    competition = forms.ChoiceField(
        required=True,
        label="Travaille déjà avec la concurrence ?*",
        label_suffix="",
        choices=(
            (True, 'Oui'),
            (False, 'Non'),
        ),
        widget=forms.Select(
            attrs={
                "class": "text-input",
            }
        )
    )

    delivery = forms.ChoiceField(
        required=True,
        label="Livre-t-il déjà ?*",
        label_suffix="",
        choices=(
            (True, 'Oui'),
            (False, 'Non'),
        ),
        widget=forms.Select(
            attrs={
                "class": "text-input",
            }
        )
    )


#CONTACT SECTION

class ContactForm(forms.Form):

    first_name = forms.CharField(
        required=True,
        label="Prénom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre prénom"
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        label="Nom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre nom"
            }
        )
    )

    phone = forms.CharField(
        required=True,
        label="Téléphone*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "06 07 08 09 10"
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label="Email*",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "vous@mail.com"
            }
        )
    )

    message = forms.CharField(
        required=True,
        label="Votre message*",
        label_suffix="",
        widget=forms.Textarea(
            attrs={
                "class": "long-text-input",
                "placeholder": ""
            }
        )
    )


class ContactFormCm(forms.Form):

    first_name = forms.CharField(
        required=True,
        label="Prénom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre prénom"
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        label="Nom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre nom"
            }
        )
    )

    city = forms.CharField(
        required=True,
        label="Ville*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Paris"
            }
        )
    )

    phone = forms.CharField(
        required=True,
        label="Téléphone*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "06 07 08 09 10"
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label="Email*",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "vous@mail.com"
            }
        )
    )

    message = forms.CharField(
        required=True,
        label="Votre message*",
        label_suffix="",
        widget=forms.Textarea(
            attrs={
                "class": "long-text-input",
                "placeholder": ""
            }
        )
    )


class ContactFormDeliveryMan(forms.Form):

    first_name = forms.CharField(
        required=True,
        label="Prénom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre prénom"
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        label="Nom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre nom"
            }
        )
    )

    phone = forms.CharField(
        required=True,
        label="Téléphone*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "06 07 08 09 10"
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label="Email*",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "vous@mail.com"
            }
        )
    )

    city = forms.CharField(
        required=True,
        label="Ville*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Paris"
            }
        )
    )

    message = forms.CharField(
        required=True,
        label="Votre message*",
        label_suffix="",
        widget=forms.Textarea(
            attrs={
                "class": "long-text-input",
                "placeholder": ""
            }
        )
    )


class ContactFormCity(forms.Form):

    first_name = forms.CharField(
        required=True,
        label="Prénom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre prénom"
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        label="Nom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre nom"
            }
        )
    )

    phone = forms.CharField(
        required=True,
        label="Téléphone*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "06 07 08 09 10"
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label="Email*",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "vous@mail.com"
            }
        )
    )

    city = forms.CharField(
        required=True,
        label="Ville*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Paris"
            }
        )
    )

    position = forms.CharField(
        required=True,
        label="Votre rôle*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Adjoint(e) au Commerce"
            }
        )
    )

    message = forms.CharField(
        required=True,
        label="Votre message*",
        label_suffix="",
        widget=forms.Textarea(
            attrs={
                "class": "long-text-input",
                "placeholder": ""
            }
        )
    )


class ContactFormMerchant(forms.Form):

    first_name = forms.CharField(
        required=True,
        label="Prénom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre prénom"
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        label="Nom*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Votre nom"
            }
        )
    )

    phone = forms.CharField(
        required=True,
        label="Téléphone*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "06 07 08 09 10"
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label="Email*",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={
                "class": "text-input",
                "placeholder": "vous@mail.com"
            }
        )
    )

    city = forms.CharField(
        required=True,
        label="Ville*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Paris"
            }
        )
    )

    business_name = forms.CharField(
        required=True,
        label="Nom de votre commerce*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Le Beau Commerce"
            }
        )
    )

    siret = forms.CharField(
        required=True,
        label="SIRET*",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "812 345 678 00011"
            }
        )
    )

    message = forms.CharField(
        required=True,
        label="Votre message*",
        label_suffix="",
        widget=forms.Textarea(
            attrs={
                "class": "long-text-input",
                "placeholder": ""
            }
        )
    )


# APP FORMS
class ProjectForm(forms.Form):

    apport = forms.IntegerField(
        required=True,
        label="Votre apport personnel (€)*",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "15000",
            }
        )
    )

    project = forms.CharField(
        required=True,
        label="Parlez-nous de votre projet*",
        label_suffix="",
        widget=forms.Textarea(
            attrs={
                "class": "long-text-input",
                "placeholder": "Dites-nous en plus !"
            }
        )
    )


class CityForm(forms.Form):

    area = forms.CharField(
        required=False,
        label="Zone Géographique",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Ma ville et sa région",
            }
        )
    )

    inhabitants = forms.IntegerField(
        required=False,
        label="Nombre d'habitants",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "28000",
            }
        )
    )

    density = forms.FloatField(
        required=False,
        label="Densité d'habitants au km2",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "496",
            }
        )
    )

    main_housing_rate = forms.FloatField(
        required=False,
        label="Taux de résidence principale (%)",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "75,8",
            }
        )
    )

    unemployment = forms.FloatField(
        required=False,
        label="Taux de chômage (%)",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "8,5",
            }
        )
    )

    activity = forms.FloatField(
        required=False,
        label="Taux d'activité des 18-64 ans (%)",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "8,5",
            }
        )
    )

    net_salary_average = forms.FloatField(
        required=False,
        label="Revenus net médian (€)",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "1999,99",
            }
        )
    )

    restaurants = forms.IntegerField(
        required=False,
        label="Nombre de restaurants & fast-food",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "200",
            }
        )
    )

    bakeries = forms.IntegerField(
        required=False,
        label="Nombre de boulangeries",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "200",
            }
        )
    )

    shops_food = forms.IntegerField(
        required=False,
        label="Nombre de commerces de bouche (épiceries, primeurs, boucheries, fromagers, producteurs locaux,...)",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "200",
            }
        )
    )

    shops_service = forms.IntegerField(
        required=False,
        label="Nombre de commerces de services (pressing, laverie, ménage, ...)",
        label_suffix="",
        widget=forms.NumberInput(
            attrs={
                "class": "text-input",
                "placeholder": "200",
            }
        )
    )

    competition = forms.CharField(
        required=False,
        label="Concurrence",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "Just Eat...",
            }
        )
    )


class CurriculumForm(forms.Form):

    curriculum = forms.CharField(
        required=True,
        label="Parlez-nous de votre parcours*",
        label_suffix="",
        widget=forms.Textarea(
            attrs={
                "class": "long-text-input",
                "placeholder": "Dites-nous en plus !"
            }
        )
    )

    AVAILABILITY_CHOICES = (
        (1, 'Immédiate'),
        (2, 'Dans les 1 à 3 mois'),
        (3, 'Dans les 3 à 6 mois'),
        (4, 'Dans plus de 6 mois'),
    )

    availability = forms.ChoiceField(
        required=True,
        label="Dites-nous quand vous êtes disponible !*",
        label_suffix="",
        choices=AVAILABILITY_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "text-input",
                "placeholder": "Vous êtes disponible ?"
            }
        ),
    )

    linkedin = forms.CharField(
        required=False,
        label="Lien vers votre profil LinkedIn",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "text-input",
                "placeholder": "https://linkedin.com/noel-flantier",
            }
        )
    )
