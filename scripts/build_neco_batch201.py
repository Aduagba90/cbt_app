"""Batch 201 - WAEC Government round 7 (WAEC top-up, R39).

Grows WAEC Government from 252 toward ~274 with angles not yet in
the bank: the GNPP of Waziri Ibrahim; Aminu Kano's PRP; Azikiwe's
NPP; the Council of State; the National Judicial Council; the
removal of a state governor; the oath of office; question time;
the constitutional monarch who reigns but does not rule; Murtala's
19 states of 1976; the ambassador; the unicameral legislature;
primary elections; deregulation; government as an institution; the
Federal Executive Council; the Official Opposition; proportional
representation; the fourth estate; censorship. Scanned against the
whole Government pool (WAEC, NECO and JAMB stems, 1,327 items).

    python3 scripts/build_neco_batch201.py -> content/batch_201_waec_gov7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_HIS = "Nigerian Government and History"
T_INS = "Organs and Institutions of Government"
T_CON = "Basic Political Concepts"
T_ELE = "Electoral Systems"
T_PTY = "Political Parties"
T_PRE = "The Media"

PASSAGES = []
PQ = []

Q = [
    (T_PTY, "Hard", "In the Second Republic, the Great Nigeria People's Party (GNPP) was led by",
     "Waziri Ibrahim", "Aminu Kano",
     "Nnamdi Azikiwe", "Obafemi Awolowo", "A",
     "The Borno-born politician carried the north-east."),
    (T_PTY, "Medium", "The People's Redemption Party of the Second Republic, champion of the talakawa, was led by",
     "Aminu Kano", "Waziri Ibrahim",
     "Shehu Shagari", "Michael Okpara", "A",
     "The teacher of the common people returned."),
    (T_PTY, "Medium", "The Nigerian People's Party, which allied with the NPN after the 1979 election, was led by",
     "Nnamdi Azikiwe", "Obafemi Awolowo",
     "Aminu Kano", "Waziri Ibrahim", "A",
     "The Zik of Africa led the eastern party."),
    (T_INS, "Hard", "The body of former heads of state, chief justices and governors which advises the President is the",
     "Council of State", "Federal Executive Council",
     "National Council of Ministers", "National Economic Council", "A",
     "The elders of the state sit in council."),
    (T_INS, "Hard", "The body that recommends the appointment of judges to the President in Nigeria's Fourth Republic is the",
     "National Judicial Council", "National Assembly",
     "Nigerian Bar Association", "Federal Character Commission", "A",
     "The bench breeds its own gatekeepers."),
    (T_INS, "Hard", "Under the 1999 Constitution, the removal of a state governor found guilty of gross misconduct follows the process of",
     "impeachment by the House of Assembly", "recall by his constituents",
     "a court martial", "a referendum of the state", "A",
     "Two-thirds of the house must concur."),
    (T_INS, "Medium", "A public officer swearing on the Qur'an or the Bible to discharge his duties faithfully is taking the",
     "oath of office", "oath of allegiance",
     "oath of secrecy", "vow of neutrality", "A",
     "The sworn word binds the officer to duty."),
    (T_INS, "Medium", "The session in the legislature during which ministers answer oral questions from members is",
     "question time", "the committee stage",
     "the second reading", "the recess", "A",
     "The executive account for their works aloud."),
    (T_INS, "Medium", "In Britain, the monarch is said to reign but not rule. This describes",
     "a constitutional monarchy", "an absolute monarchy",
     "a republican presidency", "a diarchy of parties", "A",
     "The crown is worn but the cabinet governs."),
    (T_HIS, "Hard", "The number of states in Nigeria rose to nineteen in 1976 under the regime of",
     "Murtala Mohammed", "Yakubu Gowon",
     "Olusegun Obasanjo", "Ibrahim Babangida", "A",
     "The February redivision carved seven new states."),
    (T_CON, "Medium", "A diplomatic officer accredited as his country's highest representative in a foreign state is an",
     "ambassador", "attaché",
     "consul of trade", "envoy clerk", "A",
     "He speaks for his nation abroad."),
    (T_CON, "Easy", "A legislature that consists of only one chamber or house is described as",
     "unicameral", "bicameral",
     "confederal", "diarchal", "A",
     "One house makes the laws alone."),
    (T_ELE, "Medium", "The election held within a political party to choose its candidate for a general election is called a",
     "primary election", "by-election",
     "run-off election", "general election", "A",
     "The party picks its standard-bearer first."),
    (T_ELE, "Medium", "The electoral system in which political parties win seats in proportion to the votes they receive is",
     "proportional representation", "the first-past-the-post system",
     "the electoral college", "the simple majority system", "A",
     "Twenty per cent of votes, twenty per cent of seats."),
    (T_CON, "Medium", "The removal of government controls and restrictions from the operations of an industry is called",
     "deregulation", "nationalisation",
     "privatisation", "commercialisation", "A",
     "The state loosens its grip on prices."),
    (T_CON, "Easy", "Government as an institution of the state refers to",
     "the machinery for making and enforcing policies", "the people living in a territory",
     "the constitution of a country", "the election held every four years", "A",
     "The machinery through which the state acts."),
    (T_INS, "Medium", "The body of ministers appointed by the President to assist in running the executive arm is the",
     "Federal Executive Council", "Council of State",
     "National Assembly", "civil service commission", "A",
     "The cabinet of the federation sits weekly."),
    (T_INS, "Medium", "In the British House of Commons, the largest party outside the government is styled",
     "the Official Opposition", "the shadow cabinet",
     "the backbench bloc", "the minority committee", "A",
     "Her Majesty's Opposition keeps watch."),
    (T_PRE, "Medium", "The mass media is often called the fourth estate of the realm because it",
     "watches and checks the government", "collects taxes for the crown and courts",
     "commands the armed forces", "appoints the judges", "A",
     "After clergy, nobles and commons, the press."),
    (T_PRE, "Medium", "The official banning of a publication or broadcast by government authority is called",
     "censorship", "propaganda",
     "libel", "gagging by taxation", "A",
     "The blue pencil of the state."),
    (T_CON, "Easy", "The head of state in a typical parliamentary system performs mainly",
     "ceremonial functions", "day-to-day lawmaking",
     "judicial functions", "military command", "A",
     "He opens parliament and receives envoys."),
    (T_CON, "Medium", "A system of government in which powers are shared between a central government and component units is",
     "federalism", "unitarism",
     "confederalism", "devolution only", "A",
     "Each tier holds its own powers."),
]

build_batch(
    S,
    "batch_201_waec_gov7.json",
    "201",
    "WAEC Government round 7 (R39 top-up): Waziri Ibrahim's GNPP; "
    "Aminu Kano's PRP; Azikiwe's NPP; the Council of State; the "
    "National Judicial Council; impeachment of a governor; the "
    "oath of office; question time; the constitutional monarch; "
    "nineteen states in 1976; the ambassador; unicameral "
    "legislature; primary elections; proportional representation; "
    "deregulation; government as an institution; the Federal "
    "Executive Council; the Official Opposition; the fourth "
    "estate; censorship; the ceremonial head of state; federalism "
    "defined. Scanned against the whole Government pool (WAEC, "
    "NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
