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
        # 🎭 Strings

        In diesem Notebook werden **Strings** vorgestellt, die Container für Text sind.

        ## Erstellen von Zeichenketten
        Erzeuge Zeichenketten, indem du Text in Anführungszeichen einschließt:

        ```python
        # Doppelte Anführungszeichen verwenden
        greeting = „Hallo, Python!“

        # oder einfache Anführungszeichen
        name = 'Alice'

        # oder dreifache Anführungszeichen
        mehrzeiliger_string = \„““
        Liebe Alice,
        schön, dich kennenzulernen.
        Mit freundlichen Grüßen,
        Bob.
        \„““
        ```

        Nachfolgend ein Beispielstring.
        """
    )
    return


@app.cell
def _():
    text = "Python ist erstaunlich!"
    text
    return (text,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Wesentliche String-Operationen

        Hier sind einige Methoden für die Arbeit mit Zeichenketten.

        Tipp: Versuche, den Wert von `text` oben zu ändern, und beobachte, wie sich die
        berechneten Werte unten ändern.
        """
    )
    return


@app.cell
def _(text):
    # Die Methode „len“ gibt die Anzahl der Zeichen in der Zeichenkette zurück.
    len(text)
    return


@app.cell
def _(text):
    text.upper()
    return


@app.cell
def _(text):
    text.lower()
    return


@app.cell
def _(text):
    text.title()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Verwende String-Methoden und den Operator „in“, um Dinge in Strings zu finden.""")
    return


@app.cell
def _(text):
    # Returns the index of "is" in the string
    text.find("in")
    return


@app.cell
def _(text):
    "Python" in text
    return


@app.cell
def _(text):
    "Javascript" in text
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Einfügen von Werten in Zeichenketten

        Modernes Python verwendet f-strings, um Werte in Zeichenketten einzufügen. Ein Beispiel,
        Sieh dir an, wie die nächste Zelle dich begrüßt (und beachte das `f''''`)!

        **Versuche es mal!** Gib deinen Namen in `my_name` unten ein, dann führe die Zelle aus.
        """
    )
    return


@app.cell
def _():
    my_name = ""
    return (my_name,)


@app.cell
def _(my_name):
    f"Hallo, {my_name}!"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Arbeiten mit Teilen von Zeichenketten
        Du kannst auf jeden Teil einer Zeichenkette über seine Position (Index) zugreifen:
        """
    )
    return


@app.cell
def _(text):
    first_letter = text[0]
    first_letter
    return (first_letter,)


@app.cell
def _(text):
    last_letter = text[-1]
    last_letter
    return (last_letter,)


@app.cell
def _(text):
    first_three = text[0:3]
    first_three
    return (first_three,)


@app.cell
def _(text):
    last_two = text[-2:]
    last_two
    return (last_two,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Andere hilfreiche String-Methoden

        Zum Schluss sind hier noch einige andere hilfreiche String-Methoden. Probiere ruhig an deinen eigenen Strings aus, indem du den Wert von `sentence` unten änderst.
        """
    )
    return


@app.cell
def _():
    sentence = "  python macht Spaß  "
    sentence
    return (sentence,)


@app.cell
def _(sentence):
    # Zusätzliche Leerzeichen entfernen
    sentence.strip()
    return


@app.cell
def _(sentence):
    # Aufteilung in eine Liste von Wörtern
    sentence.split()
    return


@app.cell
def _(sentence):
    sentence.replace("Spaß", "Freude")
    return


@app.cell
def _():
    "123".isdigit(), "abc".isdigit()
    return


@app.cell
def _():
    "123".isalpha(), "abc".isalpha()
    return


@app.cell
def _():
    "Python3".isalnum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Nächste Schritte

        Eine vollständige Einführung in Strings finden Sie in der [offiziellen Dokumentation] (https://docs.python.org/3/library/string.html).
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
