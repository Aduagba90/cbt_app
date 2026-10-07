"""PrepNova PDF study packs — content + on-the-fly PDF generation.

Two generators:
  build_lekki_pdf()                  -> The Lekki Headmaster study pack (content below)
  build_past_questions_pdf(conn, …)  -> past-style question packs from questions_v2

PDFs are generated at download time (no files stored), watermarked with the
PrepNova brand and a final CTA page pointing readers to the app.
"""
from io import BytesIO
from xml.sax.saxutils import escape as _esc

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

NAVY = colors.HexColor("#0f1f3d")
GOLD = colors.HexColor("#f2b705")
GREEN = colors.HexColor("#0b7a4b")
GREY = colors.HexColor("#6b7280")
LIGHT = colors.HexColor("#eef2f9")


# ---------------------------------------------------------------------------
# The Lekki Headmaster (Kabir Alabi Garba) — JAMB UTME 2026 recommended novel
# Content assembled from widely published chapter summaries and study guides.
# ---------------------------------------------------------------------------

LEKKI_TITLE = "The Lekki Headmaster — Complete JAMB 2026 Study Pack"

LEKKI_ABOUT = [
    "The Lekki Headmaster is a novel by the Nigerian writer Kabir Alabi Garba. For the "
    "2026 Unified Tertiary Matriculation Examination (UTME), JAMB adopted it as the "
    "recommended text for Use of English, replacing The Life Changer (which served from "
    "2022 to 2024). Every UTME candidate answers questions from the novel in the Use of "
    "English paper — regardless of the course or subject combination they chose.",
    "The novel follows Mr. Adewale Bepo, the respected principal of Stardom Schools, "
    "Lekki, Lagos, as he wrestles with the decision to leave Nigeria and join his family "
    "in the United Kingdom. It is a story about education, integrity, family pressure and "
    "the pull of 'Japa' — and it ends with one of the most memorable twists in recent "
    "JAMB texts.",
]

