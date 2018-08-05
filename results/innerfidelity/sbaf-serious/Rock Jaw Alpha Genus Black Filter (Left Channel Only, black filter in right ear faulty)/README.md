# Rock Jaw Alpha Genus Black Filter (Left Channel Only, black filter in right ear faulty)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 10 -84; 20 0.4; 22 -0.1; 23 -0.3; 25 -0.7; 26 -0.9; 28 -1.3; 30 -1.6; 32 -1.8; 35 -2.1; 37 -2.3; 40 -2.5; 42 -2.7; 45 -2.8; 49 -3.0; 52 -3.1; 56 -3.2; 59 -3.3; 64 -3.4; 68 -3.5; 73 -3.6; 78 -3.8; 83 -4.1; 89 -4.5; 95 -4.9; 102 -5.4; 109 -5.8; 117 -6.3; 125 -6.8; 134 -7.1; 143 -7.4; 153 -7.5; 164 -7.5; 175 -7.3; 188 -7.2; 201 -7.0; 215 -6.8; 230 -6.5; 246 -6.2; 263 -6.0; 282 -5.5; 301 -5.3; 323 -4.9; 345 -4.5; 369 -4.2; 395 -3.8; 423 -3.3; 452 -3.0; 484 -2.7; 518 -2.4; 554 -1.8; 593 -1.2; 635 -0.9; 679 -0.7; 726 -0.3; 777 0.1; 832 0.2; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.7; 1248 -1.1; 1336 -1.8; 1429 -2.6; 1529 -3.4; 1636 -4.2; 1751 -4.7; 1873 -5.1; 2004 -5.3; 2145 -5.5; 2295 -5.6; 2455 -5.5; 2627 -5.2; 2811 -4.0; 3008 -2.2; 3219 -0.2; 3444 1.7; 3685 2.0; 3943 1.1; 4219 -1.1; 4514 -3.2; 4830 -5.0; 5168 -7.6; 5530 -9.6; 5917 -6.2; 6331 -2.2; 6775 0.4; 7249 1.1; 7756 0.3; 8299 0.0; 8880 -0.3; 9502 -1.9; 10167 -3.4; 10879 -2.7; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Jaw Alpha Genus Black Filter (Left Channel Only, black filter in right ear faulty) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 1.23 | -1.6 dB  |
| Peaking | 171 Hz   | 0.63 | -7.6 dB  |
| Peaking | 2110 Hz  | 2.15 | -6.2 dB  |
| Peaking | 5455 Hz  | 6    | -10.2 dB |
| Peaking | 37752 Hz | 6.61 | -3.7 dB  |
| Peaking | 853 Hz   | 3.09 | 1.6 dB   |
| Peaking | 2723 Hz  | 4.94 | -2.7 dB  |
| Peaking | 3688 Hz  | 3.19 | 4.8 dB   |
| Peaking | 4569 Hz  | 2.9  | -2.7 dB  |
| Peaking | 7118 Hz  | 5.72 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Rock%20Jaw%20Alpha%20Genus%20Black%20Filter%20(Left%20Channel%20Only,%20black%20filter%20in%20right%20ear%20faulty)/Rock%20Jaw%20Alpha%20Genus%20Black%20Filter%20(Left%20Channel%20Only,%20black%20filter%20in%20right%20ear%20faulty).png)