# Etymotic ER4XR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 3.9; 22 3.8; 23 3.7; 25 3.6; 26 3.5; 28 3.4; 30 3.4; 32 3.3; 35 3.2; 37 3.1; 40 3.1; 42 3.0; 45 2.9; 49 2.7; 52 2.6; 56 2.4; 59 2.3; 64 2.1; 68 1.9; 73 1.7; 78 1.5; 83 1.3; 89 1.1; 95 0.9; 102 0.7; 109 0.7; 117 0.5; 125 0.4; 134 0.2; 143 0.1; 153 0.1; 164 0.0; 175 0.0; 188 0.1; 201 -0.0; 215 0.1; 230 0.1; 246 0.1; 263 0.2; 282 0.3; 301 0.4; 323 0.5; 345 0.6; 369 0.7; 395 0.8; 423 1.0; 452 1.1; 484 1.1; 518 1.2; 554 1.3; 593 1.5; 635 1.4; 679 1.3; 726 1.3; 777 1.3; 832 1.0; 890 0.7; 952 0.3; 1019 -0.2; 1090 -0.6; 1167 -1.1; 1248 -1.6; 1336 -2.1; 1429 -2.8; 1529 -3.4; 1636 -3.8; 1751 -4.1; 1873 -4.1; 2004 -4.1; 2145 -4.1; 2295 -3.7; 2455 -2.8; 2627 -1.8; 2811 -0.6; 3008 1.0; 3219 2.5; 3444 3.7; 3685 3.8; 3943 3.4; 4219 2.1; 4514 1.2; 4830 1.6; 5168 2.9; 5530 4.3; 5917 5.5; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8698692529672964dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.63 | 3.5 dB  |
| Peaking | 49 Hz   | 0.9  | 1.6 dB  |
| Peaking | 1967 Hz | 1.77 | -5.0 dB |
| Peaking | 3560 Hz | 3.33 | 4.7 dB  |
| Peaking | 6064 Hz | 3.95 | 6.1 dB  |
| Peaking | 666 Hz  | 1.13 | 1.7 dB  |
| Peaking | 1219 Hz | 3.42 | -0.7 dB |
| Peaking | 1493 Hz | 5.32 | -1.0 dB |
| Peaking | 6745 Hz | 7.71 | 1.5 dB  |
| Peaking | 7598 Hz | 2.76 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4XR/Etymotic%20ER4XR.png)