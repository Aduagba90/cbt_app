"""Batch 132 - WAEC Agricultural Science round 5 (WAEC top-up, Round 25).

Lifts WAEC Agric from 152 toward ~188 with angles not yet in any bank:
weather instruments (rain gauge, hygrometer, sunshine recorder,
anemometer) and weather vs climate; extension methods (mass media,
agent duties, T&V, ADP); survey instruments (ranging poles, prismatic
compass, theodolite); agro-forestry (alley cropping, taungya, minor
forest products); crop improvement (introduction, selection,
hybridization); farm power and implements (mouldboard plough, harrow,
daily greasing); storage (silo, crib, moisture, cold chain);
fisheries (gill nets, cage culture, fish meal); rotational grazing,
carrying capacity, Pearson square (20 kg), brooding heat, gross margin
(N100,000), marketing channels, post-harvest price falls and
diversification. Scanned against WAEC rounds 1-4, NECO Agric (all
rounds) and the JAMB pool.

    python3 scripts/build_neco_batch132.py -> content/batch_132_waec_agric5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_MET = "Agro-meteorology"
T_EXT = "Agricultural Extension"
T_SUR = "Farm Surveying"
T_FOR = "Agro-forestry and Forests"
T_CROPIMP = "Crop Improvement"
T_POWER = "Farm Power and Machinery"
T_STOR = "Post-harvest and Storage"
T_FISH = "Fisheries Detail"
T_AN = "Animal Husbandry Detail"
T_ECO = "Agricultural Economics"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- weather
    (T_MET, "Medium", "Rainfall on a farm is recorded with a",
     "rain gauge", "barometer", "hygrometer", "anemometer", "A",
     "It collects and measures the fall."),
    (T_MET, "Hard", "The instrument used to measure relative humidity is the",
     "hygrometer", "thermometer", "barometer", "wind vane", "A",
     "Dampness of the air shows on it."),
    (T_MET, "Medium", "Hours of bright sunshine are captured by a",
     "sunshine recorder", "rain gauge", "soil thermometer", "barograph", "A",
     "Card lines trace the burning sun."),
    (T_MET, "Hard", "While a wind vane shows direction, wind speed is read from an",
     "anemometer", "altimeter", "hygrometer", "evaporimeter", "A",
     "Spinning cups count the pace."),
    (T_MET, "Medium", "Weather differs from climate mainly in the",
     "period of time covered", "kind of clouds seen", "rainfall amount", "instruments used", "A",
     "Weather is climate's brief day."),

    # ------------------------------------------------------------- extension
    (T_EXT, "Medium", "Reaching farmers through radio and television is an example of the",
     "mass method", "individual method", "group method", "field method", "A",
     "One message meets many ears."),
    (T_EXT, "Medium", "The extension worker who links research institutes with rural farmers exists chiefly to",
     "pass new methods to them", "sell inputs to them", "lend money to them", "take over their lands", "A",
     "Teaching travels with him."),
    (T_EXT, "Hard", "In the T&V extension system, agents are expected to",
     "visit farmers on fixed days", "wait inside the office", "write reports only", "sell fertiliser bags", "A",
     "A timetable rules the rounds."),
    (T_EXT, "Medium", "In Nigerian agriculture, ADP stands for",
     "Agricultural Development Project", "Agricultural Data Programme", "Area Development Plan", "Animal Disease Project", "A",
     "Projects carried farming to states."),

    # ------------------------------------------------------------- surveying
    (T_SUR, "Medium", "Ranging poles on a survey farm are used to",
     "mark out straight lines", "measure land angles", "test the soil pH", "mix crop chemicals", "A",
     "They keep the line of sight true."),
    (T_SUR, "Hard", "The survey instrument used to take bearings is the",
     "prismatic compass", "abney level", "ranging pole", "measuring tape", "A",
     "Its needle reads the bearing."),
    (T_SUR, "Medium", "A theodolite can measure both horizontal and vertical",
     "angles", "distances", "areas", "slopes", "A",
     "Angles in two planes at once."),

    # ------------------------------------------------------------- agro-forestry
    (T_FOR, "Medium", "In alley cropping, food crops are planted",
     "between rows of trees", "under closed canopy", "on harvested stumps", "in pure stands", "A",
     "Hedges and crops share the rows."),
    (T_FOR, "Hard", "The taungya system involves growing",
     "crops with young trees", "fish grown with rice", "grass fed to cattle", "maize mixed with yam", "A",
     "Farmers tend the young forest."),
    (T_FOR, "Medium", "Which of these is a minor forest product?",
     "resin", "timber", "pulpwood", "poles", "A",
     "Small gums and resins count too."),

    # ------------------------------------------------------------- crop improvement
    (T_CROPIMP, "Medium", "Bringing a proven foreign variety into the country for trials is",
     "introduction", "hybridization", "mutation", "selection", "A",
     "It arrives, then proves itself."),
    (T_CROPIMP, "Medium", "A farmer who keeps seed only from his best maize cobs is practising",
     "selection", "introduction", "breeding isolation", "seed dressing", "A",
     "The best parents seed the next crop."),
    (T_CROPIMP, "Hard", "The crossing of two different parent plants to combine desirable characters is",
     "hybridization", "grafting", "layering", "mulching", "A",
     "Two good halves make one better."),

    # ------------------------------------------------------------- power and machinery
    (T_POWER, "Medium", "The oldest and most flexible source of farm power on Nigerian farms is",
     "human power", "electric power", "wind power", "steam power", "A",
     "The hoe and cutlass answer it."),
    (T_POWER, "Medium", "The implement chiefly used to break and invert the soil is the",
     "mouldboard plough", "harrow", "ridger", "cultivator", "A",
     "It slices and turns the slice."),
    (T_POWER, "Hard", "Daily greasing of tractor moving parts chiefly",
     "cuts friction and wear", "cools the radiator", "cleans the air filter", "charges the battery", "A",
     "Grease keeps metal from metal."),
    (T_POWER, "Medium", "Clods are broken and the seedbed levelled with a",
     "harrow", "planter", "roller", "mower", "A",
     "Its teeth comb the soil fine."),

    # ------------------------------------------------------------- storage
    (T_STOR, "Medium", "Bulk storage of dry grain on a large farm uses a",
     "silo", "crib", "cold store", "barn", "A",
     "Tall steel holds the tonnes."),
    (T_STOR, "Medium", "The ventilated structure for storing unshelled maize is the",
     "crib", "silo", "pit store", "tank", "A",
     "Air moves through the cobs."),
    (T_STOR, "Hard", "Grain going bad in store is most often caused by",
     "high moisture levels", "too much sunlight", "cold dry nights", "clean new sacks", "A",
     "Damp grain breathes itself rotten."),
    (T_STOR, "Medium", "Fresh tomatoes for the city market are best preserved by",
     "refrigeration", "sun drying", "smoking", "salting", "A",
     "The cold chain holds them firm."),

    # ------------------------------------------------------------- fisheries
    (T_FISH, "Medium", "Fish are caught in a gill net when they",
     "entangle their gills", "swallow the bait", "enter a trap door", "get stunned by it", "A",
     "Mesh holds them by the head."),
    (T_FISH, "Hard", "Rearing fish in enclosures fixed within a lake or river is",
     "cage culture", "raceway culture", "pond culture", "extensive culture", "A",
     "Net boxes float on open water."),
    (T_FISH, "Medium", "The chief reason fish meal enters fish feed is its",
     "protein content", "fat content", "fibre content", "ash content", "A",
     "Fish build flesh from protein."),

    # ------------------------------------------------------------- animal husbandry
    (T_AN, "Medium", "Grazing animals section by section, resting each in turn, is",
     "rotational grazing", "zero grazing", "continuous grazing", "nomadic grazing", "A",
     "Each paddock takes a holiday."),
    (T_AN, "Hard", "The stocking rate a pasture can support year after year is its",
     "carrying capacity", "grazing pressure", "feed conversion", "the herd's size", "A",
     "The land itself sets the limit."),
    (T_AN, "Hard", "A 20% protein feed is mixed with a 40% protein feed to obtain a 30% blend. For 20 kg of the first feed, the 40% feed needed is",
     "20 kg", "10 kg", "40 kg", "60 kg", "A",
     "Equal parts balance the square.", "20"),

    # ------------------------------------------------------------- economics
    (T_ECO, "Medium", "A maize farmer's revenue is N250,000 and his variable costs are N150,000. His gross margin is",
     "N100,000", "N400,000", "N150,000", "N50,000", "A",
     "Revenue less variable costs.", "100000"),
    (T_ECO, "Hard", "Farm produce moves from the farm gate to final consumers through the",
     "marketing channel", "processing plant", "customs route", "the feeder road", "A",
     "Middlemen form the channel."),
    (T_ECO, "Hard", "Prices of farm produce usually fall just after harvest mainly because",
     "supply is at its peak", "demand has ended fully", "quality is at its worst", "farmers are all idle", "A",
     "Barns brim, so prices bow."),
    (T_ECO, "Medium", "Diversifying a farm's enterprises chiefly helps to",
     "spread the farmer's risks", "spoil the soil texture", "stop all risks at once", "ban the use of inputs", "A",
     "One failure cannot ruin all."),
]

build_batch(
    S,
    "batch_132_waec_agric5.json",
    "132",
    "WAEC Agricultural Science round 5 (Round 25 top-up): rain gauge, "
    "hygrometer, sunshine recorder, anemometer, weather vs climate; "
    "mass extension method, agent duties, T&V fixed-day visits, ADP; "
    "ranging poles, prismatic compass, theodolite; alley cropping, "
    "taungya, resin as minor forest product; introduction, selection, "
    "hybridization; human power, mouldboard plough, daily greasing, "
    "harrow; silo vs crib, moisture spoilage, refrigeration; gill net "
    "action, cage culture, fish meal protein; rotational grazing, "
    "carrying capacity, Pearson square 20 kg, gross margin N100,000, "
    "marketing channel, post-harvest price fall, diversification. "
    "Scanned against WAEC rounds 1-4, NECO Agric (all rounds) and the "
    "JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
