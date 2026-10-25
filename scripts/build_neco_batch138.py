"""Batch 138 - NECO Government round 4 (NECO top-up, Round 26).

Lifts NECO Government from 156 toward ~193 with angles not yet in any
bank: legitimacy and sovereignty features; delegated legislation
controls; federalism problems; separation of powers vs checks and
balances; rule of law meaning; Clifford 1922, Richards 1946,
Macpherson 1951 and Lyttleton 1954 landmarks; parliamentary vs
presidential systems; military rule justifications and criticisms;
franchise qualifications; pressure-group methods; political party
functions; party systems; civil service permanence and neutrality;
local government functions; ombudsman-like bodies (Public Complaints
Commission); ECOWAS and OPEC aims; poverty of the census; e-voting.
Scanned against NECO rounds 1-3, WAEC Government (all rounds) and the
JAMB pool.

    python3 scripts/build_neco_batch138.py -> content/batch_138_neco_gov4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_CON = "Basic Political Concepts"
T_CONST = "Constitutions and Constitutionalism"
T_FED = "Federalism and Power Division"
T_ORG = "Organs and Principles of Government"
T_NIG = "Nigerian Constitutional Development"
T_SYS = "Systems of Government"
T_POL = "Parties, Elections and Franchise"
T_CIV = "Civil Service and Local Government"
T_INT = "Nigeria in International Bodies"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- concepts
    (T_CON, "Hard", "A government is said to have legitimacy when the people",
     "accept its right to rule", "fear its soldiers greatly", "elect foreigners to it", "print money at will", "A",
     "Consent crowns authority."),
    (T_CON, "Hard", "A key feature making sovereignty absolute is that it",
     "cannot be shared or divided", "belongs to the army", "lasts only four years", "rests with voters alone", "A",
     "The final word admits no partner."),
    (T_CON, "Medium", "Authority differs from naked power because it is",
     "recognised as rightful", "always military in form", "bought with money", "exercised by the poor", "A",
     "Right, not might, marks it."),
    (T_CON, "Medium", "From family gossip to school civics, citizens slowly absorb their political beliefs. That lifelong learning is called",
     "political socialisation", "political campaigning", "political exile", "political arithmetic", "A",
     "The mind learns its politics."),

    # ------------------------------------------------------------- constitutions
    (T_CONST, "Medium", "Parliamentary debates, judicial rulings and conventions gathered over time form the basis of",
     "an unwritten constitution", "a written constitution", "a federal constitution", "a unitary constitution", "A",
     "No single parchment holds them."),
    (T_CONST, "Medium", "A flexible constitution is one that can be amended by",
     "the ordinary lawmaking process", "a two-thirds majority only", "the courts alone", "public protest", "A",
     "Change rides the simple route."),
    (T_CONST, "Hard", "Delegated legislation is kept in check mainly through",
     "parliament and the courts", "newspaper editorials", "strike actions", "cash budgets", "A",
     "The maker audits its gift."),
    (T_CONST, "Medium", "The constitution is described as rigid when its amendment requires",
     "special cumbersome procedures", "no procedure at all", "only the president's signature", "a simple voice vote", "A",
     "The lock needs many keys."),

    # ------------------------------------------------------------- federalism
    (T_FED, "Hard", "The loudest complaint of Nigerian states against the federal arrangement concerns the centre's tight grip on",
     "revenue collection", "border control", "chieftaincy titles", "school calendars", "A",
     "The centre keeps the purse."),
    (T_FED, "Medium", "The exclusive legislative list in Nigeria is reserved for",
     "the federal government alone", "the states alone", "local governments", "the courts", "A",
     "Only Abuja writes those laws."),
    (T_FED, "Medium", "Power shared between the centre and the regions, each supreme in its sphere, defines",
     "federalism", "unitarism", "confederalism", "devolution", "A",
     "Two governments, one country."),
    (T_FED, "Hard", "The guiding principle for dividing subjects between federal and state lists is that of",
     " residuary powers, which belong to the states", "the army's choice in all matters", "the courts alone", "the Speaker's list", "A",
     "What is not listed stays local."),

    # ------------------------------------------------------------- organs & principles
    (T_ORG, "Medium", "The legislature is the organ of government chiefly responsible for",
     "lawmaking", "trying offenders", "executing budgets", "appointing clergy", "A",
     "It debates and passes bills."),
    (T_ORG, "Hard", "Separation of powers becomes workable in practice chiefly because of",
     "checks and balances", "judicial silence", "one-party rule", "military decrees", "A",
     "Each organ leans on the others."),
    (T_ORG, "Medium", "The principle that laws, not men, should rule is called the",
     "rule of law", "rule of might", "divine right", "delegated power", "A",
     "Even rulers stand beneath it."),
    (T_ORG, "Hard", "A judge sackable at the executive's pleasure cannot rule fairly against it. True judicial independence therefore rests on",
     "security of tenure", "higher salaries alone", "party membership", "frequent transfers", "A",
     "Without tenure there is no courage."),

    # ------------------------------------------------------------- Nigerian development
    (T_NIG, "Medium", "The first Nigerian constitution that allowed Lagos voters to elect their legislators was the",
     "Clifford Constitution of 1922", "Richards Constitution of 1946", "Macpherson Constitution of 1951", "Lyttleton Constitution of 1954", "A",
     "Four seats opened to the vote."),
    (T_NIG, "Medium", "Regionalism entered Nigerian government with the 1946 constitution of",
     "Governor Richards", "Governor Clifford", "Sir Macpherson", "Oliver Lyttleton", "A",
     "Three regions were created."),
    (T_NIG, "Hard", "The 1951 Macpherson Constitution made a landmark break by",
     "a central lawmaking house", "creating twelve states", "granting independence", "abolishing regions", "A",
     "African voices filled the house."),
    (T_NIG, "Hard", "The constitution that finally settled Nigeria as a federation of largely autonomous regions was that of",
     "1954 (Lyttleton)", "1946 (Richards)", "1922 (Clifford)", "1951 (Macpherson)", "A",
     "Regions gained real autonomy."),

    # ------------------------------------------------------------- systems
    (T_SYS, "Medium", "Under the Westminster model Nigeria once practised, day-to-day governance of the country lay with the",
     "prime minister", "president", "chief justice", "senate president", "A",
     "The crown reigns, the PM rules."),
    (T_SYS, "Hard", "A cardinal feature distinguishing the presidential system is",
     "the strict separation of executive and legislature", "the fusion of executive and legislature", "ministers drawn from parliament", "collective responsibility", "A",
     "Two branches stand apart."),
    (T_SYS, "Medium", "In a unitary system, constitutional power rests",
     "solely with the central government", "with the regions", "with the courts", "with traditional rulers", "A",
     "One centre alone commands all."),
    (T_SYS, "Hard", "A criticism often levelled against military rule is its",
     "suspension of the constitution", "speed of decision", "discipline in ranks", "low cost of government", "A",
     "Decrees rule where debate dies."),

    # ------------------------------------------------------------- parties & elections
    (T_POL, "Medium", "A central function of political parties is to",
     "contest elections on programmes", "audit public accounts", "sentence offenders", "print the currency", "A",
     "They bundle many wants together."),
    (T_POL, "Medium", "A two-party system operates where",
     "two major parties dominate", "only one party exists", "any number govern", "the army rules", "A",
     "Two giants share the field."),
    (T_POL, "Hard", "The political franchise of a citizen refers to his",
     "right to vote and stand", "duty to pay school fees", "licence to drive", "right to strike", "A",
     "The ballot is its plain badge."),
    (T_POL, "Hard", "The Nigerian Bar Association lobbies over court fees yet never fields candidates. Bodies like it exist to",
     "influence, not govern", "win elections outright", "command the army", "abolish government", "A",
     "They whisper, not campaign."),
    (T_POL, "Medium", "The body that registers political parties and conducts elections in Nigeria is",
     "INEC", "NYSC", "NPF", "NAFDAC", "A",
     "Its stamp legalises the ballot."),
    (T_POL, "Hard", "The strongest argument for e-voting in Nigeria is that it can",
     "cut manual collation errors", "raise paper costs", "lengthen queues at polls", "end all litigation", "A",
     "Machines sum faster than clerks."),

    # ------------------------------------------------------------- civil service & local govt
    (T_CIV, "Medium", "Civil servants remain in office regardless of which party wins because of the principle of",
     "permanence", "neutrality of the ballot", "federal character alone", "seniority of birth", "A",
     "Governments pass, the service stays."),
    (T_CIV, "Medium", "The anonymous civil servant is expected to",
     "avoid public partisanship", "campaign openly for parties", "brief the press freely", "contest elections while serving", "A",
     "His advice is secret, his loyalty civil."),
    (T_CIV, "Hard", "Clearing neighbourhood drains and keeping primary schools running are classic duties of",
     "local government", "federal government", "foreign embassies", "the electoral body", "A",
     "Nearest government, nearest needs."),
    (T_CIV, "Hard", "The Nigerian Public Complaints Commission exists to",
     "right official wrongs", "try coup plotters", "audit state accounts", "register companies", "A",
     "An ombudsman in plain clothes."),

    # ------------------------------------------------------------- international
    (T_INT, "Medium", "The founding aim of ECOWAS is the",
     "economic integration of West Africa", "military conquest of Africa", "spread of one religion", "control of world oil prices", "A",
     "One market from Dakar to Lagos."),
    (T_INT, "Medium", "Nigeria belongs to OPEC chiefly as a",
     "crude-oil exporting nation", "cocoa trading bloc", "defence alliance", "cultural festival body", "A",
     "Oil sellers keep a common house."),
    (T_INT, "Hard", "A root cause of Nigeria's unreliable census figures is the",
     "politicisation of population counts", "shortage of counting paper", "absence of any towns", "smallness of families", "A",
     "Numbers mean seats and money."),
]

build_batch(
    S,
    "batch_138_neco_gov4.json",
    "138",
    "NECO Government round 4 (Round 26 top-up): legitimacy, absolute "
    "sovereignty, authority vs power, political socialisation; "
    "unwritten and flexible constitutions, controls on delegated "
    "legislation, rigidity; fiscal centralisation problem, exclusive "
    "list, federalism definition, residuary powers; legislature's "
    "lawmaking, checks and balances, rule of law, judicial security of "
    "tenure; Clifford 1922 elective principle, Richards 1946 "
    "regionalism, Macpherson 1951 central legislature, Lyttleton 1954 "
    "federal principle; prime minister as head of government, "
    "presidential separation, unitarism, military suspension of "
    "constitutions; party functions, two-party system, franchise, "
    "pressure-group methods, INEC, e-voting; civil-service permanence "
    "and anonymity, local government functions, Public Complaints "
    "Commission; ECOWAS and OPEC aims; politicised census. Scanned "
    "against NECO rounds 1-3, WAEC Government (all rounds) and the "
    "JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
