# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.10.19"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # 📦 Sammlungen

        Eine „Sammlung“ ist eine Art von Variable, die mehrere Werte enthält.

        ## Listen
        Listen sind geordnete, veränderbare Sequenzen. Sie werden mit eckigen Klammern erstellt:

        ```python
        Früchte = [„Apfel“, „Banane“, „Orange“]
        Zahlen = [1, 2, 3, 4, 5]
        gemischt = [1, „hallo“, 3.14, Wahr]
        ```

        Im Folgenden findest du eine Beispielauflistung, mit der wir die Operationen erkunden wollen
        """
    )
    return


@app.cell
def _():
    sample_list = [1, 2, 3, 4, 5]
    return (sample_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Listenoperationen

        Hier sind allgemeine Operationen, die du mit Listen durchführen kannst.

        Versuche die Werte in `sample_list` oben zu ändern und beobachte, wie sich die Ergebnisse ändern.
        """
    )
    return


@app.cell
def _(sample_list):
    len(sample_list)  # Länge der Liste
    return


@app.cell
def _(sample_list):
    extended_list = sample_list + [6]  # Zwei Listen miteinander verknüpfen
    extended_list
    return (extended_list,)


@app.cell
def _(extended_list):
    extended_list[0]  # Zugriff auf das erste Element
    return


@app.cell
def _(extended_list):
    extended_list[-1]  # Zugriff auf das letzte Element
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Tupel

        Tupel sind unveränderliche Sequenzen. Sie sind wie Listen, die nach der Erstellung nicht mehr geändert werden können:
        """
    )
    return


@app.cell
def _():
    coordinates = (10, 20)
    return (coordinates,)


@app.cell
def _(coordinates):
    x, y = coordinates  # Entpacken von Tupeln
    x
    return x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md("""#### Tupel-Verkettung""")
    return


@app.cell
def _():
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)

    tuple3 = tuple1 + tuple2
    tuple3
    return tuple1, tuple2, tuple3


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Dictionaries (Wörterbuch)

        Dictionaries speichern Schlüssel-Werte-Paare. Sie sind perfekt für die Abbildung von Beziehungen:
        """
    )
    return


@app.cell
def _():
    person = {"name": "Max Mustermann", "age": 25, "city": "Berlin"}
    return (person,)


@app.cell
def _(person):
    person["name"]  # Zugriff auf Wert nach Schlüssel
    return


@app.cell
def _(person):
    person.keys()  # Alle Schlüssel abrufen
    return


@app.cell
def _(person):
    person.values()  # Alle Werte abrufen
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Sets (Mengen)

        Sets sind ungeordnete Sammlungen von eindeutigen Elementen:
        """
    )
    return


@app.cell
def _():
    numbers_set = {1, 2, 3, 3, 2, 1}  # Duplikate werden entfernt.
    return (numbers_set,)


@app.cell
def _(numbers_set):
    numbers_set | {4}  # Ein neues Element hinzufügen
    return


@app.cell
def _():
    {1, 2, 3} & {3, 4, 5}  # Gemeinsame Elemente finden
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Methoden und Operationen von Sammlungen

        Hier sind einige allgemeine Operationen für Sammlungen:

        ```python
        ## Listen
        meine_liste = [1, 2, 3]
        my_list.insert(0, 0) # An Position einfügen
        my_list.remove(2) # Erstes Vorkommen entfernen
        my_list.sort() # An Ort und Stelle sortieren
        sortierte_liste = sortiert(meine_liste) # Neue sortierte Liste zurückgeben

        # Dictionaries
        my_dict = {„a“: 1}
        my_dict.update({„b“: 2}) # Neue Schlüssel-Werte-Paare hinzufügen
        my_dict.get(„c“, „Nicht gefunden“) # Sicherer Zugriff mit Standard

        # Sets
        set_a = {1, 2, 3}
        set_b = {3, 4, 5}
        set_a.union(set_b) # Mengen kombinieren
        set_a.difference(set_b) # Elemente in A, aber nicht in B
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Dokumentation

        Ausführlichere Informationen finden Sie im offiziellen [Python-Tutorial über Datenstrukturen] (https://docs.python.org/3/tutorial/datastructures.html).
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
