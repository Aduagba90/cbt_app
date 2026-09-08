# Growing the question bank to 700–1,000 per subject

Mock exams and Practice Mode draw from the **same bank**, so every question you upload
serves both. Target: 700–1,000 active questions per live JAMB subject.

## The workflow (repeat per subject)

1. **Admin → Import → Download template.** The Excel file has three sheets:
   - `Questions` — the rows to fill (two sample rows show the format).
   - `Subjects & Topics` — every live subject, its exact spelling, current topics and counts.
     Give this sheet to your writers so subject names match.
   - `Instructions` — the rules below, in the file itself.
2. **Fill rows** (one question per row, 11 columns). New topic names are created
   automatically, so writers may add topics that are missing.
3. **Admin → Import → upload the file.** You get a summary: imported / duplicates skipped /
   errors with row numbers. Fix the error rows and re-upload the *same* file — already
   imported rows are skipped as duplicates, so nothing is inserted twice.
4. Questions are live in mocks and practice immediately.

Aim for batches of 100–500 rows per file so mistakes are easy to trace.

## Column rules

| Column | Rule |
|---|---|
| Exam Type | `JAMB` (WAEC / POST-UTME later) |
| Subject | exact name from `Subjects & Topics` (e.g. `Use of English`) |
| Topic | existing topic preferred; new names are accepted and created |
| Question | full text; put comprehension passages inside the question |
| Option A–D | four distinct options, no `A.` prefixes |
| Answer | one letter `A`–`D` |
| Explanation | 1–3 sentences teaching *why*; shown in corrections |
| Difficulty | `Easy` / `Medium` / `Hard` (≈40/40/20) |

## Where the questions come from

| Route | Cost (approx.) | Speed | Notes |
|---|---|---|---|
| Content writers (corpers, undergrads, tutors) typing past questions | ₦20–50 per question | 2–3 weeks with 3–4 people | Best quality per naira; give each person one subject + the template |
| AI-drafted, teacher-checked | Mostly checking time | Days | Good for Maths/Sciences; weaker for Literature set texts and English passages. **Every answer must be verified.** |
| Licensed past-question database | Varies | Fastest | Ask the vendor for CSV/Excel; check licence and answer accuracy |

Most teams combine the first two: AI drafts → cheap human checkers verify → upload.

## Prompt for AI drafting (copy, replace the CAPS)

```
You are a Nigerian JAMB UTME examiner writing SUBJECT questions for the topic "TOPIC".
Write 40 original multiple-choice questions at JAMB UTME standard, following the current
JAMB syllabus. Mix: 16 Easy, 16 Medium, 8 Hard. Each question has exactly four options
A–D with one unambiguous correct answer; balance the correct letters roughly evenly.
Avoid "all of the above" and "none of the above". After each question give a one- to
three-sentence explanation that teaches why the answer is right.

Output ONLY a table with these exact columns, one question per row, no numbering:
Exam Type | Subject | Topic | Question | Option A | Option B | Option C | Option D | Answer | Explanation | Difficulty
Use "JAMB" for Exam Type, "SUBJECT" for Subject and "TOPIC" for Topic in every row.
```

Paste the table into the `Questions` sheet (Excel: Data → Text to Columns with `|` as the
delimiter, or ask the AI for CSV and open it). Have a subject teacher check every answer
before upload.

## Priorities (from the current counts)

Live subjects and what they need to reach 700:
CRS 180 · Chemistry 260 · Mathematics 380 · Economics 380 · IRS 380 · Physics 400 ·
Biology 400 · Use of English 440 · Literature 460 · Government 460 · Commerce 460.

Subjects with 0 questions (Geography, Accounting, History, Yoruba, Igbo, Hausa, French,
Fine Arts, Music, Home Economics, Civic Education) are a later phase; add topics as you go.

Also: about 220 Use of English explanations are generic placeholders. Replacing them is
an edit job in Admin → Question bank, or re-upload corrected rows after deleting the old ones.
