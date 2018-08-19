# Stax SR-Lambda Signature

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.2; 35 3.6; 37 2.4; 40 0.9; 42 -0.0; 45 -1.0; 49 -1.7; 52 -1.6; 56 -1.5; 59 -1.3; 64 -0.6; 68 0.0; 73 0.4; 78 0.5; 83 0.6; 89 0.6; 95 0.7; 102 0.9; 109 1.0; 117 1.1; 125 1.1; 134 1.2; 143 1.2; 153 1.2; 164 1.2; 175 1.2; 188 1.3; 201 1.2; 215 1.4; 230 1.4; 246 1.4; 263 1.4; 282 1.5; 301 1.5; 323 1.5; 345 1.5; 369 1.4; 395 1.5; 423 1.7; 452 1.8; 484 1.8; 518 1.7; 554 1.6; 593 1.8; 635 1.6; 679 1.3; 726 1.2; 777 1.2; 832 1.0; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.3; 1167 -0.8; 1248 -1.5; 1336 -2.4; 1429 -3.3; 1529 -3.8; 1636 -4.0; 1751 -4.4; 1873 -4.2; 2004 -2.6; 2145 -0.4; 2295 2.1; 2455 4.0; 2627 3.5; 2811 1.6; 3008 1.3; 3219 0.8; 3444 0.9; 3685 0.4; 3943 0.0; 4219 -0.6; 4514 -0.3; 4830 0.4; 5168 1.6; 5530 2.8; 5917 2.3; 6331 0.4; 6775 -0.8; 7249 -0.3; 7756 -0.1; 8299 -1.8; 8880 -3.5; 9502 -2.9; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -1.8; 20000 -3.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Lambda Signature ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.95 | 7.0 dB  |
| Peaking | 1742 Hz  | 2.72 | -5.5 dB |
| Peaking | 2481 Hz  | 4.04 | 5.2 dB  |
| Peaking | 5628 Hz  | 7.07 | 3.3 dB  |
| Peaking | 9013 Hz  | 5.82 | -4.0 dB |
| Peaking | 51 Hz    | 2.04 | -3.8 dB |
| Peaking | 62 Hz    | 0.12 | 1.2 dB  |
| Peaking | 556 Hz   | 0.89 | 1.3 dB  |
| Peaking | 1364 Hz  | 4.3  | -1.4 dB |
| Peaking | 10711 Hz | 5.94 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Lambda%20Signature/Stax%20SR-Lambda%20Signature.png)