# Denon AH-D1100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -6.8; 22 -7.3; 23 -7.5; 25 -7.9; 26 -8.1; 28 -8.4; 30 -8.7; 32 -9.0; 35 -9.3; 37 -9.5; 40 -9.8; 42 -9.9; 45 -10.1; 49 -10.4; 52 -10.5; 56 -10.8; 59 -11.0; 64 -11.2; 68 -11.3; 73 -11.5; 78 -11.6; 83 -11.6; 89 -11.6; 95 -11.4; 102 -11.1; 109 -10.9; 117 -11.1; 125 -11.8; 134 -12.8; 143 -13.1; 153 -12.4; 164 -11.6; 175 -11.2; 188 -12.1; 201 -12.0; 215 -11.7; 230 -11.0; 246 -10.0; 263 -9.0; 282 -7.7; 301 -6.1; 323 -4.4; 345 -2.6; 369 -0.8; 395 1.0; 423 2.4; 452 3.4; 484 3.4; 518 2.9; 554 2.2; 593 1.4; 635 0.6; 679 0.1; 726 -0.3; 777 -0.5; 832 -0.6; 890 -0.4; 952 -0.2; 1019 0.2; 1090 0.4; 1167 0.5; 1248 0.5; 1336 0.4; 1429 -0.1; 1529 -0.9; 1636 -1.6; 1751 -2.5; 1873 -3.1; 2004 -3.1; 2145 -2.5; 2295 -1.3; 2455 0.3; 2627 2.0; 2811 3.9; 3008 4.9; 3219 2.9; 3444 1.2; 3685 5.1; 3943 6.0; 4219 5.8; 4514 0.4; 4830 -0.5; 5168 0.9; 5530 0.7; 5917 3.8; 6331 3.6; 6775 2.2; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -1.9; 9502 -3.5; 10167 -4.0; 10879 -3.0; 11640 -0.6; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999431830884dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 3 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 74 Hz    | 0.88 | -7.5 dB |
| Peaking | 146 Hz   | 1.85 | -7.8 dB |
| Peaking | 227 Hz   | 2.7  | -8.3 dB |
| Peaking | 25 Hz    | 0.36 | -6.6 dB |
| Peaking | 473 Hz   | 3.59 | 5.3 dB  |
| Peaking | 3884 Hz  | 4.5  | 6.3 dB  |
| Peaking | 6248 Hz  | 5.77 | 4.1 dB  |
| Peaking | 10025 Hz | 4.04 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D1100/Denon%20AH-D1100.png)