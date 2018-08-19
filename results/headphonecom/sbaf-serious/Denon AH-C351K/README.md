# Denon AH-C351K

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.6; 22 -1.7; 23 -1.7; 25 -1.8; 26 -1.8; 28 -1.9; 30 -2.0; 32 -2.0; 35 -2.0; 37 -2.1; 40 -2.1; 42 -2.2; 45 -2.3; 49 -2.5; 52 -2.6; 56 -2.8; 59 -2.9; 64 -3.2; 68 -3.4; 73 -3.6; 78 -3.8; 83 -4.0; 89 -4.2; 95 -4.4; 102 -4.6; 109 -4.8; 117 -5.0; 125 -5.2; 134 -5.4; 143 -5.6; 153 -5.7; 164 -5.7; 175 -5.8; 188 -5.9; 201 -5.7; 215 -5.8; 230 -5.6; 246 -5.5; 263 -5.3; 282 -5.4; 301 -5.6; 323 -5.4; 345 -5.1; 369 -4.8; 395 -4.5; 423 -4.3; 452 -4.0; 484 -3.7; 518 -3.3; 554 -2.9; 593 -2.5; 635 -2.1; 679 -1.7; 726 -1.3; 777 -0.9; 832 -0.6; 890 -0.4; 952 -0.2; 1019 0.0; 1090 0.2; 1167 0.6; 1248 0.8; 1336 1.0; 1429 1.0; 1529 0.9; 1636 0.8; 1751 1.1; 1873 1.8; 2004 2.7; 2145 3.9; 2295 5.1; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.1; 4830 3.3; 5168 1.7; 5530 -1.6; 5917 -5.1; 6331 -3.2; 6775 0.1; 7249 1.1; 7756 0.3; 8299 -0.9; 8880 -3.7; 9502 -4.0; 10167 -0.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.1; 15258 -2.7; 16326 -1.6; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999999970616dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C351K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 58 Hz    | 0.15 | -1.5 dB |
| Peaking | 219 Hz   | 0.44 | -4.8 dB |
| Peaking | 3418 Hz  | 0.85 | 6.9 dB  |
| Peaking | 5930 Hz  | 5.63 | -8.6 dB |
| Peaking | 9196 Hz  | 5.5  | -5.6 dB |
| Peaking | 1078 Hz  | 1.63 | 0.4 dB  |
| Peaking | 1800 Hz  | 2.47 | -2.4 dB |
| Peaking | 2475 Hz  | 1.3  | 2.2 dB  |
| Peaking | 3143 Hz  | 2.85 | -1.9 dB |
| Peaking | 15511 Hz | 5.12 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C351K/Denon%20AH-C351K.png)