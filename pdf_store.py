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
# So the Path Does Not Die (Pede Hollist) — WASSCE 2026-2030 African prose
# Content assembled from widely published chapter summaries and study guides.
# ---------------------------------------------------------------------------

SO_PATH_TITLE = "So the Path Does Not Die — Complete WASSCE Study Pack"

SO_PATH_ABOUT = [
    "So the Path Does Not Die is the West African Examinations Council's recommended African prose "
    "text for WASSCE Literature-in-English 2026-2030. It was written by Pede Hollist, a Sierra Leonean "
    "novelist and university teacher who lives in the United States, and was first published in 2008.",

    "The novel follows Finaba - 'Fina' - from a village in Sierra Leone where her grandmother Baramusu, "
    "a powerful traditional leader of women, secretly takes her into the forest to be initiated into "
    "womanhood. Fina's father Amadu storms the initiation house to save her from the fate that killed "
    "her elder sister Dimusu - and the family is cursed and driven out of the village. In Freetown, Fina "
    "battles poverty, her father's death, discrimination against her Fula people and sexual violence. A "
    "diamond dealer's gift of a passport opens the door to America, where she builds a new life, marries "
    "badly, divorces, and falls in love with Cammy, a wealthy Trinidadian doctor. But on her wedding day "
    "a secret from her past walks into the church - and the question of where she truly belongs finally "
    "pulls her back to a war-torn Sierra Leone.",

    "This pack condenses the whole novel - a prologue, twenty-four chapters and an epilogue - into twelve "
    "clear section summaries, a 25-character guide, 8 themes, exam tips, and 50 practice questions in the "
    "WASSCE objective style. Read it alongside the novel: it is a revision companion, not a replacement.",
]

