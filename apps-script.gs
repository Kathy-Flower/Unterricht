// In Google Tabellen: Erweiterungen → Apps Script → diesen Code einfügen → Bereitstellen als Web-App.
var FRAGEN = 14;

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    if (sheet.getLastRow() === 0) {
      var kopf = ["Zeit", "Name", "Mathe (von 9)", "Basis /4", "Mitte /2", "Hoch /3",
                  "Sprache (von 5)", "Gruppe", "Sprachniveau", "Richtig je Aufgabe"];
      for (var k = 1; k <= FRAGEN; k++) kopf.push("A" + k);
      sheet.appendRow(kopf);
      sheet.setFrozenRows(1);
      sheet.getRange(1, 1, 1, kopf.length).setFontWeight("bold");
    }
    var d = JSON.parse(e.postData.contents);
    var zeile = [new Date(), d.name, d.mathe, d.basis, d.mitte, d.hoch,
                 d.sprache, d.gruppe, d.niveau, "'" + d.richtig];
    (d.antworten || []).forEach(function (a) { zeile.push("'" + a); });
    sheet.appendRow(zeile);
    return ContentService.createTextOutput("ok");
  } finally {
    lock.releaseLock();
  }
}
