# Sennheiser HD 229

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.5; 22 5.7; 23 5.4; 25 4.7; 26 4.4; 28 3.8; 30 3.3; 32 2.8; 35 2.1; 37 1.7; 40 1.1; 42 0.8; 45 0.3; 49 -0.3; 52 -0.7; 56 -1.1; 59 -1.4; 64 -1.9; 68 -2.2; 73 -2.6; 78 -2.9; 83 -3.2; 89 -3.6; 95 -3.9; 102 -4.1; 109 -4.1; 117 -4.0; 125 -3.9; 134 -3.8; 143 -3.8; 153 -4.2; 164 -4.2; 175 -3.5; 188 -3.4; 201 -3.0; 215 -2.5; 230 -2.5; 246 -2.7; 263 -2.3; 282 -1.5; 301 -0.6; 323 0.1; 345 0.4; 369 0.6; 395 0.8; 423 1.3; 452 1.3; 484 0.9; 518 0.9; 554 1.1; 593 1.3; 635 1.2; 679 0.9; 726 0.7; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 -0.0; 1248 0.1; 1336 0.2; 1429 0.5; 1529 1.0; 1636 -0.6; 1751 -1.5; 1873 -1.1; 2004 -0.7; 2145 -0.2; 2295 0.3; 2455 0.8; 2627 0.4; 2811 0.2; 3008 0.3; 3219 0.3; 3444 0.6; 3685 1.0; 3943 0.2; 4219 -1.0; 4514 -1.7; 4830 -0.7; 5168 1.4; 5530 3.0; 5917 4.1; 6331 4.8; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.8; 8880 -4.0; 9502 -3.4; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.556501633806553dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 229 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.16 | 6.3 dB  |
| Peaking | 94 Hz   | 1.13 | -3.8 dB |
| Peaking | 175 Hz  | 1.88 | -2.8 dB |
| Peaking | 6315 Hz | 4.23 | 5.6 dB  |
| Peaking | 9035 Hz | 5.48 | -5.0 dB |
| Peaking | 256 Hz  | 4.25 | -1.9 dB |
| Peaking | 468 Hz  | 1.05 | 1.6 dB  |
| Peaking | 1794 Hz | 6.97 | -1.8 dB |
| Peaking | 4358 Hz | 1.64 | 1.5 dB  |
| Peaking | 4497 Hz | 5.07 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20229/Sennheiser%20HD%20229.png)