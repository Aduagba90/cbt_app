"""Batch 118 - WAEC Civic Education round 3 (WAEC top-up, Round 23).

Lifts WAEC Civic from 130 toward ~175 with angles not yet in any bank:
citizenship acquisition and loss, duties vs rights detail, rule of law
principles, separation of powers and checks, federalism features and
problems, electoral offences, recall, political parties vs pressure
groups, public service codes, corruption agencies' distinct mandates,
human trafficking and drug abuse, cultism, youth empowerment schemes,
traffic rules and order of precedence. Scanned against WAEC rounds 1-2,
NECO Civic and the JAMB Government pool.

    python3 scripts/build_neco_batch118.py -> content/batch_118_waec_civic3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_CIT = "Citizenship"
T_RIGHT = "Rights, Duties and Law"
T_GOV = "Government Structures"
T_ELEC = "Elections and Participation"
T_ILL = "Social Ills"
T_YOUTH = "Youth and Empowerment"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- citizenship
    (T_CIT, "Medium", "A foreign woman married to a Nigerian citizen for some years may become a citizen by",
     "registration", "birth", "naturalisation at once", "conquest", "A",
     "Marriage opens the registry route."),
    (T_CIT, "Hard", "A foreigner who has lived and worked in Nigeria legally for many years may seek citizenship by",
     "naturalisation", "registration", "birth", "double descent", "A",
     "It ends with an oath of allegiance."),
    (T_CIT, "Medium", "Citizenship by birth in Nigeria flows chiefly from",
     "citizen parentage", "long residence alone", "marriage alone", "buying land", "A",
     "Blood descent carries citizenship."),
    (T_CIT, "Hard", "A Nigerian citizen by birth who becomes a citizen of another country",
     "retains Nigerian citizenship", "loses it at once", "must renounce publicly", "is deported home", "A",
     "The constitution allows dual status for such citizens."),
    (T_CIT, "Medium", "Renunciation of citizenship is declared formally to the",
     "President", "Senate", "Chief Judge", "INEC chairman", "A",
     "The declaration reaches the top office."),

    # ------------------------------------------------------------- rights and law
    (T_RIGHT, "Medium", "The right to life, dignity and personal liberty are classified as",
     "fundamental human rights", "legal rights only", "privileged grants", "party rights", "A",
     "Chapter IV shelters them."),
    (T_RIGHT, "Medium", "Paying taxes honestly and obeying lawful orders are citizens'",
     "duties", "rights", "privileges", "options", "A",
     "Every right draws one behind it."),
    (T_RIGHT, "Hard", "The principle that no one is above the law is the",
     "rule of law", "rule of might", "divine right", "delegated legislation", "A",
     "Dicey championed the principle."),
    (T_RIGHT, "Hard", "Equality before the law means a governor and a farmer accused of the same offence face",
     "the same courts and process", "different judges entirely", "private tribunals", "party discipline only", "A",
     "The blindfold on Justice says it."),
    (T_RIGHT, "Medium", "Separation of powers among the three arms chiefly guards against",
     "tyranny and abuse of power", "frequent elections", "free journalism", "long budgets", "A",
     "Each arm checks the others."),
    (T_RIGHT, "Hard", "The judiciary's power to void laws that offend the constitution is",
     "judicial review", "judicial immunity", "habeas corpus", "assent", "A",
     "Courts strike down the bad law."),
    (T_RIGHT, "Medium", "A citizen detained unlawfully may invoke the writ of",
     "habeas corpus", "certiorari", "mandamus", "subpoena", "A",
     "Produce the body, the court orders."),

    # ------------------------------------------------------------- structures
    (T_GOV, "Medium", "Nigeria's federal system shares constitutional powers between",
     "the centre and the states", "the senate and police", "courts and banks", "parties and churches", "A",
     "Two tiers rule one nation."),
    (T_GOV, "Hard", "A major problem of Nigerian federalism is",
     "revenue allocation rows", "too few local languages", "excess rainfall", "small population", "A",
     "Who gets what always rankles."),
    (T_GOV, "Medium", "The 1999 Constitution came into force on",
     "29 May 1999", "1 October 1960", "1 January 1914", "17 January 1966", "A",
     "The Fourth Republic opened that day."),
    (T_GOV, "Hard", "A confederation differs from a federation because member states in a confederation",
     "retain final sovereignty", "lose all powers", "elect one king", "share no trade", "A",
     "Members may even pull out."),
    (T_GOV, "Medium", "Local governments in Nigeria are created by",
     "state laws", "federal proclamation alone", "court orders", "traditional councils", "A",
     "State assemblies map the councils."),
    (T_GOV, "Hard", "The code of conduct for public officers is administered by the",
     "Code of Conduct Bureau", "EFCC", "NPF", "NYSC", "A",
     "Asset forms go to it yearly."),

    # ------------------------------------------------------------- elections and participation
    (T_ELEC, "Medium", "Buying or selling votes during an election is",
     "an electoral offence", "a civic duty", "free marketing", "party strategy allowed", "A",
     "The electoral law frowns at it."),
    (T_ELEC, "Hard", "The process by which voters remove an elected officer before term's end is",
     "recall", "impeachment", "referendum", "plebiscite", "A",
     "Voters' signatures start it."),
    (T_ELEC, "Medium", "Snatching ballot boxes on election day attracts",
     "criminal prosecution", "a commendation", "a small fine only", "promotion", "A",
     "It is theft plus an electoral crime."),
    (T_ELEC, "Medium", "Pressure groups differ from political parties because they seek to",
     "influence policy only", "win power directly", "abolish government", "run the courts", "A",
     "Lobbying, not ballots, is their tool."),
    (T_ELEC, "Medium", "Nigeria's electoral body INEC is chaired by",
     "a chairman", "the Senate President", "the CJN", "the IGP", "A",
     "The commission is a collegiate body."),
    (T_ELEC, "Hard", "Permanent voter's cards in Nigeria are issued only to citizens who have reached age",
     "18", "16", "21", "25", "A",
     "Adults alone enter the register.", "18"),
    (T_ELEC, "Medium", "Voter education before elections mainly aims to",
     "raise informed participation", "sell party forms", "advertise candidates", "reduce polling units", "A",
     "An informed voter is a guard."),

    # ------------------------------------------------------------- social ills
    (T_ILL, "Medium", "Recruiting people by force or deceit for exploitation is",
     "human trafficking", "human capital flight", "social mobility", "brain gain", "A",
     "NAPTIP pursues the crime."),
    (T_ILL, "Hard", "The agency statutorily charged with fighting human trafficking in Nigeria is",
     "NAPTIP", "NAFDAC", "SON", "NEMA", "A",
     "Trafficking is its whole mandate."),
    (T_ILL, "Medium", "Narcotic arrests and trafficker prosecutions belong to the",
     "NDLEA", "NPF Traffic Wardens", "FRSC", "NSCDC", "A",
     "Narcotics are its sole beat."),
    (T_ILL, "Hard", "A key reason pupils join campus cults is",
     "peer pressure", "excess scholarship money", "strong parental support", "too much sport", "A",
     "Belonging seduces the lonely."),
    (T_ILL, "Medium", "Cultism on campuses is best discouraged through",
     "counselling and engagement", "banning all clubs", "closing schools", "longer holidays", "A",
     "A filled mind resists the oath."),
    (T_ILL, "Medium", "Corruption in public office includes",
     "bribery and embezzlement", "honest auditing", "open competitive bidding", "prompt salary payment", "A",
     "It is the abuse of trust."),
    (T_ILL, "Hard", "The EFCC's special focus among these crimes is",
     "economic and financial crimes", "traffic offences", "food quality", "land disputes", "A",
     "Its very name spells the focus."),
    (T_ILL, "Hard", "Punishing an offender after a fair trial enforces",
     "justice and deterrence", "impunity", "amnesty", "immunity", "A",
     "Penalty warns the next person."),

    # ------------------------------------------------------------- youth and empowerment
    (T_YOUTH, "Medium", "The NYSC scheme was established to promote",
     "national unity and integration", "military training", "foreign travel", "party politics", "A",
     "Graduates serve outside home regions."),
    (T_YOUTH, "Hard", "The NYSC was created in the year",
     "1973", "1960", "1979", "1999", "A",
     "It followed the civil war.", "1973"),
    (T_YOUTH, "Medium", "Youth empowerment programmes chiefly aim to",
     "build skills and self-reliance", "replace schools", "end all examinations", "militarise the young", "A",
     "Skill opens the door to work."),
    (T_YOUTH, "Medium", "Volunteering in community projects displays",
     "civic responsibility", "political apathy", "elite capture", "selfishness", "A",
     "Service without pay builds the town."),
    (T_YOUTH, "Medium", "Orderly queues at a bus stop display",
     "discipline and respect", "wastefulness", "cowardice", "illiteracy", "A",
     "First come, first served fairly."),
    (T_YOUTH, "Hard", "The traffic rule that keeps the road safe at an intersection without lights is",
     "give way to traffic from the right", "the loudest horn goes first", "bigger vehicle first", "pedestrians reverse", "A",
     "The rule calms the junction."),
    (T_YOUTH, "Medium", "The National Honours Award honours citizens for",
     "distinguished service", "long holidays abroad", "winning elections", "paying school fees", "A",
     "Merit earns the nation's sash."),
    (T_YOUTH, "Medium", "In protocol, the order of precedence begins with the",
     "President", "Senate President", "Chief Justice", "IGP", "A",
     "The head of state leads the line."),
]

build_batch(
    S,
    "batch_118_waec_civic3.json",
    "118",
    "WAEC Civic Education round 3 (Round 23 top-up): citizenship by "
    "registration and naturalisation, birth by descent, dual citizenship "
    "for citizens by birth, renunciation to the President, Chapter IV "
    "rights paired with duties, rule of law and equality before the law, "
    "separation of powers, judicial review, habeas corpus, federalism and "
    "revenue-allocation friction, the 1999 Constitution's commencement, "
    "confederation vs federation, local government creation, the Code of "
    "Conduct Bureau, vote-buying, recall, ballot-snatching, pressure "
    "groups vs parties, INEC's structure, PVC at 18, voter education, "
    "human trafficking and NAPTIP, NDLEA, cultism causes and cures, "
    "corruption and EFCC's focus, justice and deterrence, NYSC (1973) "
    "and its purpose, youth empowerment, volunteering, queue discipline, "
    "give-way rule, national honours and order of precedence. Scanned "
    "against WAEC rounds 1-2, NECO Civic and the JAMB Government pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