# (section heading, summary text)
SO_PATH_CHAPTERS = [
    ("Prologue — The folktale of Musudugu",
     "Before the story begins, Baramusu tells young Finaba the folktale of Musudugu, a village of only "
     "women, protected by the virgin daughter of Atala the Supreme. Its one law: darkness must never "
     "cover a man in Musudugu - any woman who bore a son had to return him to his father once he could "
     "stand. But a girl named Kumba Kargbo questioned the rule and spoke of letting a man stay, and the "
     "elders told her to follow the ways of the village or leave. The tale plants the novel's central "
     "idea: tradition holds a people together - until someone questions the path."),
    ("Chapters 1-2 — The aborted initiation",
     "Baramusu, a renowned digba (initiation leader) in the Koinadugu community, visits her son Amadu's "
     "house to insist that Finaba become a 'musu ba' - an initiated woman. Finaba's mother Nabou refuses: "
     "her first daughter Dimusu bled to death after her own initiation. While Nabou is away, Baramusu "
     "secretly leads the delighted Finaba into the fafei, the initiation house deep in the forest. Amadu "
     "does what no man may do - he enters the fafei and carries his daughter out. The family is cursed "
     "and outcast, and the famed healer Pa Yatta declares that Nabou's children are 'Denkileni' - "
     "children who come to show the path, born in pairs and rarely long-lived. To save Finaba from "
     "Dimusu's fate, the family turns its back on the village forever."),
    ("Chapter 3 — Exile and a father's death",
     "The family settles in Freetown, holding to a new family adage: each person must be free to choose "
     "their own path. Then Amadu dies suddenly - tetanus from a rusted corrugated-iron cut at the "
     "building site. Nabou turns down an offer to become Alhaji Umaru's second wife, and Finaba is "
     "placed in the household of Pa Heddle, who pays her school fees but is drawn to her young friends; "
     "one of them becomes pregnant. When life in the Heddle home turns cold and hostile, Finaba wins "
     "admission to Crowther College as a boarder - her escape."),
    ("Chapters 4-5 — Crowther College",
     "At Crowther College Fina finds freedom - and humiliation. As a Fula she faces tribal "
     "discrimination, and her boyfriend Kemi Koker drops her over her ethnic identity. Her roommate "
     "Memuna suffers abuse from her boyfriend Simeon. When Fina struggles with chemistry, the men who "
     "should help her turn predatory: Dr Davis Kamanga makes sexual advances, and Kizzy - Hezekiah "
     "Mendelssohn Bacchus, the senior laboratory technician - lures her to his room and sexually "
     "assaults her. Her late father's phantom had warned her not to take the easy path; too late. Yet "
     "two kind Americans anchor her: Meredith Frank, who runs the church mission clinic and treats "
     "Sierra Leone as home, and her fiance Chip Munroe. Then Sidibe, a diamond dealer who admires her "
     "dignity, hands her the impossible: a Sierra Leonean passport and dollars. America is suddenly "
     "within reach."),
    ("Chapter 6 — Arrival in America",
     "Fina lands in the United States, welcomed by the newly-married Chip and Meredith. She enrols in "
     "business management at County Community College, rents her own apartment and takes a night-shift "
     "job at the Twenty-four Seven Child Care and Learning Academy. School by day, work by night, sleep "
     "sacrificed - until she is fired after Juanita, the owner, finds the hyperactive Billy Bob tied to "
     "a chair. A Sierra Leonean contact, Sangallay, finds her customer-care work at Be Assured, and she "
     "moves to Maryland. There she reconnects with Edna, her foster sister from the Heddle home - who "
     "announces that she is marrying Kizzy, Fina's attacker. Fina keeps her past with Kizzy to herself "
     "and lets sleeping dogs lie."),
    ("Chapters 7-8 — Jemal, Aman and Cammy",
     "At Be Assured Fina's diligence wins over Aman, the district manager, and the two become "
     "inseparable friends. When Fina's mother dies, Aman hands her a thousand dollars without "
     "hesitation. Hoping to secure citizenship, Fina marries Jemal, a relative - ignoring warnings from "
     "Aman and Aman's sister Shantea that he is a drug-addicted wife-beater. Reality is exactly as "
     "promised: Jemal abuses her physically, sexually and financially until she divorces him and moves "
     "in with Aman. At a party thrown by a doctor friend of Bayo - Aman's boyfriend - Fina lights up "
     "the dance floor with her calypso moves and catches the eye of Cammy, Cameroon Dexter Priddy, a "
     "Trinidadian medical doctor."),
    ("Chapters 9-10 — Love and its fault lines",
     "Fina and Cammy fall deeply in love. But a news report on female genital mutilation opens a wound "
     "between them: Cammy condemns the practice; Fina, circumcised herself, defends it as tradition and "
     "compares it to male circumcision. She finally shocks him by revealing her own circumcision - he "
     "loves her still, and proposes marriage. Meanwhile Sierra Leone descends into civil war. Fina's "
     "younger sister Isa, with their mother gone, has a baby, Sarata, with Hassan; Fina arranges their "
     "escape to Guinea and carries the whole family's upkeep, even taking a home-equity loan rather "
     "than accept Cammy's repayable help. Weighed down and depressed as the wedding approaches, she "
     "discovers she is pregnant - and for a moment everything lifts."),
    ("Chapters 11-13 — The interrupted wedding",
     "On her wedding morning Fina wakes from a nightmare of the aborted initiation. It is an omen. The "
     "inter-cultural ceremony brings together Fina's people - the loud, warm 'Man dem' - and Cammy's "
     "guests, including his rascal friend Lincoln 'Scraps'. Kizzy, now Edna's husband, is among the "
     "crowd. Then, as Fina walks to the altar, a stranger rises and declares that Fina is his wife. It "
     "is Jemal. Fina flees the church with Cammy behind her, and only Scraps, waking from his nap, "
     "confronts the intruder and shoulders him out of the way. The wedding collapses in gossip and "
     "confusion."),
    ("Chapters 14-15 — The vestry",
     "In the vestry Cammy first scolds Fina for disgracing him, then cools. Fina explains: Jemal is her "
     "ex-husband; the church had pronounced the marriage dissolved during one of his mysterious "
     "disappearances, and she carries the divorce papers. Cammy is ashamed but still walks out, "
     "abandoning her at the church. Edna and Aman console her; Aman bluntly blames Fina for hiding the "
     "marriage. Fed up with America, Fina packs to go home to Sierra Leone."),
    ("Chapters 16-19 — Glen, and the slow repair",
     "Two shocks follow. At Cammy's family gathering a young man resembling Cammy's dead elder brother "
     "Donovan appears claiming to be Cammy's son - Glen, named for his foster parents, in urgent need "
     "of a kidney from a matching relative. And at the police station the church-fight case is settled: "
     "Kizzy is released with a curfew sentence. Edna begs Fina to ask Cammy to testify for Kizzy; Fina, "
     "remembering his assault, refuses - then burns with guilt, and the two foster sisters' childhood "
     "bond rekindles in a speechless embrace. Cammy apologises; Fina accepts coolly and repeats that "
     "she is going home. They trade the songs of their wounds - his brother's death, her initiation and "
     "her sister's suffering - and heal a little. When Fina finally tells Cammy everything about Jemal, "
     "he answers with his own confession, and she supports his decision to donate a kidney to Glen. "
     "Then Fina screams and faints."),
    ("Chapters 20-22 — Bitter truths",
     "In hospital, Fina has suffered a threatened miscarriage. Aman, meanwhile, is auctioning "
     "everything that reminds her of the slippery Bayo Karumwi - until he reappears, explains his "
     "near-death escape from a Lassa-fever-struck village, and proposes; Aman turns him down for "
     "changing their plans without asking her. At Edna's house-warming, Fina announces she will go home "
     "and train young girls to be independent; Cammy laughs uneasily and coins the phrase 'diaspora "
     "complex'. Then Kizzy insults Cammy and blurts out his past affair with Fina - and Fina calmly "
     "tells Cammy the truth about Kizzy's assault in college. Cammy answers with his darkest secret: "
     "as a drunk young man he believed he had killed a girl in a car crash, and Scraps buried the story "
     "with the police. At the hospital, as the families gather for the kidney transplant, Anushka "
     "reveals the real story - Scraps, not Cammy, was driving that night."),
    ("Chapters 23-24 and Epilogue — A new path",
     "Fina returns to a Sierra Leone scarred by war and searches for Baramusu through a recovery "
     "agency. The trail fails - the blind old woman Svetlana finds, Mama Yegbe, is not her grandmother "
     "- but hope returns in a new family: Mama Yegbe, the orphanage children, Mawaf the war-displaced "
     "girl she adopts as her own daughter, and her baby with Cammy, Dimusu-Celeste, named for the "
     "sister she lost and the mother-in-law who stood by her. She takes a job at the orphanage and "
     "teaches part-time at a nursery school. Old Sidibe Kaykay, scarred by rebels, proposes marriage; "
     "instead Fina sends Cammy photographs of their daughter. At Aman and Bayo's wedding in Lagos, a "
     "power outage and a dance floor reunite Fina and Cammy; she tells him of her rededication to "
     "Islam, and he is not perturbed. In the epilogue Cammy moves to Sierra Leone to share Fina's path "
     "- so the path does not die."),
]

