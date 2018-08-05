# RHA T20 Treble Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 10 -84; 20 -4.8; 22 -5.1; 23 -5.2; 25 -5.4; 26 -5.5; 28 -5.6; 30 -5.7; 32 -5.8; 35 -5.8; 37 -5.8; 40 -5.7; 42 -5.7; 45 -5.6; 49 -5.5; 52 -5.4; 56 -5.3; 59 -5.2; 64 -5.0; 68 -4.9; 73 -4.8; 78 -4.7; 83 -4.7; 89 -4.8; 95 -5.0; 102 -5.2; 109 -5.4; 117 -5.6; 125 -5.9; 134 -6.0; 143 -6.0; 153 -5.9; 164 -5.7; 175 -5.4; 188 -5.1; 201 -4.8; 215 -4.4; 230 -4.0; 246 -3.6; 263 -3.3; 282 -2.9; 301 -2.5; 323 -2.2; 345 -1.8; 369 -1.5; 395 -1.1; 423 -0.7; 452 -0.4; 484 -0.2; 518 -0.0; 554 0.4; 593 0.8; 635 0.9; 679 1.0; 726 1.0; 777 1.2; 832 1.0; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.6; 1336 -2.6; 1429 -3.6; 1529 -4.3; 1636 -4.0; 1751 -2.0; 1873 -0.1; 2004 -2.1; 2145 -3.3; 2295 -4.0; 2455 -5.0; 2627 -5.9; 2811 -6.4; 3008 -5.6; 3219 -4.5; 3444 -3.3; 3685 -3.4; 3943 -4.8; 4219 -7.7; 4514 -10.8; 4830 -10.6; 5168 -6.3; 5530 -1.4; 5917 2.1; 6331 4.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -1.1; 15258 -0.3; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.1dB` and instead set Global volume in the UI for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Treble Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.41 | -5.7 dB  |
| Peaking | 229 Hz  | 1.86 | -2.1 dB  |
| Peaking | 141 Hz  | 1.35 | -4.0 dB  |
| Peaking | 2687 Hz | 1.89 | -5.8 dB  |
| Peaking | 4624 Hz | 6.16 | -11.4 dB |
| Peaking | 751 Hz  | 1.82 | 1.8 dB   |
| Peaking | 1564 Hz | 3.05 | -4.3 dB  |
| Peaking | 1859 Hz | 5.88 | 3.6 dB   |
| Peaking | 5063 Hz | 6    | -2.9 dB  |
| Peaking | 6350 Hz | 4.29 | 6.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Treble%20Filter/RHA%20T20%20Treble%20Filter.png)