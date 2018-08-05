# AKG K3003 High Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 4.4; 22 3.8; 23 3.6; 25 3.1; 26 3.0; 28 2.6; 30 2.3; 32 2.1; 35 1.7; 37 1.5; 40 1.2; 42 1.1; 45 0.9; 49 0.7; 52 0.5; 56 0.3; 59 0.2; 64 -0.0; 68 -0.2; 73 -0.4; 78 -0.6; 83 -0.9; 89 -1.4; 95 -1.8; 102 -2.4; 109 -2.9; 117 -3.5; 125 -4.0; 134 -4.5; 143 -4.7; 153 -5.0; 164 -5.0; 175 -5.0; 188 -4.9; 201 -4.9; 215 -4.7; 230 -4.5; 246 -4.4; 263 -4.2; 282 -3.9; 301 -3.7; 323 -3.4; 345 -3.1; 369 -2.8; 395 -2.6; 423 -2.1; 452 -1.8; 484 -1.7; 518 -1.4; 554 -1.0; 593 -0.5; 635 -0.3; 679 -0.2; 726 0.1; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.5; 1336 -0.7; 1429 -0.9; 1529 -1.2; 1636 -1.6; 1751 -1.8; 1873 -1.7; 2004 -1.6; 2145 -1.6; 2295 -1.6; 2455 -1.5; 2627 -1.5; 2811 -1.7; 3008 -1.3; 3219 -0.2; 3444 2.3; 3685 3.7; 3943 3.3; 4219 0.2; 4514 -4.6; 4830 -6.6; 5168 -6.0; 5530 -6.4; 5917 -4.9; 6331 -1.4; 6775 0.8; 7249 1.2; 7756 0.0; 8299 -2.8; 8880 -6.6; 9502 -9.4; 10167 -9.3; 10879 -5.9; 11640 -0.9; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.1; 16326 -0.5; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.9dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 High Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 0.29 | 5.0 dB   |
| Peaking | 184 Hz  | 0.72 | -5.4 dB  |
| Peaking | 7173 Hz | 3.55 | 3.8 dB   |
| Peaking | 5340 Hz | 3.93 | -7.6 dB  |
| Peaking | 9713 Hz | 3.69 | -11.0 dB |
| Peaking | 822 Hz  | 2.21 | 1.2 dB   |
| Peaking | 2500 Hz | 0.95 | -2.2 dB  |
| Peaking | 3804 Hz | 3.69 | 6.5 dB   |
| Peaking | 4614 Hz | 8.85 | -4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20High%20Boost%20Filter/AKG%20K3003%20High%20Boost%20Filter.png)