LEKKI_CHAPTERS = [
    ("1", "Dusk", "During a morning assembly at Stardom Schools, the usually cheerful "
     "principal, Mr. Bepo Adewale, walks to the podium but cannot speak; he drops the "
     "microphone and breaks down in tears before the shocked students and staff. The "
     "Managing Director, Mrs. Ibidun Gloss, and the Vice Principal, Mrs. Grace Apeh, "
     "hurry to console him. The breakdown is especially shocking because the school had "
     "just celebrated a 90 percent success rate in the WASSCE, rewarding its best "
     "teachers with cash prizes."),
    ("2", "The Enticement", "After days of distress, Bepo reveals his dilemma: he is "
     "relocating to the United Kingdom to join his wife, Seri, a nurse, and their two "
     "daughters, Nike and Kike, who already live there. The separation has strained the "
     "marriage and his wife has pushed him to leave. Bepo, now 51, had planned to retire "
     "at 55, run his own business and perhaps establish his own school. Years earlier he "
     "had spent four years as head of the primary arm, Stardom Kiddies, and his charisma "
     "and problem-solving earned him the nickname \u201cThe Lekki Headmaster\u201d."),
    ("3", "Migration Tales", "This chapter surveys Nigeria's 'Japa' wave. Bepo recalls "
     "Mr. Nku, who vanished abroad after taking a \u20a62 million loan from the school's "
     "cooperative society, and a driver who tried to sell a school bus to fund his son's "
     "education overseas. A former Home Economics teacher, Sola, shares her own "
     "migration story. The chapter also shows the harsh side of life abroad: Jare, a "
     "former banker, breaks down while caring for an elderly couple in London, and Hope, "
     "an accountant, sees his marriage strained after relocating."),
    ("4", "A Case of Visa Denied", "Bepo receives a late-night call from Mrs. Ignatius, "
     "a Stardom parent. Her family's relocation plans have collapsed: a mandatory DNA "
     "test during the visa process revealed that her husband is not the biological "
     "father of one of their three children, Favour, an SSS2 student at Stardom. The "
     "chapter also follows Mrs. Ladele, a devoted Nollywood fan, whose daughter Bibi is "
     "haunted by nightmares about her government teacher, Mr. Ayesoro, a man with deep "
     "tribal marks; he is eventually transferred to another division of the Stardom "
     "organisation."),
    ("5", "Snake in the Roof", "During the long break, the MD, Mrs. Ibidun Gloss, takes "
     "a walk instead of retreating to her office and discovers that a piece of land "
     "Stardom acquired two years earlier has become a secret car park for staff. The "
     "security guard, Jombo, explains that teachers hide their cars there — some 17 "
     "vehicles, including big cars. Suspecting financial malpractice, she summons Bepo "
     "and the accountant, Mr. Jeremi Amos, who explains the staff bought their cars "
     "through loans from the Stardom Cooperative Society, repaid from their salaries."),
    ("6", "Comes vs Come", "It is Open Day at Stardom Schools. Teachers look forward to "
     "gifts from parents but also brace for complaints. A parent, Mr. Guta, accuses the "
     "English teacher, Mr. Fafore, of a grammatical error involving \u201cAde as well as "
     "Jide come/comes\u201d and demands his dismissal. Bepo calmly proves that the "
     "teacher's usage was correct, and Mr. Fafore is vindicated — showing Bepo's "
     "fairness and the vulnerability of teachers to powerful parents."),
    ("7", "Ritualists", "In flashback, Bepo remembers his former school, Beesway Group "
     "of School, on the outskirts of Lagos — its name itself grammatically wrong "
     "(\u201cGroup of School\u201d instead of \u201cGroup of Schools\u201d). When Bepo "
     "pointed out the error, the director, Mr. Egi Meko, refused to change it, claiming "
     "the name was divinely inspired. One night Bepo witnessed men performing a ritual "
     "with a cow; when he confronted them, one struck him on the head — and the group "
     "included the director himself. Bepo left Beesway. The chapter also recalls Mr. "
     "Ogo, a parent at Bepo's own failed school venture, Fruitful Future School, who "
     "suggested Bepo perform a ritual to attract more pupils and withdrew his child when "
     "Bepo refused."),
    ("8", "Missions Unaccomplished", "Bepo reflects on matters he will leave "
     "unresolved. Two students' families — Banky's and Tosh's — have been locked in a "
     "three-year legal dispute that began during a Social Prefect campaign, when Banky "
     "called Tosh \u201cthe son of an ex-convict\u201d. Stardom is also preparing "
     "democratic prefect elections (forms cost \u20a650,000 for Head Boy and Head Girl, "
     "\u20a640,000 for deputies and \u20a625,000 for other positions). Bepo worries "
     "about the Invention Club's Breath Project — a five-year-old initiative to build a "
     "phone from recycled panels and chips, supported by the NGO Life Grid — which his "
     "departure could derail."),
    ("9", "Laughing Waterfalls", "A celebration of Bepo's excursion programme, which "
     "took Stardom students across Nigeria — to the Ikogosi Warm Springs, the Point of "
     "No Return in Badagry and the Black Heritage Museum. Standing before relics of the "
     "transatlantic slave trade, Bepo draws a haunting parallel between the forced "
     "migration of the past and today's voluntary 'Japa' migration, reinforcing the "
     "novel's themes of heritage and national purpose."),
    ("10", "Passport Pains", "Bepo endures Nigeria's bureaucracy to renew his "
     "passport, dealing with agents and delays at the Ibadan immigration office; his "
     "NIN also needs validation at a separate office, and network glitches add weeks "
     "of delay that threaten his travel date. He notes, with some appreciation, the "
     "improved Lagos–Ibadan Expressway, and reflects on the irony of a country growing "
     "more religious while its systems remain difficult."),
    ("11", "Point of No Return", "Stardom Schools hosts a three-day farewell for "
     "Bepo. A grand banner across the hall reads \u201cFor He Gave Stardom His Very "
     "Best\u201d. The events include a humorous staff-versus-students football match, a "
     "debate between the arts and the sciences, and cultural performances that stir "
     "deep emotions — a testament to the love the school community has for him."),
    ("12", "Dawn", "Bepo prepares meticulously for his flight, determined not to "
     "repeat a past mistake of missing one. The school community grieves quietly. Then "
     "comes the novel's famous twist: on the Monday after his supposed departure, Bepo "
     "walks back into Stardom Schools and declares that he cannot leave — his heart and "
     "his mission remain at the school. Students and staff erupt in jubilation, singing "
     "the school's victory song."),
]

