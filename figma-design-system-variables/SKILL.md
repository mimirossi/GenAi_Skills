---
name: "figma-design-system-variables"
description: "Costruisce in Figma le variabili di un design system (Brand, Alias, Mapped, Responsive, Motion): scale tonali, light/dark, tipografia, spacing generico e semantico dei componenti, elevation, motion, breakpoint, scope e validazione."
---

# Figma Variables per Design System

Costruisce in Figma un set di variabili corretto, coerente e funzionale: primitivi di brand, semantica, mappatura dei componenti con Light/Dark, valori responsive e tipografia. Vale per design system di qualsiasi tipo (prodotti digitali, dashboard, siti di brand, editoriale): dove una regola dipende dal tipo di prodotto, la skill lo chiede o lo deduce e dichiara la scelta.

Principi che valgono ovunque:
- Si lavora sempre per gruppi.
- Ogni scala ha una regola **scritta e motivata**.
- Nessun valore inventato: se un dato obbligatorio manca, la skill si ferma e lo chiede.
- Nessun valore raw fuori da Brand.

## Strumenti

Se il server Figma MCP è connesso: aprire una sessione sul file, caricare la skill `figma-use` prima di qualsiasi `use_figma`, leggere variabili e stili esistenti con `get_variable_defs` / `get_design_context`. Se non è connesso, produrre la specifica completa (tabelle di variabili per collection e mode) pronta da importare, e dirlo all'utente.

## Flusso di lavoro

