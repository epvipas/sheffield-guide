// ---------- info ----------
function iref(id, label) { const it = ITEMS.find(x => x.id === id); return `<button class="linkchip" data-goto="${id}" style="color:${CATS[it.cat].color}">${CATS[it.cat].emoji} ${esc(label || it.name)}</button>`; }
function byName(n) { const it = ITEMS.find(x => x.name === n); if (!it) throw new Error('No place called ' + n); return it.id; }
function refs(names) { return names.map(n => iref(byName(n))).join(' '); }
function renderSpecial() {
  const stops = [
    ['Dog & Partridge', 'Start in the centre at an unspoilt Irish pub with folk sessions.'],
    ['Shakespeare\'s', 'Walk north to the Georgian coaching inn on Gibraltar Street.'],
    ['Kelham Island Tavern', 'The 2026 Pub of the Year, a few minutes away on Russell Street.'],
    ['The Fat Cat', 'The original Kelham Island real-ale pub, by the museum.'],
    ['Cutlery Works', 'Food break in the old cutlery factory.'],
    ['The Bath Hotel', 'Head back south to a 1930s heritage interior near Division Street.'],
    ['The Rutland Arms', 'Tiled corner pub near the station.'],
    ['The Sheffield Tap', 'Finish in the Edwardian refreshment room on platform 1b.'],
  ];
  $('#specialTrail').innerHTML = '<ol>' + stops.map(([n, t]) => `<li style="margin-bottom:8px">${iref(byName(n))}<br>${esc(t)}</li>`).join('') + '</ol>';
}
function renderInfo() {
  const hq = { q: 'Peace Gardens, Sheffield', name: 'Peace Gardens Sheffield', ta: true };
  $('#v-info').innerHTML = `
  <div class="hero"><img src="img/cover.svg" alt=""><div class="cap"><span style="color:#FFD23F;font-size:11px;font-weight:800;letter-spacing:2px">YOUR BASE</span><br><b>The Peace Gardens</b><br><span style="font-size:13px">The fountains in front of the Town Hall. Walking times in the guide are from here.</span></div></div>
  <div class="sec"><h2>🚗 Getting there</h2>
   <img src="img/transit.svg" alt="" style="width:100%;border-radius:12px;aspect-ratio:16/7;object-fit:cover">
   <div class="opt" style="border-color:#2F3B47"><h4 style="background:#2F3B47"><span>🚋 Supertram Park &amp; Ride</span><span>easy from the M1</span></h4><ol>
    <li>Sheffield's Supertram has Park &amp; Ride sites, including <b>Meadowhall</b> (M1 J34), <b>Nunnery Square</b> and <b>Halfway</b>, with trams into the centre. Check fares and parking rules before you go.</li>
    <li>Get off at <b>Cathedral</b> for the centre and Kelham Island, or <b>Sheffield Station</b> for the Cultural Industries Quarter.</li></ol></div>
   <div class="opt" style="border-color:#C2703D"><h4 style="background:#C2703D"><span>🅿️ Driving in</span><span>multi-storeys</span></h4><ol>
    <li>Central car parks include <b>Charter Square</b>, <b>Rockingham</b> and the <b>Q-Park</b> by the station. Kelham Island has some small car parks too.</li></ol></div>
   <div class="opt" style="border-color:#1877D0"><h4 style="background:#1877D0"><span>🚆 By train</span><span>10 min walk</span></h4><ol>
    <li>Sheffield station sits below Park Hill. Walk up through Sheaf Square and the Millennium Gallery to the Peace Gardens.</li></ol></div>
   ${actions(hq, true)}
  </div>
  <div class="sec"><h2>🗓️ Two easy days</h2>
   <div class="day" style="background:#FDE3DF"><b>Day 1 · City centre &amp; Kelham Island:</b> ${refs(['Winter Garden', 'Millennium Gallery', 'Tamper Sellers Wheel', 'Division Street & Devonshire Street', 'Steam Yard', 'Kelham Island Museum', 'Kelham Island Tavern', 'Domo'])}</div>
   <div class="day" style="background:#DDEBFA"><b>Day 2 · Antiques, records &amp; green space:</b> ${refs(['Abbeydale Road Antiques Quarter', 'Sheffield Antiques Centre', 'Cole\'s Corner', 'Harrison Cameras', 'Sheffield Botanical Gardens', 'Record Collector', 'St Luke\'s Vintage Shop', 'The Bath Hotel', 'Native'])}</div>
  </div>
  <div class="sec"><h2>🔎 Second-hand hunting</h2>
   <div class="day" style="background:#FDEFD6"><b>Cameras, records &amp; antiques:</b> ${refs(['Harrison Cameras', 'Record Collector', 'Memory Dance', 'Hub', 'Heeley Bank Antiques Centre', 'Vulgar', 'Age UK, Abbeydale Road'])}
    <p style="margin:8px 0 0;font-size:13px">Harrison Cameras' used department sells everything with a 12-month warranty.</p></div>
  </div>
  <div class="sec"><h2>🎸 Nights out &amp; sport</h2>
   <div class="day" style="background:#EFE2F8"><b>Gigs &amp; theatre:</b> ${refs(['Crucible & Lyceum Theatres', 'Sheffield City Hall', 'Abbeydale Picture House', 'Electric Studios'])}</div>
   <div class="day" style="background:#D8F3EE"><b>Football:</b> ${refs(['Bramall Lane (Sheffield United)', 'Hillsborough (Sheffield Wednesday)'])}</div>
  </div>
  <div class="sec"><h2>⛰️ Peak District days</h2>
   <div class="day" style="background:#D8F3EE"><b>Caves, edges &amp; reservoirs:</b> ${refs(['Castleton', 'Stanage Edge & Hathersage', 'Ladybower Reservoir'])}</div>
   <div class="day" style="background:#FDE3DF"><b>Big houses &amp; sculpture:</b> ${refs(['Chatsworth', 'Wentworth Woodhouse', 'Yorkshire Sculpture Park'])}</div>
  </div>
  <div class="sec"><h2>🕐 Opening hours</h2><ul>
   <li>Sheffield's museums and galleries are free, and several close on Mondays or Tuesdays, so check before you go.</li>
   <li>Kelham Island is liveliest Thursday to Saturday evenings. Book restaurants at weekends.</li>
   <li>The Antiques Quarter is best on a Saturday.</li></ul></div>
  <div class="sec"><h2>⚠️ Before you go</h2><ul>
   <li><b>Recently closed:</b> the Leadmill (its building is now Electric Studios), Rare and Racy, the Department food hall and Juke &amp; Loe have closed, and the Graves Gallery shut on 31 October 2026 when the Central Library's heating failed. Jöro has moved out to Oughtibridge.</li>
   <li>Independent places change often. Check each venue's own site or socials before a special trip.</li>
   <li>Map pins come from OpenStreetMap and are close but not exact; use the Directions buttons for door-to-door routes.</li>
   <li>Information was checked in November 2026. The illustrations are original artwork drawn for this guide.</li></ul>
   <button class="btn b-map" id="installAgain" style="width:100%;margin-top:8px">📲 Install this guide on your phone</button></div>
  <div class="sec"><h2>🔄 Updates</h2><p>The guide checks for new content whenever you're online. If something looks out of date, tap below to clear the saved copy and reload.</p>
  <button class="iconbtn" id="refreshBtn" style="padding:10px 14px;box-shadow:0 1px 5px rgba(0,0,0,.2)">Refresh guide</button></div>`;
}