LEKKI_CHARACTERS = [
    ("Mr. Adewale Bepo", "The protagonist; principal of Stardom Schools, Lekki. Humane, "
     "humorous and firm; nicknamed \u201cThe Lekki Headmaster\u201d (students also call "
     "him \u201cPrincipoo\u201d). His decision to relocate — and his final return — "
     "drives the novel."),
    ("Mrs. Ibidun Gloss", "The Managing Director of Stardom Schools; admires Bepo's "
     "leadership and manages the assembly crisis and the car-park discovery discreetly."),
    ("Mrs. Grace Apeh", "The Vice Principal of Stardom Schools."),
    ("Seri Bepo", "Bepo's wife, a nurse who has already relocated to the UK with their "
     "daughters; her pressure forces Bepo's decision."),
    ("Nike and Kike", "Bepo's two daughters, living in the UK with their mother."),
    ("Mr. Jeremi Amos", "The school accountant; explains the staff car loans from the "
     "cooperative society."),
    ("Jombo", "The security guard who reveals the secret staff car park to the MD."),
    ("Mr. Fafore", "The English teacher falsely accused of a grammatical error on Open "
     "Day; defended by Bepo and vindicated."),
    ("Mr. Guta", "The parent whose complaint nearly cost Mr. Fafore his job."),
    ("Mrs. Ignatius", "The parent whose visa plans collapse after a DNA test shows her "
     "husband is not the biological father of Favour."),
    ("Favour", "Mrs. Ignatius's daughter, an SSS2 student at Stardom."),
    ("Mr. Ayesoro", "The government teacher with deep tribal marks who frightened Bibi; "
     "transferred to another division."),
    ("Bibi", "Mrs. Ladele's daughter, who has nightmares about Mr. Ayesoro."),
    ("Mrs. Ladele", "A devoted Nollywood fan; Bibi's mother."),
    ("Mr. Egi Meko", "Director of Beesway Group of School, where Bepo previously "
     "worked; insisted his school's ungrammatical name was divinely inspired and was "
     "implicated in a midnight cow ritual."),
    ("Mr. Ogunwale", "Bepo's landlord and Jide's grandfather; sympathetic to Bepo's "
     "relocation."),
    ("Jide", "Mr. Ogunwale's grandson, mentored by Bepo."),
    ("Banky and Tosh", "Two students whose families are locked in a three-year legal "
     "feud that began with an insult during a prefect campaign."),
    ("Mr. Nku", "The man who vanished abroad after taking a \u20a62 million cooperative "
     "loan from Stardom."),
    ("Sola", "Former Home Economics teacher at Stardom who shares her migration "
     "experience."),
    ("Jare and Hope", "Nigerians abroad whose stories show the harsh side of "
     "migration — Jare cares for an elderly couple in London; Hope's marriage and "
     "finances collapse under the strain of relocation."),
]

LEKKI_THEMES = [
    ("The 'Japa' wave versus patriotism", "The novel constantly weighs the lure of a "
     "'better life' abroad against the duty to build Nigeria. Bepo's final return is "
     "Garba's answer: purpose is found where you are needed, not where life is "
     "easiest."),
    ("Leadership and integrity", "Bepo defends an unjustly accused teacher, refuses "
     "ritual shortcuts, and leads with fairness — a contrast to Mr. Egi Meko's "
     "superstition and the corruption the novel exposes."),
    ("Dedication and sacrifice", "Two decades of service, the emotional assembly "
     "breakdown, and a farewell banner that reads \u201cFor He Gave Stardom His Very "
     "Best\u201d all testify to the cost and dignity of devotion to education."),
    ("Education as nation-building", "Excursions to heritage sites, the Invention "
     "Club's Breath Project and the prefect elections present school as a rehearsal "
     "for citizenship."),
    ("Corruption and broken systems", "Passport bureaucracy, loan absconders, an "
     "attempted bus theft and ritual-for-success practices show the pressures that "
     "push Nigerians abroad."),
    ("Family separation and pressure", "Seri's ultimatum, the Ignatius family's DNA "
     "crisis and Hope's collapsing marriage show how migration strains families."),
    ("Cultural pride and heritage", "The Black Heritage Museum and the Point of No "
     "Return connect present-day migration to the slave trade and call for national "
     "self-knowledge."),
    ("Mental health and emotional pressure", "Bepo's public tears open a rare "
     "conversation about the emotional burden carried by leaders and teachers."),
]

LEKKI_TIPS = [
    "JAMB typically asks about 10 questions from the recommended novel inside the Use "
    "of English paper — know the plot order, the names and the numbers.",
    "Learn the chapter titles and their order (Dusk \u2192 Dawn); JAMB loves asking "
    "which chapter an event happened in.",
    "Master the small facts: sums of money (\u20a62 million loan, prefect form prices), "
    "places (Ikogosi, Badagry, Ibadan) and full names.",
    "Character-and-role matching is the most common question style — drill the "
    "character table until every name is automatic.",
    "Be ready for 'why' questions on Bepo's final decision — connect it to the "
    "novel's themes, not just the plot.",
    "Practise full Use of English mocks in the PrepNova CBT app to time yourself on "
    "the real paper.",
]

