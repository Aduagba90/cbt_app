"""Batch 057 - NECO Government, Paper III Objective round 1.

NECO SSCE Government Paper III is a 60-item objective paper (1 hr).
This batch covers the SSCE government syllabus with stable historical
and definitional facts (Nigerian constitutions, nationalism, organs of
government, parties, elections, federalism, foreign policy, international
organisations), near-duplicate scanned against the JAMB and WAEC banks.

    python3 scripts/build_neco_batch57.py -> content/batch_057_neco_government.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_SCOPE = "Meaning and Scope of Government"
T_CONCEPT = "Basic Political Concepts"
T_CONST = "Constitutions"
T_ORGANS = "Organs of Government"
T_PARTY = "Political Parties and Party Systems"
T_PRESS = "Pressure Groups and Public Opinion"
T_ELECT = "Electoral Systems"
T_NIGCON = "Development of the Nigerian Constitution"
T_COLON = "Colonial Administration"
T_NAT = "Nationalism in Nigeria"
T_FED = "Federalism and Regionalism"
T_LOCAL = "Local Government"
T_CIVIL = "The Civil Service"
T_PUB = "Public Corporations"
T_MIL = "The Military in Nigerian Politics"
T_FOREIGN = "Nigerian Foreign Policy"
T_INT = "International Organisations"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------- meaning and scope
    (T_SCOPE, "Easy", "Government may be defined as the machinery through which the will of the state is",
     "formulated and carried out", "suppressed",
     "ignored by the people", "written by scholars", "A",
     "Government makes and administers the policies of the state."),
    (T_SCOPE, "Easy", "An organised community of people with a defined territory and a government is a",
     "state", "club", "family", "church", "A",
     "Population, territory, government and sovereignty make a state."),
    (T_SCOPE, "Medium", "Learning government at school chiefly aims to produce citizens who are",
     "politically aware", "wealthy traders",
     "civil servants only", "professional lawyers only", "A",
     "Knowing how government works builds informed participation."),
    (T_SCOPE, "Easy", "Which of these is a feature of statehood?",
     "Sovereignty", "Written constitution only", "One-party system", "Membership of the UN", "A",
     "A state must be supreme over its territory."),
    (T_SCOPE, "Hard", "A state differs from a government because the state is",
     "outlasts every government", "is elected every four years",
     "is smaller than a government", "is always democratic", "A",
     "Governments come and go; the state endures."),

    # ------------------------------------------------------- basic concepts
    (T_CONCEPT, "Medium", "A government enjoys legitimacy when its right to rule is accepted by the",
     "people it governs", "foreign embassies",
     "courts alone", "civil servants only", "A",
     "A legitimate government is obeyed out of acceptance, not fear."),
    (T_CONCEPT, "Medium", "Power that is recognised as rightful and lawful is called",
     "authority", "force", "influence", "wealth", "A",
     "Authority is legitimate power."),
    (T_CONCEPT, "Easy", "A system of government in which supreme power belongs to the people is",
     "democracy", "monarchy", "oligarchy", "aristocracy", "A",
     "Demos (people) plus kratos (rule): democracy."),
    (T_CONCEPT, "Medium", "The doctrine that separates the functions of government among different organs is the",
     "separation of powers", "rule of law",
     "checks and balances only", "federal character", "A",
     "Montesquieu urged dividing legislative, executive and judicial powers."),
    (T_CONCEPT, "Hard", "Political authority exercised according to known laws and not at the ruler's whim is the essence of",
     "the rule of law", "delegated legislation",
     "anarchy", "administrative law", "A",
     "Dicey's rule of law subordinates everybody to ordinary law."),
    (T_CONCEPT, "Easy", "Equality before the law is a principle of",
     "the rule of law", "federalism", "dictatorship", "impeachment", "A",
     "No person is above the law under the rule of law."),

    # -------------------------------------------------------------- constitutions
    (T_CONST, "Medium", "A constitution that is contained in a single formal document is described as",
     "written", "unwritten", "rigid", "flexible", "A",
     "The 1999 Nigerian Constitution is a written one."),
    (T_CONST, "Medium", "A constitution that can be amended only by a special, difficult process is said to be",
     "rigid", "flexible", "unwritten", "unitary", "A",
     "Rigid constitutions demand special majorities for change."),
    (T_CONST, "Easy", "Every other law in a country takes its authority from the",
     "constitution", "annual budget",
     "register of political parties", "diary of the president", "A",
     "All other laws take authority from the constitution."),
    (T_CONST, "Hard", "Britain is the classic example of a country with an",
     "unwritten constitution", "entrenched bill of rights only",
     "elected monarchy", "one-party charter", "A",
     "British constitutional rules scatter across statutes and conventions."),

    # ------------------------------------------------------------ organs of govt
    (T_ORGANS, "Easy", "The organ of government responsible for making laws is the",
     "legislature", "executive", "judiciary", "civil service", "A",
     "Parliaments and assemblies debate and pass laws."),
    (T_ORGANS, "Easy", "The organ that interprets the laws and settles disputes is the",
     "judiciary", "executive", "legislature", "police council", "A",
     "Courts of law adjudicate and interpret statutes."),
    (T_ORGANS, "Easy", "The arm of government that implements and enforces laws is the",
     "executive", "judiciary", "legislature", "press", "A",
     "Ministers and agencies execute government policy."),
    (T_ORGANS, "Medium", "In Nigeria's presidential system, the President belongs to which arm of government?",
     "The executive", "The legislature", "The judiciary", "The civil service", "A",
     "The President heads the executive arm."),
    (T_ORGANS, "Hard", "The power of the courts to declare a law unconstitutional is known as",
     "judicial review", "judicial immunity", "habeas corpus",
     " parliamentary privilege", "A",
     "Judicial review keeps the legislature within constitutional limits."),
    (T_ORGANS, "Medium", "Deliberation, lawmaking and oversight of ministries are functions of the",
     "legislature", "executive council", "judicial service",
     "public service commission", "A",
     "Assemblies make laws and watch the executive."),

    # --------------------------------------------------------- political parties
    (T_PARTY, "Easy", "An organised group of people who share the same political beliefs and seek to win elections is a",
     "political party", "pressure group", "civil service", "trade union", "A",
     "Parties contest elections to capture government power."),
    (T_PARTY, "Medium", "A system in which only one party is legally permitted to exist is a",
     "one-party system", "two-party system", "multi-party system", "zero-party system", "A",
     "Some African states once banned opposition parties."),
    (T_PARTY, "Medium", "Nigeria's Second Republic (1979–1983) operated a",
     "multi-party system", "one-party system", "two-party system", "no-party system", "A",
     "NPN, UPN, NPP, GNPP and PRP among others contested in 1979."),
    (T_PARTY, "Hard", "A political party performs all of the following EXCEPT",
     "providing employment for all citizens", "recruiting political leaders",
     "educating the electorate", "organising governments", "A",
     "Parties mobilise and lead, but do not employ everybody."),
    (T_PARTY, "Medium", "The party that won the presidential election of the Nigerian First Republic in alliance was led largely by",
     "Nnamdi Azikiwe", "Ahmadu Bello", "Obafemi Awolowo",
     "Herbert Macaulay", "A",
     "The NCNC-NPC coalition produced the First Republic government."),

    # ------------------------------------------------------ pressure groups
    (T_PRESS, "Easy", "The Nigerian Labour Congress (NLC) is an example of a",
     "pressure group", "political party", "public corporation",
     "parastatal of state", "A",
     "Unions press government on policy without seeking office."),
    (T_PRESS, "Medium", "A pressure group differs from a political party because it does NOT",
     "seek to form a government", "represent members' interests",
     "lobby legislators", "educate the public", "A",
     "Pressure groups influence those in power; parties seek power."),
    (T_PRESS, "Medium", "Lobbying, strikes and public demonstrations are methods of",
     "pressure groups", "the judiciary", "the civil service", "local councils", "A",
     "These are classic instruments of group pressure."),
    (T_PRESS, "Hard", "A group formed to protect the occupational interests of its members, like the Nigerian Bar Association, is called a",
     "sectional/interest group", "promotional group", "anonymous group",
     "government agency", "A",
     "Sectional groups advance their members' direct interests."),

    # ---------------------------------------------------------- electoral systems
    (T_ELECT, "Easy", "The body constitutionally charged with conducting elections in Nigeria is",
     "INEC", "the police", "the senate committee",
     "the judiciary", "A",
     "The Independent National Electoral Commission runs elections."),
    (T_ELECT, "Medium", "An election in which citizens vote to approve or reject a proposal directly is a",
     "referendum", "plebiscite for officials", "primary election",
     "by-election", "A",
     "Referendums put questions to the voters themselves."),
    (T_ELECT, "Medium", "A vote cast in secret to protect the voter from intimidation upholds the principle of",
     "the secret ballot", "open voting", "proxy voting",
     "public acclamation", "A",
     "Secret balloting safeguards free choice."),
    (T_ELECT, "Easy", "An election held to fill a vacant seat caused by death or resignation is a",
     "by-election", "general election", "primary", "run-off", "A",
     "By-elections fill casual vacancies."),
    (T_ELECT, "Hard", "Gerrymandering is the manipulation of",
     "electoral boundaries", "ballot boxes",
     "party manifestos", "voters' registers", "A",
     "Redrawing constituencies to favour a party is gerrymandering."),
    (T_ELECT, "Medium", "Universal adult suffrage means that every qualified adult citizen",
     "may vote in elections", "must join a party",
     "can be a judge", "cannot abstain", "A",
     "Suffrage extended to all adults regardless of wealth or sex."),

    # ------------------------------------------- Nigerian constitutional development
    (T_NIGCON, "Medium", "The Clifford Constitution of 1922 introduced",
     "the elective principle", "regional governments",
     "a presidential system", "the office of prime minister", "A",
     "Legislative Council elections held in Lagos and Calabar from 1923."),
    (T_NIGCON, "Medium", "The Richards Constitution of 1946 is remembered for creating",
     "three regional houses of assembly", "a bicameral federal parliament",
     "the office of president", "universal suffrage", "A",
     "It brought the North, East and West into one legislative framework."),
    (T_NIGCON, "Hard", "The Lyttleton Constitution of 1954 is significant because it made Nigeria a",
     "federation of regions", "unitary republic",
     "British colony under one council", "one-party state", "A",
     "Regions became autonomous units: the federal idea took root."),
    (T_NIGCON, "Medium", "Nigeria attained independence on",
     "1st October 1960", "1st October 1963",
     "29th May 1999", "1st January 1914", "A",
     "Independence came in 1960; the Republic followed in 1963."),
    (T_NIGCON, "Medium", "Nigeria became a republic in 1963, meaning the",
     "a president became head of state", "the military took power",
     "regions were abolished", "constitution became unwritten", "A",
     "Cutting the monarch's link created the First Republic."),
    (T_NIGCON, "Hard", "The 1979 Constitution introduced the presidential system, replacing the",
     "the Westminster system", "the unitary system",
     "colonial governorship", "military decrees", "A",
     "An executive president replaced the prime-minister model."),
    (T_NIGCON, "Medium", "Nigeria's Fourth Republic operates under the constitution of",
     "1999", "1989", "1979", "1963", "A",
     "The 1999 Constitution (as amended) governs the Fourth Republic.",
     "1999"),

    # ------------------------------------------------------ colonial administration
    (T_COLON, "Medium", "Lord Lugard completed the amalgamation of the Northern and Southern Protectorates in",
     "1914", "1922", "1946",
     "1951", "A",
     "Lugard merged the two protectorates into one Nigeria in 1914."),
    (T_COLON, "Medium", "The policy of ruling colonies through their traditional rulers is called",
     "indirect rule", "direct rule", "assimilation",
     "association by decree", "A",
     "Britain governed Northern Nigeria through emirs."),
    (T_COLON, "Hard", "Indirect rule succeeded best in Northern Nigeria mainly because of the",
     "the centralised emirates", "absence of any rulers",
     "large number of lawyers", "coastal location", "A",
     "The emirates already had structured authority to build on."),
    (T_COLON, "Medium", "The 1929 Aba Women's Riot was largely a protest against",
     "taxation of market women", "the railway",
     "the 1946 constitution", "the second world war", "A",
     "Colonial attempts to tax market women sparked the uprising."),
    (T_COLON, "Medium", "A warrant chief in colonial Eastern Nigeria was a",
     "government-appointed local ruler", "elected senator",
     "judge of the high court", "district officer", "A",
     "Warrants created new chiefs where none had traditional standing."),

    # ------------------------------------------------------------- nationalism
    (T_NAT, "Medium", "The first major political party in Nigeria, founded in 1923, was the",
     "Nigerian National Democratic Party", "National Council of Nigeria and the Cameroons",
     "Action Group", "Northern Peoples Congress", "A",
     "Herbert Macaulay formed the NNDP to contest Lagos seats."),
    (T_NAT, "Medium", "Herbert Macaulay is popularly regarded as the father of",
     "Nigerian nationalism", "Nigerian literature",
     "the civil service", "the 1999 constitution", "A",
     "His campaigns in the 1920s launched organised nationalism."),
    (T_NAT, "Medium", "The NCNC, founded in 1944, was led in its early years by",
     "Nnamdi Azikiwe", "Ahmadu Bello", "Obafemi Awolowo",
     "Tafawa Balewa", "A",
     "Zik led the national council from its inception."),
    (T_NAT, "Hard", "The West African Student's Union (WASU) contributed to nationalism by",
     "campaigning against colonial rule abroad", "funding the military",
     "drafting the 1954 constitution", "creating regions", "A",
     "London-based students kept colonial criticism alive overseas."),
    (T_NAT, "Medium", "Nigerian newspapers like the West African Pilot advanced the nationalist cause chiefly by",
     "spreading anti-colonial ideas", "advertising British goods",
     "supporting warrant chiefs", "reporting cricket only", "A",
     "Zik's Pilot gave nationalism a loud popular voice."),

    # ----------------------------------------------------- federalism/regionalism
    (T_FED, "Medium", "A federal system is one in which power is",
     "shared between tiers of government", "held by one government only",
     "held by traditional rulers", "exercised by the courts", "A",
     "Nigeria shares powers between Abuja and the states."),
    (T_FED, "Hard", "The Exclusive Legislative List in Nigeria contains matters on which only the",
     "federal government may legislate", "states may legislate",
     "local councils legislate", "judges make rules", "A",
     "Defence and currency are federal-only subjects."),
    (T_FED, "Medium", "One argument for federalism in a large country like Nigeria is that it",
     "allows communities self-rule", "makes the country smaller",
     "abolishes local languages", "ends all elections", "A",
     "Federalism accommodates diversity through autonomy."),
    (T_FED, "Hard", "Fiscal federalism concerns the sharing of",
     "revenue among governments", "cabinet posts",
     "diplomatic postings", "university admissions", "A",
     "FAAC allocations are the heart of Nigerian fiscal federalism."),

    # ------------------------------------------------------------ local government
    (T_LOCAL, "Medium", "The primary purpose of local government is to",
     "bring government closer to the people", "replace state governments",
     "conduct national elections", "print the currency", "A",
     "Grassroots administration serves local needs directly."),
    (T_LOCAL, "Hard", "The 1976 local government reforms introduced a uniform system of local government",
     "throughout Nigeria", "in Lagos only", "in the north only",
     "in the east only", "A",
     "Uniform councils on a nationwide pattern date from 1976."),
    (T_LOCAL, "Medium", "Collecting local rates and maintaining markets are functions of",
     "local government councils", "the federal executive council",
     "the judiciary", "INEC", "A",
     "Councils run markets, motor parks and local rates."),

    # --------------------------------------------------------------- civil service
    (T_CIVIL, "Easy", "The body of appointed officials who implement government policies is the",
     "civil service", "cabinet", "judiciary", "legislature", "A",
     "Civil servants serve governments of every party."),
    (T_CIVIL, "Medium", "The head of the civil service of a Nigerian state is typically the",
     "head of service", "governor", "speaker",
     "chief judge", "A",
     "The Head of Service administers the state bureaucracy."),
    (T_CIVIL, "Medium", "Permanence, neutrality and anonymity are core principles of the",
     "civil service", "armed forces", "political parties", "pressure groups", "A",
     "Civil servants stay politically neutral and serve continuously."),
    (T_CIVIL, "Hard", "The policy direction of a ministry is set by the",
     "minister", "permanent secretary alone", "clerical officers",
     "trade unions", "A",
     "Ministers give political leadership; the permanent secretary administers."),

    # ------------------------------------------------------------ public corporations
    (T_PUB, "Medium", "A public corporation is established mainly to",
     "provide essential services", "win elections",
     "interpret the constitution", "train judges", "A",
     "Utility bodies like the old NEPA served the public."),
    (T_PUB, "Medium", "Which of these was a public corporation in Nigeria?",
     "The old Nigerian Railway Corporation", "The senate",
     "A private limited company", "A law court", "A",
     "Railways, NEPA and NITEL were public corporations."),
    (T_PUB, "Hard", "Public corporations are usually created by an",
     "act of the legislature", "order of the judiciary",
     "internal memo", "election", "A",
     "Statutes establish and empower parastatals."),

    # ------------------------------------------------------- military in politics
    (T_MIL, "Medium", "The military first seized power in Nigeria in",
     "January 1966", "October 1960", "January 1963",
     "May 1999", "A",
     "The January 1966 coup ended the First Republic.",
     "1966"),
    (T_MIL, "Medium", "Military governments in Nigeria ruled mainly by",
     "decrees", "acts of parliament", "referenda",
     "common law only", "A",
     "Decrees replaced ordinary statutes under military rule."),
    (T_MIL, "Hard", "The military handed power to a civilian government on 29 May 1999, beginning the",
     "Fourth Republic", "First Republic", "Second Republic",
     "Third Republic", "A",
     "The Fourth Republic began with the 1999 handover."),
    (T_MIL, "Medium", "A major reason advanced to justify military intervention in Nigerian politics was",
     "political instability and corruption", "the colour of the flag",
     "abundance of foreign aid", "the census of 1963 only", "A",
     "Coups were defended as rescue operations."),

    # --------------------------------------------------------- foreign policy
    (T_FOREIGN, "Medium", "Nigeria's foreign policy is constitutionally directed by the",
     "president", "chief justice", "senate president",
     "council of traditional rulers", "A",
     "The executive president steers external relations."),
    (T_FOREIGN, "Hard", "The principle that Africa remains the centrepiece of Nigeria's foreign policy was championed especially by",
     "the Murtala/Obasanjo era", "the colonial office",
     "the 1922 constitution", "the Lagos chamber of commerce", "A",
     "The 1976 Africa-centred doctrine shaped engagements like Angola."),
    (T_FOREIGN, "Medium", "Nigeria's leading role in creating ECOWAS in 1975 reflects its policy of",
     "African regional cooperation", "isolationism",
     "colonial loyalty", "trade with Asia only", "A",
     "Nigeria championed West African integration."),
    (T_FOREIGN, "Easy", "Nigeria belongs to all of these organisations EXCEPT",
     "the European Union", "the United Nations",
     "the African Union", "the Commonwealth", "A",
     "Nigeria is African; the EU is a European club."),

    # -------------------------------------------------- international organisations
    (T_INT, "Easy", "The United Nations was founded in 1945 primarily to maintain international",
     "peace and security", "trade tariffs",
     "colonial rule", "sports", "A",
     "The UN Charter's first purpose is world peace."),
    (T_INT, "Medium", "The five permanent members of the UN Security Council include",
     "Britain and China", "Nigeria and Ghana",
     "Brazil and India", "Egypt and Kenya", "A",
     "The USA, Russia, China, Britain and France hold permanent seats."),
    (T_INT, "Medium", "The African Union, formerly the Organisation of African Unity, was relaunched in",
     "2002", "1963", "1999",
     "2010", "A",
     "The OAU became the AU at Durban in 2002.",
     "2002"),
    (T_INT, "Hard", "The Commonwealth is best described as an association of",
     "mostly former British territories", "oil-producing countries",
     "military allies of the USA", "European states only", "A",
     "Membership grew out of the old British Empire."),
    (T_INT, "Medium", "The ECOWAS treaty of 1975 was signed in",
     "Lagos", "Accra", "Dakar",
     "Abuja", "A",
     "The treaty establishing ECOWAS was signed in Lagos."),
]

build_batch(
    S,
    "batch_057_neco_government.json",
    "057",
    "NECO Government Paper III round 1: fresh SSCE-standard items on stable "
    "historical and definitional facts — Nigerian constitutions 1922-1999, "
    "colonial administration, nationalism, organs of government, parties, "
    "pressure groups, elections, federalism, local government, civil "
    "service, public corporations, military era, foreign policy and "
    "international organisations. Near-duplicate scanned against the JAMB "
    "and WAEC banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
