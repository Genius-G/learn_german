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
        # 🔄 Bedingte Logik

        In diesem Lernprogramm lernst du, wie du **Entscheidungen** in deinem Code treffen kannst, indem du
        Pythons bedingte Anweisungen verwenden.

        ## If-Anweisungen
        Die Grundlage der Entscheidungsfindung in Python:
        ```python
        if Bedingung:
            # Code, der ausgeführt wird, wenn die Bedingung wahr ist
        elif andere_Bedingung:
            # Code, der ausgeführt wird, wenn eine andere_Bedingung wahr ist
        else:
            # Code, der ausgeführt wird, wenn keine Bedingung wahr ist
        ```
        Schauen wir uns einige Beispiele an:
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""**Versuchen Sie es!** Versuchen Sie, den Wert von „42“ unten zu ändern und sehen Sie, wie sich die Ausgabe ändert.""")
    return


@app.cell
def _():
    number = 42
    return (number,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Vergleiche die Zahlen mit Operatoren wie

        - `>`
        - `>=`
        - `<`
        - `<=`
        - `==` (beachte die beiden Gleichheitszeichen!)
        """
    )
    return


@app.cell
def _(mo, number):
    if number > 42:
        result = "Größer als 42"
    elif number == 42:
        result = "Gleich 42!"
    else:
        result = "Kleiner als 42"
    mo.md(result)
    return (result,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Interaktive Entscheidungsfindung
        **Probiere es aus!** Ändere die untenstehenden Bedingungen und achte darauf, wie sich die Ergebnisse ändern:
        """
    )
    return


@app.cell(hide_code=True)
def _(mo, threshold, value):
    mo.hstack([value, threshold], justify="start")
    return


@app.cell(hide_code=True)
def _(mo):
    value = mo.ui.number(value=25, start=0, stop=100, label="Eine Nummer eingeben")
    threshold = mo.ui.slider(value=50, start=0, stop=100, label="Schwellenwert festlegen")
    return threshold, value


@app.cell(hide_code=True)
def _(mo, threshold, value):
    if value.value > threshold.value:
        decision = f"{value.value} größer ist als {threshold.value}"
    elif value.value == threshold.value:
        decision = f"{value.value} ist gleich {threshold.value}"
    else:
        decision = f"{value.value} ist kleiner als {threshold.value}"

    mo.hstack(
        [
            mo.md(f"**Entscheidung**: {decision}"),
            mo.md(
                f"**Schwelle überschritten? **: {'✅' if value.value >= threshold.value else '❌'}"
            ),
        ],
        justify="space-around",
    )
    return (decision,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Boolesche Operationen
        Python verwendet boolesche Operatoren, um Bedingungen zu kombinieren:

        - `und`: Beide Bedingungen müssen wahr sein

        - `oder`: Mindestens eine Bedingung muss wahr sein

        - nicht": Invertiert die Bedingung
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    _text = mo.md("""
        - Probieren Sie verschiedene Kombinationen von Alter und Ausweisstatus aus
        - Beachten Sie, dass beide Bedingungen wahr sein müssen, damit Sie wählen dürfen.
        - Experimentieren Sie mit Sonderfällen (genau 18, kein Ausweis usw.)
    """)
    mo.accordion({"💡 Experimentiertipps": _text})
    return


@app.cell(hide_code=True)
def _(age, has_id, mo):
    mo.hstack([age, has_id], justify="start")
    return


@app.cell(hide_code=True)
def _(mo):
    age = mo.ui.number(value=18, start=0, stop=120, label="Alter")
    has_id = mo.ui.switch(value=True, label="Hat Ausweis")
    return age, has_id


@app.cell(hide_code=True)
def _(age, has_id, mo):
    can_vote = age.value >= 18 and has_id.value

    explanation = f"""
    ### Überprüfung der Wahlberechtigung

    Aktueller Status:

    - Alter: {age.value} Jahre alt

    - Hat Ausweis: {"Ja" if has_id.value else "Nein"}

    - Kann wählen gehen: {"Ja ✅" if can_vote else "Nein ❌"}

    Grund: {
        "Alters- und Ausweisvoraussetzungen erfüllt"
        if can_vote
        else "Kein " + ("erforderliches Alter erreicht" if age.value < 18 else "gültiger Ausweis")
    }
    """

    mo.md(explanation)
    return can_vote, explanation


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Probiere es aus!** Schreibe Python-Code, der berechnet, ob eine Person wählen darf.""")
    return


@app.cell
def _():
    my_age = 18
    return (my_age,)


@app.cell
def _():
    has_an_id = False
    return (has_an_id,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Komplexe Bedingungen
        Kombiniere mehrere Bedingungen für eine komplexere Logik:
        ```python
        ## Mehrere Bedingungen
        if (age >= 18 and has_id) or has_special_permission:
            print(„Zugriff gewährt“)

        # Verschachtelte Bedingungen
        if age >= 18:
            if has_id:
                print(„Voller Zugang“)
            else:
                print(„Eingeschränkter Zugang“)
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(humidity, mo, temp, wind):
    mo.hstack([temp, humidity, wind])
    return


@app.cell(hide_code=True)
def _(mo):
    temp = mo.ui.number(value=25, start=-20, stop=50, label="Temperatur (°C)")
    humidity = mo.ui.slider(value=60, start=0, stop=100, label="Luftfeuchtigkeit (%)")
    wind = mo.ui.number(value=10, start=0, stop=100, label="Windstärke (km/h)")
    return humidity, temp, wind


@app.cell(hide_code=True)
def _(humidity, mo, temp, wind):
    def get_weather_advice():
        conditions = []

        if temp.value > 30:
            conditions.append("🌡️ High Temperatur")
        elif temp.value < 10:
            conditions.append("❄️ Kalte Temperatur")

        if humidity.value > 80:
            conditions.append("💧 Hohe Luftfeuchtigkeit")
        elif humidity.value < 30:
            conditions.append("🏜️ Niedrige Luftfeuchtigkeit")

        if wind.value > 30:
            conditions.append("💨 Starker Wind")

        return conditions


    conditions = get_weather_advice()

    message = f"""
    ### Wetteranalyse

    Aktuelle Bedingungen:

    - Temperatur: {temp.value}°C

    - Luftfeuchtigkeit: {humidity.value}%

    - Windstärke: {wind.value} km/h

    Warnungen: {",".join(conditions) if conditions else "Keine Warnungen"}
    """

    mo.md(message)
    return conditions, get_weather_advice, message


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Nächste Schritte

    - Übe die Kombination mehrerer Bedingungen
    - Verschachtelte if-Anweisungen erforschen
    - Versuche deine eigenen komplexen Entscheidungsbäume zu erstellen

    Keep coding! 🎯✨
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