# (question, [A-D], correct letter, explanation)
LEKKI_QUESTIONS = [
    ("Mr. Bepo Adewale is the principal of which school?",
     ["Stardom Schools, Lekki", "Beesway Group of School", "Fruitful Future School", "Stardom Hub College"], "A",
     "Bepo is the beloved principal of Stardom Schools in Lekki, Lagos."),
    ("What is the title of Chapter 1 of the novel?",
     ["Dawn", "Dusk", "The Enticement", "Migration Tales"], "B",
     "Chapter 1 is titled 'Dusk', where Bepo breaks down at assembly."),
    ("Why does Mr. Bepo break down in tears at the assembly?",
     ["He was sacked", "He is seriously ill", "He must leave the school to relocate abroad", "He lost his wallet"], "C",
     "He is distressed because he has decided to relocate to the UK and leave Stardom."),
    ("Who is the Managing Director of Stardom Schools?",
     ["Mrs. Grace Apeh", "Mrs. Ibidun Gloss", "Mrs. Ladele", "Seri Bepo"], "B",
     "Mrs. Ibidun Gloss is the MD; Mrs. Apeh is the Vice Principal."),
    ("What nickname did Bepo earn from his years at Stardom?",
     ["Principoo only", "The Lekki Headmaster", "Father of Stardom", "Mr. Integrity"], "B",
     "His charisma and problem-solving earned him 'The Lekki Headmaster'; students also call him 'Principoo'."),
    ("Bepo's wife, who already lives in the UK, is called…",
     ["Nike", "Kike", "Seri", "Sola"], "C",
     "Seri, a nurse, relocated with their daughters Nike and Kike."),
    ("Bepo's two daughters are named…",
     ["Nike and Kike", "Bibi and Favour", "Seri and Sola", "Grace and Ibidun"], "A",
     "Nike and Kike live in the UK with their mother, Seri."),
    ("How old is Bepo, and at what age had he planned to retire?",
     ["49 at 55", "51 at 55", "51 at 60", "55 at 65"], "B",
     "He is 51 and had planned to retire at 55 to run his own business."),
    ("Bepo's first school venture, which collapsed, was called…",
     ["Beesway Group of School", "Fruitful Future School", "Stardom Kiddies", "Life Grid School"], "B",
     "Fruitful Future School collapsed; he later joined Stardom."),
    ("Before becoming principal, Bepo headed Stardom's primary arm called…",
     ["Stardom Kiddies", "Stardom Hub", "Stardom Angels", "Stardom Early Years"], "A",
     "He spent four years as head of Stardom Kiddies."),
    ("What success rate had Stardom just celebrated before Bepo's breakdown?",
     ["70 percent", "80 percent", "90 percent", "100 percent"], "C",
     "The school celebrated 90 percent success in the WASSCE and rewarded teachers."),
    ("Mr. Nku is remembered in the novel for…",
     ["Selling a school bus", "Vanishing with a \u20a62 million cooperative loan", "Failing the visa interview", "Striking Bepo on the head"], "B",
     "He took a \u20a62 million loan from the cooperative society and disappeared abroad."),
    ("The school driver's offence in 'Migration Tales' was that he…",
     ["Stole exam papers", "Tried to sell a school bus to fund his son's education abroad", "Ran away with school fees", "Falsified the accounts"], "B",
     "He confessed to attempting to sell the school bus for his son's tuition."),
    ("Who is the Vice Principal of Stardom Schools?",
     ["Mrs. Grace Apeh", "Mrs. Ignatius", "Mrs. Gloss", "Mrs. Ogunwale"], "A",
     "Mrs. Grace Apeh is the Vice Principal."),
    ("In 'Snake in the Roof', the MD discovers that staff secretly…",
     ["Sold school property", "Parked 17 vehicles on the school's land", "Ran a private school", "Stole library books"], "B",
     "Seventeen staff vehicles were hidden on land Stardom acquired two years earlier."),
    ("Which security guard reveals the secret car park to the MD?",
     ["Jombo", "Jeremi", "Jide", "Jare"], "A",
     "Jombo, the security guard, explains that teachers hide their cars there."),
    ("The accountant of Stardom Schools is…",
     ["Mr. Jeremi Amos", "Mr. Egi Meko", "Mr. Fafore", "Mr. Ogunwale"], "A",
     "Mr. Jeremi Amos explains the cooperative car loans."),
    ("Mrs. Ignatius's relocation plans collapse because…",
     ["Her visa was denied", "A DNA test revealed her husband is not Favour's biological father", "She lost her job", "Her husband fell ill"], "B",
     "The mandatory DNA test during the visa process exposed the paternity of Favour."),
    ("Favour, the SSS2 student at the centre of the Ignatius family crisis, is…",
     ["Mrs. Ignatius's niece", "Mrs. Ignatius's daughter", "Bibi's sister", "Tosh's cousin"], "B",
     "Favour is one of Mrs. Ignatius's three children."),
    ("Bibi's nightmares are about which teacher?",
     ["Mr. Fafore", "Mr. Ayesoro", "Mr. Egi Meko", "Mr. Nku"], "B",
     "Mr. Ayesoro, the government teacher with deep tribal marks, frightened Bibi."),
    ("On Open Day, which parent accused Mr. Fafore of a grammatical error?",
     ["Mr. Guta", "Mr. Ogunwale", "Mr. Ogo", "Mr. Jombo"], "A",
     "Mr. Guta complained about 'Ade as well as Jide come/comes'."),
    ("How does Bepo handle the accusation against Mr. Fafore?",
     ["He sacks him quietly", "He suspends him for a week", "He proves the teacher's usage correct and defends him", "He refers it to the MD"], "C",
     "Bepo's fair handling vindicates Fafore — a key moment of leadership."),
    ("The grammatical problem in Beesway's name was that it read…",
     ["'Group of Schools' instead of 'Group of School'", "'Group of School' instead of 'Group of Schools'", "'College' instead of 'School'", "'Beesway' was misspelt"], "B",
     "Bepo insisted on 'Beesway Group of Schools'; the director refused."),
    ("Who is the director of Beesway Group of School?",
     ["Mr. Egi Meko", "Mr. Jeremi Amos", "Mr. Ogo", "Mr. Guta"], "A",
     "Mr. Egi Meko claimed the ungrammatical name was divinely inspired."),
    ("What did Bepo witness at night at Beesway that made him leave?",
     ["A robbery", "A ritual involving a cow", "An exam malpractice ring", "A fight between teachers"], "B",
     "He confronted the men and was struck on the head; the director was among them."),
    ("Mr. Ogo, a parent at Fruitful Future School, withdrew his child because Bepo…",
     ["Raised the school fees", "Refused to perform a ritual to attract pupils", "Sacked a teacher", "Moved the school"], "B",
     "Ogo suggested a supernatural ritual for enrolment; Bepo refused."),
    ("The three-year legal dispute in the novel is between the families of…",
     ["Banky and Tosh", "Jide and Bibi", "Fafore and Guta", "Nku and Jombo"], "A",
     "The feud began when Banky called Tosh 'the son of an ex-convict' during a prefect campaign."),
    ("The insult that started the students' feud was made during a campaign for…",
     ["Head Boy", "Social Prefect", "Sports Prefect", "Head Girl"], "B",
     "It happened during the Social Prefect campaign on Speech Day."),
    ("How much did the form for Head Boy or Head Girl cost in the prefect elections?",
     ["\u20a625,000", "\u20a640,000", "\u20a650,000", "\u20a6100,000"], "C",
     "Head Boy/Girl forms cost \u20a650,000; deputies \u20a640,000; others \u20a625,000."),
    ("The Invention Club's project to build a phone from recycled materials is called…",
     ["The Breath Project", "The Life Grid Project", "The Dawn Project", "The Stardom Project"], "A",
     "The Breath Project is five years old and supported by the NGO Life Grid."),
    ("The NGO supporting the students' phone project is called…",
     ["Life Grid", "Breath Foundation", "Stardom Hub", "Future Fruit"], "A",
     "Life Grid supports the Invention Club's Breath Project."),
    ("Which of these places did Stardom students visit on Bepo's excursions?",
     ["Olumo Rock", "Ikogosi Warm Springs", "Zuma Rock", "Yankari Games Reserve"], "B",
     "Excursions included Ikogosi Warm Springs, the Point of No Return and the Black Heritage Museum."),
    ("Standing before the slave-trade relics, Bepo compares the past to…",
     ["Colonial taxation", "Modern 'Japa' migration", "The civil war", "The slave trade of the future"], "B",
     "He draws a parallel between forced migration then and voluntary migration now."),
    ("Bepo renewed his passport at the immigration office in…",
     ["Lagos", "Ibadan", "Abuja", "Abeokuta"], "B",
     "The Ibadan office, with agents, delays and NIN validation troubles."),
    ("What delayed Bepo's travel date in 'Passport Pains'?",
     ["A missing birth certificate", "NIN validation requiring a separate office with network glitches", "His wife's illness", "A court case"], "B",
     "The NIN validation added weeks of delay."),
    ("The banner at Bepo's farewell read…",
     ["'Farewell, Our Leader'", "'For He Gave Stardom His Very Best'", "'The Best Headmaster in Lagos'", "'Dusk to Dawn'"], "B",
     "The three-day farewell carried the banner 'For He Gave Stardom His Very Best'."),
    ("Which event was part of Bepo's farewell ceremony?",
     ["A staff-versus-students football match", "A wedding", "A book launch", "A political rally"], "A",
     "The farewell included the football match, an arts-versus-sciences debate and cultural performances."),
    ("How does the novel end?",
     ["Bepo flies to the UK", "Bepo retires quietly", "Bepo returns to Stardom and stays", "The school closes down"], "C",
     "In 'Dawn' (Chapter 12) he returns, declaring his heart and mission remain at Stardom."),
    ("Which is the correct order of the first three chapter titles?",
     ["Dusk, The Enticement, Migration Tales", "Dawn, Dusk, The Enticement", "The Enticement, Dusk, Dawn", "Dusk, Migration Tales, The Enticement"], "A",
     "Chapter 1 'Dusk', Chapter 2 'The Enticement', Chapter 3 'Migration Tales'."),
    ("Jare's story in London shows that migration can lead to…",
     ["Instant wealth", "Loss of status and emotional strain", "Political power", "A better marriage"], "B",
     "The former banker broke down while caring for an elderly couple."),
    ("Hope's experience abroad involved…",
     ["A profitable business", "A strained marriage after his wife stopped supporting him financially", "A new degree", "Deportation"], "B",
     "The accountant's marriage and finances collapsed under relocation strain."),
    ("Sola, who shares her migration story with Bepo, was formerly a…",
     ["Home Economics teacher", "Nurse", "Banker", "Accountant"], "A",
     "She taught Home Economics at Stardom before relocating."),
    ("Jide, who is mentored by Bepo, is the grandson of…",
     ["Mr. Ogunwale, Bepo's landlord", "Mr. Egi Meko", "Mr. Guta", "Mr. Jeremi Amos"], "A",
     "Mr. Ogunwale is Bepo's landlord and Jide's grandfather."),
    ("The novel was written by…",
     ["Khadija Abubakar Jalli", "Kabir Alabi Garba", "Chinua Achebe", "Wale Okediran"], "B",
     "Kabir Alabi Garba wrote The Lekki Headmaster."),
    ("The Lekki Headmaster replaced which novel as JAMB's recommended text?",
     ["The Concubine", "The Life Changer", "Sweet Sixteen", "Without a Silver Spoon"], "B",
     "It replaced The Life Changer (used from 2022 to 2024)."),
    ("The central conflict of the novel is best described as…",
     ["A land dispute", "Bepo's struggle between relocating abroad and his mission at home", "A student strike", "An election crisis"], "B",
     "The 'Japa' versus purpose conflict drives the entire plot."),
    ("The major theme of 'Snake in the Roof' is…",
     ["Sportsmanship", "Suspicion and misunderstanding versus transparency", "Religion", "Romance"], "B",
     "The MD's suspicion of corruption is resolved by honest explanation."),
    ("Stardom Schools is the backbone of a wider group that includes…",
     ["A bank", "A property wing called Stardom Hub", "A transport company", "A farm"], "B",
     "The Stardom Group of Companies includes the Stardom Hub property wing."),
    ("The novel's style is notable for balancing…",
     ["Poetry and prose", "Humour and seriousness", "English and Yoruba", "Past and future tenses only"], "B",
     "Garba mixes warmth and humour with weighty social issues."),
    ("Bepo's final decision teaches that…",
     ["Money answers all things", "Purpose and service can outweigh the lure of migration", "Education is a scam", "Family does not matter"], "B",
     "His return affirms dedication to nation and calling."),
    ("A recurring historical parallel in the novel links migration to…",
     ["The transatlantic slave trade", "The industrial revolution", "World War II", "Colonial taxation"], "A",
     "The Black Heritage Museum and Point of No Return anchor this parallel."),
]


