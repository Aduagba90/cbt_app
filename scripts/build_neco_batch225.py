"""Batch 225 - WAEC Civic Education round 8 (WAEC top-up, R45).

Grows WAEC Civic from 265 toward ~290 with angles verified absent
from the whole Civic pool (535 items across WAEC and NECO):
constitutional democracy; independence of the judiciary; presumption
of innocence; probity; religious intolerance; volunteerism;
self-esteem; goal setting; time management; consumer rights;
minimum wage; strike; gender discrimination; social security;
national flower (Costus spectabilis); tiers of government;
environmental sanitation; peacekeeping; declaration of assets; due
process; bail; NHRC; right to property; election violence; tree
planting. Checked and avoided (already banked): fair hearing, checks
and balances, universal adult suffrage, equality before the law,
election observers, voter education, inter-marriage, youth
restiveness, nepotism, separation of powers, national consciousness,
cybercrime, self-reliance, transparency, accountability, cultism,
drug abuse, political apathy, human trafficking, examination
malpractice, selfless citizen, constitutionalism, legal aid,
domestic violence, public property, disability rights, right to
life, right to education, federal character (13 hits), recall,
impeachment, referendum, franchise, naturalisation, duties,
tolerance, honesty, justice, discipline, contentment, integrity,
EFCC, bribery.

    python3 scripts/build_neco_batch225.py -> content/batch_225_waec_civic8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_DRL = "Democracy and the Rule of Law"
T_CRA = "Constitution, Rule of Law and Arms of Government"
T_RDL = "Rights, Duties and Law"
T_ACC = "Anti-Corruption and Conduct"
T_NUI = "National Unity and Integration"
T_DOC = "Duties and Obligations of Citizens"
T_VAL = "Values"
T_RD = "Rights and Duties"
T_HR = "Human Rights"
T_GS = "Government Structures"
T_NS = "National Symbols"
T_NNB = "Nationalism and Nation Building"
T_HRI = "Human Rights Instruments"
T_EPP = "Elections and Political Participation"

PASSAGES = []
PQ = []

Q = [
    (T_DRL, "Medium", "A system of government in which the people's elected representatives rule, but only within the limits that the constitution sets, is called",
     "constitutional democracy", "absolute monarchy",
     "military dictatorship", "anarchy", "A",
     "The constitution holds the leash of power."),
    (T_CRA, "Medium", "The arrangement by which judges decide cases free from threats, sackings and interference from the president, governors or rich men is called",
     "independence of the judiciary", "immunity of the legislature",
     "impartiality of the police", "insulation of the executive", "A",
     "No big man may lean on the judge's scale."),
    (T_RDL, "Medium", "The legal principle that every person accused of a crime is treated as innocent until a court of law has proved him guilty is the",
     "presumption of innocence", "presumption of guilt",
     "principle of parity", "privilege of silence", "A",
     "The burden of proof rests on the accuser."),
    (T_ACC, "Hard", "The strict honesty and sound character expected of a public officer, shown in complete and upright handling of public money, is called",
     "probity", "probation",
     "prominence", "promotion", "A",
     "Clean hands and open books at all times."),
    (T_NUI, "Medium", "A citizen who hates his neighbour simply because the neighbour prays in a different way from him is displaying",
     "religious intolerance", "religious tolerance",
     "national consciousness", "party loyalty", "A",
     "Another man's faith has become his offence."),
    (T_DOC, "Easy", "A graduate spends her Saturdays teaching pupils in an orphanage without asking for any payment. This spirit of offering service freely is",
     "volunteerism", "vacationing",
     "vandalism", "verbosity", "A",
     "Her only wage is the good she does."),
    (T_VAL, "Medium", "A student who knows her own worth, walks tall and speaks up in class without fear or arrogance is said to have",
     "self-esteem", "selfishness",
     "self-pity", "self-employment", "A",
     "She values herself without looking down on others."),
    (T_VAL, "Easy", "Before the school year begins, Ada writes down that she will finish her syllabus by March and score above 80 in Civic Education. This practice is",
     "goal setting", "gossiping",
     "gambling", "grumbling", "A",
     "The target is chosen before the race starts."),
    (T_VAL, "Easy", "A trader plans her day the night before, fixing hours for market, rest and family so that no duty is swallowed by another. Her habit is",
     "time management", "time wasting",
     "time sharing", "time serving", "A",
     "Every hour is given its own work."),
    (T_RD, "Medium", "When a buyer is cheated with a false measure or a spoilt tin of milk, the civic right of his that has been breached is his right as a",
     "consumer", "commuter",
     "candidate", "creditor", "A",
     "Fair measure and true quality are his due."),
    (T_HR, "Medium", "The least amount an employer may legally pay a worker for a month's labour, fixed by government and reviewed from time to time, is the",
     "minimum wage", "maximum wage",
     "median income", "tax allowance", "A",
     "No lawful pay may fall beneath that floor."),
    (T_HR, "Medium", "The right of workers, acting together through their union, to refuse to work until their grievances are addressed is the right to",
     "go on strike", "go on holiday",
     "go to court only", "go slow in speech", "A",
     "The tools lie down until the talk is done."),
    (T_HR, "Medium", "A firm rejects the best-qualified candidate for its manager post simply because she is a woman. This act is",
     "gender discrimination", "general recruitment",
     "genuine competition", "graded promotion", "A",
     "Her sex, not her skill, decided the matter."),
    (T_GS, "Medium", "The support, in money and services, which a government gives to the aged, the jobless and the disabled who cannot fully provide for themselves, is",
     "social security", "social media",
     "social status", "societal pressure", "A",
     "The state carries those who cannot carry themselves."),
    (T_NS, "Easy", "Nigeria's national flower, shown on the coat of arms, whose flat red flowers bloom close to the ground across the savanna, is the",
     "Costus spectabilis", "rose of Sharon",
     "hibiscus flower", "lily of the Nile", "A",
     "It lies on the shield's base in the arms."),
    (T_GS, "Easy", "The division of government in Nigeria into the federal level, the thirty-six states and the 774 local government areas is the division into",
     "tiers of government", "terms of government",
     "tenets of government", "teams of government", "A",
     "Each level serves its own layer of the people."),
    (T_DOC, "Easy", "Residents of a street come out together one Saturday to cut the grass, clear the gutters and sweep the drainage. This civic duty is",
     "environmental sanitation", "environmental pollution",
     "environmental degradation", "environmental audit", "A",
     "A clean street is dug by every hand on it."),
    (T_NNB, "Medium", "Nigerian soldiers serve in troubled lands under the United Nations and ECOWAS, keeping warring parties apart and protecting civilians. This service abroad is called",
     "peacekeeping", "pleasure travel",
     "peaceful protest", "picketing", "A",
     "They stand between fighters and the weak."),
    (T_ACC, "Medium", "On taking office, a governor publicly lists his houses, bank accounts and other wealth, and does so again when he leaves. This practice is the",
     "declaration of assets", "denial of assets",
     "devaluation of assets", "distribution of assets", "A",
     "His pocket is opened for all to inspect."),
    (T_CRA, "Medium", "The requirement that government business follow the correct laid-down steps — advertisement, shortlisting, interview, approval — before a contract is awarded, is",
     "due process", "due date",
     "dual mandate", "day-to-day rule", "A",
     "No corner may be cut on the way."),
    (T_RDL, "Medium", "A sum of money or a surety which an accused person lodges, or a person stands for him, so that he is released from custody until his trial comes up, is",
     "bail", "bond of slavery",
     "bribe", "bill of rights", "A",
     "He answers his charge from outside the cell."),
    (T_HRI, "Medium", "The government body established to receive complaints from citizens whose human rights have been violated and to investigate such complaints is the",
     "National Human Rights Commission", "National Health Insurance Scheme",
     "Nigeria Labour Congress", "National Youth Service Corps", "A",
     "The complainant's cry reaches its desk."),
    (T_HR, "Medium", "The guarantee that a citizen may own land, houses and businesses, and that they cannot be seized from him without the law and fair compensation, is the",
     "right to property", "right to poverty",
     "right to publicity", "right to possession of votes", "A",
     "What he honestly owns, he honestly keeps."),
    (T_EPP, "Medium", "On election day, thugs beat up voters, snatch ballot boxes and burn election materials at a polling unit. These acts are collectively",
     "election violence", "election observers' work",
     "electoral education", "electoral goodwill", "A",
     "The ballot is stolen by fist and fire."),
    (T_DOC, "Easy", "Members of a town union return every December to plant shade trees along the new road and teach pupils to water them. This service protects",
     "the environment", "the currency",
     "the constitution", "the coat of arms", "A",
     "Every seedling is a gift to the air."),
]

build_batch(
    S,
    "batch_225_waec_civic8.json",
    "225",
    "WAEC Civic round 8 (R45 top-up): constitutional democracy; "
    "independence of the judiciary; presumption of innocence; "
    "probity; religious intolerance; volunteerism; self-esteem; goal "
    "setting; time management; consumer rights; minimum wage; "
    "strike; gender discrimination; social security; national flower "
    "(Costus spectabilis); tiers of government; environmental "
    "sanitation; peacekeeping; declaration of assets; due process; "
    "bail; National Human Rights Commission; right to property; "
    "election violence; tree planting. Scanned against the whole "
    "Civic pool (WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
