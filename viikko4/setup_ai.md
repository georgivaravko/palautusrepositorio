VAROITUS: Tein tämän tehtävän copypastella Geminin avulla, koska copilot integraatio 
vscodeen ei näytä toimivan tällä hetkellä. Yritin selvittää missä virhe, mutta en saanut 
vielä kiinni. Liitän saamani virheen loppuun.

Käsittääkseni agentti ei poistanut mitään, mitä ei olisi tarkoitus. Käytännössä ei 
poistanut siis mitään. Koodi on nyt todella helpommin luoettavaa varsinkin meille, jotka 
näemme koodin jo toista kertaa. Niile ketkä sen kohtaa ensimmäistä kertaa enismmäinen 
versio olisi voinut olla jopa helpompi, jottei tarvitse muistaa mitä setupissa oikein on 
tehty jo. Tulee säästettyä skrollausta. 

En myöskään huomannut, että agentti olisi muuttanut testien toiminnallisuutta. Testien 
toiminnot ja itse testikomennot ovat ennallaan.

Itse asiassa koodin tarkasteleminen ennen copy pasteamista oli jopa helpompaa, koska 
pääsin lukemaan sen läpi ja hyväksymään muutokset, ennen niiden implementointia.

En joutunut pyytämään tai tekemään muutoksia.

Virhe, joka minulle ilmenee copilotille yhtään mitään lähettäessäni:

Error: CLI server exited with code 1 stderr: copilot-runtime: failed to load runtime 
cdylib /Applications/Visual Studio 
Code.app/Contents/Resources/app/node_modules.asar.unpacked/@github/copilot-sdk-darwin-x64/prebuilds/darwin-x64/runtime.node: 
dlopen failed at ChildProcess.<anonymous> 
(file:///Applications/Visual%20Studio%20Code.app/Contents/Resources/app/node_modules.asar/@github/copilot-sdk/dist/client.js:3196:15) 
at ChildProcess.emit (node:events:526:24) at ChildProcess._handle.onexit 
(node:internal/child_process:324:12)