# (name, who they are)
SO_PATH_CHARACTERS = [
    ("Finaba 'Fina' Marah", "The protagonist; a 'yeliba' (born storyteller) and a 'Denkileni' (a child "
     "who shows the path). Her aborted initiation shapes a lifelong search for belonging that finally "
     "ends in Sierra Leone."),
    ("Baramusu", "Fina's grandmother, a powerful digba (women's initiation leader) in Koinadugu. She "
     "starts Fina's initiation and later disappears in the war; Fina's search for her frames the ending."),
    ("Nabou", "Fina's mother. She loses her first daughter Dimusu to initiation and refuses to let "
     "Finaba be cut; after Amadu's death she rejects becoming Alhaji Umaru's second wife."),
    ("Amadu", "Fina's father and Baramusu's son. He breaks the greatest taboo by carrying Fina out of "
     "the fafei, and dies of tetanus in Freetown soon after the family's exile."),
    ("Dimusu", "Fina's elder sister, a 'Denkileni' who dies after her initiation - the reason Fina is "
     "never cut. Fina later names her own daughter Dimusu-Celeste in her memory."),
    ("Isa", "Fina's younger sister, born in Freetown. Her boyfriend Hassan fathers her children; during "
     "the war Fina funds their escape to Guinea."),
    ("Pa Yatta", "The famed healer who examines Dimusu and Finaba and declares them 'Denkileni' - "
     "children who come to show the path, born fifteen moons apart."),
    ("Pa Heddle", "Fina's guardian in Freetown after Amadu's death. He pays her school fees but preys "
     "on her young friends; one of them becomes pregnant."),
    ("Edna", "Pa Heddle's daughter and Fina's foster sister. She emigrates to America and - unknowingly "
     "- marries Kizzy, Fina's assailant; their childhood bond survives everything."),
    ("Kemi Koker", "Fina's boyfriend at Crowther College, who drops her because she is Fula - the face "
     "of ethnic discrimination in the novel."),
    ("Memuna", "Fina's roommate at Crowther College, trapped in an abusive relationship with Simeon."),
    ("Kizzy (Hezekiah Mendelssohn Bacchus)", "Senior laboratory technician at Crowther College who "
     "sexually assaults Fina; later Edna's husband in America. His church-fight sentence and his "
     "drunken outburst about Fina drive the late twists."),
    ("Meredith Frank", "The American who manages the church mission clinic, grew up in Sierra Leone and "
     "treats it as home; Fina's model of resilience. She marries Chip Munroe and welcomes Fina to "
     "America."),
    ("Sidibe (Sidibe Kaykay)", "The diamond dealer who respects Fina's dignity and gifts her the "
     "passport and dollars that open the door to America; later, rebel-scarred and aged, he proposes "
     "marriage to her in Sierra Leone."),
    ("Aman", "Fina's best friend in America, a district manager at Be Assured. Sharp-tongued and loyal "
     "- a thousand dollars for Fina's mother's burial; her on-off romance with Bayo mirrors Fina's "
     "story."),
    ("Shantea", "Aman's sister, who warns Fina about Jemal's violence and drug addiction."),
    ("Jemal", "Fina's first husband - a relative, drug addict and wife-beater. His dramatic "
     "interruption of her wedding to Cammy is the novel's climax."),
    ("Cammy (Cameroon Dexter Priddy)", "A wealthy Trinidadian medical doctor; Fina's great love. He "
     "carries secrets - a son, Glen, and a fatal crash - and finally relocates to Sierra Leone to "
     "share Fina's path."),
    ("Celeste Priddy", "Cammy's mother, who urges the couple to continue the interrupted wedding; "
     "Fina's daughter is named after her."),
    ("Glen", "Cammy's son by a former relationship, raised by foster parents; his failing kidney leads "
     "Cammy to donate his own."),
    ("Lincoln 'Scraps'", "Cammy's loyal rascal of a friend. He buried Cammy's drunk-driving story with "
     "the police - and had himself been the driver that fatal night."),
    ("Bayo Karumwi", "A Yoruba doctoral student in mechanical engineering; Aman's on-off boyfriend, "
     "later her husband. Their Lagos wedding reunites Fina and Cammy."),
    ("Mama Yegbe", "The blind old woman found by the recovery agency - not Baramusu, but she becomes "
     "Fina's adopted grandmother and names Fina's daughter."),
    ("Mawaf", "The war-displaced girl who keeps Mama Yegbe company; Fina adopts her as her second "
     "daughter."),
    ("Dimusu-Celeste", "Fina and Cammy's baby daughter, named for Fina's dead sister and Cammy's "
     "mother - the next generation of the path."),
]

