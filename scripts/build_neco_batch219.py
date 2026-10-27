"""Batch 219 - NECO Agricultural Science round 7 (NECO top-up, R44).

Grows NECO Agric from 246 toward ~271 with angles verified absent from
the whole Agricultural Science pool (1,070 items across JAMB, WAEC and
NECO): rumination; capon; branding; shearing; flushing; milking
parlour; coryza; ringworm; bee smoker; swarming; apiary; monk (pond
outlet); coppicing; mounding; dibbling; beniseed; quelea; thrips; top
dressing; succulent feed; mattock; hand fork; rhumbus; sales record;
climate change. Checked and avoided (already banked): incubation
period, germination test, mouthparts, rodenticide, contour ploughing,
cud/ruminant/monogastric, ruminant stomach items, mixed cropping, seed
rate, polyculture, green manure, sheet erosion, cross-breeding,
hatchery, fry, overstocking, shelterbelt, queen bee, mastitis,
rhizobium, agroforestry, chain survey, deworming, earthing up, hook
and line, pasteurisation, salt lick, pellets, pre-emergence, mildew,
damping off, ginger, carrying capacity, ley farming, steer, night
blindness (vit A item exists), creep feed, rickets.

    python3 scripts/build_neco_batch219.py -> content/batch_219_neco_agric7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_ANI = "Animal Production"
T_API = "Apiculture and Small Stock"
T_FISH = "Fisheries and Forestry"
T_CROP = "Crop Production"
T_CROPS = "Crops and Cropping Practices"
T_PEST = "Pests and Diseases"
T_NUT = "Plant Nutrition"
T_FEED = "Livestock Breeds and Feeds"
T_TOOL = "Farm Tools and Machinery"
T_STR = "Farm Structures and Nigerian Agriculture"
T_REC = "Farm Records and Surveying"
T_ENV = "Agriculture and the Environment"

PASSAGES = []
PQ = []

Q = [
    (T_ANI, "Medium", "After grazing, a resting cow returns partly digested grass from its rumen to the mouth, chews it again and swallows it once more. This process is called",
     "rumination", "regurgitation of waste",
     "digestion of protein", "mastication of cud grass", "A",
     "Chewed twice, the coarse grass yields more."),
    (T_ANI, "Medium", "A male chicken that has been castrated so that it grows plumper for the table is a",
     "capon", "cockerel",
     "pullet", "broiler", "A",
     "Castration is done while the bird is young."),
    (T_ANI, "Easy", "A herdsman marks his cattle for identification by pressing a hot iron carrying his sign onto their hides. This practice is",
     "branding", "docking",
     "tagging", "culling", "A",
     "The burn leaves a permanent owner's mark."),
    (T_ANI, "Easy", "The removal of the fleece from a sheep, once a year, is called",
     "shearing", "shedding",
     "skinning", "thinning", "A",
     "The wool is clipped close with shears."),
    (T_ANI, "Hard", "A sheep farmer gives his ewes extra rich feed for about two weeks before putting them to the ram, so that more eggs are shed and twinning improves. This practice is",
     "flushing", "steaming up",
     "creep feeding", "fattening", "A",
     "The extra feed readies the ewes to breed."),
    (T_ANI, "Medium", "The special clean building on a dairy farm where cows are brought in to be milked, by hand or by machine, is the",
     "milking parlour", "calving pen",
     "crush", "brooder house", "A",
     "Cows walk in, are milked and walk out."),
    (T_ANI, "Hard", "A poultry disease caused by bacteria, in which the face and wattles of the fowl swell and a watery discharge runs from the nostrils, is",
     "infectious coryza", "Newcastle disease",
     "fowl pox", "gumboro", "A",
     "The swollen face gives the sick bird away."),
    (T_ANI, "Medium", "A contagious skin disease of farm animals, caused by a fungus and showing as round bare patches on the skin, is",
     "ringworm", "foot rot",
     "mange-free eczema", "mastitis", "A",
     "The circular patches spread by contact."),
    (T_API, "Easy", "Before opening a hive, the beekeeper puffs gentle smoke over the bees with an instrument. This instrument is the",
     "bee smoker", "honey press",
     "queen excluder", "swarm net", "A",
     "The smoke keeps the bees calm and docile."),
    (T_API, "Medium", "When a colony becomes too crowded, the old queen flies off with a band of workers to start a new colony elsewhere. This event is",
     "swarming", "absconding dance",
     "migrating", "hiving off honey", "A",
     "The apiarist catches the swarm to house it."),
    (T_API, "Easy", "The farm or plot on which beehives are kept for the production of honey and beeswax is called an",
     "apiary", "aviary",
     "arboretum", "aquarium", "A",
     "Hives stand in rows where flowers are near."),
    (T_FISH, "Hard", "In a fish pond, the wooden or concrete outlet structure fitted with boards that lets the farmer drain the pond or adjust the water level is the",
     "monk", "spillway",
     "inlet pipe", "screen gate", "A",
     "Boards slid into it hold back the water."),
    (T_FISH, "Medium", "The practice of cutting a tree close to the ground so that several new shoots sprout from the stump is known as",
     "coppicing", "pollarding high",
     "pruning of branches", "thinning of wood", "A",
     "The stump lives on and sends up fresh shoots."),
    (T_CROP, "Easy", "On a flat piece of land, a yam farmer heaps the soil into separate mounds in which he plants his seed yams. This practice is",
     "mounding", "levelling",
     "harrowing", "mulching", "A",
     "Each heap of soft soil carries one yam vine."),
    (T_CROP, "Medium", "A sowing method in which seeds are dropped into small holes made in the soil with a stick or a pointed tool is",
     "dibbling", "broadcasting",
     "drilling in rows", "transplanting", "A",
     "One hole, one seed, at the right spacing."),
    (T_CROPS, "Medium", "Beniseed, an oil-producing seed crop grown mainly in Benue and Taraba states, is another name for",
     "sesame", "sunflower",
     "soya bean", "castor seed", "A",
     "The tiny seeds are rich in oil."),
    (T_PEST, "Medium", "Red-billed birds that descend on rice and sorghum farms in the savanna in huge flocks and strip the grain heads are",
     "quelea", "weaver sparrows",
     "cattle egrets", "pied kingfishers", "A",
     "A flock can clear a field in a single day."),
    (T_PEST, "Hard", "Very tiny, slender insects that rasp the leaves and flowers of crops such as onions and cowpea, leaving silvery patches, are",
     "thrips", "stem borers",
     "grasshoppers", "caterpillars", "A",
     "So small that a leaf looks merely silvered."),
    (T_NUT, "Medium", "The application of fertiliser on the surface of the soil around a standing crop is called",
     "top dressing", "basal application",
     "side dressing only", "foliar spraying", "A",
     "The fertiliser is spread after the crop is up."),
    (T_FEED, "Medium", "Feeds that are fresh, green and full of moisture, such as young elephant grass and freshly cut forage, are described as",
     "succulent feeds", "dry roughages",
     "concentrate meals", "mineral licks", "A",
     "Animals relish their juicy, leafy bulk."),
    (T_TOOL, "Medium", "The heavy hand tool with a pick at one end and an adze-like blade at the other, used for digging hard or stony ground, is the",
     "mattock", "hand trowel",
     "secateurs", "garden shears", "A",
     "It bites where an ordinary hoe would bounce."),
    (T_TOOL, "Easy", "The short-handled, pronged tool used for loosening the soil around plants and lifting seedlings in the nursery bed is the",
     "hand fork", "spade",
     "crowbar", "sickle", "A",
     "Its three or four prongs tease the soil loose."),
    (T_STR, "Hard", "The conical or dome-shaped traditional store, woven from grass or palm fronds and mounted on a platform, in which grain such as maize is kept off the ground, is the",
     "rhumbus", "silo pit",
     "crib shed", "ware house", "A",
     "Air moves freely through its woven walls."),
    (T_REC, "Easy", "The farm record that shows each article the farm has sold, the quantity, the price and the buyer is the",
     "sales record", "labour record",
     "inventory list", "feeding record", "A",
     "Every sale enters it the day it is made."),
    (T_ENV, "Easy", "The long-term shift in the world's temperature and rainfall patterns, blamed largely on gases such as carbon dioxide, is",
     "climate change", "soil erosion",
     "desert reclamation", "global dimming", "A",
     "The weather itself is slowly changing gear."),
]

build_batch(
    S,
    "batch_219_neco_agric7.json",
    "219",
    "NECO Agric round 7 (R44 top-up): rumination; capon; branding; "
    "shearing; flushing; milking parlour; coryza; ringworm; bee "
    "smoker; swarming; apiary; monk (pond outlet); coppicing; "
    "mounding; dibbling; beniseed = sesame; quelea; thrips; top "
    "dressing; succulent feed; mattock; hand fork; rhumbus; sales "
    "record; climate change. Scanned against the whole Agric pool "
    "(JAMB, WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
