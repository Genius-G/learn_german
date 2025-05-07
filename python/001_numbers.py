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
        # 🔢 Zahlen

        
        Dieses Lernprogramm gibt einen kurzen Überblick über die Arbeit mit Zahlen.

        ## Zahlentypen

        Python hat mehrere Arten von Zahlen:

        ```python
        integer = 42 # ganze Zahlen (int)
        decimal = 3.14 # Fließkommazahlen (float)
        complex_num = 2 + 3j # komplexe Zahlen
        ```

        Im Folgenden findest du ein Zahlenbeispiel, mit dem wir die Operationen erkunden können.
        """
    )
    return


@app.cell
def _():
    number = 42
    return (number,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Mathematische Grundoperationen

        Python unterstützt alle mathematischen Standardoperationen.

        Versuche den Wert von `number` oben zu ändern und beobachte, wie sich die Ergebnisse ändern.
        """
    )
    return


@app.cell
def _(number):
    number + 10  # Addition
    return


@app.cell
def _(number):
    number - 5  # Subtraktion
    return


@app.cell
def _(number):
    number * 3  # Multiplikation
    return


@app.cell
def _(number):
    number / 2  # Division (gibt immer einen float zurück)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Python hat weitere Versionen von Division und Exponentiation.""")
    return


@app.cell
def _(number):
    number // 5  # Division (rundet ab)
    return


@app.cell
def _(number):
    number % 5  # Modulo (Teilen mit Rest)
    return


@app.cell
def _(number):
    number**2  # Exponentiation
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Typumwandlung

        Du kannst zwischen verschiedenen Zahlentypen konvertieren. Versuche diese Werte zu ändern!
        """
    )
    return


@app.cell
def _():
    decimal_number = 3.14
    return (decimal_number,)


@app.cell
def _(decimal_number):
    int(decimal_number)  # In Ganzzahl umwandeln (schneidet den Dezimalteil ab)
    return


@app.cell
def _(number):
    float(number)  # Umwandlung in „Float“ oder Dezimalwert
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Eingebaute mathematische Funktionen
        Python bietet viele nützliche eingebaute Funktionen für die Arbeit mit Zahlen:
        """
    )
    return


@app.cell
def _(number):
    abs(-number)  # Betrag einer Zahl
    return


@app.cell
def _():
    round(3.14159, 2)  # Auf 2 Nachkommastellen runden
    return


@app.cell
def _():
    max(1, 5, 3, 7, 2)  # Bestimme das Maximum
    return


@app.cell
def _():
    min(1, 5, 3, 7, 2)  # Bestimme das Minimum
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Erweiterte Operationen

        Für komplexere mathematische Operationen verwende das [math-Modul] von Python (https://docs.python.org/3/library/math.html).
        """
    )
    return


@app.cell
def _():
    import math
    return (math,)


@app.cell
def _(math):
    math.sqrt(16)
    return


@app.cell
def _(math):
    math.sin(math.pi/2)
    return


@app.cell
def _(math):
    math.cos(0)
    return


@app.cell
def _(math):
    math.pi, math.e
    return


@app.cell
def _(math):
    math.log10(100)
    return


@app.cell
def _(math):
    math.log(math.e)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Nächste Schritte:

    - Verschiedene mathematische Operationen üben
    - Experimentieren Sie mit Typkonvertierungen
    - Probieren Sie die Funktionen des mathematischen Moduls aus

    Rechnen Sie weiter! 🧮✨
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
