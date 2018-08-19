# RHA T20 Reference Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 -4.9; 22 -5.2; 23 -5.3; 25 -5.6; 26 -5.7; 28 -5.8; 30 -5.9; 32 -6.0; 35 -6.1; 37 -6.1; 40 -6.1; 42 -6.1; 45 -6.2; 49 -6.2; 52 -6.2; 56 -6.3; 59 -6.3; 64 -6.3; 68 -6.3; 73 -6.3; 78 -6.3; 83 -6.3; 89 -6.4; 95 -6.4; 102 -6.3; 109 -6.1; 117 -5.9; 125 -5.8; 134 -5.7; 143 -5.5; 153 -5.4; 164 -5.1; 175 -4.8; 188 -4.6; 201 -4.3; 215 -4.0; 230 -3.6; 246 -3.3; 263 -3.0; 282 -2.6; 301 -2.3; 323 -2.0; 345 -1.6; 369 -1.3; 395 -1.0; 423 -0.6; 452 -0.3; 484 -0.2; 518 0.1; 554 0.4; 593 0.9; 635 1.0; 679 1.0; 726 1.1; 777 1.2; 832 1.0; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.6; 1336 -2.6; 1429 -3.6; 1529 -4.3; 1636 -3.9; 1751 -2.0; 1873 -0.2; 2004 -2.2; 2145 -3.2; 2295 -3.7; 2455 -4.4; 2627 -4.8; 2811 -4.5; 3008 -3.4; 3219 -2.4; 3444 -1.7; 3685 -2.2; 3943 -3.8; 4219 -6.8; 4514 -9.4; 4830 -8.5; 5168 -4.2; 5530 0.1; 5917 3.2; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.157005278596179dB` and instead set Global volume in the UI for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.36 | -6.0 dB  |
| Peaking | 147 Hz  | 0.9  | -3.2 dB  |
| Peaking | 2411 Hz | 1.34 | -3.8 dB  |
| Peaking | 4641 Hz | 4.6  | -10.3 dB |
| Peaking | 6269 Hz | 4.06 | 6.7 dB   |
| Peaking | 744 Hz  | 1.66 | 2.0 dB   |
| Peaking | 1563 Hz | 3.13 | -3.9 dB  |
| Peaking | 1863 Hz | 5.05 | 4.1 dB   |
| Peaking | 3162 Hz | 1.85 | -1.7 dB  |
| Peaking | 3402 Hz | 4.27 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Reference%20Filter/RHA%20T20%20Reference%20Filter.png)