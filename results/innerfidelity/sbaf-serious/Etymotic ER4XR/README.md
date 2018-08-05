# Etymotic ER4XR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 4.0; 22 3.8; 23 3.8; 25 3.7; 26 3.6; 28 3.6; 30 3.5; 32 3.5; 35 3.5; 37 3.5; 40 3.5; 42 3.5; 45 3.5; 49 3.5; 52 3.4; 56 3.4; 59 3.4; 64 3.4; 68 3.3; 73 3.3; 78 3.2; 83 3.0; 89 2.6; 95 2.3; 102 1.7; 109 1.4; 117 0.9; 125 0.4; 134 -0.0; 143 -0.3; 153 -0.4; 164 -0.5; 175 -0.5; 188 -0.4; 201 -0.5; 215 -0.3; 230 -0.2; 246 -0.1; 263 -0.0; 282 0.1; 301 0.3; 323 0.4; 345 0.5; 369 0.6; 395 0.7; 423 0.9; 452 1.0; 484 1.1; 518 1.2; 554 1.3; 593 1.5; 635 1.4; 679 1.3; 726 1.3; 777 1.3; 832 1.0; 890 0.7; 952 0.3; 1019 -0.2; 1090 -0.6; 1167 -1.1; 1248 -1.6; 1336 -2.1; 1429 -2.8; 1529 -3.4; 1636 -3.8; 1751 -4.1; 1873 -4.1; 2004 -4.1; 2145 -4.1; 2295 -3.7; 2455 -2.8; 2627 -1.8; 2811 -0.6; 3008 1.0; 3219 2.5; 3444 3.7; 3685 3.8; 3943 3.4; 4219 2.1; 4514 1.2; 4830 1.6; 5168 2.9; 5530 4.3; 5917 5.5; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.3dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.68 | 3.8 dB  |
| Peaking | 71 Hz   | 1.79 | 2.5 dB  |
| Peaking | 1968 Hz | 1.75 | -5.0 dB |
| Peaking | 3559 Hz | 3.32 | 4.7 dB  |
| Peaking | 6064 Hz | 3.95 | 6.1 dB  |
| Peaking | 101 Hz  | 2.51 | 0.9 dB  |
| Peaking | 163 Hz  | 1.19 | -1.2 dB |
| Peaking | 669 Hz  | 0.91 | 1.7 dB  |
| Peaking | 1362 Hz | 2.46 | -1.3 dB |
| Peaking | 8103 Hz | 5.14 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4XR/Etymotic%20ER4XR.png)