# ---------------------------------------------------------------------------
# PDF generation
# ---------------------------------------------------------------------------

def _styles():
    st = getSampleStyleSheet()
    return {
        "brand": ParagraphStyle("brand", parent=st["Title"], fontSize=22, textColor=NAVY, spaceAfter=2),
        "sub": ParagraphStyle("sub", parent=st["Normal"], fontSize=9.5, textColor=GREY),
        "h1": ParagraphStyle("h1", parent=st["Heading1"], fontSize=15, textColor=NAVY, spaceBefore=14, spaceAfter=6),
        "h2": ParagraphStyle("h2", parent=st["Heading2"], fontSize=12, textColor=GREEN, spaceBefore=10, spaceAfter=4),
        "chap": ParagraphStyle("chap", parent=st["Heading3"], fontSize=11.5, textColor=NAVY, spaceBefore=10, spaceAfter=3),
        "body": ParagraphStyle("body", parent=st["Normal"], fontSize=10, leading=14.5),
        "q": ParagraphStyle("q", parent=st["Normal"], fontSize=10, leading=14, spaceBefore=7),
        "opt": ParagraphStyle("opt", parent=st["Normal"], fontSize=9.5, leading=13, leftIndent=14),
        "key": ParagraphStyle("key", parent=st["Normal"], fontSize=9.5, leading=13, spaceBefore=3),
        "cta": ParagraphStyle("cta", parent=st["Normal"], fontSize=11, leading=16, alignment=1, textColor=NAVY),
        "tag": ParagraphStyle("tag", parent=st["Normal"], fontSize=10, textColor=colors.white, alignment=1),
    }


