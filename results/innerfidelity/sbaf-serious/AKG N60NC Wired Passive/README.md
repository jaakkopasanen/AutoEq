# AKG N60NC Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -2.9; 22 -2.9; 23 -2.8; 25 -2.8; 26 -2.8; 28 -2.7; 30 -2.7; 32 -2.6; 35 -2.5; 37 -2.5; 40 -2.5; 42 -2.5; 45 -2.6; 49 -2.7; 52 -2.7; 56 -2.7; 59 -2.7; 64 -2.7; 68 -2.7; 73 -2.8; 78 -2.9; 83 -3.3; 89 -3.8; 95 -4.1; 102 -4.1; 109 -4.0; 117 -4.0; 125 -4.2; 134 -4.3; 143 -4.4; 153 -4.3; 164 -4.0; 175 -3.9; 188 -3.7; 201 -3.3; 215 -2.6; 230 -2.3; 246 -2.1; 263 -2.8; 282 -2.1; 301 -2.6; 323 -1.9; 345 -1.5; 369 -1.3; 395 -1.2; 423 -1.0; 452 -1.1; 484 -1.9; 518 -1.5; 554 -0.5; 593 -0.3; 635 -0.2; 679 -0.1; 726 -0.0; 777 0.2; 832 0.1; 890 0.0; 952 0.0; 1019 -0.0; 1090 -0.0; 1167 -0.0; 1248 -0.0; 1336 -0.4; 1429 -0.7; 1529 -1.0; 1636 -1.4; 1751 -1.8; 1873 -1.8; 2004 -1.8; 2145 -2.0; 2295 -2.1; 2455 -1.8; 2627 -1.8; 2811 -1.9; 3008 -1.8; 3219 -1.7; 3444 -1.6; 3685 -1.6; 3943 -1.1; 4219 -0.5; 4514 1.0; 4830 3.1; 5168 1.5; 5530 2.3; 5917 4.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.755563573706075dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N60NC Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.81 | -2.6 dB |
| Peaking | 26 Hz   | 0.31 | -1.8 dB |
| Peaking | 136 Hz  | 0.96 | -3.2 dB |
| Peaking | 808 Hz  | 0.06 | -0.9 dB |
| Peaking | 6175 Hz | 3.68 | 6.5 dB  |
| Peaking | 301 Hz  | 6    | -0.7 dB |
| Peaking | 1035 Hz | 0.98 | 1.7 dB  |
| Peaking | 2262 Hz | 0.76 | -1.7 dB |
| Peaking | 4774 Hz | 9.95 | 3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20N60NC%20Wired%20Passive/AKG%20N60NC%20Wired%20Passive.png)