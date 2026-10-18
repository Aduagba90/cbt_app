"""Batch 096 - WAEC Civic Education round 2 (WAEC lift, Round 19).

WAEC Civic Paper 1 draws 50 items; the bank stood at 85. This lift adds
fresh items - rights and duties, rule of law, separation of powers and
checks, federalism, suffrage, electoral offences, pressure groups,
orderliness, road signs and vehicle papers, drug classes and help,
cultism prevention, HIV stigmatisation, skills acquisition, democracy
forms, nationalists (Sardauna, Zik, Awolowo), corruption forms, criminal
vs civil law, arms' functions, family types - scanned against WAEC r1,
NECO Civic rounds 1-2 and all banks.

    python3 scripts/build_neco_batch96.py -> content/batch_096_waec_civic2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_RIGHT = "Rights and Duties"
T_LAW = "Constitution, Rule of Law and Arms of Government"
T_ELEC = "Elections and Political Participation"
T_ORDER = "Orderliness and Traffic Regulations"
T_DRUG = "Drugs and Substance Abuse"
T_CULT = "Cultism and Youth Empowerment"
T_HIV = "HIV/AIDS and Health"
T_HIST = "Nationalism and Nation Building"
T_ANTI = "Corruption and the Law"
T_FAM = "Family and Responsible Parenthood"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- rights and duties
    (T_RIGHT, "Medium", "The right of every accused person to be heard before a judge decides is the right to",
     "fair hearing", "free movement", "freedom of speech", "privacy", "A",
     "Justice hears both sides first."),
    (T_RIGHT, "Medium", "Publishing one's opinion in a newspaper without fear is an exercise of",
     "freedom of expression", "freedom of association", "right to work", "right to life", "A",
     "The pen speaks freely within law."),
    (T_RIGHT, "Easy", "Paying taxes honestly when due is a citizen's",
     "duty", "right", "privilege", "punishment", "A",
     "Duties keep the state running."),
    (T_RIGHT, "Easy", "Defending Nigeria when she is threatened is the duty of",
     "every citizen", "soldiers alone", "senators alone", "the police alone", "A",
     "The constitution calls on all."),
    # ---------------------------------------------------------------- constitution and law
    (T_LAW, "Medium", "The principle that no one, however high, stands above the law is",
     "equality before the law", "separation of powers", "federal character", "delegated legislation", "A",
     "The law is no respecter of rank."),
    (T_LAW, "Hard", "Giving each arm of government the power to check the others is",
     "checks and balances", "decentralisation", "devolution", "privatisation", "A",
     "Each arm brakes the others."),
    (T_LAW, "Hard", "Dividing governmental powers between the centre and the states describes",
     "federalism", "unitarism", "confederalism", "totalitarianism", "A",
     "Two tiers share the powers."),
    (T_LAW, "Medium", "The arm of government that interprets the laws is the",
     "judiciary", "legislature", "executive", "civil service", "A",
     "Courts explain what the law means."),
    (T_LAW, "Medium", "The arm that implements and enforces laws is the",
     "executive", "judiciary", "legislature", "press", "A",
     "Ministers and agencies execute."),
    (T_LAW, "Hard", "A law that punishes an act that was not an offence when it was done is called a",
     "retroactive law", "by-law", "decree", "subsidiary law", "A",
     "Backward-reaching laws are unjust."),
    # ---------------------------------------------------------------- elections and participation
    (T_ELEC, "Easy", "The right of every adult citizen to vote regardless of wealth or gender is",
     "universal adult suffrage", "limited franchise", "property franchise", "open ballot", "A",
     "Every adult counts equally."),
    (T_ELEC, "Medium", "Offering money or gifts to influence a voter is the offence of",
     "vote buying", "canvassing", "lobbying", "campaigning", "A",
     "Bribing the ballot is a crime."),
    (T_ELEC, "Medium", "Snatching ballot boxes on election day is an offence against",
     "the Electoral Act", "the Land Use Act", "labour laws", "company law", "A",
     "The Act protects the polls."),
    (T_ELEC, "Medium", "Groups like the NLC and NMA that press government for change without seeking office are",
     "pressure groups", "political parties", "civil service unions", "quasi-courts", "A",
     "They influence, not govern."),
    (T_ELEC, "Medium", "Joining a peaceful protest march is a form of",
     "political participation", "political apathy", "civil disobedience only", "electoral malpractice", "A",
     "Citizens engage their leaders."),
    (T_ELEC, "Easy", "An election held to fill a vacant legislative seat mid-term is a",
     "by-election", "run-off", "primary", "referendum", "A",
     "Vacancies call by-elections."),
    # ---------------------------------------------------------------- orderliness and traffic
    (T_ORDER, "Easy", "Waiting on a queue at the bank or bus stop shows",
     "orderliness", "cowardice", "wastefulness", "weakness", "A",
     "Queues keep public life smooth."),
    (T_ORDER, "Medium", "Road signs shaped like red triangles with symbols inside are",
     "warning signs", "regulatory signs", "information signs", "direction signs", "A",
     "Triangles shout 'beware'."),
    (T_ORDER, "Medium", "The certificate proving a vehicle is fit to be on the road is the",
     "roadworthiness certificate", "insurance certificate only", "licence disc only", "customs paper", "A",
     "Roadworthiness says the car is sound."),
    (T_ORDER, "Medium", "Pedestrians are advised to walk facing oncoming traffic where there is no walkway because it",
     "lets them see vehicles early", "saves them a few steps", "keeps the sun behind", "avoids school zones", "A",
     "Facing traffic saves lives."),
    (T_ORDER, "Hard", "The amber traffic light instructs drivers to",
     "prepare to stop", "speed through quickly", "park at once", "reverse carefully", "A",
     "Yellow warns of the change."),
    # ---------------------------------------------------------------- drugs
    (T_DRUG, "Medium", "Cocaine and other substances that speed up the body's activity are",
     "stimulants", "depressants", "narcotics", "hallucinogens", "A",
     "They race the heart dangerously."),
    (T_DRUG, "Medium", "Heroin and codeine-based cough syrups, which dull pain and induce sleep, are",
     "narcotics", "stimulants", "barbiturates only", "inhalants", "A",
     "Narcotics numb and enslave."),
    (T_DRUG, "Easy", "A drug dependent person who suddenly stops may suffer",
     "withdrawal symptoms", "improved appetite", "better sleep", "clearer skin", "A",
     "The body screams for the drug."),
    (T_DRUG, "Medium", "Recovered drug users helping new patients at a rehabilitation centre show that recovery",
     "is possible with support", "happens overnight", "requires no effort", "depends on luck alone", "A",
     "Support systems speed healing."),
    # ---------------------------------------------------------------- cultism and empowerment
    (T_CULT, "Medium", "Many students join campus cults in search of",
     "power and protection", "better grades", "sports glory", "church membership", "A",
     "Fear drives the searching."),
    (T_CULT, "Medium", "Orientation programmes that warn new students about cult dangers are part of",
     "prevention", "prosecution", "punishment", "propaganda", "A",
     "Early warnings save freshmen."),
    (T_CULT, "Easy", "Learning a trade such as tailoring or welding is called",
     "skills acquisition", "talent hunting", "labour mixing", "casual work", "A",
     "A skill keeps paying for life."),
    (T_CULT, "Medium", "Which pair of problems most fuels youth restiveness in the oil-bearing states?",
     "joblessness and grievance", "excess schools and parks", "free rides and levies", "sports festivals", "A",
     "Idle hands and anger feed it."),
    # ---------------------------------------------------------------- hiv
    (T_HIV, "Medium", "Refusing to hire a qualified person because of their HIV status is",
     "stigmatisation", "rational planning", "safety practice", "company policy", "A",
     "The law forbids such exclusion."),
    (T_HIV, "Easy", "An HIV-positive mother can protect her unborn baby by taking",
     "treatment during pregnancy", "no medicine at all", "traditional baths only", "extra exercise", "A",
     "Drugs cut mother-to-child risk."),
    # ---------------------------------------------------------------- nationalism and nation building
    (T_HIST, "Medium", "The nationalist whom the North still calls the Sardauna of Sokoto is",
     "Ahmadu Bello", "Nnamdi Azikiwe", "Obafemi Awolowo", "Tafawa Balewa", "A",
     "He led the Northern Peoples Congress."),
    (T_HIST, "Medium", "The nationalist popularly remembered as 'Zik of Africa' is",
     "Nnamdi Azikiwe", "Ahmadu Bello", "Ernest Ikoli", "Samuel Akisanya", "A",
     "His pan-African paper made the name."),
    (T_HIST, "Medium", "Obafemi Awolowo introduced free primary education in the",
     "Western Region", "Eastern Region", "Northern Region", "Lagos Colony", "A",
     "The West schooled its children free."),
    (T_HIST, "Medium", "The federal character principle exists to make appointments reflect",
     "Nigeria's diversity", "the ruling party only", "seniority in age", "family lineage", "A",
     "Every group gets a share."),
    (T_HIST, "Hard", "Unity schools that admit students from all states exist to promote",
     "national integration", "private profit", "religious teaching", "local culture", "A",
     "Children mix and merge as one."),
    # ---------------------------------------------------------------- corruption and law
    (T_ANTI, "Medium", "A cashier who quietly diverts company money commits",
     "embezzlement", "extortion", "smuggling", "perjury", "A",
     "Trusted funds vanish inside."),
    (T_ANTI, "Medium", "Favouring one's relatives in public appointments is",
     "nepotism", "federal character", "meritocracy", "seniority", "A",
     "Family ties trump fairness."),
    (T_ANTI, "Medium", "Offences like theft and murder that are prosecuted by the state are",
     "criminal matters", "civil matters", "family matters", "commercial matters", "A",
     "The state prosecutes crimes."),
    (T_ANTI, "Medium", "A dispute over land between two neighbours that ends in damages is a",
     "civil matter", "criminal case", "treason trial", "juvenile case", "A",
     "Individuals sue each other."),
    (T_ANTI, "Hard", "Punishments for crime in Nigeria chiefly aim at",
     "correction and deterrence", "entertainment", "revenge by victims", "population control", "A",
     "Justice reforms and warns."),
    # ---------------------------------------------------------------- family
    (T_FAM, "Easy", "A family made up of father, mother and their children only is a",
     "nuclear family", "extended family", "single-parent family", "blended family", "A",
     "One roof, one small circle."),
    (T_FAM, "Medium", "Grandparents, uncles and cousins living with the immediate family form the",
     "extended family", "nuclear family", "nuclear", "commune", "A",
     "The wide family shares one yard."),
    (T_FAM, "Medium", "Children of parents who neglect their duties are most likely to",
     "drop out of school", "win scholarships early", "learn faster than peers", "avoid bad groups", "A",
     "Neglect pushes them to the street."),
    (T_FAM, "Medium", "Parents teaching children honesty and hard work at home equips the nation with",
     "responsible future citizens", "cheaper school fees", "shorter school terms", "less homework", "A",
     "The home builds the country."),
]

build_batch(
    S,
    "batch_096_waec_civic2.json",
    "096",
    "WAEC Civic round 2 (Round 19 lift): rights (fair hearing, expression) "
    "and duties (tax, defence), equality before law, checks and balances, "
    "federalism, judiciary/executive functions, retroactive laws, universal "
    "suffrage, vote buying, ballot snatching, pressure groups (NLC, NMA), "
    "protest as participation, by-election, queue orderliness, warning "
    "triangles, roadworthiness, walking facing traffic, amber light, "
    "stimulants/narcotics, withdrawal, rehabilitation, cult motives and "
    "orientation, skills acquisition, restiveness, HIV stigmatisation and "
    "PMTCT, Sardauna, Zik of Africa, Awolowo free education, federal "
    "character, unity schools, embezzlement, nepotism, criminal vs civil, "
    "purposes of punishment, nuclear/extended family, neglect "
    "consequences, home values. Scanned against WAEC r1, NECO Civic "
    "rounds 1-2 and all banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
