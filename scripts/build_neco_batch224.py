"""Batch 224 - WAEC Agricultural Science round 8 (WAEC top-up, R45).

Grows WAEC Agric from 255 toward ~280 with angles verified absent
from the whole Agricultural Science pool (1,095 items across JAMB,
WAEC and NECO): palatability; blackquarter; fowl typhoid; tillering;
eluviation; laterite; young farmers club; FADAMA; River Basin
Development Authorities; Green Revolution; Land Use Decree; dibbler;
wheelbarrow; clutch (poultry); steaming up; incubator; farm-gate
price; middlemen; guaranteed price; cashew; gum arabic; curing;
parboiling; egg grading; dissolved oxygen. Checked and avoided
(already banked): incubation period, germination test, cud, ruminant
stomach, mastitis, coccidiosis, Newcastle, gumboro, trypanosomiasis,
anthrax, ringworm (R44 item), candling, debeaking, clutch (tractor
PTO item - distinct machine sense), flushing (R44 item), steaming up
was only a distractor in it, deep litter, battery cage, moulting,
free range, maintenance ration, bloat, salvage value, depreciation,
marketing board, marketing channel, OFN, ADP, IITA, kola, sorghum,
millet, cocoyam, sweet potato, alley cropping, furrow, salinity,
waterlogging, threshing, winnowing, reforestation, clear felling,
plankton, poaching, compass bearing, tillage, seedbed, ridging,
grafting, layering, budding, tissue culture, dormancy, roguing,
hardening off, soil profile, loam, hygroscopic water, field
capacity, foliar (top-dressing R44 item's family).

    python3 scripts/build_neco_batch224.py -> content/batch_224_waec_agric8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_PF = "Pasture and Feed"
T_AH = "Animal Health"
T_ACH = "Animal and Crop Health"
T_CROP = "Crop Production"
T_SSF = "Soil Science Further"
T_SS = "Soil Science and Fertility"
T_EXT = "Agricultural Extension"
T_ILT = "Institutions and Land Tenure"
T_IPM = "Institutions, Processing and Mechanisation"
T_MSA = "Meaning and Scope of Agriculture"
T_LT = "Land Tenure and Land Use"
T_TOOL = "Farm Tools and Machinery"
T_LP = "Livestock and Poultry"
T_AN = "Animal Nutrition"
T_FPM = "Farm Power and Machinery"
T_FME = "Farm Management and Economics"
T_AE = "Agricultural Economics"
T_PH = "Post-harvest and Storage"
T_APS = "Agro-processing and Storage"
T_FF = "Fish Farming"

PASSAGES = []
PQ = []

Q = [
    (T_PF, "Medium", "The quality that makes an animal glad to eat a feed because it tastes good to it, whether fresh and juicy or otherwise, is called",
     "palatability", "digestibility",
     "profitability", "portability", "A",
     "The tongue decides before the stomach does."),
    (T_AH, "Hard", "A young bull in the herd develops a hot swelling on the thigh, limps and dies quickly. The disease that causes such gassy muscle swellings in young cattle is",
     "blackquarter", "foot and mouth",
     "rinderpest", "mastitis", "A",
     "The swelling crackles under the fingers."),
    (T_ACH, "Hard", "A poultry disease caused by bacteria in which adult hens grow pale, droop, lose appetite and their laying drops sharply is",
     "fowl typhoid", "Newcastle disease",
     "gumboro", "coccidiosis", "A",
     "The pale comb tells of the fever within."),
    (T_CROP, "Medium", "A maize plant sends out extra shoots from its base near the soil, so that one stand later carries several stems. This production of side shoots is called",
     "tillering", "tilling",
     "topping", "trailing", "A",
     "One seed becomes a small family of stems."),
    (T_SSF, "Hard", "The washing down of minerals and other materials from the upper layer of a soil into the layer beneath it is called",
     "eluviation", "erosion",
     "evaporation", "afforestation", "A",
     "The top layer gives; the layer below receives."),
    (T_SS, "Medium", "The reddish, iron-rich tropical soil, soft when dug from below but hardening like brick on exposure to sun and air, is",
     "laterite", "loam",
     "humus", "marl", "A",
     "Cut it and leave it; it soon sets like stone."),
    (T_EXT, "Easy", "The club formed in many secondary schools, in which students keep a school garden and rear small animals to learn farming practically, is the",
     "Young Farmers' Club", "Boys' Scout",
     "Red Cross Society", "Press Club", "A",
     "Members learn farming with their own hands."),
    (T_ILT, "Hard", "The World Bank-assisted Nigerian project under which farmers in the low, seasonally flooded valley bottoms of the north grow irrigated vegetables and rice is the",
     "FADAMA project", "OFN programme",
     "Green Revolution", "River Basin scheme", "A",
     "Its name is the Hausa word for the wet lowlands."),
    (T_IPM, "Medium", "The government authorities created in the 1970s to control rivers, build dams and provide water all year for irrigation farming in their areas are the",
     "River Basin Development Authorities", "Local Government Councils",
     "Agricultural Development Projects", "Marketing Boards", "A",
     "Each watches over the rivers of its own basin."),
    (T_MSA, "Medium", "The programme launched in 1980 by the Nigerian government, using fertiliser subsidies and new seeds to push the country towards growing enough food for itself, was the",
     "Green Revolution", "Operation Feed the Nation",
     "Structural Adjustment", "FADAMA project", "A",
     "Its name promised fields of plenty."),
    (T_LT, "Medium", "The 1978 decree that vested all land in each state in the hands of the military governor, making farmers seek rights of occupancy, is the",
     "Land Use Decree", "Hire Purchase Act",
     "Minerals Act", "Agricultural Loans Act", "A",
     "Land title now flowed from the governor's office."),
    (T_TOOL, "Medium", "The short, pointed, T-handled tool with which a farmer makes small holes in the seedbed and drops seeds into them one by one is the",
     "dibbler", "mattock",
     "hand fork", "hand trowel", "A",
     "Poke, drop, cover: the hole-maker earns its name."),
    (T_TOOL, "Easy", "The one-wheeled cart with two handles, pushed like a barrow, with which a worker carries small loads of manure or harvest across the farm, is the",
     "wheelbarrow", "head pan",
     "ox cart", "tractor trailer", "A",
     "One wheel, two handles, many trips."),
    (T_LP, "Medium", "A hen lays one egg each day for about three weeks, then pauses and turns broody. The whole batch of eggs she lays before pausing is called a",
     "clutch", "brood of eggs",
     "pullet", "moult", "A",
     "The eggs come in one unbroken run."),
    (T_AN, "Hard", "A dairy farmer gives his in-calf cow a rising allowance of rich concentrate in the last weeks before calving, so that she calves strongly and milks well. This feeding is",
     "steaming up", "flushing",
     "creep feeding", "roughage feeding", "A",
     "The udder is prepared before the calf arrives."),
    (T_FPM, "Easy", "The warm cabinet in a poultry house, heated by electricity or kerosene, in which fertile eggs are turned daily until they hatch, is an",
     "incubator", "brooder",
     "hutch", "crush", "A",
     "The eggs rest in its steady warmth."),
    (T_FME, "Medium", "The price a farmer receives for his produce right at the farm, before any transporter or middleman adds his own cost, is the",
     "farm-gate price", "retail price",
     "floor price of the market", "export price", "A",
     "It is what the buyer pays at the gate."),
    (T_AE, "Medium", "The chain of traders — assemblers, wholesalers and retailers — who stand between the farmer and the final consumer of his produce are collectively called",
     "middlemen", "marketers of banks",
     "millers only", "middle class", "A",
     "The produce passes through their hands."),
    (T_AE, "Medium", "The minimum price at which the government promises to buy a farmer's grain in a season of plenty, so that he is not ruined by crashing prices, is the",
     "guaranteed price", "grey price",
     "black market price", "general price index", "A",
     "The farmer can plant without fear of a crash."),
    (T_CROP, "Medium", "A tree crop of the savanna belt, grown in Kogi and Enugu for its curved, kidney-shaped nut and its juicy false fruit, is the",
     "cashew", "castor",
     "cocoa", "coconut", "A",
     "The nut hangs below a swollen juicy apple."),
    (T_CROP, "Medium", "The gum, tapped from thorny acacia trees of the Sudan savanna and exported for use in sweets and inks, is",
     "gum arabic", "rubber latex",
     "copal resin", "chewing gum base", "A",
     "The bark is cut and the gum oozes out."),
    (T_PH, "Medium", "After harvest, freshly dug yams are kept warm and shaded for some days until their small wounds dry and heal over before storage. This treatment is called",
     "curing", "cooling",
     "coating", "canning", "A",
     "Healed wounds refuse the rot entry."),
    (T_APS, "Medium", "Rice paddy is first soaked and steamed, then dried before milling, so that the grain hardens and keeps more of its food value. This treatment is",
     "parboiling", "polishing",
     "pickling", "pasteurising", "A",
     "The half-cooked grain resists breaking in the mill."),
    (T_LP, "Easy", "On a poultry farm, eggs are examined and sorted by weight and shell quality before packing, the big ones apart from the small. This process is",
     "egg grading", "egg candling",
     "beak trimming", "egg incubation", "A",
     "Each size travels to its own crate."),
    (T_FF, "Medium", "Fish in a crowded pond gasp at the surface at dawn because the level of the gas they need in the water has fallen. That gas is",
     "dissolved oxygen", "carbon dioxide",
     "nitrogen", "ammonia gas", "A",
     "Their breath is dissolved in the water."),
]

build_batch(
    S,
    "batch_224_waec_agric8.json",
    "224",
    "WAEC Agric round 8 (R45 top-up): palatability; blackquarter; "
    "fowl typhoid; tillering; eluviation; laterite; Young Farmers' "
    "Club; FADAMA; River Basin Development Authorities; Green "
    "Revolution 1980; Land Use Decree 1978; dibbler; wheelbarrow; "
    "clutch (poultry); steaming up; incubator; farm-gate price; "
    "middlemen; guaranteed price; cashew; gum arabic; curing of "
    "yams; parboiling of rice; egg grading; dissolved oxygen. "
    "Scanned against the whole Agric pool (JAMB, WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