1. Raccogliere i dati in ingresso
2. Verificare il piano Figma
3. Dichiarare il naming
4. Brand (primitivi, scale tonali, size, tipografia, colori d'ombra, durate ed easing)
5. Alias (semantica, livelli di elevation)
6. Mapped (componenti, Light/Dark, colore delle ombre)
7. Responsive (font, spacing, breakpoint, grid)
8. Motion (durate, easing, Default/Reduced)
9. Tipografia (ruoli, scala, text styles)
10. Configurazione (scope, effect styles, code syntax, descrizioni)
11. Validazione finale e report

---

## 1. Dati in ingresso

| Dato | Obbligatorio | Come ottenerlo |
|---|---|---|
| Colori del brand (HEX o RGB) | Sì | Link Figma (stili o variabili), oppure incollati, brand guidelines PDF, screenshot |
| Font family, style e weight | Sì | Link Figma (text styles), oppure elenco |
| Dimensioni tipografiche per ruolo e mode | No: se mancano si generano (sezione 9) | Link Figma, oppure tabella |
| Breakpoint e grid (colonne, margini, container, baseline) | Sì | Link Figma (layout grid dei frame), oppure valori |
| Piano Figma del file | Sì | Domanda diretta |
| Tipo di prodotto | No (si deduce) | Domanda o materiale ricevuto; serve per il fattore tipografico |
| Componenti previsti (card, button, input, tag/badge, navigation) | No: se mancano si creano i cinque gruppi di default | Dal file (leggere l'auto layout dei componenti esistenti per ricavarne gli spazi reali) o da elenco, per lo spacing dei componenti (sezione 7) |

## 2. Piano Figma e modes

| Collection | Ruolo | Riferisce a | Modes |
|---|---|---|---|
| `Brand` | Primitivi: tutti i valori raw | Valori raw | Nessuno |
| `Alias` | Semantica: categorie principali, livelli di elevation | Brand | Nessuno |
| `Mapped` | Componenti e tutto ciò che cambia con il tema | Alias | Light (default), Dark |
| `Responsive` | Tipografia, spacing, breakpoint, grid | Brand | Desktop, Tablet, Mobile |
| `Motion` | Ruoli delle animazioni (entrata, uscita, feedback…) | Brand | Default, Reduced |

Il numero di modes per collection dipende dal piano (limiti noti: Starter 1, Professional e Organization 4, Enterprise fino a 40; riverificarli perché cambiano). La struttura richiede al massimo 3 modes.

- **Starter:** avvisare l'utente prima di iniziare. Creare comunque tutte le variabili **senza modes**: Mapped con i soli valori Light, Responsive con i soli valori Desktop, Motion con i soli valori Default. I valori Dark, Tablet, Mobile e Reduced vanno nel report finale in una tabella pronta, per aggiungerli come modes se il piano cambia.
- **Altri piani:** creare i modes come da tabella.

## 3. Naming

Fissato. La skill lo dichiara all'utente prima di creare le variabili e lo applica senza eccezioni.

| Regola | Valore | Esempio |
|---|---|---|
| Maiuscole | Tutto minuscolo | `text/primary/hover` |
| Parole composte | kebab-case | `hover-on-colour`, `page-secondary` |
| Gruppi | `/` | `surface/error/default-subtle` |
| Colori e misure in Brand | Centesimale | `blue/500`, `size/400` |
| Border, ombre, elevation e spacing generico in Alias/Responsive | T-shirt size | `radius/md`, `shadow/sm`, `elevation/lg/blur`, `spacing/stack/lg` |
| Colori d'ombra in Brand | Colore + opacità in due cifre | `shadow/black-08`, `shadow/black-32` |
| Spacing dei componenti in Responsive | Nome semantico della relazione, mai t-shirt size | `spacing/card/header-content`, `spacing/button/inset-vertical` |
| Durate in Brand | Centesimale = millisecondi | `duration/200` = 200ms |
| Easing in Brand | Nome della curva | `easing/standard`, `easing/decelerate` |
| Ruoli in Motion | Funzione dell'animazione, mai velocità | `motion/enter/duration`, non `motion/fast` |
| Collection | Iniziale maiuscola, una parola | `Brand`, `Alias`, `Mapped`, `Responsive`, `Motion` |
| Caratteri vietati | `.` `{` `}` | — |

## 4. Brand — primitivi

- **Colori:** una scala tonale completa per ogni colore del brand (`blue/100 … blue/900`, brand su `500`).
- **Foundations:** `white`, `black`.
- **Size:** griglia 4px (0, 2, 4, 8, 12, 16, 20, 24, 32…), nominazione centesimale.
- **Border:** valori raw di width e radius.
- **Tipografia:** `font-family/`, `font-weight/`, `font-size/`, `letter-spacing/` (sezione 9).
- **Colori d'ombra:** `shadow/black-<alpha>` (es. `shadow/black-08`, `black-16`, `black-32`: nero con l'opacità indicata). Unica eccezione voluta alla regola "mai opacità": un'ombra deve lasciar vedere il fondo, e non si usa mai per testo o superfici, quindi il contrasto non è in gioco.
- **Motion:** `duration/0`, `050`, `100`, `150`, `200`, `300`, `500` (Number, ms); `easing/linear`, `standard`, `decelerate`, `accelerate` (String, `cubic-bezier(…)`); le distanze di spostamento usano `size/` (sezione 8).

### Scale tonali

1. Prendere la palette del brand.
2. Convertire ogni colore in RGB e HEX; verificare che dopo la conversione resti visivamente coerente col brand.
3. Generare la scala sulla **luminosità percepita (OKLCH)**, mai con l'opacità (un colore trasparente cambia aspetto su ogni sfondo e il contrasto non è misurabile):
    - convertire il colore di brand in OKLCH (L luminosità, C chroma, H tinta);
    - il brand resta su `500` con il suo valore esatto;
    - L fissa per gradino, a distanze regolari: `100` 0.95, `200` 0.88, `300` 0.79, `400` 0.69, `600` 0.46, `700` 0.38, `800` 0.30, `900` 0.22;
    - H identica su tutta la scala;
    - C = C del brand × coefficiente, per restare vicini al carattere del brand: `100` 0.25, `200` 0.45, `300` 0.65, `400` 0.85, `500` 1, `600` 0.95, `700` 0.85, `800` 0.70, `900` 0.55; se il colore esce dallo spazio sRGB, ridurre ancora C fino a rientrare;
    - riconvertire ogni gradino in HEX pieno.
4. Esempio con `#3366CC`: `100` `#E7EFFE`, `300` `#96BBFE`, `500` `#3366CC`, `700` `#133B8D`, `900` `#021644`.
5. I valori di L possono cambiare se il brand lo richiede, purché la regola sia scritta e motivata nel report.
6. Check di contrasto WCAG sulle coppie d'uso.

## 5. Alias — semantica

- **Colori:** per ogni categoria, l'intera scala tonale del colore scelto, referenziata a Brand: `primary`, `secondary`, `accent`, `neutral`, `error`, `success`, `warning`, `information`. Ogni categoria deve funzionare sia in Light sia in Dark.
- **Border:** `width` e `radius` in t-shirt size (`xs`, `sm`, `md`, `lg`…) referenziati a Brand.
- **Ombre:** `shadow/` in t-shirt size (`xs` … `xl`), dal più leggero al più scuro, referenziati ai `shadow/black-<alpha>` di Brand. Così Mapped punta ad Alias e la catena resta Mapped → Alias → Brand.
- **Elevation:** livelli in t-shirt size, ognuno con le misure dell'ombra referenziate a `size/` di Brand. Il colore dell'ombra non sta qui: Alias non ha modes, e il colore deve cambiare tra Light e Dark (sezione 6).

```
elevation/
  sm/   offset-y, blur, spread      card, elementi appena sollevati
  md/   offset-y, blur, spread      dropdown, menu, popover, tooltip
  lg/   offset-y, blur, spread      modal, dialog, drawer
  xl/   offset-y, blur, spread      toast, notifiche sopra tutto
```

  - Ogni livello ha un uso scritto, come i ruoli tipografici: si sceglie per funzione (quanto sta in alto l'elemento), mai per gusto.
  - `offset-x` è 0 di default (luce dall'alto); si aggiunge solo se il brand prevede una luce laterale.
  - Al crescere del livello crescono offset-y e blur, in modo regolare (es. offset-y 2/4/8/16, blur 4/8/16/24, tutti valori di `size/`): l'ombra più alta è più morbida e più lontana.
  - Ombre a più strati (es. una stretta e scura più una larga e chiara) solo se il brand le chiede: in quel caso `elevation/<livello>/1/…` e `…/2/…`.

## 6. Mapped — componenti e temi

I primi valori sono **Light**. Il mode **Dark** parte dall'inversione delle scale (`100` ↔ `900`) come base, poi va rifinito:
- superfici più in alto (card, modali) leggermente più chiare della pagina, non più scure (al buio le ombre non si vedono);
- colori di brand e feedback un passo più chiari o meno saturi se sul fondo scuro sono troppo accesi o non passano il contrasto (l'inversione lascia il `500` dov'è: un link che passa 4.5:1 su bianco può fallire su fondo scuro);
- testo principale off-white, non `white` puro;
- ogni coppia testo/superficie e bordo/superficie verificata WCAG anche in Dark.

**Elevation nei temi.** Il colore dell'ombra per livello sta in Mapped, perché cambia con il tema:

```
elevation/
  sm/ md/ lg/ xl/
                 color        → Alias shadow/. Light: ombre leggere (es. sm → shadow/xs); Dark: più scure (es. sm → shadow/md)
```

In Dark un'ombra nera su fondo scuro quasi non si vede: l'ombra si scurisce, ma il segnale principale dell'altezza è la superficie, che a ogni livello diventa un passo più chiara (`surface/default` per `sm`, un gradino più chiaro per `md`, e così via). Se servono superfici dedicate, si aggiungono come `surface/raised-<livello>` in Mapped.

```
text/
  default/       heading, body, caption, placeholder (+ altri se servono)
  on-colour/     stessi ruoli di default, con valori per testo su colore
  primary/       default, default-on-colour, hover, hover-on-colour   (es. link)
  secondary/     stessa struttura di primary (se esiste)
  error/ success/ warning/ information/   stessa struttura di primary, con i relativi alias
  disabled/      default, default-on-colour   (senza hover)

icon/
  neutral/       default, on-colour   (icone neutre: UI generica, azioni secondarie)
  primary/ secondary/ error/ success/ warning/ information/ disabled/   (come text, senza default e on-colour)

surface/
  primary/ secondary/ error/ warning/ information/ success/
                 default, default-hover, default-subtle, default-subtle-hover, active
  disabled/      default, default-subtle   (senza hover e active)
  page
  page-secondary
  default        (card)
  secondary      (card)

border/
  default/       default, on-colour
  primary/ secondary/ error/ warning/ information/ success/
                 default, default-hover, default-subtle, default-subtle-hover, active, focus
  disabled/      default, default-subtle   (senza hover, active, focus)
```

`subtle` = varianti per superfici chiare. `focus` usa gli stessi colori di `default`.

## 7. Responsive

Collection con modes Desktop, Tablet, Mobile.

```
font/<ruolo>/    font-size, line-height, paragraph-spacing, letter-spacing   (sezione 9)
spacing/
  inset/         spazio dentro gli elementi              ┐
  inline/        spazio tra elementi in orizzontale       │ scala generica,
  stack/         spazio tra elementi in verticale         │ t-shirt size → Brand size/
  section/       spazio tra sezioni                       ┘
  card/          title-subtitle, header-content, content-action, inset
  button/        icon-label, inset-vertical, inset-horizontal
  input/         label-field, field-description
  tag-badge/     icon-label, inset-vertical, inset-horizontal
  navigation/    item-gap, group-gap
breakpoint/      min-width, frame-width
grid/            columns, margin, container, baseline
```

- Spacing generico in t-shirt size, referenziato a `size/` di Brand.
- `inline` e non `gap`: in Figma "gap" indica lo spazio di auto layout in entrambe le direzioni.

### Spacing dei componenti

La scala generica dice **quanto** spazio; il token di componente dice **dove**. Chi progetta o sviluppa collega il token della relazione ("tra header e contenuto della card") invece di scegliere una misura: cambiare la densità di un componente diventa la modifica di una sola variabile, e il codice riceve un nome che spiega l'intento.

**Naming**

| Pattern | Significato | Esempi |
|---|---|---|
| `<parte>-<parte>` | Spazio tra due parti, in ordine di lettura (alto→basso, sinistra→destra). La direzione è data dalla struttura del componente, non dal nome | `title-subtitle`, `label-field`, `icon-label` |
| `inset` | Padding uguale su tutti i lati | `card/inset` |
| `inset-vertical`, `inset-horizontal` | Padding quando i due assi differiscono | `button/inset-vertical` |
| `<parte>-inset` | Padding intorno a una sola parte interna al componente (es. area cliccabile di un'icona). Il nome dice quale parte, mai un generico `icon-inset` | `modal/close-inset` |
| `<elemento>-gap` | Solo quando lo stesso spazio vale in entrambe le direzioni: la direzione cambia tra modes (navigation orizzontale su Desktop, verticale su Mobile) oppure il gruppo va a capo (wrap, stesso token su gap e counter axis gap). Qui "gap" è corretto proprio perché copre entrambe le direzioni | `navigation/item-gap`, `chip/item-gap` |

- Niente t-shirt size nei token di componente: il nome descrive la relazione, la misura sta nella scala generica.
- Stessi nomi di parte in tutti i componenti (`icon`, `label`, `title`, `subtitle`, `header`, `content`, `action`, `field`, `description`, `item`, `group`). Un nuovo componente riusa questi termini prima di inventarne altri.
- Un token per relazione reale: se due spazi hanno sempre lo stesso valore e lo stesso motivo, è un token solo.

**Riferimenti**

- Ogni token di componente punta alla scala generica della stessa collection (`spacing/card/header-content` → `spacing/stack/md`), non direttamente a `size/`. Così una modifica alla scala si propaga a tutti i componenti, e la catena resta Responsive → Brand.
- L'alias va impostato in ogni mode. Di norma è lo stesso alias in Desktop, Tablet e Mobile, perché la scala generica cambia già per mode. Si usa un alias diverso per mode solo dove il componente si comporta diversamente dalla scala (es. card più compatta su Mobile), e il report lo motiva.
- **Spazi dei controlli vs spazi di layout.** Gli spazi dentro i controlli piccoli (button, input, chip, tag-badge: `inset-vertical` e `icon-label`, più `input/label-field`) seguono il testo `ui/`, che su Mobile non cambia: devono restare uguali in px. Se la scala generica scende su Mobile, su Mobile si punta a una taglia più grande che dà lo stesso valore (es. `button/inset-vertical` → `inset/md` = 12 su Desktop, `inset/lg` = 12 su Mobile). `inset-horizontal` può invece ridursi su Mobile per recuperare larghezza, perché non incide sull'altezza. Gli spazi di layout (card, modal, form, navigation) seguono la scala e si riducono. Il motivo: un button che passa da 44 a 36px su Mobile perde area di tocco mentre il suo testo resta della stessa misura.

**Ordine di prossimità** (in ogni mode, le relazioni interne sono più strette di quelle esterne, altrimenti i gruppi visivi si leggono male):

- Card: `title-subtitle` < `header-content` ≤ `content-action` ≤ `inset`
- Input: `label-field` e `field-description` < spazio tra due input nel form (`spacing/stack/*`)
- Button, tag-badge: `icon-label` < `inset-horizontal`
- Navigation: `item-gap` < `group-gap`

**Binding in Figma** (un auto layout ha un solo gap: se due token cadono nello stesso frame con valori diversi, serve un frame annidato)

| Componente | Struttura auto layout | Token → campo |
|---|---|---|
| Card | `card` (verticale) > `body` (verticale) > `header` (verticale) + `content`; poi `action` | `inset` → padding di `card`; `content-action` → gap di `card`; `header-content` → gap di `body`; `title-subtitle` → gap di `header` |
| Button | `button` (orizzontale) > icona + label | `inset-vertical` → padding top/bottom; `inset-horizontal` → padding left/right; `icon-label` → gap |
| Input | `input` (verticale) > label + `field-group` (verticale) > field + description | `label-field` → gap di `input`; `field-description` → gap di `field-group` |
| Tag/badge | come Button | come Button |
| Navigation | `nav` > `group` > item | `group-gap` → gap di `nav`; `item-gap` → gap di `group` |

Se due relazioni nello stesso frame hanno davvero lo stesso valore in tutti i modes, il frame annidato non serve: lo si dice nel report.

**Target di interazione:** altezza di button e input = line height del ruolo `ui/` + 2 × `inset-vertical` ≥ 44px su Mobile (minimo assoluto WCAG 2.5.8: 24px). Con `ui/button` a 20px di line height, `inset-vertical` ≥ 12. Un tag-badge interattivo (chip, filtro) rispetta almeno i 24px.

**Esempio** (valori in px risolti dalla scala generica; da adattare al brand)

| Token | Desktop | Tablet | Mobile |
|---|---|---|---|
| `card/title-subtitle` | 4 | 4 | 4 |
| `card/header-content` | 16 | 16 | 12 |
| `card/content-action` | 24 | 24 | 16 |
| `card/inset` | 24 | 24 | 16 |
| `button/icon-label` | 8 | 8 | 8 |
| `button/inset-vertical` | 12 | 12 | 12 |
| `button/inset-horizontal` | 24 | 24 | 20 |
| `input/label-field` | 8 | 8 | 8 |
| `input/field-description` | 4 | 4 | 4 |
| `tag-badge/icon-label` | 4 | 4 | 4 |
| `tag-badge/inset-vertical` | 4 | 4 | 4 |
| `tag-badge/inset-horizontal` | 8 | 8 | 8 |
| `navigation/item-gap` | 24 | 24 | 8 |
| `navigation/group-gap` | 48 | 32 | 24 |

## 8. Motion

Le animazioni si salvano come variabili per avere un'unica fonte di durate ed easing per il codice e per Dev Mode.

**Limite di Figma.** Nei prototipi la durata e l'easing delle transizioni non si collegano alle variabili (verificare sul file: Figma Motion potrebbe averlo cambiato). Le variabili di Motion sono quindi la specifica: nei prototipi i valori si applicano a mano o con un plugin, e il report lo dice.

### Cosa si salva

| Valore | Tipo | Dove |
|---|---|---|
| Durata | Number (ms) | Brand `duration/`, ruoli in Motion |
| Easing | String (`cubic-bezier(x1, y1, x2, y2)`) | Brand `easing/`, ruoli in Motion |
| Delay / stagger | Number (ms) | Motion, solo se serve (es. liste che entrano in sequenza) |
| Distanza di spostamento | Number | Motion → `size/` di Brand |

### Collection `Motion`

Modes: **Default** e **Reduced**. Si usa una collection a parte perché la riduzione del movimento dipende da una preferenza dell'utente (prefers-reduced-motion, WCAG 2.3.3), non dallo schermo: non sta in Responsive, e non sta in Alias perché Alias non ha modes.

```
motion/
  enter/      duration, easing, distance     elementi che compaiono (modal, toast, dropdown)
  exit/       duration, easing, distance     elementi che spariscono
  expand/     duration, easing               accordion, pannelli che si aprono sul posto
  move/       duration, easing               elementi che cambiano posizione o dimensione
  feedback/   duration, easing               hover, press, focus, toggle
  stagger/    delay                          ritardo tra elementi di una lista (se serve)
```

Ruoli per funzione, come per la tipografia: chi progetta sceglie "entrata", non "veloce".

### Regole

- **Uscita più rapida dell'entrata:** chi chiude qualcosa vuole che sparisca subito (es. enter 200ms, exit 150ms).
- **Easing per direzione:** entrata `decelerate` (arriva e rallenta), uscita `accelerate` (parte e se ne va), movimento sul posto `standard`. `linear` solo per opacità pura o indicatori continui (progress, spinner).
- **Durata proporzionale alla distanza e alla superficie:** feedback 100–150ms, dropdown e toast 200ms, modal e drawer 300ms. Nessuna animazione d'interfaccia oltre 500ms, salvo transizioni di pagina motivate nel report.
- **Reduced:** le durate di `enter`, `exit`, `expand`, `move` scendono a `duration/0` o restano brevi solo per le dissolvenze (es. 100ms solo opacità); `distance` → `size/0`; `stagger/delay` → 0. `feedback` può restare: un cambio di colore non è movimento.
- Nessun valore raw: ogni ruolo di Motion punta a Brand in entrambi i modes.

### Esempio

| Variabile | Default | Reduced |
|---|---|---|
| `motion/enter/duration` | `duration/200` | `duration/100` (solo dissolvenza) |
| `motion/enter/easing` | `easing/decelerate` | `easing/linear` |
| `motion/enter/distance` | `size/400` (16px) | `size/0` |
| `motion/exit/duration` | `duration/150` | `duration/0` |
| `motion/exit/easing` | `easing/accelerate` | `easing/linear` |
| `motion/expand/duration` | `duration/300` | `duration/0` |
| `motion/feedback/duration` | `duration/100` | `duration/100` |
| `motion/stagger/delay` | `duration/050` | `duration/0` |

Curve di partenza (da adattare al carattere del brand e dichiarare nel report): `standard` `cubic-bezier(0.2, 0, 0, 1)`, `decelerate` `cubic-bezier(0, 0, 0, 1)`, `accelerate` `cubic-bezier(0.3, 0, 1, 1)`.

## 9. Tipografia

Costruita per superare i checkpoint di `typography-audit` verificabili in Figma.

### Architettura

```
Brand        font-family/  font-weight/  font-size/  letter-spacing/  size/ (4px grid)
Responsive   font/<ruolo>/  font-size · line-height · paragraph-spacing · letter-spacing
Text styles  un style per ruolo e variante, ogni campo collegato a una variabile
```

- `font-size/` in Brand: centesimale crescente, `font-size/300` = base 16px, un gradino per step di scala.
- Line height e paragraph spacing stanno sulla griglia 4px e puntano a `size/`.
- Nessun text style con valori scritti a mano; ogni ruolo definisce tutti i campi (family, weight, size, line-height, paragraph-spacing, letter-spacing).

### Ruoli (per funzione, mai per aspetto)

| Ruolo | Tipo | Funzione | Non usarlo per | Step |
|---|---|---|---|---|
| `display` | Lettura | Titolo di apertura: hero, copertina | Pagine di contenuto, card | +6 |
| `heading/h1` | Lettura | Titolo della pagina, uno per pagina | Enfatizzare testo | +5 |
| `heading/h2` | Lettura | Titolo di sezione | Titoli di card | +4 |
| `heading/h3` | Lettura | Titolo di sottosezione | Etichette di controlli | +3 |
| `heading/h4` | Lettura | Titolo di card o blocco | Testo di lettura | +2 |
| `body/default` | Lettura | Testo di lettura principale | Note e metadati | 0 |
| `body/supporting` | Lettura | Testo secondario: descrizioni, intro brevi | Contenuto principale | −1 |
| `caption` | Lettura | Metadati, didascalie, note legali | Contenuto principale | −2 |
| `ui/label` | Interfaccia | Etichette di campi e controlli | Testo di lettura | −1 |
| `ui/button` | Interfaccia | Testo dei pulsanti | Link nel testo | 0 |
| `ui/input` | Interfaccia | Testo digitato e placeholder | Etichette | 0 |
| `ui/navigation` | Interfaccia | Menu, tab, breadcrumb | Titoli di sezione | 0 |
| `ui/tag` | Interfaccia | Tag, badge, chip | Testo di stato lungo | −2 |

- `h5` e `h6` solo se il prodotto li usa davvero.
- Varianti: `/strong` e, se il font la prevede, `/italic`. Cambiano solo peso o stile, mai size, line height o letter spacing. L'enfasi usa la variante, mai il ruolo superiore.
- Due ruoli adiacenti differiscono di almeno 2px; se la scala non li separa, si fondono e la distinzione passa a colore o peso.

### Scala

- Base 16px (si cambia solo su richiesta esplicita del brand).
- Size di uno step = 16 × fattore^step, arrotondata al pixel intero.
- Fattore per tipo di prodotto; la skill dichiara quale e perché. Senza indizi: 1.2.

| Tipo di prodotto | Desktop/Tablet | Mobile |
|---|---|---|
| Dashboard, tool interni, app dense di dati | 1.125 | 1.067 |
| Prodotto digitale generico, web app, servizi | 1.2 | 1.125 |
| Siti di brand, e-commerce, landing | 1.25 | 1.2 |
| Editoriale, marketing, eventi, portfolio | 1.333 | 1.25 |

- **Line height**, per eccesso al multiplo di 4: display e heading 1.2× (1.1× per `display` e `h1` con fattore ≥ 1.25); lettura 1.5×; interfaccia 1.25×.
- **Paragraph spacing:** uguale alla size, al multiplo di 4 più vicino (a parità, per eccesso); interfaccia 0.
- **Weight**, massimo 3 tra quelli del font: regular per la lettura; medium per `ui/label`, `ui/button`, `ui/navigation`, `ui/tag`; bold o semibold per display, heading, `/strong`.
- **Letter spacing:** regola in percentuale della size (−2% per `display` e `h1`, 0 per il resto, +5% per `ui/tag` e maiuscolo). Le variabili Figma applicano il letter spacing **solo in px**, quindi: px = size × percentuale per ruolo e mode, arrotondato al primitivo più vicino di Brand (`letter-spacing/neg-100` −1px, `neg-050` −0.5px, `000` 0, `050` +0.5px, `100` +1px). Mai una variabile "−2" intesa come percentuale: Figma la applicherebbe come −2px.

### Responsive

- Un solo text style per ruolo; i modes cambiano i valori. Mai copie per breakpoint.
- Tablet = Desktop. Mobile usa il fattore di un gradino più basso; si riducono solo display e heading.
- Line height e paragraph spacing si ricalcolano dalla nuova size.
- Anche su Mobile due ruoli adiacenti differiscono di almeno 2px.

### Accessibilità

- Classe di contrasto per ruolo e mode: testo grande = ≥ 24px regular o ≥ 18.66px bold → 3:1; il resto → 4.5:1. Se un ruolo scende sotto soglia su Mobile, si verifica a 4.5:1.
- Contrasto verificato per ogni ruolo × colore `text/` usabile × Light e Dark.
- Minimi: nessun testo sotto 12px; lettura almeno 14px; `body/default` e `ui/input` almeno 16px. I valori calcolati sotto soglia si alzano al minimo e il report lo dice.
- Lettura con line height almeno 1.5×.
- Nei componenti i testi sono in auto height / hug, senza altezze fisse: devono reggere line height 1.5×, paragraph spacing 2×, letter spacing 0.12em e testo al 200% (WCAG 1.4.12, 1.4.4).

### Handoff e AI-ready

- Code syntax su ogni variabile tipografica; text styles con lo stesso nome del token in codice.
- Descrizione di ogni text style: funzione e "non usarlo per".
- Regole responsive scritte come tabella con i `min-width` dei breakpoint.
- Invarianti scritti nel report: base 16px; `body/default` e `ui/input` mai sotto 16px; nessun valore raw nei text styles; varianti senza cambi di size, line height, letter spacing; un solo style per ruolo; ruoli scelti per funzione.
- Produrre `typography-context.md`: token, ruoli con funzione e divieti, relazioni di scala, regole responsive, invarianti; ogni dato mancante "Not defined" e raccolto in "Context gaps"; versione e data del file Figma.

### Esempio (fattore 1.2, Mobile 1.125, heading bold)

| Ruolo | Desktop size / LH / PS | Mobile size / LH / PS |
|---|---|---|
| `display` | 48 / 60 / 48 | 32 / 40 / 32 |
| `heading/h1` | 40 / 48 / 40 | 29 / 36 / 28 |
| `heading/h2` | 33 / 40 / 32 | 26 / 32 / 28 |
| `heading/h3` | 28 / 36 / 28 | 23 / 28 / 24 |
| `heading/h4` | 23 / 28 / 24 | 20 / 24 / 20 |
| `body/default` | 16 / 24 / 16 | uguale |
| `body/supporting` | 14 / 24 / 16 | uguale |
| `caption` | 12 / 20 / 12 | uguale |
| `ui/label` | 13 / 20 / 0 | uguale |
| `ui/button`, `ui/input`, `ui/navigation` | 16 / 20 / 0 | uguale |
| `ui/tag` | 12 / 16 / 0 | uguale |

## 10. Configurazione delle variabili

**Scope** (dove la variabile compare nei menu di Figma):

| Gruppo | Scope |
|---|---|
| `text/*` | Text fill |
| `icon/*` | Shape fill, Stroke |
| `surface/*` | Frame fill, Shape fill |
| `border/*` colori, border width | Stroke |
| radius | Corner radius |
| `spacing/*` | Gap (copre anche il padding) |
| `font/*` | Rispettivi campi tipografici |
| `elevation/*` misure (Alias) | Effects (campi numerici dell'effetto) |
| `elevation/*/color` (Mapped), `shadow/*` (Alias, Brand) | Effects (colore dell'effetto) |
| `breakpoint/*`, `grid/container` | Width and height |
| `duration/*`, `easing/*`, `motion/*` | Nessuno: non hanno campi da collegare nei menu, servono per codice e Dev Mode |

Brand e Alias restano visibili (non nascosti dalla pubblicazione), con scope coerenti col loro tipo.

**Text styles:** uno per ruolo e variante, ogni campo collegato a una variabile.

**Effect styles:** un'ombra non si salva come variabile, solo come effect style. Uno style per livello (`elevation/sm`, `md`, `lg`, `xl`), drop shadow con X, Y, blur, spread e colore collegati alle variabili: misure da Alias, colore da Mapped. Così lo stesso style cambia ombra passando da Light a Dark. Descrizione dello style: uso del livello (es. "modal, dialog, drawer").

**Code syntax delle ombre:** una variabile per campo (`var(--elevation-md-blur)`); nel report indicare anche la composizione CSS del livello (`box-shadow: 0 var(--elevation-md-offset-y) var(--elevation-md-blur) var(--elevation-md-spread) var(--elevation-md-color)`).

**Code syntax:** Web, derivata dal nome (`/` → `-`, prefisso `--`): `text/primary/hover` → `var(--text-primary-hover)`. Le durate escono con l'unità: `motion/enter/duration` → `var(--motion-enter-duration)` = `200ms`. Nel report, il blocco `@media (prefers-reduced-motion: reduce)` con i valori del mode Reduced.

**Descrizioni:** una riga per variabile su quando usarla.

## 11. Validazione finale e report

| Controllo | Regola |
|---|---|
| Catena dei riferimenti | Mapped → Alias → Brand; Responsive → Brand; Motion → Brand; nessun valore raw fuori da Brand |
| Alias rotti | Nessuna variabile che punta a una variabile inesistente |
| Modes completi | Un valore per ogni mode; su Starter, valori degli altri modes nel report |
| Contrasto testo | ≥ 4.5:1 normale, ≥ 3:1 grande, Light e Dark |
| Contrasto UI | ≥ 3:1 per bordi, focus, icone, Light e Dark |
| Naming | Minuscolo, kebab-case, `/`, nessun carattere vietato |
| Scope | Nessuna variabile di Mapped o Responsive con scope "tutti" |
| Spacing dei componenti | Nomi semantici per relazione; ogni token punta alla scala generica `spacing/`; ordine di prossimità rispettato in ogni mode; button e input ≥ 44px su Mobile; binding sul campo auto layout corretto |
| Text styles | Tutti collegati, nessun valore fisso |
| Elevation | Misure in Alias → Brand; colore in Mapped con Light e Dark; effect styles con ogni campo collegato; livelli crescenti in offset-y e blur; in Dark superfici più chiare per livello |
| Motion | Ruoli per funzione; ogni ruolo → Brand in Default e Reduced; uscita ≤ entrata; nessuna durata > 500ms senza motivo; Reduced senza spostamenti |
| Code syntax e descrizioni | Presenti ovunque |
| Tipografia | Checkpoint di `typography-audit` verificabili in Figma (esclusi i due Handoff sul codice): obiettivo 40/40 |

Il report finale contiene: errori trovati e corretti, regole dichiarate (scale tonali, fattore tipografico, naming), valori alzati ai minimi, punteggio tipografico, eventuale tabella dei modes non creati (Starter), blocco CSS per prefers-reduced-motion, `typography-context.md`.

## Checklist di uscita

- [ ] Dati in ingresso raccolti
- [ ] Piano verificato prima di creare i modes
- [ ] Brand, Alias, Mapped, Responsive create e popolate
- [ ] Scale tonali OKLCH, regola scritta e motivata
- [ ] Foundations white e black
- [ ] Light e Dark in Mapped, Dark rifinito oltre l'inversione
- [ ] Desktop, Tablet, Mobile in Responsive
- [ ] Spacing dei componenti: nomi semantici, riferiti alla scala generica, ordine di prossimità, binding e target verificati
- [ ] Elevation: livelli per uso, misure in Alias, colore in Mapped, effect styles collegati
- [ ] Motion: collection con Default e Reduced, ruoli per funzione, limite dei prototipi dichiarato
- [ ] Scope assegnati, Brand e Alias visibili
- [ ] Text styles collegati
- [ ] Code syntax e descrizioni
- [ ] Naming dichiarato e applicato
- [ ] Tipografia: fattore dichiarato, ruoli per funzione, 40/40
- [ ] `typography-context.md` con versione e data
- [ ] Report consegnato