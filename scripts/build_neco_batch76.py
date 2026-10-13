"""Batch 076 - WAEC Agricultural Science, Paper 1 Objective round 1.

WASSCE Agricultural Science Paper 1 (Objective) is a 50-item paper (50 min;
official 2026 second-series timetable, paper 5021). This batch covers the
WASSCE agricultural syllabus with FRESH angles and phrasings - scenario-led
items (streaked maize leaves, crashed tomato prices, fish-pond draining),
Nigeria-specific facts (groundnut savanna, cocoa belt, West African Dwarf
goat) and question-form stems - because the near-dup scan checks every item
against the JAMB, WAEC and NECO banks, including the large JAMB Agric banks
(batches 039-040) and our 90-item NECO Agric bank.

    python3 scripts/build_neco_batch76.py -> content/batch_076_waec_agric.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_MEAN = "Meaning and Scope of Agriculture"
T_SOIL = "Soil Science and Fertility"
T_CROP = "Crop Production"
T_PEST = "Pests and Diseases"
T_ANIM = "Animal Production"
T_TOOL = "Farm Tools and Machinery"
T_REC = "Farm Management and Economics"
T_FISH = "Fisheries, Forestry and Wildlife"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- meaning and scope
    (T_MEAN, "Easy", "A farmer grows maize and rears goats for sale. Both activities together are called",
     "agriculture", "manufacturing", "mining", "commerce", "A",
     "Crop growing plus animal rearing is agriculture."),
    (T_MEAN, "Easy", "Which of these is a branch of agriculture?",
     "fishery", "carpentry", "mining", "pottery", "A",
     "Fishery falls directly under agriculture."),
    (T_MEAN, "Medium", "The agro-allied industry that supplies hides and skins to tanneries depends on",
     "cattle production", "fisheries", "poultry", "bee-keeping", "A",
     "Hides and skins come from livestock."),
    (T_MEAN, "Easy", "The cultivation of vegetables, fruits and ornamental plants is called",
     "horticulture", "agronomy", "apiculture", "silviculture", "A",
     "Horticulture covers fruits and vegetables."),
    (T_MEAN, "Medium", "Farming that supplies raw materials to industries shows agriculture as a source of",
     "industrial input", "foreign exchange", "employment only", "medical drugs", "A",
     "Farms feed factories with raw materials."),
    (T_MEAN, "Easy", "A farmer who keeps insects that produce honey and wax practises",
     "apiculture", "aquaculture", "horticulture", "sericulture", "A",
     "Bee-keeping for honey is apiculture."),
    (T_MEAN, "Medium", "Which of these occupations is NOT directly under agriculture?",
     "quarrying", "fishing", "poultry keeping", "forestry", "A",
     "Quarrying digs stones, not farm work."),
    # ---------------------------------------------------------------- soil
    (T_SOIL, "Easy", "The best soil for most crops, holding both water and air well, is",
     "loam", "clay", "sand", "gravel", "A",
     "Loam balances drainage and retention."),
    (T_SOIL, "Medium", "Soil particles joined together into small clumps are said to form its",
     "structure", "texture", "profile", "consistency", "A",
     "Structure is about how particles clump."),
    (T_SOIL, "Medium", "A handful of soil feels gritty and drains water fast. Its particle-size make-up is its",
     "texture", "structure", "tilth", "profile", "A",
     "Texture is the particle-size mix."),
    (T_SOIL, "Medium", "Adding lime to a very acidic soil mainly",
     "raises its pH level", "lowers its pH", "raises its salinity", "hardens its pan", "A",
     "Lime reduces soil acidity."),
    (T_SOIL, "Medium", "For most food crops, the most suitable soil pH range is",
     "6.0 to 7.0", "2.0 to 3.0", "9.0 to 10.0", "4.0 to 4.5", "A",
     "Most crops like a near-neutral pH."),
    (T_SOIL, "Hard", "The washing of soil nutrients deep down the profile by heavy rain is called",
     "leaching", "erosion", "capping", "denudation", "A",
     "Rain water carries solubles downwards."),
    (T_SOIL, "Easy", "Farmyard manure improves soil mainly by adding",
     "organic matter", "sand particles", "lime salts", "soil water", "A",
     "Manure feeds the soil with humus."),
    (T_SOIL, "Medium", "On a fertiliser bag marked NPK 15:15:15, the numbers show the",
     "nutrient percentages", "weight of the bag", "price per tonne", "application rate", "A",
     "Each figure is a nutrient's share."),
    (T_SOIL, "Hard", "Water erosion that carves small channels across farmland is",
     "rill erosion", "gully erosion", "sheet erosion", "wind erosion", "A",
     "Rills are the small early channels."),
    # ---------------------------------------------------------------- crop production
    (T_CROP, "Easy", "Which of these crops is planted using stem cuttings rather than seeds?",
     "cassava", "maize", "rice", "sorghum", "A",
     "Cassava stem pieces sprout roots."),
    (T_CROP, "Easy", "Yams are mainly propagated through",
     "seed yams or setts", "stem cuttings", "bulbils only", "vine grafts", "A",
     "Setts from tubers grow new yams."),
    (T_CROP, "Medium", "A farmer grows maize and cowpea together on the same plot at the same time. This is",
     "intercropping", "crop rotation", "monocropping", "fallowing", "A",
     "Mixed stands on one plot is intercrop."),
    (T_CROP, "Medium", "Growing different crops on the same land in a fixed order over seasons is",
     "crop rotation", "intercropping", "continuous cropping", "mixed farming", "A",
     "A fixed seasonal sequence rotates."),
    (T_CROP, "Medium", "A farmer alternates maize, cowpea and fallow on one plot over four seasons. The system is",
     "crop rotation", "monocropping", "taungya farming", "land tenuring", "A",
     "Alternating crops in sequence."),
    (T_CROP, "Medium", "The savanna cash crop that feeds groundnut oil mills of the North is",
     "groundnut", "cocoa", "oil palm", "rubber", "A",
     "Groundnut pyramids fed the mills."),
    (T_CROP, "Medium", "Cocoa in Nigeria performs best in the",
     "forest belt of the South-West", "mangrove swamps", "Sahel grassland", "Jos plateau savanna", "A",
     "Cocoa loves the forest zone."),
    (T_CROP, "Easy", "Rice grows best in",
     "flooded lowland fields", "sandy hilltops", "saline flats", "deep forest shade", "A",
     "Swamp rice thrives under water."),
    (T_CROP, "Easy", "Weeds are best described as plants that grow",
     "where they are not wanted", "only in the forest", "with taproots only", "that bear no seeds", "A",
     "Wrong place makes a plant a weed."),
    # ---------------------------------------------------------------- pests and diseases
    (T_PEST, "Hard", "Maize plants showing yellow streaks on leaves and stunted growth are likely attacked by",
     "maize streak virus", "maize weevil", "stalk borer", "army worm", "A",
     "Streaking is the viral signature."),
    (T_PEST, "Medium", "The insect that bores into maize stems and causes deadheart is the",
     "stem borer", "army worm", "grasshopper", "termite", "A",
     "Borers tunnel the stem bases."),
    (T_PEST, "Easy", "Birds eating rice grains at the milk stage are classified as",
     "field pests", "storage pests", "vectors", "parasites", "A",
     "Field pests attack crops outside."),
    (T_PEST, "Medium", "Weevils attacking stored maize grains are best controlled by",
     "fumigation", "spraying herbicide", "hand-picking", "flooding the store", "A",
     "Fumigants reach insects in grain."),
    (T_PEST, "Hard", "Groundnut plants with clumped, yellow leaves are suffering from",
     "groundnut rosette", "leaf rust", "early blight", "root knot", "A",
     "Rosette is aphid-spread and viral."),
    (T_PEST, "Medium", "The cheapest cultural way to cut pest build-up between seasons is",
     "destroying crop residues", "increasing irrigation", "planting very late", "weeding at harvest", "A",
     "Residues shelter pests off-season."),
    (T_PEST, "Easy", "Bird flu outbreak on a poultry farm is caused by",
     "a virus", "a bacterium", "a fungus", "a protozoan", "A",
     "Avian influenza is a viral disease."),
    (T_PEST, "Medium", "A blood-sucking parasite found on the body of a cow is the",
     "tick", "tapeworm", "roundworm", "liver fluke", "A",
     "Ticks attach to skin externally."),
    # ---------------------------------------------------------------- animal production
    (T_ANIM, "Medium", "Birds in a flock gasp for air and twist their necks. Newcastle disease attacks mainly the",
     "respiratory and nervous systems", "reproductive system alone", "skin and the feathers", "digestive tract only", "A",
     "Gasping and twisted necks show it."),
    (T_ANIM, "Easy", "Chickens kept specially for meat are called",
     "broilers", "layers", "cockerels", "pullets", "A",
     "Broilers pack meat quickly."),
    (T_ANIM, "Easy", "A mare has just given birth on the stable floor. The young one is a",
     "foal", "calf", "kid", "lamb", "A",
     "A young horse is called a foal."),
    (T_ANIM, "Medium", "For about how long does a cow carry its calf before calving?",
     "283 days", "60 days", "150 days", "365 days", "A",
     "Cows carry calves about nine months."),
    (T_ANIM, "Easy", "Which farm animal belongs to the West African Dwarf breed?",
     "goat", "pig", "cattle", "rabbit", "A",
     "It is the small local goat breed."),
    (T_ANIM, "Medium", "Ruminants such as cattle digest cellulose mainly in the",
     "rumen", "abomasum", "gizzard", "caecum", "A",
     "The rumen holds fermenting microbes."),
    (T_ANIM, "Medium", "Colostrum fed to a newborn calf is important because it",
     "carries antibodies", "is very sweet", "contains no fat", "keeps for years", "A",
     "First milk passes on immunity."),
    (T_ANIM, "Medium", "A balanced ration is one that",
     "supplies all needed nutrients", "contains only protein", "is made of one feed type", "is cheapest on the market", "A",
     "Balance means every nutrient present."),
    (T_ANIM, "Medium", "Farmers vaccinate chickens against Newcastle disease because it",
     "has no cure once it starts", "spreads only by air", "affects only cocks", "occurs only in dry season", "A",
     "Prevention beats the incurable."),
    (T_ANIM, "Medium", "Eggs that will hatch into chicks must be",
     "fertile", "infertile", "double-yolked", "soft-shelled", "A",
     "Only fertile eggs carry embryos."),
    # ---------------------------------------------------------------- farm tools and machinery
    (T_TOOL, "Easy", "The farm tool used for transplanting seedlings is the",
     "transplanting trowel", "sickle", "axe", "pick axe", "A",
     "The trowel lifts roots with soil."),
    (T_TOOL, "Medium", "When breaking new land, the first tillage pass that cuts and inverts the soil uses a",
     "mouldboard plough", "harrow", "planter", "mower", "A",
     "Ploughs open new land first."),
    (T_TOOL, "Medium", "The second tillage operation that smoothes the just-ploughed field is done with a",
     "harrow", "plough", "thresher", "baler", "A",
     "Harrows refine the ploughed land."),
    (T_TOOL, "Easy", "A tractor-drawn implement that places seeds at set spacing is a",
     "planter", "plough", "baler", "mower", "A",
     "Planters sow at fixed intervals."),
    (T_TOOL, "Medium", "The machine that separates grain from chaff after harvest is the",
     "thresher", "planter", "ridger", "sprayer", "A",
     "Threshing loosens grain from chaff."),
    (T_TOOL, "Easy", "Which source of farm power is most available to the Nigerian smallholder?",
     "human power", "wind power", "electrical power", "steam power", "A",
     "Hands and hoes power most farms."),
    (T_TOOL, "Medium", "Irrigation water usually reaches a farm from a reservoir through",
     "canals", "roads", "ridges", "drills", "A",
     "Canals carry the stored water."),
    (T_TOOL, "Medium", "Land measurement during farm surveying is commonly done with a",
     "measuring tape", "pruning shear", "soil auger", "kitchen sieve", "A",
     "Tapes and chains measure distance."),
    # ---------------------------------------------------------------- farm records and economics
    (T_REC, "Medium", "The farm record that summarises income and expenses over a period is the",
     "income statement", "inventory", "yield record", "labour roster", "A",
     "It totals money in and money out."),
    (T_REC, "Medium", "The record showing the number and types of assets on the farm is the",
     "inventory", "cash book", "farm diary", "sales note", "A",
     "Inventories list what the farm owns."),
    (T_REC, "Medium", "Farm planning simply means",
     "deciding what to produce and how", "recording rainfall data", "borrowing money for farming", "hiring workers for tasks", "A",
     "Plans map production ahead."),
    (T_REC, "Medium", "Tomato prices crash at harvest because supply is abundant. The price fall reflects",
     "excess supply over demand", "high cost of transport", "poor storage methods", "government subsidy", "A",
     "Glut pushes market prices down."),
    (T_REC, "Easy", "Subsistence farming means farming mainly to",
     "feed the farmer's family", "export cash crops", "supply factories", "employ labourers", "A",
     "Subsistence feeds the household."),
    (T_REC, "Easy", "Farmers hear about a new maize variety through extension workers, whose main job is to",
     "pass research findings to farmers", "buy up the whole harvest", "insure crops against failure", "fix prices of farm produce", "A",
     "Agents carry research to farms."),
    (T_REC, "Medium", "Credit a farmer takes for inputs is normally repaid",
     "after harvest with interest", "before planting begins", "in the form of crops only", "never in cash at all", "A",
     "Loans return with interest later."),
    (T_REC, "Hard", "Depreciation of a tractor refers to the",
     "loss of value with use", "rise in market price", "cost of fuel used", "wages of the driver", "A",
     "Machines lose value as they age."),
    # ---------------------------------------------------------------- fisheries, forestry and wildlife
    (T_FISH, "Easy", "Fish farming in managed ponds and tanks is called",
     "aquaculture", "fish capture", "trawling", "gill-netting", "A",
     "Aquaculture rears fish, not hunts."),
    (T_FISH, "Medium", "Harvesting mature table fish from a pond normally starts with",
     "draining the pond", "burning the dyke", "poisoning the fish", "flooding the banks", "A",
     "Lowering water gathers the fish."),
    (T_FISH, "Medium", "A forest managed to yield timber for years is best harvested by",
     "selective cutting", "clear felling", "slash and burn", "ring barking", "A",
     "Selective logging keeps the stand."),
    (T_FISH, "Medium", "Taungya farming combines",
     "trees with food crops", "fish with poultry", "fallow with pasture", "game with cattle", "A",
     "Food crops grow between young trees."),
    (T_FISH, "Easy", "Illegal felling and bush burning lead to",
     "deforestation", "afforestation", "reforestation", "irrigation", "A",
     "Tree cover is lost wholesale."),
    (T_FISH, "Medium", "Grasscutter and snail rearing are grouped under",
     "mini-livestock production", "poultry production", "fisheries work", "apiculture work", "A",
     "Small stock count as mini-livestock."),
    (T_FISH, "Easy", "Bees kept in hives pollinate crops while producing",
     "honey and wax", "milk and ghee", "eggs and feathers", "wool and hides", "A",
     "Hives yield honey and beeswax."),
]

build_batch(
    S,
    "batch_076_waec_agric.json",
    "076",
    "WAEC Agricultural Science Paper 1 round 1 (Round 16e): the WASSCE "
    "syllabus with FRESH angles - scenario stems (streaked maize leaves, "
    "deadheart, tomato glut prices, pond draining), Nigerian specifics "
    "(groundnut savanna, cocoa belt, West African Dwarf goat, tilapia-free "
    "wording) and question-form items - because the near-dup scan checks "
    "every item against the JAMB, WAEC and NECO banks INCLUDING the big "
    "JAMB Agric banks (039-040) and the 90-item NECO Agric bank. Topics: "
    "meaning and scope, soil science, crop production, pests and diseases, "
    "animal production, farm tools and machinery, farm management and "
    "economics, fisheries, forestry and wildlife.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
