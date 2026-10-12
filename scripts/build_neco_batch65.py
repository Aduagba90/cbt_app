"""Batch 065 - NECO Civic Education top-up (round 2).

Grows the Civic Education bank from 95 to ~151 items so students get two
full practice papers without repeats. Fresh angles across all 14 topics.
Near-dup scanned against JAMB, WAEC and the existing NECO bank.

    python3 scripts/build_neco_batch65.py -> content/batch_065_neco_civic2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_VAL = "Values"
T_CIT = "Citizenship and Nationalism"
T_SYM = "National Symbols"
T_HR = "Human Rights"
T_LAW = "Law and Order"
T_PAR = "Responsible Parenthood"
T_TRAF = "Traffic Regulations"
T_CULT = "Cultism"
T_DRUG = "Drugs and Drug Abuse"
T_HIV = "HIV/AIDS"
T_HT = "Human Trafficking"
T_YOUTH = "Youth Restiveness and Empowerment"
T_UNITY = "National Unity and Integration"
T_AP = "Political Apathy and Popular Participation"

PASSAGES = []
PQ = []

Q = [
    # --------------------------------------------------------------------- values
    (T_VAL, "Medium", "A magistrate who turns down a ₦500,000 offer to free a guilty thief has demonstrated",
     "justice and integrity", "fear of money", "wealth",
     "popularity", "A",
     "Fairness plus honesty in the face of temptation is integrity."),
    (T_VAL, "Easy", "The quality of being fair and reasonable in one's decisions is called",
     "justice", "revenge", "bias", "favouritism", "A",
     "Justice means giving every person what is right."),
    (T_VAL, "Medium", "Children learn honesty best when the adults around them",
     "practise it themselves", "preach it on television",
     "deny it exists", "pay them money", "A",
     "Example teaches values better than words."),
    (T_VAL, "Hard", "A community that rewards hard work and openly punishes cheating is building a culture of",
     "merit and fairness", "fear and silence",
     "wealth at any cost", "idle waiting", "A",
     "What a society rewards, it gets more of."),

    # ------------------------------------------------------------- citizenship
    (T_CIT, "Hard", "A Nigerian who loses his citizenship after a court conviction for a grave crime has lost it by",
     "deprivation", "renunciation", "registration",
     "naturalisation", "A",
     "Deprivation is the state's forced removal of citizenship."),
    (T_CIT, "Easy", "Voting during elections is a civic right and also a civic",
     "duty", "punishment", "privilege of the rich",
     "hobby", "A",
     "Rights and duties are two sides of citizenship."),
    (T_CIT, "Medium", "A good citizen who dislikes a government policy expresses the criticism",
     "constructively and lawfully", "by burning buildings",
     "through bribery", "by fleeing abroad", "A",
     "Responsible citizens criticise to improve, not destroy."),
    (T_CIT, "Medium", "The National Orientation Agency (NOA) exists mainly to",
     "promote citizen values", "fix federal roads",
     "print the currency", "conduct elections", "A",
     "NOA carries government's civic message to the people."),

    # ------------------------------------------------------------ national symbols
    (T_SYM, "Hard", "The black shield on the Nigerian coat of arms stands for",
     "Nigeria's fertile soil", "the armed forces",
     "the oil industry", "dark nights", "A",
     "The shield's black recalls the nation's rich earth."),
    (T_SYM, "Medium", "The flower at the base of the coat of arms represents",
     "the beauty of the nation", "the dry season",
     "the navy", "foreign friendship", "A",
     "The Costus spectabilis stands for Nigeria's beauty."),
    (T_SYM, "Easy", "The Nigerian flag is made up of how many colours?",
     "2", "3", "1", "4", "A",
     "The flag carries only the green and white colours.",
     "2"),
    (T_SYM, "Easy", "The national pledge begins with the words",
     "I pledge to Nigeria my country", "Nigeria we hail thee",
     "Arise O compatriots", "God bless our land", "A",
     "The pledge opens 'I pledge to Nigeria my country'."),

    # ---------------------------------------------------------------- human rights
    (T_HR, "Hard", "When government compulsorily acquires a citizen's land for a public road, the citizen is entitled to",
     "fair and adequate compensation", "nothing at all",
     "a new passport", "a government job", "A",
     "The constitution requires compensation for acquired property."),
    (T_HR, "Easy", "The rights of citizens and the duties they owe the state are best described as",
     "two sides of the same coin", "opposites that never meet",
     "rights for adults only", "duties for the poor", "A",
     "Every right enjoyed implies a duty performed."),
    (T_HR, "Medium", "The Universal Declaration of Human Rights was adopted by the United Nations in",
     "1948", "1960", "1999",
     "1975", "A",
     "The UN General Assembly adopted it on 10 December 1948.",
     "1948"),
    (T_HR, "Easy", "Freedom of association means that citizens may",
     "join lawful groups freely", "never gather together",
     "join only one club", "form secret cults", "A",
     "Peaceful assembly and association are guaranteed."),

    # ---------------------------------------------------------------- law and order
    (T_LAW, "Easy", "A school's rules against bullying are a small version of the body of rules that governs the whole society, which is called",
     "law", "gossip", "fashion",
     "opinion", "A",
     "Law is the collection of enforced social rules."),
    (T_LAW, "Easy", "A driver who ignores a red traffic light has committed a breach of",
     "traffic law", "school rules", "company policy",
     "family tradition", "A",
     "Traffic lights carry the force of law."),
    (T_LAW, "Medium", "Minor criminal cases in Nigeria are first heard at the",
     "magistrate court", "Supreme Court", "Court of Appeal",
     "election tribunal", "A",
     "Magistrate courts sit at the base of the judiciary."),
    (T_LAW, "Medium", "In a democracy, the punishment of an offender can only be decided by",
     "a court of law", "the police station", "the victim's family",
     "a government minister", "A",
     "Only courts lawfully determine guilt and punishment."),

    # ----------------------------------------------------------------- parenthood
    (T_PAR, "Medium", "A parent who attends PTA meetings and tracks the child's report card is performing the duty of",
     "educational support", "tax payment", "voting",
     "traffic control", "A",
     "Following a child's schooling is part of responsible parenting."),
    (T_PAR, "Easy", "Ensuring a baby receives every scheduled immunisation is primarily the role of the",
     "parents", "classmates", "neighbours",
     "motor park union", "A",
     "Parents drive the child's health programme."),
    (T_PAR, "Medium", "The number of children parents can comfortably train is determined chiefly by their",
     "income and resources", "family name", "religious book only",
     "neighbours' advice", "A",
     "Family size should match family means."),
    (T_PAR, "Medium", "Adoption is best described as",
     "legally taking over a child's care", "renting a child for school runs",
     "employing a house help", "sponsoring a relation abroad", "A",
     "Adoption transfers parental rights and duties lawfully."),

    # --------------------------------------------------------------------- traffic
    (T_TRAF, "Easy", "The legal minimum age for driving in Nigeria is",
     "18", "16", "21",
     "25", "A",
     "Eighteen is the qualifying age for a licence.",
     "18"),
    (T_TRAF, "Medium", "Driver's licences in Nigeria are issued by the",
     "Federal Road Safety Corps", "ministry of education",
     "postal service", "courts", "A",
     "The FRSC issues and renews driver's licences."),
    (T_TRAF, "Easy", "Wearing a seat belt is compulsory in a moving car because it",
     "reduces injury in a crash", "makes the car faster",
     "saves fuel", "silences the horn", "A",
     "Belts hold occupants safe during sudden stops."),
    (T_TRAF, "Medium", "A reflective warning triangle placed behind a broken-down vehicle at night serves to",
     "warn oncoming traffic", "advertise the car",
     "light the engine", "call the police", "A",
     "The triangle gives other drivers early warning."),

    # --------------------------------------------------------------------- cultism
    (T_CULT, "Hard", "The secret oaths and rituals of cults make it difficult for members to",
     "leave the group freely", "write examinations",
     "eat in the hostel", "travel home", "A",
     "Fear of oaths traps members in the group."),
    (T_CULT, "Medium", "A student approached by cult recruiters should first",
     "report to school authorities or parents", "join to watch them",
     "collect the money offered", "fight the recruiters alone", "A",
     "Early reporting ends the recruitment quietly."),
    (T_CULT, "Medium", "Cultism tends to thrive in schools where authorities",
     "fail to enforce discipline", "feed students daily",
     "build new hostels", "hold morning assembly", "A",
     "Weak enforcement gives cults room to grow."),
    (T_CULT, "Medium", "Families and religious bodies help to check cultism mainly by",
     "teaching sound values early", "paying school fees late",
     "buying textbooks", "organising parties", "A",
     "Early moral grounding inoculates the child."),

    # ----------------------------------------------------------------------- drugs
    (T_DRUG, "Medium", "Medicines legally obtained only with a doctor's prescription are called",
     "prescription drugs", "over-the-counter drugs",
     "herbal mixtures", "food supplements", "A",
     "The law keeps potent medicines behind the pharmacist's counter."),
    (T_DRUG, "Easy", "Beer and other alcoholic drinks slow down the brain, so they are classified as",
     "depressants", "stimulants", "vitamins",
     "antibiotics", "A",
     "Alcohol depresses the nervous system."),
    (T_DRUG, "Medium", "Rehabilitation of a drug addict means",
     "helping him stop and recover", "jailing him for life",
     "mocking him publicly", "giving him more drugs", "A",
     "Rehab treats the addiction and rebuilds the person."),
    (T_DRUG, "Medium", "Warning signs of drug abuse in a student include",
     "falling grades and bad friends", "steady attendance",
     "higher scores", "respect for teachers", "A",
     "Sudden decline and strange company are red flags."),

    # ---------------------------------------------------------------------- HIV/AIDS
    (T_HIV, "Medium", "A person canNOT contract HIV by",
     "sharing plates and toilets", "sharing sharp needles",
     "unsafe blood transfusion", "mother to baby", "A",
     "HIV never spreads through casual contact."),
    (T_HIV, "Easy", "The full meaning of AIDS is",
     "Acquired Immune Deficiency Syndrome", "African Immune Disease System",
     "Acquired Illness Deficiency Set", "Annual Immune Disease Survey", "A",
     "AIDS is the late stage of untreated HIV."),
    (T_HIV, "Medium", "Voluntary counselling and testing for HIV is best done at",
     "approved health facilities", "motor parks",
     "beer parlours", "internet cafes", "A",
     "Trained counsellors handle the test and its results."),
    (T_HIV, "Medium", "Antiretroviral drugs help people living with HIV by",
     "slowing the virus in the body", "curing the virus at once",
     "spreading the virus faster", "removing the need for tests", "A",
     "Daily ARVs keep the virus suppressed."),

    # ------------------------------------------------------------------ trafficking
    (T_HT, "Easy", "A favourite trick of human traffickers is promising young girls",
     "jobs abroad", "free school books", "free medical care",
     "new parents", "A",
     "Fake job offers lure victims across borders."),
    (T_HT, "Medium", "The main law against human trafficking in Nigeria established which agency?",
     "NAPTIP", "NAFDAC", "FRSC",
     "SON", "A",
     "The anti-trafficking act created NAPTIP."),
    (T_HT, "Hard", "A smuggled person agrees to be moved for a fee, but a trafficked person is moved mainly for",
     "exploitation", "education", "tourism",
     "vaccination", "A",
     "Exploitation, not transport, defines trafficking."),
    (T_HT, "Medium", "Children most at risk of being trafficked are those",
     "out of school and poor", "in boarding houses",
     "at private schools", "on holiday abroad", "A",
     "Idle, desperate children are the easiest targets."),

    # ----------------------------------------------------------------------- youth
    (T_YOUTH, "Medium", "The NYSC Skills Acquisition and Entrepreneurship Development programme trains corps members to",
     "start their own businesses", "join secret cults",
     "avoid all work", "travel abroad", "A",
     "SAED equips graduates to employ themselves."),
    (T_YOUTH, "Hard", "Youth restiveness in the Niger Delta has historically been linked to",
     "damage from oil operations", "too many universities",
     "excess rainfall", "football matches", "A",
     "Polluted farmlands and waters fuelled grievances."),
    (T_YOUTH, "Easy", "A graduate who learns tailoring instead of waiting for office work shows",
     "self-reliance", "laziness", "pride",
     "weakness", "A",
     "Creating one's own work beats idle waiting."),
    (T_YOUTH, "Medium", "Community youth associations reduce restiveness by channeling members' energy into",
     "productive projects", "night parties",
     "street brawls", "betting shops", "A",
     "Organised youths direct their strength into development."),

    # ----------------------------------------------------------------------- unity
    (T_UNITY, "Hard", "The National Youth Service Corps scheme was created during the regime of",
     "General Yakubu Gowon", "General Sani Abacha",
     "Alhaji Shehu Shagari", "Chief Olusegun Obasanjo", "A",
     "Gowon's government set up the NYSC in 1973."),
    (T_UNITY, "Medium", "Workers from the South taking jobs in the North, and northerners in the South, promote unity by",
     "mixing peoples and cultures", "raising transport fares",
     "closing the borders", "printing maps", "A",
     "Labour mobility weaves Nigerians together."),
    (T_UNITY, "Medium", "The National Festival of Arts and Culture (NAFEST) brings Nigerians together mainly to",
     "celebrate cultural diversity", "fix fuel prices",
     "elect leaders", "award contracts", "A",
     "The festival showcases every state's culture."),
    (T_UNITY, "Medium", "Requiring a presidential candidate to win votes across the country, not just one region, encourages",
     "national unity", "ethnic politics",
     "regional parties", "voter apathy", "A",
     "Spread-out support forces national appeal."),

    # ------------------------------------------------------------------- apathy
    (T_AP, "Medium", "Voter education campaigns before an election aim mainly at",
     "raising participation", "closing polling units",
     "raising taxes", "banning parties", "A",
     "Informed citizens turn out and vote wisely."),
    (T_AP, "Easy", "A citizen who canvasses votes for the candidate she prefers is engaged in",
     "political participation", "political apathy",
     "treason", "rioting", "A",
     "Campaigning is lawful civic participation."),
    (T_AP, "Hard", "When party primaries are openly rigged, ordinary members often respond by",
     "losing interest in the party", "voting twice",
     "joining the army", "burning offices", "A",
     "Unfair processes drive members into apathy."),
    (T_AP, "Medium", "A free press helps to fight political apathy by",
     "informing and educating citizens", "selling more papers only",
     "supporting one party", "cancelling elections", "A",
     "News and analysis equip citizens to take part."),
]

build_batch(
    S,
    "batch_065_neco_civic2.json",
    "065",
    "NECO Civic Education top-up (round 2): grows the bank to ~151 items "
    "so students get two full 60-question papers without repeats. Fresh "
    "angles - justice scenario, citizenship deprivation, NOA, coat of arms "
    "details, land compensation, UDHR 1948, magistrate courts, adoption, "
    "driving age and licences, cult oaths, prescription drugs, ARVs, "
    "smuggling vs trafficking, SAED, NAFEST, spread-vote requirement - "
    "near-dup scanned against the JAMB, WAEC and existing NECO banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
