"""Batch 236 - NECO Physics round 4 (NECO top-up, R48).

Grows NECO Physics from 257 toward ~282 with angles verified absent
from the whole Physics pool (1,341 items across JAMB, WAEC and
NECO). Fresh angles: principle of moments; types of equilibrium;
law of flotation; regular vs diffuse reflection; high-voltage
transmission; impurities lower the melting point; equilibrant;
charging by friction; charging by induction; primary vs secondary
cells; solar cell; electron volt; E = mc²; magnetic field around a
straight current-carrying wire; sonar; luminous vs non-luminous
bodies; the mirror formula; near point and far point; primary
colours of light; internal energy; ice cooling drinks; thick glass
tumbler cracking; alcohol vs mercury in thermometers; why the sky is
blue; calorimeter. Avoided as banked or cross-subject twins:
equations-of-motion calcs, efficiency, horsepower, evaporation
cooling, Archimedes apparent-weight calc, apparent-loss phrasing
(one calc banked), equilibrium-force items (58 family), wave
equation v=fλ, Doppler ×2, regular reflection family exceptions,
pinhole camera, periscope, filters, thermos, land/sea breeze,
pressure cooker, mountain barometer, rheostat, angle of dip,
three-pin earth, thermistor, LDR, Rutherford, gamma nucleon item,
penetrating-power, medical tracer, background radiation, Geiger,
cathode rays, oscilloscope, photoelectric, semiconductors, diodes,
transistors, logic gates, transformer, generator, motor, induction
family, capacitor, kWh, fuses, magnetic induction, echo, sonometer,
resonance tube, beats, pitch/loudness, sound speed, plane mirror,
curved mirrors family, focal length family, magnification,
refraction, critical angle, mirage, lenses, eye defects,
dispersion, rainbow, umbra, X-rays, isotopes, fission/fusion,
inertia, mass vs weight, satellites, gravitation, resultant,
couples, torque, circular motion, angular velocity, simple
pendulum, vernier, micrometer, zero error, accuracy, Kelvin family,
capillarity, surface tension, viscosity, bimetallic, thermostat,
expansion gaps, radiation surfaces, dew/frost, heating of tyres,
thermal conductivity, latent-heat calcs, specific heat calcs,
clinical/thermocouple thermometers, resistor circuits, Ohm, EMF,
internal resistance, ammeter/voltmeter/galvanometer, electroscope,
Coulomb, lightning conductor, LED, shock items, Newton's laws,
momentum, projectiles, machines family, friction, density, relative
density, pressure, Pascal/hydraulics, manometer, barometer,
atmospheric pressure, Hooke, Young modulus, work/energy/power,
conduction/convection/radiation, vacuum flask.

    python3 scripts/build_neco_batch236.py -> content/batch_236_neco_phys4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Physics"

T_FORCE = "Force, Momentum and Newton's Laws"
T_PRESS = "Pressure and Upthrust"
T_LIGHT = "Light and Optics"
T_LENS = "Light and Lenses"
T_ELEC = "Electricity"
T_ELEC2 = "Electricity Further"
T_MAG = "Magnetism and Electromagnetism"
T_MOD = "Modern Physics"
T_MODE = "Modern Physics and Electronics"
T_WAVE = "Waves and Sound"
T_WSL = "Waves, Sound and Light"
T_HEAT = "Heat Energy"
T_MEAS = "Measurement and Instruments"
T_MOTION = "Motion, Force and Momentum"

PASSAGES = []
PQ = []

Q = [
    (T_FORCE, "Medium", "For a body balanced on a pivot under the action of several forces, the sum of the clockwise moments about the pivot equals the sum of the anticlockwise moments. This is the",
     "principle of moments", "principle of momentum",
     "law of inertia", "law of mass action", "A",
     "The see-saw balances when the turns of both sides match."),
    (T_MOTION, "Medium", "A traffic cone standing on its broad base returns to its upright position after a small tilt. A cone balanced on its point falls at the slightest touch. These are examples of",
     "stable and unstable equilibrium", "neutral and stable equilibrium",
     "unstable and neutral equilibrium", "forced and damped equilibrium", "A",
     "Broad base, low centre — the cone keeps its peace."),
    (T_PRESS, "Medium", "A ship floating on the sea displaces a weight of water exactly equal to its own weight. This statement is the",
     "law of flotation", "law of pressures",
     "Archimedes' screw principle", "law of displacement volume", "A",
     "The sea yields back exactly what the ship weighs."),
    (T_LIGHT, "Easy", "A rough wall and a smooth mirror are both struck by sunlight. The wall scatters the light in all directions while the mirror sends it back in one direction. The wall's behaviour is called",
     "diffuse reflection", "regular refraction",
     "total internal reflection", "selective absorption", "A",
     "Every bump on the wall throws light its own way."),
    (T_ELEC2, "Hard", "Electric power is transmitted from the generating station at very high voltage mainly in order to",
     "reduce the energy lost as heat in the cables", "make the cables thicker",
     "increase the current through the cables", "charge consumers more per unit", "A",
     "A small current whispers through the wires, wasting little."),
    (T_HEAT, "Medium", "When salt is sprinkled on ice on a road, the ice melts even though the temperature is below 0 °C. This is because dissolved impurities",
     "lower the melting point of the ice", "raise the melting point of the ice",
     "warm the ice directly", "make the ice freeze harder", "A",
     "Salt bribes the ice to give up its shape early."),
    (T_FORCE, "Hard", "The single force that would exactly balance a system of forces acting on a body and keep it at rest is called the",
     "equilibrant", "resultant",
     "equator of forces", "effort of the system", "A",
     "It stands opposite the resultant and holds the peace."),
    (T_ELEC, "Easy", "A plastic comb rubbed vigorously on dry hair gains the ability to attract small pieces of paper. The comb has become charged by",
     "friction", "induction",
     "conduction through air", "chemical action", "A",
     "Rubbing transfers electrons from hair to comb."),
    (T_ELEC, "Medium", "A charged balloon is brought near an uncharged metal sphere. Charges in the sphere separate, with unlike charges drawn to the near side. The sphere has been charged by",
     "induction", "friction only",
     "contact with the balloon", "heating", "A",
     "The balloon never touches, yet the sphere answers."),
    (T_ELEC, "Medium", "A cell that cannot be recharged once its chemicals are used up, such as the common torch cell, is called a",
     "primary cell", "secondary cell",
     "solar cell", "fuel cell", "A",
     "One journey only — then it is spent."),
    (T_MODE, "Easy", "The device that converts the energy of sunlight directly into electrical energy, without any moving parts, is the",
     "solar cell", "dynamo",
     "dry cell", "transformer", "A",
     "Light lands on the panel and current flows."),
    (T_MOD, "Hard", "The energy gained by an electron when it is accelerated through a potential difference of one volt is called one",
     "electron volt", "electron charge",
     "watt-second", "volt-ampere", "A",
     "A tiny energy unit fitted to tiny particles."),
    (T_MOD, "Hard", "Einstein's equation E = mc² shows that",
     "mass can be converted into energy", "energy has no units",
     "mass always remains constant", "light travels slowly", "A",
     "A pinch of matter holds a mountain of energy."),
    (T_MAG, "Medium", "The magnetic field produced around a straight wire carrying an electric current consists of",
     "concentric circles centred on the wire", "straight lines along the wire",
     "radial lines away from the wire", "no pattern at all", "A",
     "Iron filings ring the wire like ringles round a stone in water."),
    (T_WAVE, "Medium", "A ship sends a pulse of sound to the sea bed and times the echo to measure the depth of the water. This technique is the principle of",
     "sonar", "radar",
     "laser ranging", "echo sounding of light", "A",
     "The sea answers the ship's question from below."),
    (T_LIGHT, "Easy", "The sun and an electric lamp are bodies that produce their own light, while the moon and a page of paper only reflect light from elsewhere. The sun and the lamp are described as",
     "luminous bodies", "non-luminous bodies",
     "transparent bodies", "luminiferous voids", "A",
     "Firemakers and lamplighters shine on their own."),
    (T_LIGHT, "Hard", "For an image formed by a curved mirror, the object distance u, the image distance v and the focal length f are related by the equation",
     "1/f = 1/u + 1/v", "f = u + v",
     "1/f = u + v", "f = uv − u − v", "A",
     "The mirror's three distances share one fraction."),
    (T_LENS, "Medium", "The nearest point at which the eye can focus an object clearly without strain, about 25 cm for a normal young adult, is called the",
     "near point", "far point",
     "focal point", "blind point", "A",
     "Beyond this point the eye must strain to see."),
    (T_WSL, "Medium", "Red, green and blue light, when mixed together in equal proportions, produce white light. They are therefore called the",
     "primary colours of light", "secondary colours of paint",
     "complementary colours", "pigment primaries", "A",
     "Three beams of the screen build every colour on it."),
    (T_HEAT, "Medium", "The total energy contained in the molecules of a substance, both by their motion and by their positions, is called the",
     "internal energy", "external energy",
     "latent energy", "chemical energy", "A",
     "The hidden treasury of every molecule's jiggle."),
    (T_HEAT, "Medium", "Ice cubes cool a bottle of drink more effectively than the same mass of cold water at 0 °C because the melting ice",
     "absorbs latent heat from the drink", "releases latent heat to the drink",
     "is heavier than the drink", "conducts electricity better", "A",
     "The quiet melting steals warmth from the bottle."),
    (T_HEAT, "Easy", "A thick glass tumbler often cracks when boiling water is suddenly poured into it because",
     "the inner surface expands before the outer", "glass shrinks in hot water",
     "water enters the pores of the glass", "the outer surface expands first", "A",
     "One face races ahead; the other lags and tears."),
    (T_MEAS, "Medium", "Alcohol is preferred to mercury in thermometers used in very cold regions mainly because alcohol",
     "freezes at a much lower temperature", "expands less than mercury",
     "is a better conductor of heat", "is silvery and easy to read", "A",
     "Mercury sleeps at −39 °C; alcohol works on to −112 °C."),
    (T_WSL, "Medium", "The sky appears blue in daytime mainly because air molecules",
     "scatter blue light more than the other colours", "emit blue light of their very own",
     "absorb every other colour completely", "reflect the blue of the seas upward", "A",
     "The small molecules favour the short blue waves."),
    (T_HEAT, "Easy", "The polished metal vessel, with its stirrer and lid, used in the laboratory for finding heat quantities by mixing hot and cold substances is the",
     "calorimeter", "barometer",
     "caliper", "calculus", "A",
     "Its shining walls keep the heat from escaping."),
]

build_batch(
    S,
    "batch_236_neco_phys4.json",
    "236",
    "NECO Physics round 4 (R48 top-up): principle of moments; stable "
    "and unstable equilibrium; law of flotation; diffuse reflection; "
    "high-voltage transmission; impurities lower melting point; "
    "equilibrant; charging by friction; charging by induction; "
    "primary cell; solar cell; electron volt; E = mc²; field around a "
    "straight wire; sonar; luminous bodies; mirror formula; near "
    "point; primary colours; internal energy; ice and latent heat; "
    "thick glass tumbler; alcohol thermometer; why the sky is blue; "
    "calorimeter. Scanned against the whole Physics pool (JAMB, WAEC "
    "and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
