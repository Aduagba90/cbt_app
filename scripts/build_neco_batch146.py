"""Batch 146 - WAEC Government round 5 (WAEC top-up, R27).

Grows WAEC Government from 184 toward ~220 with angles not yet in the
bank: pre-colonial systems (emirate officials, Igbo age grades,
Oyomesi's check on the Alaafin); nationalists and their parties
(Macaulay, Azikiwe, Awolowo, Bello); constitutional milestones (the
1963 republic, 1979 executive presidency, state creations of 1967 and
1996); the 1966 coups; the National Assembly's shape and sizes (109
senators, 360 members); electoral systems (first-past-the-post,
proportional representation, the referendum); Senate confirmation of
appointments; judicial review and the Supreme Court; pressure-group
types (NLC); lobbying; non-alignment and Africa as the centrepiece;
UN organs and the OAU-to-AU shift; the 1976 local government reform;
why Nigeria chose federalism. Scanned against WAEC rounds 1-4, NECO
Government (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch146.py -> content/batch_146_waec_gov5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_PRE = "Pre-colonial Political Systems"
T_NAT = "Nationalists and Their Parties"
T_MIL = "Constitutional Milestones and the Army"
T_LEG = "The National Assembly"
T_ELS = "Electoral Systems"
T_EXEC = "The Executive"
T_JUD = "The Judiciary"
T_PG = "Pressure Groups Further"
T_FP = "Foreign Policy"
T_INT = "International Bodies"
T_LOC = "Local Government Reform"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- pre-colonial
    (T_PRE, "Hard", "In the Sokoto emirate system, the official who ranked as the emir's chief minister was the",
     "waziri", "alkali", "madawaki", "sarkin fada", "A",
     "The waziri ran the emirate's daily council."),
    (T_PRE, "Hard", "In the old Sokoto caliphate, court cases under shariah were heard by the",
     "alkali judges", "age grades", "ogboni elders", "palace drummers", "A",
     "The alkali sat with law books open."),
    (T_PRE, "Hard", "In traditional Igbo society, executing community projects and defence often fell to the",
     "age grades", "oba's court", "emir's cavalry", "waziri's clerks", "A",
     "Sets of age-mates built the roads."),
    (T_PRE, "Medium", "Among the Yoruba, the council of chiefs that could check an erring Alaafin was the",
     "Oyomesi", "Ozo society", "umuada", "noforeigners", "A",
     "The Bashorun could even present an 'rejected' symbolic parrot's egg.",
     ),

    # ------------------------------------------------------------- nationalists
    (T_NAT, "Medium", "Nigeria's first political party, the Nigerian National Democratic Party of 1923, was founded by",
     "Herbert Macaulay", "Nnamdi Azikiwe", "Obafemi Awolowo", "Ahmadu Bello", "A",
     "The electrical engineer of Lagos politics led it."),
    (T_NAT, "Medium", "The NCNC, fronted by Nnamdi Azikiwe from 1944, drew its early strength mainly from",
     "the eastern region and Zik's press", "Kano traders alone", "the army's officer corps", "Lagos market women only", "A",
     "Zik's newspapers carried the message."),
    (T_NAT, "Hard", "Free primary education in the Western Region, introduced in 1955, is credited to the government of",
     "Obafemi Awolowo", "Ahmadu Bello", "Abubakar Tafawa Balewa", "Nnamdi Azikiwe", "A",
     "The Action Group's manifesto paid the fees."),
    (T_NAT, "Medium", "The Northern People's Congress, dominant in the 1950s north, was led by",
     "Ahmadu Bello", "Aminu Kano", "Joseph Tarka", "Michael Okpara", "A",
     "The Sardauna steered the north."),

    # ------------------------------------------------------------- milestones & army
    (T_MIL, "Hard", "Nigeria cut its last tie with the British monarchy and elected a president in the year",
     "1963", "1960", "1979", "1966", "A",
     "The republican constitution did it.", "1963"),
    (T_MIL, "Hard", "The executive presidency, separating the head of state from parliament, first came into force under the constitution of",
     "1979", "1963", "1960", "1999", "A",
     "Shagari became president under it.", "1979"),
    (T_MIL, "Hard", "To blunt the secession threat in May 1967, General Gowon created",
     "12 states", "4 regions", "19 states", "36 states", "A",
     "The old regions were carved smaller.", "12"),
    (T_MIL, "Hard", "The number of states finally reached 36 in 1996 under",
     "Sani Abacha", "Ibrahim Babangida", "Murtala Mohammed", "Olusegun Obasanjo", "A",
     "Six more states completed the map."),
    (T_MIL, "Hard", "Nigeria's first military coup of January 1966 swept away the civilian government of",
     "Tafawa Balewa", "Shehu Shagari", "Ernest Shonekan", "Goodluck Jonathan", "A",
     "The prime minister died in it."),

    # ------------------------------------------------------------- assembly
    (T_LEG, "Medium", "A lawmaking house of two chambers, like Nigeria's Senate and House of Representatives, is",
     "bicameral", "unicameral", "confederal", "collegial", "A",
     "Two chambers share the law."),
    (T_LEG, "Hard", "Three senators come from each state and one from Abuja, making the Senate's full complement",
     "109 members", "108 members", "360 members", "774 members", "A",
     "Three per state plus Abuja's one.", "109"),
    (T_LEG, "Hard", "The House of Representatives seats",
     "360 members", "109 members", "774 members", "450 members", "A",
     "Population-weighted constituencies fill it.", "360"),

    # ------------------------------------------------------------- electoral systems
    (T_ELS, "Medium", "The candidate with the highest votes in a constituency wins the seat outright under the",
     "first-past-the-post system", "proportional system", "referendum", "collegial system", "A",
     "A single vote ahead is victory."),
    (T_ELS, "Hard", "Under proportional representation, parliamentary seats are shared out according to",
     "each party's vote share", "seniority of candidates", "the ruler's pleasure", "polling-unit size", "A",
     "Twenty per cent of votes, twenty per cent of seats."),
    (T_ELS, "Medium", "A direct vote in which the whole electorate decides one constitutional question is a",
     "referendum", "by-election", "plea bargain", "primary election", "A",
     "The people answer yes or no."),

    # ------------------------------------------------------------- executive
    (T_EXEC, "Hard", "Before the President's ministerial nominees take office, their names must be confirmed by the",
     "Senate", "House of Representatives only", "Supreme Court", "Council of State", "A",
     "The red chamber screens them."),
    (T_EXEC, "Medium", "Counting from his swearing-in, a Nigerian president's elected term runs for",
     "four years", "five years", "six years", "seven years", "A",
     "Renewable once, and once only."),

    # ------------------------------------------------------------- judiciary
    (T_JUD, "Hard", "The power of courts to declare a law inconsistent with the constitution void is",
     "judicial review", "judicial immunity", "habeas corpus", "assent", "A",
     "The gavel guards the constitution."),
    (T_JUD, "Medium", "The final court of appeal in Nigeria's court hierarchy is the",
     "Supreme Court", "Court of Appeal", "Federal High Court", "Sharia Court of Appeal", "A",
     "From its bench there is no further climb."),

    # ------------------------------------------------------------- pressure groups
    (T_PG, "Hard", "The Nigeria Labour Congress, united by members' occupations, is best classed as",
     "an occupational group", "a promotional group", "a religious body", "a government agency", "A",
     "Workers of many trades, one union house."),
    (T_PG, "Medium", "Quietly persuading legislators over a bill, rather than marching, is the pressure-group method of",
     "lobbying", "picketing", "rioting", "canvassing votes", "A",
     "Corridors, not barricades."),

    # ------------------------------------------------------------- foreign policy
    (T_FP, "Hard", "Nigeria's refusal to camp permanently in either Western or Eastern bloc during the Cold War followed the policy of",
     "non-alignment", "containment", "detente", "satellite status", "A",
     "Friendship with all, bondage to none."),
    (T_FP, "Medium", "Decades of Nigerian diplomacy have upheld Africa as the",
     "centrepiece of foreign policy", "second thought of policy", "private reserve of the army", "province of the churches", "A",
     "The continent comes first."),

    # ------------------------------------------------------------- international
    (T_INT, "Hard", "The five permanent members of the United Nations Security Council each hold the",
     "power of veto", "largest armies", "secret ballot", "budget control", "A",
     "One 'no' can stall a resolution."),
    (T_INT, "Medium", "In the United Nations General Assembly, each member state casts",
     "one equal vote", "votes by population", "votes by wealth", "two votes", "A",
     "Tuvalu and China weigh the same."),
    (T_INT, "Hard", "The Organisation of African Unity was transformed into the African Union in the year",
     "2002", "1963", "1994", "2010", "A",
     "Durban hosted the rebirth.", "2002"),

    # ------------------------------------------------------------- local government
    (T_LOC, "Hard", "The 1976 local government reform is remembered for introducing",
     "a uniform single-tier system nationwide", "traditional rulers' councils", "party caretaker committees", "military administrators", "A",
     "One pattern replaced the patchwork."),
    (T_LOC, "Hard", "Nigeria adopted a federal structure at independence chiefly because the country was",
     "large and deeply plural", "small and uniform", "without regions", "ruled by one king", "A",
     "Diversity demanded shared rule."),
]

build_batch(
    S,
    "batch_146_waec_gov5.json",
    "146",
    "WAEC Government round 5 (R27 top-up): waziri and alkali of the "
    "emirate, Igbo age grades, Oyomesi's check on the Alaafin; "
    "Macaulay's NNDP 1923, Zik's NCNC, Awolowo's free education, "
    "Bello's NPC; 1963 republic, 1979 executive presidency, Gowon's 12 "
    "states of 1967, Abacha's 36 of 1996, the January 1966 coup; "
    "bicameralism, 109 senators, 360 House members; "
    "first-past-the-post, proportional representation, referendum; "
    "Senate confirmation, four-year presidential term; judicial review, "
    "Supreme Court as final court; NLC as occupational group, lobbying; "
    "non-alignment, Africa as centrepiece; Security Council veto, "
    "General Assembly equal votes, OAU to AU 2002; the 1976 uniform "
    "local government reform; why federalism was adopted. Scanned "
    "against WAEC rounds 1-4, NECO Government (all rounds) and the "
    "JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
