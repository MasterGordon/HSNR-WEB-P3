% window.setTitle("Laufende Weiterbildungen")
<h2>Laufende Weiterbildungen:</h2>
<div class="list-header list-participation-trainings">
  <div>Bezeichnung</div>
  <div>Beschreibung</div>
  <div>Von</div>
  <div>Bis</div>
  <div>Teilnehmer</div>
  <div>Aktionen</div>
</div>
% trainings.forEach(training => {
  <div data-training-id="${training['id']}" class="list-row list-participation-trainings">
    <input disabled name="title" value="${training['title']}"/>
    <input disabled name="desc" value="${training['desc'].replace("\n", " ")}"/>
    <input disabled name="data_from" type="date" value="${training['date_from']}"/>
    <input disabled name="date_to" type="date" value="${training['date_to']}"/>
    <input disabled name="participants" value="${training['participations']}/${training['max_participants']}"/>
    <div class="actions">
      <a href="/participation-training/${training["id"]}" class="display"><img title="Anzeigen" class="icon" src="/static/icons/search.svg" /></a>
    </div>
  </div>
% })
<div></div>
