import json
from django.core.management.base import BaseCommand
from www.models import (
    sportSite,
    Typo,
    Denomination,
    DateReference,
    site
)

class Command(BaseCommand):
    help = "Importe les sportSite depuis un fichier JSON"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str)

    def handle(self, *args, **kwargs):
        json_file = kwargs["json_file"]

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            # 🔹 ForeignKey site_olympique
            site_olympique = None
            if item.get("site_olympique"):
                site_olympique, _ = site.objects.get_or_create(
                    name=item["site_olympique"]
                )

            # 🔹 Création du sportSite
            sport_site = sportSite.objects.create(
                departement=item["departement"],
                commune=item["commune"],
                adresse=item["adresse"],
                code_postal=item["code_postal"],
                longitude=float(item["longitude"]),
                latitude=float(item["latitude"]),
                informations_d_acces_en_transport_en_commun=item.get(
                    "informations_d_acces_en_transport_en_commun", ""
                ),
                appellation=item["appellation"],
                datation=item.get("datation", ""),
                periode_de_construction=item.get(
                    "periode_de_construction", ""
                ),
                historique_et_description=item.get(
                    "historique_et_description", ""
                ),
                credits=item.get("credits", ""),
                url_image=item.get("url_image", ""),
                adresse_com=item.get("adresse_com", ""),
                site_olympique=site_olympique,
            )

            # 🔹 ManyToMany : Typologie
            for typo_name in item.get("typologie", []):
                typo, _ = Typo.objects.get_or_create(name=typo_name)
                sport_site.typologie.add(typo)

            # 🔹 ManyToMany : Denomination
            for denom_name in item.get("denomination", []):
                denom, _ = Denomination.objects.get_or_create(name=denom_name)
                sport_site.denomination.add(denom)

            # 🔹 ManyToMany : DateReference
            for date_ref in item.get("date_s_de_reference", []):
                date_obj, _ = DateReference.objects.get_or_create(name=date_ref)
                sport_site.date_s_de_reference.add(date_obj)

            self.stdout.write(
                self.style.SUCCESS(f"Importé : {sport_site.appellation}")
            )

        self.stdout.write(self.style.SUCCESS("✅ Import terminé"))
