"""Batch 120 - WAEC Government round 3 (WAEC top-up, Round 23).

Lifts WAEC Government from 138 toward ~180 with angles not yet in any
bank: political concepts (power vs authority vs legitimacy, sovereignty),
constitutions classified, organs of government compared, party systems,
electoral systems, franchise, pressure-group methods, Nigerian
constitutional development (Richards to 1999), nationalism heroes and
parties, military rule, local government, and foreign policy through
Afrocentrism. Scanned against WAEC rounds 1-2, NECO Government and the
JAMB Government pool.

    python3 scripts/build_neco_batch120.py -> content/batch_120_waec_gov3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_CON = "Political Concepts"
T_CONST = "Constitutions and Organs"
T_PARTY = "Parties, Elections and Franchise"
T_HIST = "Nigerian Constitutional History"
T_NAT = "Nationalism and Independence"
T_MIL = "Military Rule and Local Government"
T_EXT = "Foreign Policy"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- concepts
    (T_CON, "Medium", "The recognised right of a leader to be obeyed is",
     "authority", "power", "influence", "force", "A",
     "Legitimacy crowns that right."),
    (T_CON, "Hard", "The ability to compel obedience through sanctions is",
     "power", "authority", "legitimacy", "protocol", "A",
     "The stick behind the word."),
    (T_CON, "Hard", "Popular acceptance of a government's right to rule is",
     "legitimacy", "sovereignty", "authority", "mandela", "A",
     "Elections and consent feed it."),
    (T_CON, "Hard", "The quality that makes a state supreme over all within its territory is",
     "sovereignty", "population", "nationalism", "federalism", "A",
     "No higher power inside its borders."),
    (T_CON, "Medium", "A society with a defined territory, population, government and sovereignty is a",
     "state", "nation only", "tribe", "club", "A",
     "Those four marks complete it."),
    (T_CON, "Medium", "A nation is a people bound chiefly by",
     "common culture and sentiment", "one police force", "a written budget", "trade treaties", "A",
     "Feeling makes the nation."),
    (T_CON, "Medium", "Political socialisation means the process by which citizens",
     "acquire political values", "register parties", "pay campaign levies", "count ballot boxes", "A",
     "Home and school start it."),
    (T_CON, "Hard", "The transfer of central powers to weaker units below is",
     "devolution", "revolution", "evolution", "resolution", "A",
     "Law-making power flows downward."),

    # ------------------------------------------------------------- constitutions and organs
    (T_CONST, "Medium", "A constitution that is contained in many scattered documents is",
     "unwritten", "written", "rigid", "unitary", "A",
     "Britain keeps the classic example."),
    (T_CONST, "Hard", "Changing a rigid constitution demands",
     "special cumbersome procedures", "a simple act of parliament", "presidential mood", "court order alone", "A",
     "The amendment hurdle is set high."),
    (T_CONST, "Medium", "The legislature's power to investigate ministries and agencies is part of its",
     "oversight function", "judicial function", "ceremonial role", "fiscal immunity", "A",
     "Committees summon and probe."),
    (T_CONST, "Medium", "Power to make laws resides with the",
     "legislature", "judiciary", "civil service", "press", "A",
     "The elected house drafts and passes."),
    (T_CONST, "Hard", "Judicial independence is best secured by",
     "tenure protection", "annual dismissal drills", "compulsory party membership", "executive promotion lists", "A",
     "Secure tenure and funding free the judge."),
    (T_CONST, "Medium", "The executive arm's chief function is",
     "implementing laws", "interpreting statutes", "printing currency", "auditing courts", "A",
     "Policy execution is its burden."),
    (T_CONST, "Hard", "A bicameral legislature has",
     "two chambers", "one chamber", "no chambers", "party chambers only", "A",
     "Senate plus House in Nigeria."),
    (T_CONST, "Medium", "The fusion of executive and legislative members in a cabinet describes a",
     "parliamentary system", "presidential system", "confederal system", "monastic system", "A",
     "Ministers sit in parliament."),

    # ------------------------------------------------------------- parties, elections, franchise
    (T_PARTY, "Medium", "A system with only two strong parties contesting power is a",
     "two-party system", "multi-party system", "one-party system", "no-party system", "A",
     "Two giants share the arena."),
    (T_PARTY, "Hard", "Party competition under the Second Republic followed the",
     "multi-party system", "two-party system", "one-party system", "no-party system", "A",
     "Six parties registered in 1989 to 1993 elections era context aside."),
    (T_PARTY, "Hard", "The First Republic's major parties divided largely along",
     "regional and ethnic lines", "football clubs", "trade unions", "age grades", "A",
     "NPC, NCNC and AG mapped the regions."),
    (T_PARTY, "Medium", "An election in which only one candidate is presented is a",
     "plebiscite-style affirmation", "primary contest", "run-off", "proportional poll", "A",
     "The yes or no answers it."),
    (T_PARTY, "Hard", "Under first-past-the-post, the seat goes to the candidate with",
     "the highest votes cast", "over half of all votes", "the most regions", "party approval", "A",
     "A simple plurality carries the seat."),
    (T_PARTY, "Hard", "Proportional representation allocates seats according to",
     "each party's vote share", "district size only", "seniority of leaders", "number of governors", "A",
     "Votes map directly onto benches."),
    (T_PARTY, "Medium", "Universal adult suffrage means the vote belongs to",
     "all adult citizens", "taxpayers only", "graduates only", "landowners only", "A",
     "Adulthood is the only gate."),
    (T_PARTY, "Medium", "Lobbying, demonstrations and peaceful rallies are common methods of",
     "pressure groups", "electoral commissions", "civil service", "the judiciary", "A",
     "The street and the lobby are their stage."),
    (T_PARTY, "Hard", "A trade union seeking members' welfare functions mainly as a",
     "pressure group", "political party", "court of appeal", "government agency", "A",
     "It presses but does not rule."),

    # ------------------------------------------------------------- constitutional history
    (T_HIST, "Hard", "What lasting feature did the 1946 Richards Constitution bring in?",
     "regionalism", "universal suffrage", "party government", "independence at once", "A",
     "Three regional blocks entered."),
    (T_HIST, "Hard", "The 1951 constitution named after Governor Macpherson is noted for",
     "wider African participation", "ending all indirect rule", "creating the senate", "the coup clause", "A",
     "Nigerians debated its draft nationwide."),
    (T_HIST, "Hard", "The Lyttleton Constitution of 1954 made Nigeria formally a",
     "federation", "unitary state", "protectorate", "dominion", "A",
     "Regions gained real powers."),
    (T_HIST, "Medium", "Self-government arrived in 1960 under which constitution?",
     "1960", "1954", "1963", "1979", "A",
     "The Queen remained head of state.", "1960"),
    (T_HIST, "Hard", "The 1963 constitution made Nigeria a",
     "a republic", "a monarchy", "a colony", "a protectorate", "A",
     "Azikiwe became President."),
    (T_HIST, "Medium", "Which system of government did the 1979 constitution plant?",
     "presidential system", "parliamentary system", "unitary system", "chiefdom system", "A",
     "An executive president emerged."),
    (T_HIST, "Hard", "The clause requiring a presidential candidate to score one-quarter of votes in two-thirds of the states appeared first in the",
     "1979 constitution", "1960 constitution", "1963 constitution", "1999 constitution only", "A",
     "It produced the famous 12 two-thirds case."),

    # ------------------------------------------------------------- nationalism
    (T_NAT, "Medium", "Herbert Macaulay's party, Nigeria's first political party, was the",
     "NNDP", "NCNC", "NPC", "AG", "A",
     "It surfaced in 1923 in Lagos."),
    (T_NAT, "Hard", "The NCNC was formed in 1944 with which figure as a leading light?",
     "Macaulay and Azikiwe", "Ahmadu Bello alone", "Obafemi Awolowo alone", "Tafawa Balewa alone", "A",
     "The veteran passed Zik the torch."),
    (T_NAT, "Hard", "The Action Group, formed in 1951, grew out of the Yoruba cultural association called",
     "Egbe Omo Oduduwa", "Igbo State Union", "Jam'iyyar Mutanen Arewa", "Niger Delta Congress", "A",
     "The cultural seed became a party."),
    (T_NAT, "Medium", "Nnamdi Azikiwe's chain of newspapers advanced nationalism through",
     "mass enlightenment", "sports sponsorship", "land deals", "railway building", "A",
     "The West African Pilot led."),
    (T_NAT, "Medium", "The constitutional conferences of the 1950s were held mostly in",
     "London and Lagos", "Paris and Accra", "Kano and Cairo", "New York and Rome", "A",
     "Talks shuttled between the two cities."),

    # ------------------------------------------------------------- military and local govt
    (T_MIL, "Medium", "Military governments in Nigeria usually seized power through",
     "coups d'etat", "elections", "court judgments", "referenda", "A",
     "The gun replaced the ballot."),
    (T_MIL, "Hard", "A hallmark of military regimes is the suspension of",
     "the constitution", "the air force", "all schools", "all hospitals", "A",
     "Decrees then replace laws and parties."),
    (T_MIL, "Medium", "Decrees issued by military rulers rank above",
     "ordinary laws", "themselves", "international law", "court precedents", "A",
     "The decree is the supreme text."),
    (T_MIL, "Medium", "Local government's constitutional role includes providing",
     "primary services", "foreign policy", "currency issue", "army command", "A",
     "The grassroots serves daily needs."),
    (T_MIL, "Hard", "Uniform councils nationwide came from which year's local government reforms?",
     "the whole country", "the north only", "the west only", "Lagos only", "A",
     "Uniform councils replaced the patchwork."),

    # ------------------------------------------------------------- foreign policy
    (T_EXT, "Medium", "Nigeria's foreign policy is built on Afrocentrism, meaning",
     "Africa first in her diplomacy", "Europe first always", "isolation from Africa", "trade with America only", "A",
     "The continent leads the list."),
    (T_EXT, "Hard", "Nigeria's leading role in forming the OAU in 1963 flowed from her",
     "commitment to liberation", "oil wealth only", "colonial ties", "army size", "A",
     "Liberation movements found support."),
    (T_EXT, "Medium", "The principle of non-alignment in the Cold War meant Nigeria",
     "avoided joining either power bloc", "joined the Warsaw Pact", "joined NATO", "annexed neighbours", "A",
     "Neither East nor West held her."),
    (T_EXT, "Hard", "Nigeria's technical aid corps, sending professionals to sister African states, is a tool of",
     "soft power", "hard power", "military rule", "censorship", "A",
     "Shared skill builds friendship."),
]

build_batch(
    S,
    "batch_120_waec_gov3.json",
    "120",
    "WAEC Government round 3 (Round 23 top-up): authority vs power vs "
    "legitimacy, sovereignty, the state's four marks, nation, political "
    "socialisation, devolution, unwritten and rigid constitutions, "
    "legislative oversight, judicial independence, bicameralism, "
    "parliamentary fusion, two-party and multi-party systems, First "
    "Republic regional parties, first-past-the-post vs proportional "
    "representation, universal adult suffrage, pressure-group methods "
    "and trade unions, Richards 1946 regionalism, Macpherson 1951, "
    "Lyttleton 1954 federation, 1960 independence, 1963 republic, 1979 "
    "presidential system and the two-thirds clause, NNDP 1923, NCNC "
    "1944, Egbe Omo Oduduwa and the AG, Zik's newspapers, London-Lagos "
    "conferences, coups and decrees, 1976 local government reforms, "
    "Afrocentrism, OAU role, non-alignment and technical aid as soft "
    "power. Scanned against WAEC rounds 1-2, NECO Government and the "
    "JAMB Government pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
