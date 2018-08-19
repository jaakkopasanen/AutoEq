# Sennheiser CX 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.3; 22 -1.6; 23 -1.8; 25 -2.1; 26 -2.2; 28 -2.5; 30 -2.7; 32 -2.9; 35 -3.0; 37 -3.1; 40 -3.2; 42 -3.3; 45 -3.5; 49 -3.7; 52 -3.8; 56 -3.9; 59 -4.0; 64 -4.2; 68 -4.3; 73 -4.4; 78 -4.6; 83 -4.7; 89 -4.8; 95 -4.9; 102 -5.0; 109 -4.9; 117 -4.8; 125 -4.9; 134 -4.8; 143 -4.8; 153 -4.6; 164 -4.5; 175 -4.3; 188 -4.1; 201 -3.9; 215 -3.6; 230 -3.4; 246 -3.1; 263 -2.9; 282 -2.6; 301 -2.3; 323 -2.1; 345 -1.8; 369 -1.5; 395 -1.3; 423 -0.9; 452 -0.6; 484 -0.5; 518 -0.3; 554 -0.0; 593 0.4; 635 0.5; 679 0.4; 726 0.6; 777 0.8; 832 0.6; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -0.9; 1336 -1.4; 1429 -1.8; 1529 -2.1; 1636 -2.2; 1751 -2.1; 1873 -1.6; 2004 -1.0; 2145 -0.2; 2295 0.8; 2455 2.3; 2627 3.3; 2811 4.5; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.6; 4514 3.1; 4830 2.3; 5168 2.1; 5530 1.6; 5917 0.8; 6331 -0.0; 6775 -0.3; 7249 0.3; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -0.4; 10879 -1.6; 11640 -0.6; 12455 0.0; 13327 -0.1; 14260 -2.1; 15258 -2.0; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999028093dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 11 Hz    |  0.64 | -1.3 dB |
| Peaking | 73 Hz    |  0.53 | -3.9 dB |
| Peaking | 174 Hz   |  0.94 | -2.6 dB |
| Peaking | 1717 Hz  |  2.28 | -3.3 dB |
| Peaking | 3386 Hz  |  1.77 | 7.0 dB  |
| Peaking | 316 Hz   |  2.41 | -0.5 dB |
| Peaking | 745 Hz   |  1.46 | 1.2 dB  |
| Peaking | 1221 Hz  |  2.53 | -0.7 dB |
| Peaking | 4042 Hz  | 12.37 | 1.2 dB  |
| Peaking | 13452 Hz |  0.81 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20CX%20200/Sennheiser%20CX%20200.png)