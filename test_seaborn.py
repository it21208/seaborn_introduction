import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

global fmri

def seaborn_lineplot() -> None:
    fmri = sns.load_dataset("fmri")
    print(fmri.head())
    # sns.lineplot(x="timepoint", y="signal", hue="event", data=fmri)
    sns.lineplot(x="timepoint", y="signal", hue="event", style="event", markers=True, data=fmri)
    plt.show()


def seaborn_pokemon() -> None:
    sns.set(style="whitegrid")
    pokemon=pd.read_csv("pokemon.csv")
    print(pokemon.head())
    sns.barplot(x="Legendary", y="Speed", hue="Generation", data=pokemon, palette="Blues_d") # , color = "orange"
    plt.show()


def seaborn_iris() -> None:
    iris = pd.read_csv("iris.csv")
    print(iris.head())
    sns.scatterplot(x="sepal.length", y="petal.length", data=iris, hue = "petal.length")
    plt.show()


def seaborn_diamond() -> None:
    diamond=pd.read_csv("diamonds.csv")
    diamond.head()
    # sns.distplot(diamond["price"], color="green", bins=10, kde=False, vertical=True)
    sns.jointplot(x="sepal.length", y="petal.length", data=iris, color="olive", kind="reg")
    plt.show()


def seaborn_churn() -> None:
    churn = pd.read_csv("churn.csv")
    print(churn.head())
    # sns.boxplot(y="tenure", x="Churn", data=churn)
    sns.boxplot(y="Night Calls", x="Night Charge", data=churn, palette="Set1", linewidth=1, hue="Churn?")
    plt.show()


def seaborn_battle() -> None:
    battle = pd.read_csv("battles.csv")
    print(battle.head())
    # print(battle.shape())
    battle.rename(columns={'attacke_1':'primary_attacker'}, inplace=True)
    # attacker_king is a categorical column
    print(battle["attacker_king"].value_counts())
    print(battle["location"].value_counts()) 
    sns.set(rc={"figure.figsize":(13,5)})
    # sns.barplot(x="attacker_king", y="attacker_size", data=battle)
    # sns.barplot(x="defender_king", y="defender_size", data=battle)
    sns.countplot(x=battle['attacker_king'], hue = battle['battle_type'])
    plt.show()


def seaborn_character() -> None:
    character = pd.read_csv('character-death.csv')
    print(character.head(), character.shape())
    print(character["Nobility"].value_counts())
    sns.set(rc={'figure.figsize':(30,10)})
    sns.countplot(death['Allegiances'])
    plt.show



# seaborn_lineplot()
# seaborn_pokemon()
# seaborn_iris()
# seaborn_diamond()
# seaborn_churn()
# seaborn_battle()
seaborn_character()