def _doc(buf, title):
    return SimpleDocTemplate(buf, pagesize=A4, leftMargin=17 * mm, rightMargin=17 * mm,
                             topMargin=15 * mm, bottomMargin=15 * mm, title=title,
                             author="PrepNova CBT")


def _cover(story, s, title, subtitle, tagline):
    banner = Table([[Paragraph("PrepNova CBT — Study Pack", s["tag"])]],
                   colWidths=[176 * mm], rowHeights=[12 * mm])
    banner.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY),
                                ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    story += [banner, Spacer(1, 18), Paragraph(title, s["brand"]), Spacer(1, 4),
              Paragraph(subtitle, s["sub"]), Spacer(1, 10),
              Paragraph(tagline, s["body"]), Spacer(1, 6)]


def _final_cta(story, s, site_url):
    story += [PageBreak(), Spacer(1, 30),
              Paragraph("Practise the full paper — free", s["h1"]),
              Paragraph("This pack covers the knowledge. To score high, you also need exam-day "
                        "speed and nerves of steel. The PrepNova CBT app gives you the real "
                        "experience: full timed JAMB, WAEC and Post-UTME mocks on your phone or "
                        "laptop, instant corrections, performance analytics and a free 7-day "
                        "trial.", s["body"]),
              Spacer(1, 8), Paragraph(f"<b>{site_url}</b> — Practice. Prepare. Pass.", s["cta"]),
              Spacer(1, 6), Paragraph("This PDF is for the personal use of the buyer. Please do not "
                                      "redistribute — support Nigerian-built learning tools.", s["sub"])]


