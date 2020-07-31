import scipy.stats

import pandas as pd
import numpy as np


###############################################################################
# Constants
###############################################################################
PHYLUM_CO_LIST = [
    "phylum_Actinobacteria",
    "phylum_Bacteroidetes",
    "phylum_Firmicutes",
    "phylum_Proteobacteria",
    "phylum_Verrucomicrobia",
    "phylum_unclassified_Bacteria",
]
CLASS_CO_LIST = [
    "class_Actinobacteria",
    "class_Bacilli",
    "class_Bacteroidia",
    "class_Betaproteobacteria",
    "class_Clostridia",
    "class_Deltaproteobacteria",
    "class_Erysipelotrichia",
    "class_Gammaproteobacteria",
    "class_Negativicutes",
    "class_Verrucomicrobiae",
    "class_unclassified_Bacteria",
    "class_unclassified_Firmicutes",
]
ORDER_CO_LIST = [
    "order_Bacteroidales",
    "order_Burkholderiales",
    "order_Clostridiales",
    "order_Coriobacteriales",
    "order_Desulfovibrionales",
    "order_Enterobacteriales",
    "order_Erysipelotrichales",
    "order_Lactobacillales",
    "order_Selenomonadales",
    "order_Verrucomicrobiales",
    "order_unclassified_Bacteria",
    "order_unclassified_Firmicutes",
]
FAMILY_CO_LIST = [
    "family_Acidaminococcaceae",
    "family_Bacteroidaceae",
    "family_Clostridiaceae.1",
    "family_Clostridiales_Incertae.Sedis.XIII",
    "family_Coriobacteriaceae",
    "family_Desulfovibrionaceae",
    "family_Enterobacteriaceae",
    "family_Erysipelotrichaceae",
    "family_Lachnospiraceae",
    "family_Peptostreptococcaceae",
    "family_Porphyromonadaceae",
    "family_Prevotellaceae",
    "family_Rikenellaceae",
    "family_Ruminococcaceae",
    "family_Streptococcaceae",
    "family_Sutterellaceae",
    "family_Veillonellaceae",
    "family_Verrucomicrobiaceae",
    "family_unclassified_Bacteria",
    "family_unclassified_Clostridiales",
    "family_unclassified_Firmicutes",
]
GENUS_CO_LIST = [
    "genus_Akkermansia",
    "genus_Alistipes",
    "genus_Anaerotruncus",
    "genus_Anaerovorax",
    "genus_Bacteroides",
    "genus_Barnesiella",
    "genus_Bilophila",
    "genus_Blautia",
    "genus_Butyricicoccus",
    "genus_Butyricimonas",
    "genus_Clostridium.IV",
    "genus_Clostridium.XI",
    "genus_Clostridium.XVIII",
    "genus_Clostridium.XlVa",
    "genus_Clostridium.XlVb",
    "genus_Clostridium.sensu.stricto",
    "genus_Collinsella",
    "genus_Coprococcus",
    "genus_Dorea",
    "genus_Eggerthella",
    "genus_Erysipelotrichaceae_incertae_sedis",
    "genus_Faecalibacterium",
    "genus_Flavonifractor",
    "genus_Holdemania",
    "genus_Lachnospiracea_incertae_sedis",
    "genus_Odoribacter",
    "genus_Oscillibacter",
    "genus_Parabacteroides",
    "genus_Parasutterella",
    "genus_Phascolarctobacterium",
    "genus_Prevotella",
    "genus_Pseudoflavonifractor",
    "genus_Roseburia",
    "genus_Ruminococcus",
    "genus_Streptococcus",
    "genus_Veillonella",
    "genus_unclassified_Bacteria",
    "genus_unclassified_Clostridiales",
    "genus_unclassified_Clostridiales_Incertae.Sedis.XIII",
    "genus_unclassified_Coriobacteriaceae",
    "genus_unclassified_Erysipelotrichaceae",
    "genus_unclassified_Firmicutes",
    "genus_unclassified_Lachnospiraceae",
    "genus_unclassified_Porphyromonadaceae",
    "genus_unclassified_Ruminococcaceae",
]
CORR_METHOD = "pearson"
INPUT = "/app/data/gut_16s_abundance.csv"
###############################################################################
# Functions
###############################################################################


def main():

    # Create Dataframes
    phylum_df = pd.read_csv(INPUT, usecols=PHYLUM_CO_LIST)
    class_df = pd.read_csv(INPUT, usecols=CLASS_CO_LIST)
    order_df = pd.read_csv(INPUT, usecols=ORDER_CO_LIST)
    family_df = pd.read_csv(INPUT, usecols=FAMILY_CO_LIST)
    genus_df = pd.read_csv(INPUT, usecols=GENUS_CO_LIST)

    df_list = [phylum_df, class_df, order_df, family_df, genus_df]

    # Correlation test for each data frame
    for df in df_list:
        print(df.corr(method=CORR_METHOD))


if __name__ == "__main__":
    main()
