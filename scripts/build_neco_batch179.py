"""Batch 179 - NECO Agricultural Science round 6 (NECO top-up, R34).

Grows NECO Agric from 211 toward ~246 with angles not yet in the
bank: pepper and ginger as spices; cocoa and kola as beverage
crops; human labour as the small farm's power; the farmstead's
water; the farm budget; culling unproductive stock; debeaking to
stop pecking; candling eggs; the hen's 21-day incubation; pond
overcrowding; selective forest exploitation; waterlogged soil
starving seeds of air; rills; farmyard manure against fertiliser;
the ring method round citrus; mass selection; rotational grazing;
the monogastric pig; farrowing; the heifer; colostrum; smoke-
drying fish; cover crops; weaning; ventilating livestock houses;
the footbath; the yam minisett; the germination test; agricultural
credit; stylo enriching pasture; tilapia; water need at flowering;
oiling tools after use; the prismatic compass; broilers for meat.
Scanned against NECO rounds 1-5, WAEC Agric (all rounds) and the
JAMB pool.

    python3 scripts/build_neco_batch179.py -> content/batch_179_neco_agric6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_CRO = "Crop Production"
T_ANI = "Animal Production"
T_SCI = "Soil Science"
T_NUT = "Plant Nutrition"
T_PRO = "Crop Propagation"
T_PDC = "Pests and Disease Control"
T_ECO = "Agricultural Economics and Extension"
T_STR = "Farm Structures and Nigerian Agriculture"
T_FIS = "Fisheries and Forestry"
T_GEN = "Genetics and Breeding"
T_TOO = "Farm Tools and Machinery"
T_REC = "Farm Records and Surveying"
T_CCP = "Crops and Cropping Practices"

PASSAGES = []
PQ = []

Q = [
    (T_CRO, "Easy", "Pepper, ginger and onion, grown to season our food, are classified as",
     "spices", "cereals",
     "legumes", "fibres", "A",
     "Their flavour, not their bulk, feeds the pot."),
    (T_CRO, "Easy", "Cocoa, coffee, kola and tea are grouped together as",
     "beverage crops", "spice crops",
     "oil crops", "fibre crops", "A",
     "From their seeds and leaves the nation brews its drinks."),
    (T_ECO, "Medium", "On most small Nigerian farms, the chief source of farm power remains",
     "human labour", "the petrol engine",
     "animal draught only", "electric motors", "A",
     "The hoe and cutlass still ride on human muscle."),
    (T_STR, "Medium", "In choosing a site for the farmstead, the first need to confirm is a reliable",
     "water source", "radio mast",
     "neighbouring school", "gravel pit", "A",
     "Every plan on the farm drinks water first."),
    (T_ECO, "Medium", "The plan of expected income and expenditure a farmer draws up before the production season is his",
     "farm budget", "balance sheet",
     "inventory", "receipt book", "A",
     "He pens his hopes and costs before he plants."),
    (T_GEN, "Medium", "Selling off the dull, unproductive cow from the herd so the better ones stay is called",
     "culling", "weaning",
     "tagging", "quarantine", "A",
     "The weak and idle are cut from the herd."),
    (T_ANI, "Medium", "Layers in deep litter are often debeaked to prevent them from",
     "pecking one another", "flying out at night",
     "laying soft shells", "breaking their waterers", "A",
     "A trimmed beak spares their neighbours' backs."),
    (T_ANI, "Hard", "Holding each egg before a bright lamp to check for cracks and fertility is called",
     "candling", "culling",
     "grading", "sorting", "A",
     "The lamp's glow shows the egg's secrets."),
    (T_ANI, "Easy", "A hen sits on her fertile eggs for about",
     "21 days", "14 days",
     "30 days", "10 days", "A",
     "Three weeks of warmth brings the chick out.", "21"),
    (T_ANI, "Easy", "Birds reared specially for meat rather than eggs are called",
     "broilers", "layers",
     "cocks", "pullets", "A",
     "Broilers bulk up quickly for the pot."),
    (T_ANI, "Easy", "A ewe bringing forth her lambs is said to be",
     "lambing", "farrowing",
     "kidding", "kindling", "A",
     "The shepherd watches the lambing pen."),
    (T_ANI, "Easy", "A sow gives birth to piglets in an event called",
     "farrowing", "kindling",
     "lambing", "kidding", "A",
     "The farrowing crate guards the litter."),
    (T_ANI, "Medium", "The single-stomached pig, unlike the cow, is described as a",
     "monogastric animal", "ruminant",
     "pseudo-ruminant", "cud chewer", "A",
     "One simple stomach handles its feed."),
    (T_ANI, "Medium", "The first yellowish milk a newborn calf sucks from its mother, rich in antibodies, is",
     "colostrum", "whey",
     "butter milk", "replacer", "A",
     "It arms the young one against disease."),
    (T_ANI, "Medium", "Separating young animals from their mothers so they stop suckling is",
     "weaning", "culling",
     "docking", "creep feeding", "A",
     "The milk bar closes on weaning day."),
    (T_STR, "Medium", "Livestock houses are built with openings and fans chiefly to",
     "remove dampness and harmful gases", "let in dust from the harmattan",
     "keep the animals in darkness", "shade the roof beams", "A",
     "Fresh dry air keeps stock breathing well."),
    (T_PDC, "Hard", "A shallow bath of disinfectant placed at the entrance of a poultry house chiefly",
     "checks the spread of disease on boots", "waters the birds passing in",
     "cools the house at noon", "repels snakes and hawks", "A",
     "Every visitor's shoes are washed clean."),
    (T_FIS, "Medium", "When too many fingerlings share one pond, their growth slows because they",
     "compete for food and oxygen", "grow frightened of the water",
     "turn on one another always", "lose their taste for feed", "A",
     "Crowded water starves its tenants."),
    (T_FIS, "Easy", "Besides catfish, the other fish widely reared in Nigerian ponds is the",
     "tilapia", "shark",
     "mackerel", "croaker", "A",
     "Tilapia breeds freely in pond water."),
    (T_FIS, "Easy", "Smoke-drying preserves freshly caught fish chiefly by",
     "driving off its moisture", "adding salt to its flesh",
     "freezing its oils", "bleaching its scales", "A",
     "Without moisture, spoilage germs starve."),
    (T_FIS, "Medium", "In forest management, felling only the mature trees while the young ones keep growing is",
     "selective exploitation", "clear felling",
     "afforestation", "taungya farming", "A",
     "The forest keeps its youth for tomorrow."),
    (T_PRO, "Hard", "Yam is multiplied rapidly by cutting the mother tuber into many small clean setts under the",
     "minisett technique", "layering method",
     "grafting method", "sucker method", "A",
     "One tuber becomes many plantings."),
    (T_PRO, "Medium", "Before sowing, a farmer sprouts a handful of the seeds to check how many will grow. This is a",
     "germination test", "soil test",
     "purity test", "moisture test", "A",
     "The sample speaks for the whole sack."),
    (T_SCI, "Medium", "Seeds planted in waterlogged soil germinate poorly because the excess water drives out the",
     "air the seed needs", "warmth of the sun",
     "soil's fine particles", "seed coats themselves", "A",
     "A drowned seed suffocates in the ground."),
    (T_SCI, "Medium", "On a freshly tilled slope after heavy rain, the tiny channels that first carve the surface are",
     "rills", "gullies",
     "deltas", "levees", "A",
     "Unchecked rills widen into gullies."),
    (T_NUT, "Medium", "Farmyard manure improves the soil in a way chemical fertiliser cannot, because it also improves the soil's",
     "structure and water holding", "acidity alone",
     "colour only", "salt content", "A",
     "Organic matter glues the crumbs together."),
    (T_NUT, "Medium", "Applying fertiliser in a circle round the trunk of a bearing citrus tree is the",
     "ring method", "broadcast method",
     "drilling method", "foliar method", "A",
     "The ring feeds the feeding roots below."),
    (T_CCP, "Medium", "A fast-growing crop sown to shield and protect bare soil between main crops is a",
     "cover crop", "cash crop",
     "catch crop", "fallow crop", "A",
     "Its green blanket keeps the soil in place."),
    (T_CCP, "Hard", "Saving the best maize cobs from the harvest to plant next season is the breeding practice called",
     "mass selection", "hybridisation",
     "crossing", "mutation breeding", "A",
     "The finest ears seed the next field."),
    (T_CCP, "Medium", "Dividing the grazing ground into paddocks and moving the herd so each part rests and regrows is",
     "rotational grazing", "zero grazing",
     "continuous grazing", "strip ploughing", "A",
     "Rested paddocks feed better grass."),
    (T_ANI, "Hard", "A legume like stylo sown into the pasture improves the grazing because it",
     "adds nitrogen to the soil", "poisons the stubborn weeds",
     "drains away surplus water", "shades out every grass", "A",
     "Its nodules feed the sward naturally."),
    (T_CRO, "Medium", "A crop's need for water is greatest around the stage of",
     "flowering and grain filling", "harvest and storage",
     "germination only", "dormancy", "A",
     "Filling the grain is thirsty work."),
    (T_ECO, "Medium", "Money a farmer borrows from a bank or cooperative to buy inputs before the season is agricultural",
     "credit", "subsidy",
     "grant", "premium", "A",
     "The loan plants, the harvest repays."),
    (T_TOO, "Easy", "Cleaning and oiling metal tools after each day's work chiefly prevents",
     "rusting", "blunting",
     "breaking of handles", "theft", "A",
     "A wiped and oiled blade outlives its owner."),
    (T_REC, "Hard", "In farm surveying, the instrument used to measure the bearing of a line from magnetic north is the",
     "prismatic compass", "gunter's chain",
     "cross staff", "ranging pole", "A",
     "Its prism reads the bearing at a glance."),
]

build_batch(
    S,
    "batch_179_neco_agric6.json",
    "179",
    "NECO Agric round 6 (R34 top-up): pepper and ginger as spices; "
    "cocoa and kola as beverages; human labour as small-farm power; "
    "the farmstead's water source; the farm budget; culling; "
    "debeaking; candling; the 21-day incubation; broilers for "
    "meat; the heifer; farrowing; the monogastric pig; colostrum; "
    "weaning; ventilating livestock houses; the footbath; pond "
    "overcrowding; tilapia; smoke-drying fish; selective "
    "exploitation; the yam minisett; the germination test; "
    "waterlogged soil starving seeds; rills; farmyard manure "
    "against fertiliser; the ring method; cover crops; mass "
    "selection; rotational grazing; stylo feeding the pasture; "
    "water need at flowering; agricultural credit; oiling tools; "
    "the prismatic compass. Scanned against NECO rounds 1-5, WAEC "
    "Agric (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
