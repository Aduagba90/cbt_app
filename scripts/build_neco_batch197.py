"""Batch 197 - NECO Government round 7 (NECO top-up, R38).

Grows NECO Government from 228 toward ~253 with angles not yet in
the bank: the NNDP of 1923; Awolowo's UPN; INEC's federal
elections; FEDECO in 1979; judicial review; the Waziri; the
Ogboni; the Igbo age-grade; gerrymandering; Aguiyi-Ironsi the
first military Head of State; Nzeogwu's January 1966 coup; the
July 1966 counter-coup; the Mid-West Region of 1963; the Code of
Conduct Bureau; the ICPC; the register of voters; the returning
officer; the election petition tribunal; a hung parliament; the
Speaker; the constituency; the constitution as supreme law; the
electorate; party symbols on the ballot; the mace. Scanned against
the whole Government pool (WAEC, NECO and JAMB stems, 1,303
items).

    python3 scripts/build_neco_batch197.py -> content/batch_197_neco_gov7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_CON = "Nigerian Constitutions and History"
T_PTY = "Political Parties and Elections"
T_PRE = "Pre-colonial Political Systems"
T_CON2 = "Basic Political Concepts"
T_MIL = "The Military in Nigerian Politics"
T_ADM = "Public Administration and Control"

PASSAGES = []
PQ = []

Q = [
    (T_PTY, "Medium", "The party on whose platform Chief Obafemi Awolowo contested the presidency in the Second Republic was the",
     "Unity Party of Nigeria", "National Party of Nigeria",
     "Great Nigeria People's Party", "Nigeria Advance Party", "A",
     "It rose from the old Action Group family."),
    (T_PTY, "Easy", "Presidential, National Assembly, governorship and state assembly elections in Nigeria are conducted by",
     "INEC", "FEDECO",
     "the political parties", "the civil service", "A",
     "The commission prints the ballots and declares results."),
    (T_PTY, "Hard", "The body that conducted the 1979 general elections that ushered in the Second Republic was",
     "FEDECO", "INEC",
     "the Electoral Commission of Nigeria", "NADECO", "A",
     "Its full name was the Federal Electoral Commission."),
    (T_CON2, "Medium", "The power of the law courts to declare a legislation null and void because it conflicts with the constitution is called",
     "judicial review", "judicial precedent",
     "judicial immunity", "judicial independence", "A",
     "The judges test every law against the constitution."),
    (T_PRE, "Hard", "In the Hausa-Fulani emirate system, the official who ranked next to the Emir and oversaw administration was the",
     "Waziri", "Galadima",
     "Madawaki", "Sarkin Fada", "A",
     "The vizier of the emirate's daily government."),
    (T_PRE, "Hard", "In the Old Oyo Empire, the secret society that checked the excesses of the Oyo Mesi themselves was the",
     "Ogboni", "Are-Ona-Kakanfo",
     "Ilari", "Bale council", "A",
     "The elders' cult balanced the kingmakers."),
    (T_PRE, "Hard", "In pre-colonial Igbo society, the age-grade functioned chiefly as an organ of",
     "communal labour and defence", "tax collection",
     "the chief priests", "foreign trade", "A",
     "Men of one age worked and fought as one."),
    (T_PTY, "Hard", "The drawing of constituency boundaries in a way that favours one political party is called",
     "gerrymandering", "franchise restriction",
     "proportional zoning", "rotational candidacy", "A",
     "The map is bent to bend the vote."),
    (T_MIL, "Medium", "After the January 1966 coup, the command of the federal military government was handed to",
     "Major-General J.T.U. Aguiyi-Ironsi", "General Yakubu Gowon",
     "General Murtala Mohammed", "Major Kaduna Nzeogwu", "A",
     "The General Officer Commanding became Head of State."),
    (T_MIL, "Hard", "The coup of 15 January 1966, Nigeria's first, was led by",
     "Major Chukwuma Kaduna Nzeogwu", "Major-General Aguiyi-Ironsi",
     "Colonel Adekunle Fajuyi", "Major Theophilus Danjuma", "A",
     "The Kaduna major struck on a cold night."),
    (T_MIL, "Hard", "The officer who emerged as Head of State after the July 1966 counter-coup was",
     "Yakubu Gowon", "Aguiyi-Ironsi",
     "Murtala Mohammed", "Olusegun Obasanjo", "A",
     "The young general took charge at thirty-one."),
    (T_CON, "Hard", "The Mid-West Region, created in 1963, is remembered as the only Nigerian region created through a",
     "referendum", "military decree",
     "order of the Privy Council", "constitutional conference", "A",
     "The people of the area voted for their own region."),
    (T_ADM, "Hard", "The body that receives asset declarations from public officers and enforces the code of conduct is the",
     "Code of Conduct Bureau", "Public Complaints Commission",
     "Federal Character Commission", "National Assembly", "A",
     "Every public officer must file his assets with it."),
    (T_ADM, "Medium", "The Independent Corrupt Practices and Other Related Offences Commission was established mainly to",
     "prosecute official corruption", "conduct general elections",
     "audit government accounts", "vet judicial appointments", "A",
     "It charges the bribe-taker to court."),
    (T_PTY, "Easy", "The official list containing the names of all persons qualified to vote in an election is the",
     "register of voters", "ballot paper",
     "electoral college", "census paper", "A",
     "A name absent from it cannot vote."),
    (T_PTY, "Medium", "The official who counts the votes at the end of a constituency election and declares the winner is the",
     "returning officer", "presiding officer",
     "party agent", "electoral commissioner", "A",
     "The final declaration is his to make."),
    (T_PTY, "Medium", "A candidate dissatisfied with the declared result of an election challenges it before the",
     "election petition tribunal", "Council of State",
     "police service commission", "party's national caucus", "A",
     "Lawyers argue the ballots one by one."),
    (T_CON2, "Easy", "A parliament in which no single political party commands an overall majority is called",
     "a hung parliament", "a shadow parliament",
     "a bicameral house", "a constituent assembly", "A",
     "Coalitions must be built to govern."),
    (T_CON2, "Easy", "The officer who presides over the sittings of the House of Representatives is the",
     "Speaker", "Senate President",
     "Clerk of the House", "Majority Leader", "A",
     "He keeps order and puts every question."),
    (T_PTY, "Easy", "The electoral area that one member of a legislature represents is called a",
     "constituency", "ward",
     "district of residence", "province", "A",
     "Its people send him to speak for them."),
    (T_CON2, "Easy", "The law that stands above every other law of a country and overrides them all is the",
     "constitution", "decree of the ruler",
     "majority resolution", "common law", "A",
     "Any law that fights it falls."),
    (T_CON2, "Easy", "All the qualified voters of a country taken together are known as",
     "the electorate", "the legislature",
     "the delegates", "the caucus", "A",
     "Their collective voice chooses the government."),
    (T_PTY, "Medium", "Party symbols are printed on ballot papers in Nigeria chiefly to help",
     "illiterate voters identify their party", "the police verify the results",
     "the printer sort the papers", "candidates check their names", "A",
     "The broom and the umbrella speak for those who cannot read."),
    (T_CON2, "Medium", "The ornamented staff carried into the chamber before the Speaker symbolises",
     "the authority of the House", "the unity of the parties",
     "the independence of the judiciary", "the wealth of the nation", "A",
     "No sitting is valid without it present."),
]

build_batch(
    S,
    "batch_197_neco_gov7.json",
    "197",
    "NECO Government round 7 (R38 top-up): NNDP 1923; Awolowo's "
    "UPN; INEC's federal elections; FEDECO 1979; judicial review; "
    "the Waziri; the Ogboni check on the Oyo Mesi; the Igbo "
    "age-grade; gerrymandering; Aguiyi-Ironsi the first military "
    "Head of State; Nzeogwu's January 1966 coup; the July 1966 "
    "counter-coup; the Mid-West Region of 1963 by referendum; the "
    "Code of Conduct Bureau; the ICPC; the register of voters; the "
    "returning officer; the election petition tribunal; a hung "
    "parliament; the Speaker; the constituency; the constitution "
    "as supreme law; the electorate; party symbols for illiterate "
    "voters; the mace. Scanned against the whole Government pool "
    "(WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
