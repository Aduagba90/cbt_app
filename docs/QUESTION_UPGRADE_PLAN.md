# Question-bank upgrade plan — from "direct" to real exam standard

Tester feedback (Sept 2026): *"Most of the questions were direct questions, not applied."*
Audit of the 3,500 live JAMB questions confirmed it — only Mathematics (63 % applied) is at
JAMB standard; Physics 28 %, Economics 16 %, English 11 % (only 11 passages), Chemistry 6 %,
everything else 0–7 %.

This plan replaces the bank subject by subject. **Nothing on the website needs to change** —
the importer, the exam engine and the admin tools already do everything below.

## The routine (same for every subject)

1. **Generate**: paste the prompt for the subject (below) into an AI, one topic at a time.
   Ask for the answer as CSV, open it in Excel, or paste the `|` table and use
   *Data → Text to Columns*. Save as `.xlsx` with the header row exactly:
   `Exam Type | Subject | Topic | Question | Option A | Option B | Option C | Option D | Answer | Explanation | Difficulty`
2. **Check**: a subject teacher or a strong student (your tester!) verifies every answer.
   AI is good at *style*, not always at *correctness*. Never skip this.
3. **Upload**: Admin → Import → choose the file → Import. Duplicates are skipped, unknown
   topics are created, and you get a row-by-row error report.
4. **Retire the old ones**: Admin → Question Bank → filter Subject = X → tick the old
   direct-recall questions → *Deactivate* (not delete — results that used them stay intact).
   Deactivated questions are never served again.
5. **Test**: write one mock in that subject as a student. Check the pace meter — applied
   questions should feel like ~40 s each.

Do one subject per week. Order: **Use of English → Chemistry → Physics → Biology →
Economics → Government → Commerce → Literature → CRS → IRS.**

## Style rules the prompt enforces

- Max **10 of 40** questions may be direct recall. The rest must make the student *do* something.
- Sciences / Maths / Economics: real numbers to calculate, data described in words to read,
  an equation to balance, an outcome to predict. Hard questions = two steps.
- Use of English: passages of 4–6 sentences with 5 questions each; sentence completion;
  nearest/opposite in meaning **in context**; stress/emphasis; oral forms.
- Arts / Religion / Commerce / Government: a quote, a case or a situation to interpret or
  apply a principle to. Not definitions.
- JAMB-length: question + options readable in ~40 seconds (Post-UTME ~60 s, WAEC ~70 s).
- Four options, one unambiguous answer, correct letters balanced, no "all/none of the above".
- Explanation = the *working* or the *reasoning*, 1–3 sentences, teaches the method.

## The master prompt (copy; replace the CAPS)

```
You are a Nigerian EXAM examiner (EXAM = JAMB UTME / WAEC SSCE / university Post-UTME).
Write 40 original multiple-choice questions on SUBJECT, topic "TOPIC", at the real EXAM
standard and syllabus. Mix: 16 Easy, 16 Medium, 8 Hard.

STYLE — this matters most. EXAM tests application, not memory. At most 10 questions may be
direct recall ("What is…", "Which of the following is…"). The other 30 must present a
situation the student has to work through:
SUBJECT-SPECIFIC RULE (see list below).
Hard questions need two steps of reasoning or calculation. Keep each question readable in
about 40 seconds. Use Nigerian names, places, prices in naira and everyday contexts.

FORMAT — exactly four options A–D, one unambiguous correct answer, correct letters spread
evenly, never "all of the above" / "none of the above". The explanation must show the
working or the reasoning in 1–3 sentences so a student learns the method.

Output ONLY a CSV with this header and one question per row, no numbering, no extra text:
Exam Type,Subject,Topic,Question,Option A,Option B,Option C,Option D,Answer,Explanation,Difficulty
Use "EXAM" for Exam Type, "SUBJECT" for Subject and "TOPIC" for Topic in every row.
Wrap any field that contains a comma in double quotes.
```

### Subject-specific rule (paste in place of SUBJECT-SPECIFIC RULE)

| Subject | Rule |
|---|---|
| Mathematics | Word problems with numbers (money, distance, ages, sets, probability), expressions to simplify, equations to solve, a described graph/table to read. Show the working in the explanation. |
| Physics | A described physical situation with quantities and SI units to calculate (e.g. "A 2 kg block is pulled with 10 N…"), a circuit or graph described in words, a prediction of what happens when a quantity changes. |
| Chemistry | Mole/mass/volume calculations, equations to balance or complete, a described experiment whose result must be predicted or explained, periodic-trend reasoning, IUPAC naming from a described structure. |
| Biology | A described experiment or observation to interpret, a genetics cross to work out, a food-chain/population scenario, a diagram described in words to identify parts or function, cause→effect reasoning in physiology. |
| Economics | Numerical questions (elasticity, national income, cost/revenue tables, exchange rates in naira), a described demand/supply graph, a Nigerian policy situation to analyse. |
| Use of English | 4 passages of 4–6 sentences with 5 comprehension/inference/vocabulary-in-context questions each (put the passage inside the Question cell of every one of its 5 questions); the rest: sentence completion, nearest-in-meaning and opposite-in-meaning for an underlined word in a sentence, stress and emphatic stress, oral English (vowel/consonant sounds). No grammar-definition questions. |
| Literature in English | A quoted line or described scene from the current JAMB set texts or general literary situations; identify device, theme, character motive, narrative technique or effect. Not "what is a metaphor". |
| Government | A political scenario (a bill, an election dispute, a coup, a court ruling, a federal/state clash) to analyse with concepts and Nigerian constitutional facts; comparisons of systems in context. |
| Commerce | Business situations: a trader's costs and profit, a described document (invoice, bill of lading) to identify, insurance/banking cases, a described transport or communication choice to justify. |
| CRS | A described biblical event or quoted verse; ask for the lesson, the character's motive, the consequence, or how the principle applies to a modern situation. |
| IRS | A described situation or quoted ayah/hadith; ask for the ruling, the moral lesson, the pillar/principle involved, or the correct action. |

## Post-UTME and WAEC

- Same routine, same importer. Put **WAEC** or **POST-UTME** in the Exam Type column.
- Post-UTME: longer, slightly harder than JAMB (universities allow ~60 s per question).
  Add university-specific banks later via Admin → Post-UTME → courses.
- WAEC: stays "Coming soon" for students until you have real WAEC-standard questions; then
  set `WAEC_ENABLED=1` in `~/.prepnova.env` and run `python3 setup.py reload`.

## Targets

| Milestone | Per subject | What it means |
|---|---|---|
| Now | ~320 mostly direct | Works, but testers notice |
| Standard | 400 applied-style, old ones deactivated | Real exam feel |
| Serious | 700+ with 3+ years of past-question coverage per topic | No repeats across a student's 5+ mocks |