def build_lekki_pdf(site_url):
    """The Lekki Headmaster study pack: summaries, characters, themes, 50 questions."""
    s = _styles()
    buf = BytesIO()
    story = []
    _cover(story, s, LEKKI_TITLE,
           "JAMB UTME 2026 Use of English — recommended novel by Kabir Alabi Garba",
           "Chapter summaries \u00b7 character guide \u00b7 themes \u00b7 exam tips \u00b7 50 practice "
           "questions with answers. Compiled for PrepNova CBT.")
    story += [Paragraph("About this pack", s["h1"])]
    for para in LEKKI_ABOUT:
        story.append(Paragraph(_esc(para), s["body"]))
    story += [Paragraph("Chapter-by-chapter summary", s["h1"])]
    for num, name, text in LEKKI_CHAPTERS:
        story += [Paragraph(f"Chapter {num}: {name}", s["chap"]), Paragraph(_esc(text), s["body"])]
    story += [PageBreak(), Paragraph("Character guide", s["h1"]),
              Paragraph("Drill this table — JAMB's favourite question style is matching names to roles.", s["body"])]
    rows = [[Paragraph("<b>Name</b>", s["key"]), Paragraph("<b>Who they are</b>", s["key"])]]
    for name, role in LEKKI_CHARACTERS:
        rows.append([Paragraph(f"<b>{_esc(name)}</b>", s["key"]), Paragraph(_esc(role), s["key"])])
    tbl = Table(rows, colWidths=[42 * mm, 134 * mm])
    tbl.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LIGHT),
                             ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                             ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story += [tbl, Paragraph("Themes", s["h1"])]
    for name, text in LEKKI_THEMES:
        story += [Paragraph(name, s["chap"]), Paragraph(_esc(text), s["body"])]
    story += [Paragraph("Exam tips", s["h1"])]
    for i, tip in enumerate(LEKKI_TIPS, 1):
        story.append(Paragraph(f"{i}. {_esc(tip)}", s["body"]))
    story += [PageBreak(), Paragraph("50 practice questions", s["h1"]),
              Paragraph("Answer them, then check the key on the next pages. Every answer is "
                        "explained.", s["body"])]
    for i, (q, opts, _ans, _exp) in enumerate(LEKKI_QUESTIONS, 1):
        story += [Paragraph(f"<b>{i}.</b> {_esc(q)}", s["q"]),
                  Paragraph(f"A. {_esc(opts[0])}", s["opt"]),
                  Paragraph(f"B. {_esc(opts[1])}", s["opt"]),
                  Paragraph(f"C. {_esc(opts[2])}", s["opt"]),
                  Paragraph(f"D. {_esc(opts[3])}", s["opt"])]
    story += [PageBreak(), Paragraph("Answer key with explanations", s["h1"])]
    for i, (_q, _opts, ans, exp) in enumerate(LEKKI_QUESTIONS, 1):
        story.append(Paragraph(f"<b>{i}. {ans}</b> — {_esc(exp)}", s["key"]))
    _final_cta(story, s, site_url)
    _doc(buf, LEKKI_TITLE).build(story)
    buf.seek(0)
    return buf