# (theme, explanation)
SO_PATH_THEMES = [
    ("Tradition and the individual — 'the path'",
     "The novel's controlling image. The prologue's all-women village of Musudugu shows tradition as "
     "survival; Amadu's rescue of Fina shows it as a death sentence when followed blindly. Every major "
     "character must choose between the inherited path and a self-made one - and the title insists the "
     "path itself must not die, only change."),
    ("Female genital mutilation: culture versus human rights",
     "Baramusu's initiation carries belonging, status and womanhood; Dimusu's death and Fina's lifelong "
     "sense of incompleteness carry its cost. Hollist refuses a simple villain: the digba is the "
     "novel's most loving grandmother, and Fina herself defends the practice to Cammy before revealing "
     "her own circumcision."),
    ("Identity and belonging",
     "Fina is cursed at home for an initiation she never chose, mocked in Freetown as a Fula, and "
     "'other' in America. Her belief that the aborted initiation is the root of every misfortune gives "
     "the search for belonging its psychological engine."),
    ("The diaspora condition — 'home' and 'abroad'",
     "The Washington chapters dramatise the immigrant's bargains: papers, menial night work, the myth "
     "of the American dream, and the debates - Africans, African Americans and Caribbeans arguing over "
     "the 'diaspora complex'. Baramusu's proverb of the bird that must fly out to find food sums it up."),
    ("Ethnic discrimination and tribalism",
     "Fina is rejected by Kemi Koker and humiliated at Crowther College simply for being Fula - a "
     "minority identity. The novel shows tribalism as the village curse's urban twin."),
    ("War, displacement and loss",
     "Sierra Leone's civil war offstage: Isa's flight to Guinea, Sidibe's rebel scars, Mawaf's refuge "
     "story, an orphanage of traumatised children. War strips Fina of the past yet hands her the "
     "family she finally chooses."),
    ("Love, marriage and gender-based violence",
     "Three men shadow Fina: the predator Kizzy, the abuser Jemal, the loving but secretive Cammy. "
     "Alongside them stand Memuna's Simeon and Pa Heddle's prey. Hollist weighs marriage as both "
     "women's ruin and - with honesty and sacrifice - their repair."),
    ("Female resilience, survival and sisterhood",
     "From Nabou's refusal to Aman's thousand dollars, Edna's embrace, Meredith's example and Mama "
     "Yegbe's naming ceremony, women pass strength down the generations. Fina's final vocation - "
     "raising and training girls - turns survival into inheritance."),
]

SO_PATH_TIPS = [
    "Master the journey, not just the events: village (Koinadugu) to Freetown, then America (the "
    "Washington area and Maryland), then back to Sierra Leone - with a short stop in Lagos for Aman "
    "and Bayo's wedding. Every WASSCE question on plot, setting or character development sits on this "
    "map.",
    "Learn names AND aliases: Fina is Finaba; Kizzy is Hezekiah Mendelssohn Bacchus; Cammy is Cameroon "
    "Dexter Priddy; Scraps is Lincoln. Objective questions love asking 'who is…?' and 'whose full name "
    "is…?'",
    "Know the key terms: digba (initiation leader), musu ba (initiated woman), fafei (the initiation "
    "house), yeliba (born storyteller), Denkileni (children who come to show the path), sara (memorial "
    "service). WAEC quotes them directly in options.",
    "Track the two interrupted ceremonies - the initiation in the forest and the church wedding. The "
    "novel is book-ended by them; comparing what each interruption costs is a classic essay question.",
    "Understand the title: 'the path' is tradition and destiny. Baramusu says Fina will show the "
    "people the way because they have strayed. The epilogue answers the question the prologue asks - "
    "the path survives by bending, not by breaking.",
    "For essay answers, pair your characters: Fina and Dimusu (the path not taken), Fina and Baramusu "
    "(two kinds of power), Aman-and-Bayo versus Fina-and-Cammy (two marriages), Mama Yegbe and Mawaf "
    "(the family Fina chooses).",
]

