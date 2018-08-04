# Flare Audio Reference R1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.7; 56 4.7; 59 3.9; 64 2.7; 68 1.8; 73 0.7; 78 -0.1; 83 -0.8; 89 -1.5; 95 -2.1; 102 -3.1; 109 -3.7; 117 -4.2; 125 -4.7; 134 -5.1; 143 -5.3; 153 -5.5; 164 -5.6; 175 -5.5; 188 -5.6; 201 -5.6; 215 -5.6; 230 -5.7; 246 -5.7; 263 -5.7; 282 -5.8; 301 -5.8; 323 -5.7; 345 -5.6; 369 -5.7; 395 -5.7; 423 -5.7; 452 -6.0; 484 -6.5; 518 -7.0; 554 -7.2; 593 -7.3; 635 -7.4; 679 -7.4; 726 -6.9; 777 -6.1; 832 -5.0; 890 -3.4; 952 -1.6; 1019 0.7; 1090 3.0; 1167 5.6; 1248 6.0; 1336 6.0; 1429 6.0; 1529 6.0; 1636 3.2; 1751 -1.6; 1873 -4.3; 2004 -4.7; 2145 -1.8; 2295 0.8; 2455 3.4; 2627 5.3; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Flare Audio Reference R1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 43 Hz   | 0.42 | 8.6 dB   |
| Peaking | 118 Hz  | 0.65 | -7.6 dB  |
| Peaking | 1318 Hz | 0.32 | -12.8 dB |
| Peaking | 1265 Hz | 1.9  | 17.4 dB  |
| Peaking | 3641 Hz | 0.8  | 13.8 dB  |
| Peaking | 1558 Hz | 7.37 | 5.5 dB   |
| Peaking | 1931 Hz | 4.31 | -5.7 dB  |
| Peaking | 2627 Hz | 3.61 | 4.3 dB   |
| Peaking | 5913 Hz | 2.16 | 7.2 dB   |
| Peaking | 6021 Hz | 0.85 | -4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Flare%20Audio%20Reference%20R1/Flare%20Audio%20Reference%20R1.png)