def build_past_questions_pdf(conn, exam_name, subject_like, title, subtitle, count, site_url):
    """A past-style question pack generated from the PrepNova question bank."""
    rows = conn.execute(
        """SELECT q.question_text, q.option_a, q.option_b, q.option_c, q.option_d,
                  q.correct_answer, q.explanation
             FROM questions_v2 q
             JOIN subjects s ON s.id = q.subject_id
             JOIN exam_types e ON e.id = s.exam_type_id
            WHERE e.exam_name = ? AND s.subject_name LIKE ? AND q.status = 'Active'
            ORDER BY q.id LIMIT ?""", (exam_name, subject_like, count)).fetchall()
    if not rows:  # fall back to any subject matching the exam
        rows = conn.execute(
            """SELECT q.question_text, q.option_a, q.option_b, q.option_c, q.option_d,
                      q.correct_answer, q.explanation
                 FROM questions_v2 q
                 JOIN subjects s ON s.id = q.subject_id
                 JOIN exam_types e ON e.id = s.exam_type_id
                WHERE e.exam_name = ? AND q.status = 'Active'
                ORDER BY q.id LIMIT ?""", (exam_name, count)).fetchall()
    s = _styles()
    buf = BytesIO()
    story = []
    _cover(story, s, title, subtitle,
           f"{len(rows)} real past-style questions with options, a clean layout, and a full "
           f"answer key with explanations at the end. Compiled for PrepNova CBT.")
    story += [Paragraph("How to use this pack", s["h1"]),
              Paragraph("Work through the questions honestly — no peeking. Write your answers on "
                        "paper, then mark yourself with the key at the end. Every wrong answer "
                        "has an explanation: read it, understand it, and re-test that topic in "
                        "the PrepNova app until it is automatic.", s["body"]),
              Paragraph("Questions", s["h1"])]
    for i, q in enumerate(rows, 1):
        story += [Paragraph(f"<b>{i}.</b> {_esc(q['question_text'])}", s["q"]),
                  Paragraph(f"A. {_esc(q['option_a'])}", s["opt"]),
                  Paragraph(f"B. {_esc(q['option_b'])}", s["opt"]),
                  Paragraph(f"C. {_esc(q['option_c'])}", s["opt"]),
                  Paragraph(f"D. {_esc(q['option_d'])}", s["opt"])]
    story += [PageBreak(), Paragraph("Answer key with explanations", s["h1"])]
    for i, q in enumerate(rows, 1):
        exp = f" — {_esc(q['explanation'])}" if q["explanation"] else ""
        story.append(Paragraph(f"<b>{i}. {_esc(q['correct_answer'])}</b>{exp}", s["key"]))
    _final_cta(story, s, site_url)
    _doc(buf, title).build(story)
    buf.seek(0)
    return buf
