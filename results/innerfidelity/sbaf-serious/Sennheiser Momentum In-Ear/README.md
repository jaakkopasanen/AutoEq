# Sennheiser Momentum In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -6.8; 22 -6.9; 23 -6.9; 25 -6.9; 26 -7.0; 28 -7.0; 30 -7.1; 32 -7.1; 35 -7.2; 37 -7.2; 40 -7.2; 42 -7.3; 45 -7.4; 49 -7.4; 52 -7.5; 56 -7.6; 59 -7.6; 64 -7.8; 68 -7.9; 73 -8.0; 78 -8.1; 83 -8.2; 89 -8.3; 95 -8.4; 102 -8.4; 109 -8.4; 117 -8.3; 125 -8.3; 134 -8.2; 143 -8.1; 153 -8.0; 164 -7.8; 175 -7.5; 188 -7.3; 201 -7.1; 215 -6.7; 230 -6.4; 246 -6.0; 263 -5.8; 282 -5.3; 301 -4.9; 323 -4.5; 345 -4.1; 369 -3.7; 395 -3.3; 423 -2.8; 452 -2.3; 484 -2.0; 518 -1.7; 554 -1.1; 593 -0.6; 635 -0.3; 679 -0.2; 726 0.1; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.0; 1429 -1.3; 1529 -1.7; 1636 -1.8; 1751 -1.8; 1873 -1.5; 2004 -1.1; 2145 -0.7; 2295 -0.0; 2455 1.1; 2627 2.0; 2811 3.1; 3008 4.6; 3219 5.6; 3444 6.0; 3685 6.0; 3943 5.3; 4219 3.5; 4514 2.0; 4830 1.2; 5168 0.9; 5530 -0.3; 5917 -2.5; 6331 -5.1; 6775 -4.9; 7249 -3.1; 7756 -1.4; 8299 -0.2; 8880 0.0; 9502 0.0; 10167 -0.3; 10879 -1.9; 11640 -3.0; 12455 -3.4; 13327 -3.5; 14260 -1.9; 15258 -0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999844387975dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 1.39 | -6.5 dB |
| Peaking | 51 Hz    | 0.33 | -6.5 dB |
| Peaking | 177 Hz   | 0.64 | -4.7 dB |
| Peaking | 3552 Hz  | 2.7  | 7.0 dB  |
| Peaking | 6566 Hz  | 4.2  | -6.1 dB |
| Peaking | 787 Hz   | 2.27 | 1.3 dB  |
| Peaking | 1726 Hz  | 2.12 | -2.5 dB |
| Peaking | 6832 Hz  | 0.22 | 0.6 dB  |
| Peaking | 12872 Hz | 2.23 | -4.5 dB |
| Peaking | 15408 Hz | 3.43 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)