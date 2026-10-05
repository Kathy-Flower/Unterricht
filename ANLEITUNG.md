# Diagnosetest online – Anleitung

Der Test liegt in `index.html`. GitHub Pages zeigt die Seite an, kann aber selbst keine
Ergebnisse speichern. Deshalb schickt der Test die Ergebnisse in eine **Google-Tabelle**.

## 1. Google-Tabelle für die Ergebnisse (einmalig, ca. 5 Minuten)

1. Auf <https://sheets.google.com> eine neue, leere Tabelle anlegen (z. B. „Diagnosetest Ergebnisse“).
2. Menü **Erweiterungen → Apps Script**.
3. Den vorhandenen Code löschen und den Inhalt von [`apps-script.gs`](apps-script.gs) einfügen. Speichern.
4. Oben rechts **Bereitstellen → Neue Bereitstellung**.
   - Typ (Zahnrad): **Web-App**
   - Ausführen als: **Ich**
   - Zugriff: **Jeder** (wichtig, sonst können die Schüler nichts senden – sie sehen die Tabelle trotzdem nicht)
5. **Bereitstellen** klicken, Zugriff erlauben (Google warnt „App nicht überprüft“ → *Erweitert* → *Zu … wechseln*).
6. Die **Web-App-URL** kopieren (endet auf `/exec`).

## 2. URL in den Test eintragen

In `index.html` (auf GitHub: Datei öffnen → Stift-Symbol) diese Zeile ändern:

```js
var SCRIPT_URL="";
```

zu

```js
var SCRIPT_URL="https://script.google.com/macros/s/.../exec";
```

und speichern („Commit changes“).

## 3. GitHub Pages einschalten (einmalig)

Im Repository: **Settings → Pages → Build and deployment**
- Source: **Deploy from a branch**
- Branch: **main**, Ordner **/ (root)** → **Save**

**Wichtig:** Bei einem kostenlosen GitHub-Konto gibt es Pages nur für **öffentliche** Repositories.
Falls „Pages“ fehlt oder gesperrt ist: Settings → General → ganz unten „Danger Zone“ →
**Change visibility → Make public**. Die Ergebnisse der Schüler liegen nicht im Repository,
sondern nur in deiner Google-Tabelle – sie werden dadurch also nicht öffentlich.

Nach 1–2 Minuten ist der Test erreichbar unter:

**https://kathy-flower.github.io/Unterricht/**

Diesen Link an die Schülerinnen und Schüler geben.

## Ergebnisse ansehen

Jede abgeschickte Arbeit erscheint als neue Zeile in der Google-Tabelle: Zeit, Name, Punkte,
Gruppe, Sprachniveau und die einzelnen Antworten (A1–A14).

Falls das Senden einmal nicht klappt, zeigt der Test wie bisher einen Code zum Abfotografieren.

**Hinweis:** Bei Änderungen am Apps-Script muss unter *Bereitstellen → Bereitstellungen verwalten*
eine neue Version bereitgestellt werden.
