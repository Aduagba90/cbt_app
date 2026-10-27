"""Batch 214 - WAEC Physics round 8 (WAEC top-up, R43).

Grows WAEC Physics from 253 toward ~271 with angles not yet in
the bank: the principal focus; power defined; specific heat
capacity and latent heat defined; convection in a pot;
dispersion; reverberation; Young's modulus; the real image; the
magnetic field; frequency defined; rectilinear propagation; work
against gravity; conditions of equilibrium; long sight; the
rheostat; the potential divider; the couple. Scanned against the
whole Physics pool (WAEC, NECO and JAMB stems, 1,323 items).

    python3 scripts/build_neco_batch214.py -> content/batch_214_waec_physics8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Physics"

T_WAV = "Waves and Light"
T_MEC = "Mechanics and Energy"
T_HEA = "Heat"
T_ELE = "Electricity and Magnetism"

PASSAGES = []
PQ = []

Q = [
    (T_WAV, "Easy", "Rays of light arriving parallel to the principal axis of a convex lens are brought together at a point called the",
     "principal focus", "pole of the lens",
     "optical centre", "aperture point", "A",
     "Every parallel ray bows to that one spot."),
    (T_WAV, "Medium", "The number of complete waves passing a fixed point in one second is the wave's",
     "frequency", "period",
     "wavelength", "amplitude", "A",
     "It counts the crests as they go by."),
    (T_WAV, "Hard", "The separation of white light into its band of colours by a glass prism is called",
     "dispersion", "diffraction",
     "deviation only", "decomposition", "A",
     "The prism unpacks the rainbow hidden in white light."),
    (T_WAV, "Medium", "In a large hall, a hand-clap is heard to linger and roll about after the clap itself has ended. This persistence of sound is called",
     "reverberation", "an echo",
     "resonance", "refraction of sound", "A",
     "Many quick reflections crowd upon one another."),
    (T_WAV, "Medium", "An image formed by the actual meeting of light rays, and which can therefore be caught on a screen, is",
     "a real image", "a virtual image",
     "an inverted shadow", "a laterally inverted picture", "A",
     "The rays truly pass through the spot."),
    (T_WAV, "Easy", "Sharp shadows cast by small sources of light show that light travels in straight lines. This property is called the",
     "rectilinear propagation of light", "reflection of light by mirrors",
     "refraction of light at surfaces", "diffraction of light at edges", "A",
     "The straight edge of every shadow testifies to it."),
    (T_MEC, "Medium", "One watt of power is the same as",
     "one joule of work per second", "one newton of force per second",
     "one kilogram per metre", "one coulomb per second", "A",
     "The same work done faster means more power."),
    (T_MEC, "Medium", "The work done in lifting a body of mass m through a height h against gravity is equal to",
     "mgh", "mg/h",
     "mh", "½mh", "A",
     "Weight times height is the whole story."),
    (T_MEC, "Hard", "For a body acted upon by several forces to remain at rest, the resultant force and the resultant moment must both be",
     "zero", "equal and upward",
     "maximum", "clockwise only", "A",
     "No push and no turn may survive."),
    (T_MEC, "Hard", "Within the elastic limit, the constant ratio of tensile stress to tensile strain for a wire is known as its",
     "Young's modulus", "elastic limit",
     "force constant", "yield point", "A",
     "Stiff wires have large values of it."),
    (T_MEC, "Hard", "Two equal and opposite forces whose lines of action do not meet and which therefore turn a body are together called a",
     "couple", "moment arm",
     "parallel pair", "torque rest", "A",
     "A mechanic's two hands on a steering wheel form one."),
    (T_MEC, "Easy", "An old man who holds his newspaper at arm's length to read small print suffers from the eye defect called",
     "long sight", "short sight",
     "night blindness", "colour blindness", "A",
     "The ageing eye focuses close objects behind the retina."),
    (T_HEA, "Hard", "The quantity of heat needed to raise the temperature of one kilogram of a substance by one degree is its",
     "specific heat capacity", "heat capacity only",
     "specific latent heat", "thermal unit", "A",
     "Water's own value is unusually large."),
    (T_HEA, "Hard", "Ice melting at 0 °C keeps absorbing heat from the room while its temperature stays fixed. The heat so absorbed is called",
     "latent heat", "sensible heat",
     "specific heat", "heat of reaction", "A",
     "It loosens the solid without warming it."),
    (T_HEA, "Medium", "Water at the bottom of a pot is heated, becomes lighter and rises while cooler water sinks to take its place. This circulation transfers heat by",
     "convection", "conduction",
     "radiation", "evaporation", "A",
     "The water itself carries the warmth around."),
    (T_ELE, "Easy", "The region around a magnet or a current-carrying wire in which a magnetic force can be detected is called the",
     "magnetic field", "magnetic pole",
     "magnetic axis", "flux container", "A",
     "A compass placed anywhere inside it trembles."),
    (T_ELE, "Easy", "The variable resistor used in a circuit to adjust the current flowing through it is called a",
     "rheostat", "resistor bridge",
     "voltmeter shunt", "fuse wire", "A",
     "Slide its contact and the lamp brightens or dims."),
    (T_ELE, "Medium", "Two resistors joined in series across a supply can be tapped between them to obtain a fraction of the supply voltage. Such an arrangement is a",
     "potential divider", "potential barrier",
     "wheatstone bridge", "transformer coil", "A",
     "The tap slides along to choose the share."),
]

build_batch(
    S,
    "batch_214_waec_physics8.json",
    "214",
    "WAEC Physics round 8 (R43 top-up): principal focus; frequency "
    "defined; dispersion; reverberation; real image; rectilinear "
    "propagation; power as rate of doing work; work against "
    "gravity mgh; conditions of equilibrium; Young's modulus; the "
    "couple; long sight; specific heat capacity; latent heat; "
    "convection in a pot; magnetic field; the rheostat; the "
    "potential divider. Scanned against the whole Physics pool "
    "(WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
