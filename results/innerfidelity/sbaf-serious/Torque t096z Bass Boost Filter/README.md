# Torque t096z Bass Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -11.4; 22 -11.4; 23 -11.4; 25 -11.3; 26 -11.3; 28 -11.2; 30 -11.1; 32 -11.0; 35 -10.8; 37 -10.7; 40 -10.5; 42 -10.4; 45 -10.1; 49 -9.8; 52 -9.6; 56 -9.4; 59 -9.2; 64 -8.9; 68 -8.6; 73 -8.4; 78 -8.3; 83 -8.2; 89 -8.2; 95 -8.3; 102 -8.4; 109 -8.5; 117 -8.6; 125 -8.7; 134 -8.8; 143 -8.8; 153 -8.6; 164 -8.3; 175 -7.9; 188 -7.5; 201 -7.1; 215 -6.6; 230 -6.2; 246 -5.7; 263 -5.3; 282 -4.7; 301 -4.3; 323 -3.8; 345 -3.3; 369 -2.8; 395 -2.4; 423 -1.8; 452 -1.4; 484 -1.1; 518 -0.8; 554 -0.3; 593 0.2; 635 0.5; 679 0.6; 726 0.7; 777 1.0; 832 0.9; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.5; 1336 -2.3; 1429 -3.2; 1529 -4.2; 1636 -5.3; 1751 -6.3; 1873 -7.2; 2004 -7.5; 2145 -7.2; 2295 -5.7; 2455 -3.1; 2627 -0.8; 2811 1.2; 3008 3.5; 3219 4.5; 3444 5.1; 3685 3.8; 3943 1.6; 4219 -1.4; 4514 -1.2; 4830 2.1; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 0.84 | -11.1 dB |
| Peaking | 32 Hz   | 0.39 | -9.1 dB  |
| Peaking | 166 Hz  | 0.73 | -6.3 dB  |
| Peaking | 1971 Hz | 1.38 | -17.1 dB |
| Peaking | 2406 Hz | 0.5  | 9.4 dB   |
| Peaking | 2357 Hz | 5.89 | -1.8 dB  |
| Peaking | 3359 Hz | 3.43 | 3.2 dB   |
| Peaking | 4353 Hz | 4.21 | -8.3 dB  |
| Peaking | 5787 Hz | 1.69 | 7.3 dB   |
| Peaking | 7665 Hz | 1.28 | -4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Bass%20Boost%20Filter/Torque%20t096z%20Bass%20Boost%20Filter.png)