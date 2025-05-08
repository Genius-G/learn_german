# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.10.19"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # 🔄 Schleifen

        Wir wollen lernen, wie Python uns hilft, Aufgaben mit Schleifen effizient zu wiederholen.

        Eine „Schleife“ ist eine Möglichkeit, einen Codeblock mehrmals auszuführen. Python hat zwei 
        Haupttypen von Schleifen:

        ```python
        # For-Schleife: wenn man weiß, wie oft man wiederholen muss
        for i in range(5):
            print(i)

        # While-Schleife: wenn man nicht weiß, wie viele Wiederholungen
        while Bedingung:
            do_something()
        ```

        Beginnen wir mit einer einfachen Liste, um Schleifen zu untersuchen. Du kannst diese Liste beliebig verändern und sehen, wie sich die nachfolgenden Ausgaben ändern.
        """
    )
    return


@app.cell
def _():
    sample_fruits = ["apple", "banana", "orange", "grape"]
    return (sample_fruits,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Die for-Schleife

        Die for-Schleife ist perfekt für die Iteration über Sequenzen.
        Versuche die obige Liste „sample_fruits“ zu ändern und achte darauf, wie sich die Ausgabe ändert.
        """
    )
    return


@app.cell
def _(sample_fruits):
    for _fruit in sample_fruits:
        print(f"I like {_fruit}s!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### Ermitteln der Position eines Eintrags

        Wenn Sie sowohl das Element als auch seine Position benötigen, verwenden Sie „enumerate()“:
        """
    )
    return


@app.cell
def _(sample_fruits):
    for _idx, _fruit in enumerate(sample_fruits):
        print(f"{_idx + 1}. {_fruit}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### Iterieren über eine range (Bereich) von Zahlen

        range() ist eine leistungsfähige Funktion zur Erzeugung von Zahlenfolgen:
        """
    )
    return


@app.cell
def _():
    print("range(5):", list(range(5)))
    print("range(2, 5):", list(range(2, 5)))
    print("range(0, 10, 2):", list(range(0, 10, 2)))
    return


@app.cell
def _():
    for _i in range(5):
        print(_i)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Die „while“-Schleife

        While-Schleifen werden so lange fortgesetzt, wie eine Bedingung `True` ist.
        """
    )
    return


@app.cell
def _():
    _count = 0
    while _count < 5:
        print(f"The count is {_count}")
        _count += 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Kontrolle der Schleifenausführung

        Python bietet mehrere Möglichkeiten, die Ausführung von Schleifen zu steuern:

        - `break`: die Schleife sofort verlassen

        - `continue`: zur nächsten Iteration übergehen

        Diese können sowohl mit `for`- als auch mit `while`-Schleifen verwendet werden.
        """
    )
    return


@app.cell
def _():
    for _i in range(1, 6):
        if _i == 4:
            print("Aus der Schleife ausbrechen.")
            break
        print(_i)
    return


@app.cell
def _():
    for _i in range(1, 6):
        if _i == 3:
            continue
        print(_i)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Praktische Schleifenmuster

        Hier sind einige gängige Muster, die du mit Schleifen verwenden kannst:

        ```python
        ## Muster 1: Akkumulator
        value = 0
        for num in [1, 2, 3, 4, 5]:
            value += num

        # Muster 2: Suche
        found = False
        for item in items:
            if condition:
                found = True
                break

        # Muster 3: Filter
        filtered = []
        for item in items:
            if condition:
                filtered.append(item)
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Nächste Schritte

        Lies die offiziellen [Python-Dokumente zu Schleifen und Kontrollfluss] (https://docs.python.org/3/tutorial/controlflow.html).
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
