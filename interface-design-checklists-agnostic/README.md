# Interface Design Checklists — Pacchetto agnostico

Questo pacchetto contiene tutto il materiale necessario per configurare
l'agente "Interface Design Checklists" su **qualsiasi piattaforma AI
enterprise**, indipendentemente dal modello o dal motore sottostante.

## Contenuto

```
AGENT-INSTRUCTIONS.md          → istruzioni/system prompt dell'agente
knowledge-base/                → 31 file .md, uno per pattern (1.084 domande totali)
templates-html-di-riferimento/ → 3 template HTML originali, come specifica
                                  di struttura per gli output (checklist,
                                  report, wireframe)
```

## Come usarlo, in generale

Qualunque piattaforma "crea un agente" chiede tipicamente tre cose. Ecco dove
trovarle in questo pacchetto:

| La piattaforma chiede... | Usa questo |
|---|---|
| Istruzioni / system prompt / comportamento dell'agente | `AGENT-INSTRUCTIONS.md` (caricalo intero, o incollane il contenuto) |
| Documenti di conoscenza / knowledge base da allegare | tutti i file in `knowledge-base/` |
| Come deve essere strutturato l'output | `templates-html-di-riferimento/` — usali come riferimento dei campi/sezioni richiesti, anche se l'output finale sarà Word/PowerPoint/Markdown invece di HTML |

## Un'attenzione sui tre output visivi

I template HTML originali erano pensati per essere generati "al volo" da
un modello che scrive JS con i dati compilati. Su una piattaforma diversa,
questo passaggio va riprodotto in modo diverso: l'importante è che l'agente,
quando produce un output, includa gli stessi elementi che questi template
richiedono (es. per il report: titolo, elenco di problemi con gravità,
posizione nel design, domanda di checklist collegata, proposta di fix,
sezione "cosa funziona").

## Prossimo passo consigliato

Prima di configurare l'agente sulla piattaforma interna, verifica con il team
IT/platform:
1. Il formato esatto richiesto per le istruzioni (system prompt puro? file
   caricato? entrambi?)
2. Come vanno caricati i documenti di knowledge base (upload diretto? tramite
   retrieval/indicizzazione?)
3. Quali formati di output sa produrre nativamente l'agente (la piattaforma
   ha confermato: Markdown, Word, PowerPoint, HTML, CSV, PDF, testo)

Una volta chiarito questo, il pacchetto va adattato di conseguenza — ma la
sostanza (istruzioni + 1.084 domande + struttura degli output) resta questa.
