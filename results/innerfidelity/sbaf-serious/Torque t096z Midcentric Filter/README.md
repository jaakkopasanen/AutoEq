# Torque t096z Midcentric Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.9dB
GraphicEQ: 10 -84; 20 6.3; 22 5.9; 23 5.7; 25 5.4; 26 5.3; 28 5.0; 30 4.8; 32 4.6; 35 4.4; 37 4.3; 40 4.1; 42 4.1; 45 3.9; 49 3.8; 52 3.7; 56 3.6; 59 3.5; 64 3.4; 68 3.3; 73 3.0; 78 2.7; 83 2.5; 89 2.1; 95 1.5; 102 0.9; 109 0.5; 117 -0.1; 125 -0.8; 134 -1.4; 143 -1.7; 153 -1.9; 164 -2.1; 175 -2.2; 188 -2.3; 201 -2.4; 215 -2.3; 230 -2.1; 246 -2.2; 263 -2.1; 282 -1.9; 301 -1.8; 323 -1.7; 345 -1.5; 369 -1.4; 395 -1.2; 423 -0.9; 452 -0.6; 484 -0.5; 518 -0.4; 554 -0.1; 593 0.3; 635 0.5; 679 0.5; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.7; 1529 -1.9; 1636 -2.3; 1751 -2.2; 1873 -1.8; 2004 -1.6; 2145 -1.3; 2295 -0.7; 2455 0.4; 2627 0.8; 2811 1.2; 3008 2.0; 3219 2.4; 3444 1.8; 3685 0.2; 3943 -1.7; 4219 -3.9; 4514 -4.2; 4830 -2.7; 5168 0.2; 5530 2.7; 5917 4.5; 6331 5.2; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.6; 10167 -1.8; 10879 -1.9; 11640 -0.8; 12455 -0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.9dB` and instead set Global volume in the UI for both channels to **-69**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Midcentric Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.44 | 6.2 dB  |
| Peaking | 75 Hz    | 0.9  | 2.7 dB  |
| Peaking | 175 Hz   | 0.79 | -3.4 dB |
| Peaking | 4481 Hz  | 6.22 | -5.6 dB |
| Peaking | 6188 Hz  | 4.39 | 5.9 dB  |
| Peaking | 771 Hz   | 2.11 | 1.3 dB  |
| Peaking | 1725 Hz  | 1.73 | -2.5 dB |
| Peaking | 3207 Hz  | 2.51 | 3.1 dB  |
| Peaking | 3992 Hz  | 6.12 | -2.0 dB |
| Peaking | 10518 Hz | 4.45 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Midcentric%20Filter/Torque%20t096z%20Midcentric%20Filter.png)