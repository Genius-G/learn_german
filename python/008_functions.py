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
        # 🧩 Funktionen

        In diesem Tutorium geht es um ein wichtiges Thema: **Funktionen.**

        Eine Funktion ist ein wiederverwendbarer Code-Block, ähnlich wie eine mathematische Funktion. Jede Funktion hat einen **Namen** und akzeptiert eine bestimmte Anzahl von **Argumenten**. Diese Argumente werden im „Körper“ der Funktion (ihrem Codeblock) verwendet, und jede Funktion kann Werte **zurückgeben**.

        **Beispiel** Nachfolgend findest eine Beispielfunktion.
        """
    )
    return


@app.cell
def _():
    def greet(your_name):
        return f"Hallo, {your_name}!"
    return (greet,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Das Schlüsselwort `def` leitet die Funktionsdefinition ein. Der **Name** der Funktion ist `greet`. Diese akzeptiert eine **Eingabe** namens `your_name`. Sie erzeugt dann eine Zeichenkette und **gibt** sie zurück.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        In der nächsten Zelle **rufen** wir die Funktion mit einem Wert auf und weisen ihren Rückgabewert einer Variablen zu.

        **Versuchen Sie es!** Versuchen Sie, die Eingabe für die Funktion zu ändern.
        """
    )
    return


@app.cell
def _(greet):
    greeting = greet(your_name="<Dein Name hier>")
    greeting
    return (greeting,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        **Warum Funktionen verwenden?** Funktionen helfen dir:

        - Komplexe Probleme aufzuschlüsseln
        - Wiederverwendbare Code-Blöcke zu erstellen
        - die Lesbarkeit des Codes zu verbessern
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Standardparameter
        Erhöhen Sie die Flexibilität Ihrer Funktionen, indem Sie Standardwerte vorgeben.
        """
    )
    return


@app.cell
def _():
    def create_profile(name, age=18):
        return f"{name} ist {age} Jahre alt"
    return (create_profile,)


@app.cell
def _(create_profile):
    # Example usage
    example_name = "Alex"
    example_profile = create_profile(example_name)
    example_profile
    return example_name, example_profile


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Du kannst auch Funktionen erstellen, die auf Variablen außerhalb des Funktionskörpers verweisen. Dies wird „Schließen über“ Variablen genannt""")
    return


@app.cell
def _():
    base_multiplier = 2

    def multiplier(x):
        """
        Erstelle eine Funktion, die die Eingabe mit einem Basiswert multipliziert.

        Dies demonstriert, wie Funktionen Werte 
        aus dem sie umgebenden Bereich übernehmen können.
        """
        return x * base_multiplier
    return base_multiplier, multiplier


@app.cell
def _(multiplier):
    print([multiplier(num) for num in [1, 2, 3]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Rückgabe mehrerer Werte

        Funktionen können mehrere Werte zurückgeben: Trenne einfach die zurückzugebenden Werte durch Kommata. In der nächsten Zelle findest du ein Beispiel.
        """
    )
    return


@app.cell
def _():
    def weather_analysis(temp):
        """
        Analysiert das Wetter anhand der Temperatur.

        Args:
            temp (float): Temperatur in Celsius

        Rückgabe:
            Tupel: Wetterstatus, Empfehlung, Warnstufe
        """
        if temp <= 0:
            return "Eiskalt", "Treage besser eine warme Jacke", "Hoch"
        elif 0 < temp <= 15:
            return "Kalt", "Warm anziehen", "Medium"
        elif 15 < temp <= 25:
            return "Mild", "Bequeme Klamotten", "Niedrig"
        else:
            return "Heiß", "Trink ausreichend Wasser", "Hoch"
    return (weather_analysis,)


@app.cell
def _():
    temperature = 25
    return (temperature,)


@app.cell
def _(temperature, weather_analysis):
    status, recommendation, warning_level = weather_analysis(temperature)
    status, recommendation, warning_level
    return recommendation, status, warning_level


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