# (question, [A-D], correct letter, explanation)
SO_PATH_QUESTIONS = [
    ("Who is the protagonist of So the Path Does Not Die?",
     ["Aman", "Nabou", "Celeste Priddy", "Finaba Marah"], "D",
     "Finaba - 'Fina' - Marah is the protagonist; the novel follows her from a Sierra Leonean village "
     "to Freetown, America and back."),
    ("The story moves through all of these places EXCEPT",
     ["Freetown", "Washington DC area", "Lagos", "Accra"], "D",
     "The settings span Sierra Leone (village, Freetown, Koidu), the Washington area and Maryland, and "
     "briefly Lagos for Aman's wedding. Accra never appears."),
    ("Baramusu is a renowned ______ in the Koinadugu community.",
     ["healer", "digba", "trader", "warrior"], "B",
     "A digba is a traditional leader of women who conducts initiations - Baramusu is the most "
     "respected one in Koinadugu."),
    ("In the novel, a 'musu ba' is",
     ["a born storyteller", "a widow", "an initiated woman", "a priestess"], "C",
     "'Musu ba' means an initiated woman - belonging to the age-group and the people. Fina's aborted "
     "initiation leaves her longing for that belonging."),
    ("Nabou refuses to let Finaba be initiated because",
     ["she hates Baramusu", "her first daughter Dimusu died after her own initiation",
      "the family had become Christians", "Amadu had forbidden all tradition"], "B",
     "Dimusu, a Denkileni like Fina, dies after her initiation - so Nabou vows that Fina will never "
     "face the knife."),
    ("The 'fafei' is",
     ["the village market", "the chief's palace", "the healing shrine", "the initiation house in the forest"], "D",
     "The fafei, deep in the forest, is where girls are initiated into womanhood. No man may enter it - "
     "which is why Amadu's rescue is an abomination."),
    ("Who breaks tradition by carrying Finaba out of the fafei?",
     ["Pa Yatta", "Alhaji Umaru", "Amadu, her father", "Nabou"], "C",
     "Amadu does what no man may do - enters the initiation house and carries his daughter out to save "
     "her from Dimusu's fate."),
    ("Pa Yatta, the healer, declares that Nabou's children are",
     ["yeliba", "Denkileni", "musu ba", "digba"], "B",
     "Denkileni are children who come to show the path, born in pairs fifteen moons apart, and usually "
     "short-lived - Dimusu and Finaba are such a pair."),
    ("'Denkileni' are children who",
     ["never grow old", "are born twins", "must become healers", "come to show the path and often die young"], "D",
     "The term names children sent to show the people the way; their lives are typically cut short, as "
     "Dimusu's is."),
    ("The folktale of Musudugu told in the prologue is about a village of",
     ["famous hunters", "only women", "fishermen", "gold traders"], "B",
     "Musudugu is a legendary village of only women, protected by the virgin daughter of Atala the "
     "Supreme."),
    ("In the Musudugu folktale, the one law was that",
     ["darkness must not cover a man in Musudugu", "everyone must farm daily",
      "only virgins could speak", "children must be seen and not heard"], "A",
     "Any woman who bore a son had to return him to his father once he could stand - no man could "
     "remain overnight. Kumba Kargbo questioned the rule."),
    ("Amadu dies in Freetown of",
     ["malaria", "a motor accident", "tetanus", "Lassa fever"], "C",
     "He cuts his heel on a rusted corrugated-iron sheet at the building site and, afraid of losing "
     "his job, refuses hospital treatment until the tetanus kills him."),
    ("After Amadu's death, Nabou rejects an offer to become the second wife of",
     ["Pa Heddle", "Pa Yatta", "Sidibe", "Alhaji Umaru"], "D",
     "She turns down the wealthy Alhaji Umaru, choosing independence over security - an early lesson "
     "for Fina."),
    ("Finaba is sent to live in whose household in Freetown?",
     ["The Heddles", "The Munroes", "The Priddys", "The Kokers"], "A",
     "Pa Heddle's household - with Taiwo, Kehinde, Ade and Edna - becomes Fina's foster home."),
    ("Edna is",
     ["Aman's sister", "Pa Heddle's daughter", "Cammy's sister", "Meredith's daughter"], "B",
     "Edna is Pa Heddle's daughter; she and Fina grow up as foster sisters and their bond survives "
     "even the Kizzy secret."),
    ("Kemi Koker ends his relationship with Finaba because",
     ["she is Fula", "she is poor", "she refused to marry him", "she was leaving for America"], "A",
     "At Crowther College Fina suffers tribal humiliation as a Fula - Kemi Koker drops her over her "
     "ethnic identity."),
    ("Kizzy's full name is",
     ["Hezekiah Mendelssohn Bacchus", "Henry Mendeleyev Bacchus",
      "Hezekiah Moses Bacchus", "Kamara Dexter Bacchus"], "A",
     "Kizzy is Hezekiah Mendelssohn Bacchus, the senior laboratory technician at Crowther College."),
    ("Kizzy works at Crowther College as",
     ["a lecturer", "the bursar", "the senior laboratory technician", "the provost"], "C",
     "He is the college's senior lab technician - the man Fina turns to for chemistry help, with "
     "devastating consequences."),
    ("The American who manages the church mission clinic and treats Sierra Leone as home is",
     ["Celeste Priddy", "Anushka", "Juanita", "Meredith Frank"], "D",
     "Meredith Frank grew up in Sierra Leone, runs the mission clinic with quiet resilience, and later "
     "marries Chip Munroe."),
    ("Who gives Fina a Sierra Leonean passport and dollars for her American dream?",
     ["Chip Munroe", "Sidibe", "Cammy", "Sangallay"], "B",
     "Sidibe, the diamond dealer, respects Fina's dignity and surprises her with the passport and "
     "money - cautioning her that 'the world is a trade zone'."),
    ("In America, Fina studies ______ at County Community College.",
     ["nursing", "law", "business management", "pharmacy"], "C",
     "Meredith helps her enrol, and Fina studies business management by day while working at night."),
    ("Fina's first job in America is a night shift at",
     ["a gas station", "a hospital ward", "a restaurant", "the Twenty-four Seven Child Care and Learning Academy"], "D",
     "She works nights at the Twenty-four Seven Child Care and Learning Academy while schooling by "
     "day."),
    ("Juanita fires Fina from the daycare after",
     ["Fina stole money", "Fina came late three times", "a child, Billy Bob, was found tied to a chair",
      "the parents complained"], "C",
     "The hyperactive Billy Bob is found tied to a chair without Fina's knowledge - exhausted from "
     "school and night work, she loses the job."),
    ("______ helps Fina get the customer-care job at Be Assured.",
     ["Sangallay", "Kizzy", "Glen", "Bayo"], "A",
     "Sangallay, a Sierra Leonean contact, secures her the Be Assured job, and she moves to Maryland."),
    ("Aman works at Be Assured as",
     ["a cleaner", "the district manager", "the accountant", "the CEO's secretary"], "B",
     "Aman is Fina's district manager at Be Assured; Fina's faithfulness at work earns her a "
     "friendship for life."),
    ("Aman gives Fina one thousand dollars when",
     ["Fina's mother dies", "Fina loses her job", "Fina is hospitalised", "Fina's rent is due"], "A",
     "When Isa breaks the news of Nabou's death, Aman hands Fina a thousand dollars without "
     "hesitation - and is surprised how quickly Muslims bury their dead."),
    ("Fina's first husband in America is",
     ["Cammy", "Bayo", "Jemal", "Kizzy"], "C",
     "Hoping to secure citizenship through marriage, Fina marries Jemal, a relative - against all "
     "warnings."),
    ("Jemal is best described as",
     ["a wealthy diamond dealer", "a drug-addicted wife-beater", "a quiet pastor", "a medical doctor"], "B",
     "Shantea, Aman's sister, confirms the warnings: Jemal abuses Fina physically, sexually and "
     "financially until she divorces him."),
    ("Who confirms to Fina that Jemal beats his wives?",
     ["Edna", "Shantea, Aman's sister", "Celeste", "Meredith"], "B",
     "Shantea - Aman's sister - confirms what Aman suspects; Fina, already emotionally gone, marries "
     "him anyway."),
    ("Fina meets Cammy at",
     ["a church programme", "the hospital where she works", "a party thrown by a doctor friend of Bayo",
      "a wedding in Lagos"], "C",
     "At the party, Fina's knowledge of calypso songs and dance moves captures Cammy - himself a "
     "Caribbean man."),
    ("Cammy, whose full name is Cameroon Dexter Priddy, is a medical doctor from",
     ["Nigeria", "Ghana", "Jamaica", "Trinidad"], "D",
     "Cammy is a Trinidadian doctor - the 'wealthy, successful young doctor from Trinidad'."),
    ("What first causes a sharp misunderstanding between Fina and Cammy?",
     ["money", "a news report on female genital mutilation", "Jemal", "Fina's family"], "B",
     "Cammy condemns FGM as it relates to African culture; Fina defends it as tradition, comparing it "
     "to male circumcision - before shocking him with the news of her own circumcision."),
    ("Fina's younger sister Isa has a baby girl named",
     ["Sarata", "Dimusu", "Mawaf", "Nabou"], "A",
     "Isa welcomes Sarata with her boyfriend Hassan, who cohabits with her - and another baby follows."),
    ("When the civil war intensifies, Fina arranges for Isa and her children to escape to",
     ["Liberia", "Ghana", "Guinea", "Senegal"], "C",
     "Devoid of funds in Guinea, Isa and her family become 'a financial cross Fina must carry'."),
    ("Rather than accept Cammy's repayable help, Fina",
     ["sells her car", "works double shifts", "asks Aman", "takes a home-equity loan"], "D",
     "Fina's independence maddens Cammy: she cuts her expensive living, mortgages belongings and takes "
     "a home-equity loan instead."),
    ("Fina's relatives at her wedding are playfully called",
     ["'Man dem'", "'Kono boys'", "'Fula squad'", "'Wahala men'"], "A",
     "The 'Man dem' - identified by their greeting style - fill the wedding with noise, debate and "
     "social commentary."),
    ("The wedding is interrupted by a stranger who",
     ["claims to be Cammy's father", "claims Fina is his wife", "says the church is on fire",
      "demands the bride price"], "B",
     "Jemal, Fina's ex-husband, stands up and claims her as his wife - and Fina flees the church."),
    ("Who eventually confronts the intruder at the church?",
     ["Glen", "Kizzy", "Scraps", "Bayo"], "C",
     "Lincoln 'Scraps', asleep through most of the drama, wakes up and shoulders the "
     "stranger-proposing husband out of the way."),
    ("Fina proves her marriage to the intruder was dissolved by producing",
     ["church divorce papers", "a police report", "a witness, Edna", "her diary"], "A",
     "The church had pronounced the marriage dissolved during Jemal's mysterious disappearance - and "
     "Fina carries the papers."),
    ("Cammy's mother is",
     ["Anushka", "Celeste Priddy", "Juanita", "Meredith"], "B",
     "Celeste Priddy urges the couple to continue the interrupted ceremony - and Fina later names her "
     "daughter after her."),
    ("Glen shocks Cammy's family by claiming to be",
     ["Cammy's creditor", "a distant cousin", "Scraps' brother", "Cammy's son"], "D",
     "The young man, resembling Cammy's dead elder brother Donovan, claims to be Cammy's son."),
    ("Glen urgently needs from Cammy",
     ["money for school", "a job", "forgiveness", "a kidney transplant from a matching relative"], "D",
     "Glen's kidney is failing; he searches for his closest relative whose kidney might match - and "
     "Cammy eventually donates his own."),
    ("After the church fight, Kizzy is",
     ["deported", "jailed for a year", "released with a curfew sentence", "fined"], "C",
     "The police case over the wedding scuffle ends with Kizzy released on a curfew sentence binding "
     "within the Washington area."),
    ("Cammy believed for years that he had killed a girl while",
     ["serving in the army", "working as a doctor", "fighting in a club", "drunk driving"], "D",
     "Cammy confesses his rueful past: he believed he had accidentally killed a girl while driving "
     "drunk, and Scraps had 'died the issue down' with the police."),
    ("Who reveals that Scraps, not Cammy, was driving on the night of the fatal accident?",
     ["Anushka", "Edna", "Glen", "Celeste"], "A",
     "At the hospital, Anushka tells Cammy the real version: Scraps was the driver that night, and "
     "switched positions with Cammy because they were all drunk."),
    ("The blind old woman the recovery agency finds for Fina is",
     ["Baramusu", "Mama Yegbe", "Nabou", "Dimusu"], "B",
     "Svetlana's agency finds a blind old woman - but she is Mama Yegbe, not Baramusu. The search for "
     "her grandmother is dashed, yet a new family begins."),
    ("Mawaf is",
     ["Mama Yegbe's nurse", "Fina's cousin", "the war-displaced girl Fina adopts as her daughter",
      "Sidibe's daughter"], "C",
     "Mawaf is Mama Yegbe's 'girl Friday', a war refugee whose refuge story Fina learns; with "
     "Svetlana's help Fina adopts her."),
    ("Fina names her own daughter",
     ["Sarata", "Nabou-Junior", "Finaba", "Dimusu-Celeste"], "D",
     "The baby is named for Fina's dead sister Dimusu and Cammy's mother Celeste - two women who "
     "shaped her path. Mama Yegbe conducts the naming ceremony."),
    ("At Edna's house-warming, Fina announces that she will go home to",
     ["marry Sidibe", "train young girls to be independent", "open a clinic", "farm cocoa"], "B",
     "Fina reveals her future intention to travel home and train young girls to be independent - "
     "Cammy laughs amidst discomfort and coins 'diaspora complex'."),
    ("In the epilogue, Cammy",
     ["remarries in America", "takes Fina to Trinidad", "dies in the war",
      "relocates to Sierra Leone to live with Fina"], "D",
     "Cammy resolves not to leave the woman he loves: he returns to live with Fina in Sierra Leone and "
     "encourage her 'path'."),
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


def _build_novel_pack(title, subtitle, tagline, about, chapters, characters_note,
                      characters, themes, tips, questions, site_url):
    """Shared engine for the recommended-novel study packs."""
    s = _styles()
    buf = BytesIO()
    story = []
    _cover(story, s, title, subtitle, tagline)
    story += [Paragraph("About this pack", s["h1"])]
    for para in about:
        story.append(Paragraph(_esc(para), s["body"]))
    story += [Paragraph("Chapter-by-chapter summary", s["h1"])]
    for heading, text in chapters:
        story += [Paragraph(_esc(heading), s["chap"]), Paragraph(_esc(text), s["body"])]
    story += [PageBreak(), Paragraph("Character guide", s["h1"]),
              Paragraph(characters_note, s["body"])]
    rows = [[Paragraph("<b>Name</b>", s["key"]), Paragraph("<b>Who they are</b>", s["key"])]]
    for name, role in characters:
        rows.append([Paragraph(f"<b>{_esc(name)}</b>", s["key"]), Paragraph(_esc(role), s["key"])])
    tbl = Table(rows, colWidths=[42 * mm, 134 * mm])
    tbl.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LIGHT),
                             ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                             ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story += [tbl, Paragraph("Themes", s["h1"])]
    for name, text in themes:
        story += [Paragraph(_esc(name), s["chap"]), Paragraph(_esc(text), s["body"])]
    story += [Paragraph("Exam tips", s["h1"])]
    for i, tip in enumerate(tips, 1):
        story.append(Paragraph(f"{i}. {_esc(tip)}", s["body"]))
    story += [PageBreak(), Paragraph(f"{len(questions)} practice questions", s["h1"]),
              Paragraph("Answer them, then check the key on the next pages. Every answer is "
                        "explained.", s["body"])]
    for i, (q, opts, _ans, _exp) in enumerate(questions, 1):
        story += [Paragraph(f"<b>{i}.</b> {_esc(q)}", s["q"]),
                  Paragraph(f"A. {_esc(opts[0])}", s["opt"]),
                  Paragraph(f"B. {_esc(opts[1])}", s["opt"]),
                  Paragraph(f"C. {_esc(opts[2])}", s["opt"]),
                  Paragraph(f"D. {_esc(opts[3])}", s["opt"])]
    story += [PageBreak(), Paragraph("Answer key with explanations", s["h1"])]
    for i, (_q, _opts, ans, exp) in enumerate(questions, 1):
        story.append(Paragraph(f"<b>{i}. {ans}</b> — {_esc(exp)}", s["key"]))
    _final_cta(story, s, site_url)
    _doc(buf, title).build(story)
    buf.seek(0)
    return buf


