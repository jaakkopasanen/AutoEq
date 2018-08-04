# AKG N60NC Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 10 -84; 20 -2.9; 22 -2.9; 23 -2.8; 25 -2.8; 26 -2.7; 28 -2.7; 30 -2.6; 32 -2.6; 35 -2.5; 37 -2.4; 40 -2.3; 42 -2.3; 45 -2.4; 49 -2.4; 52 -2.4; 56 -2.3; 59 -2.3; 64 -2.2; 68 -2.1; 73 -2.1; 78 -2.2; 83 -2.5; 89 -3.0; 95 -3.4; 102 -3.6; 109 -3.6; 117 -3.8; 125 -4.2; 134 -4.5; 143 -4.6; 153 -4.5; 164 -4.3; 175 -4.2; 188 -3.9; 201 -3.5; 215 -2.8; 230 -2.4; 246 -2.2; 263 -2.9; 282 -2.2; 301 -2.6; 323 -1.9; 345 -1.6; 369 -1.3; 395 -1.2; 423 -1.0; 452 -1.1; 484 -1.9; 518 -1.5; 554 -0.5; 593 -0.3; 635 -0.2; 679 -0.1; 726 -0.0; 777 0.2; 832 0.1; 890 0.0; 952 0.0; 1019 -0.0; 1090 -0.0; 1167 -0.0; 1248 -0.0; 1336 -0.4; 1429 -0.7; 1529 -1.0; 1636 -1.4; 1751 -1.8; 1873 -1.8; 2004 -1.8; 2145 -2.0; 2295 -2.1; 2455 -1.8; 2627 -1.8; 2811 -1.9; 3008 -1.8; 3219 -1.7; 3444 -1.6; 3685 -1.6; 3943 -1.1; 4219 -0.5; 4514 1.0; 4830 3.1; 5168 1.5; 5530 2.3; 5917 4.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.2dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N60NC Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.97 | -2.6 dB |
| Peaking | 45 Hz   | 1.72 | -0.9 dB |
| Peaking | 146 Hz  | 0.75 | -4.3 dB |
| Peaking | 2557 Hz | 1.26 | -2.3 dB |
| Peaking | 6156 Hz | 3.81 | 6.0 dB  |
| Peaking | 493 Hz  | 8.79 | -1.4 dB |
| Peaking | 841 Hz  | 1.69 | 0.6 dB  |
| Peaking | 4613 Hz | 2.35 | -1.2 dB |
| Peaking | 4782 Hz | 8.42 | 3.8 dB  |
| Peaking | 8011 Hz | 6.43 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20N60NC%20Wired%20Passive/AKG%20N60NC%20Wired%20Passive.png)