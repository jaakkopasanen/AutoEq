# Shure SRH1440

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.6; 78 4.9; 83 4.4; 89 3.8; 95 3.3; 102 2.8; 109 2.5; 117 2.1; 125 1.7; 134 1.3; 143 0.9; 153 0.6; 164 0.5; 175 0.4; 188 0.1; 201 0.0; 215 0.0; 230 0.0; 246 0.0; 263 0.1; 282 0.1; 301 0.1; 323 0.2; 345 0.3; 369 0.3; 395 0.5; 423 0.7; 452 0.9; 484 0.9; 518 0.9; 554 1.2; 593 1.3; 635 1.8; 679 1.9; 726 1.4; 777 1.3; 832 0.8; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.7; 1248 -1.1; 1336 -1.6; 1429 -2.3; 1529 -3.2; 1636 -4.1; 1751 -4.9; 1873 -5.4; 2004 -5.5; 2145 -5.9; 2295 -6.0; 2455 -5.9; 2627 -5.6; 2811 -6.2; 3008 -6.2; 3219 -6.3; 3444 -6.4; 3685 -6.1; 3943 -5.8; 4219 -5.6; 4514 -4.9; 4830 -3.4; 5168 -1.8; 5530 -0.5; 5917 0.2; 6331 1.1; 6775 1.5; 7249 0.4; 7756 -1.8; 8299 -4.6; 8880 -7.0; 9502 -7.4; 10167 -5.2; 10879 -1.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.55 | 6.8 dB  |
| Peaking | 773 Hz   | 1.24 | 2.6 dB  |
| Peaking | 3001 Hz  | 0.61 | -7.0 dB |
| Peaking | 6454 Hz  | 2.17 | 5.3 dB  |
| Peaking | 9163 Hz  | 4.03 | -7.9 dB |
| Peaking | 41 Hz    | 2.54 | -1.0 dB |
| Peaking | 70 Hz    | 2.51 | 1.4 dB  |
| Peaking | 182 Hz   | 1.36 | -1.0 dB |
| Peaking | 1260 Hz  | 6.35 | 0.7 dB  |
| Peaking | 11748 Hz | 5    | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1440/Shure%20SRH1440.png)