def build_lekki_pdf(site_url):
    """The Lekki Headmaster study pack: summaries, characters, themes, 50 questions."""
    return _build_novel_pack(
        LEKKI_TITLE,
        "JAMB UTME 2026 Use of English — recommended novel by Kabir Alabi Garba",
        "Chapter summaries \u00b7 character guide \u00b7 themes \u00b7 exam tips \u00b7 50 practice "
        "questions with answers. Compiled for PrepNova CBT.",
        LEKKI_ABOUT,
        [(f"Chapter {num}: {name}", text) for num, name, text in LEKKI_CHAPTERS],
        "Drill this table — JAMB's favourite question style is matching names to roles.",
        LEKKI_CHARACTERS, LEKKI_THEMES, LEKKI_TIPS, LEKKI_QUESTIONS, site_url)


def build_so_path_pdf(site_url):
    """So the Path Does Not Die study pack: summaries, characters, themes, 50 questions."""
    return _build_novel_pack(
        SO_PATH_TITLE,
        "WASSCE 2026-2030 Literature-in-English — African prose by Pede Hollist",
        "Chapter summaries \u00b7 character guide \u00b7 themes \u00b7 key terms \u00b7 exam tips "
        "\u00b7 50 practice questions with answers. Compiled for PrepNova CBT.",
        SO_PATH_ABOUT,
        SO_PATH_CHAPTERS,
        "Drill this table — WAEC's favourite question style is 'who did what'. Know every name "
        "and alias.",
        SO_PATH_CHARACTERS, SO_PATH_THEMES, SO_PATH_TIPS, SO_PATH_QUESTIONS, site_url)


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
