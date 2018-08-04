# AKG Quincy Jones Q701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.7; 35 5.3; 37 5.0; 40 4.5; 42 4.2; 45 3.9; 49 3.5; 52 3.2; 56 2.9; 59 2.7; 64 2.4; 68 2.2; 73 2.3; 78 2.4; 83 2.3; 89 1.9; 95 1.2; 102 0.7; 109 0.3; 117 -0.2; 125 -0.9; 134 -1.3; 143 -1.6; 153 -1.8; 164 -1.8; 175 -1.8; 188 -1.9; 201 -2.0; 215 -2.0; 230 -1.9; 246 -1.9; 263 -1.9; 282 -1.8; 301 -1.6; 323 -1.5; 345 -1.5; 369 -1.3; 395 -1.2; 423 -1.0; 452 -0.9; 484 -0.8; 518 -0.6; 554 -0.1; 593 1.0; 635 0.7; 679 0.6; 726 0.8; 777 1.0; 832 0.7; 890 0.3; 952 0.1; 1019 0.1; 1090 -0.1; 1167 -0.5; 1248 -0.9; 1336 -1.6; 1429 -2.4; 1529 -3.2; 1636 -4.0; 1751 -4.7; 1873 -5.4; 2004 -5.6; 2145 -5.3; 2295 -4.9; 2455 -3.9; 2627 -2.9; 2811 -1.7; 3008 -1.1; 3219 -0.3; 3444 0.6; 3685 0.3; 3943 -0.4; 4219 -2.0; 4514 -2.6; 4830 -1.7; 5168 -1.7; 5530 -2.9; 5917 -3.8; 6331 -4.7; 6775 -4.7; 7249 -4.4; 7756 -4.9; 8299 -5.5; 8880 -4.8; 9502 -2.3; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.3; 18692 -2.1; 20000 -2.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Quincy Jones Q701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.2  | 6.4 dB  |
| Peaking | 196 Hz   | 0.64 | -2.8 dB |
| Peaking | 738 Hz   | 1.69 | 1.7 dB  |
| Peaking | 1960 Hz  | 2.11 | -5.9 dB |
| Peaking | 7348 Hz  | 1.82 | -5.4 dB |
| Peaking | 55 Hz    | 3.51 | -0.7 dB |
| Peaking | 2433 Hz  | 5.62 | -1.0 dB |
| Peaking | 3581 Hz  | 3.47 | 2.2 dB  |
| Peaking | 4364 Hz  | 4.96 | -1.8 dB |
| Peaking | 10831 Hz | 5.42 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Quincy%20Jones%20Q701/AKG%20Quincy%20Jones%20Q701.png)