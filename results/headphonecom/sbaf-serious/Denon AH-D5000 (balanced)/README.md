# Denon AH-D5000 (balanced)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 10 -84; 20 -1.2; 22 -2.2; 23 -2.6; 25 -3.3; 26 -3.6; 28 -4.0; 30 -4.3; 32 -4.5; 35 -4.7; 37 -4.8; 40 -5.0; 42 -5.0; 45 -5.0; 49 -4.8; 52 -4.6; 56 -4.5; 59 -4.6; 64 -4.6; 68 -4.6; 73 -4.5; 78 -4.5; 83 -4.4; 89 -4.3; 95 -4.0; 102 -3.9; 109 -3.7; 117 -3.5; 125 -3.3; 134 -3.2; 143 -2.9; 153 -2.7; 164 -2.5; 175 -2.5; 188 -2.5; 201 -2.4; 215 -2.4; 230 -2.1; 246 -2.0; 263 -1.8; 282 -1.6; 301 -1.6; 323 -1.4; 345 -1.0; 369 -0.9; 395 -0.6; 423 -0.3; 452 -0.1; 484 0.1; 518 0.4; 554 1.1; 593 1.7; 635 1.9; 679 1.4; 726 0.4; 777 -0.8; 832 -2.0; 890 0.3; 952 1.2; 1019 -0.2; 1090 -0.9; 1167 -1.4; 1248 -1.7; 1336 -2.3; 1429 -2.7; 1529 -3.0; 1636 -3.4; 1751 -3.6; 1873 -3.4; 2004 -3.2; 2145 -3.4; 2295 -3.1; 2455 -1.9; 2627 0.5; 2811 2.0; 3008 1.7; 3219 1.1; 3444 0.4; 3685 -0.1; 3943 -1.1; 4219 -2.5; 4514 -2.9; 4830 -2.7; 5168 -1.8; 5530 -0.3; 5917 0.2; 6331 -1.8; 6775 -3.4; 7249 -4.3; 7756 -4.1; 8299 -3.8; 8880 -4.1; 9502 -3.8; 10167 -1.6; 10879 -0.0; 11640 0.0; 12455 -0.6; 13327 -2.0; 14260 -0.7; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.0; 20000 -4.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 56 Hz    | 0.32 | -4.7 dB |
| Peaking | 611 Hz   | 4.06 | 2.6 dB  |
| Peaking | 1736 Hz  | 2.15 | -3.9 dB |
| Peaking | 8071 Hz  | 1.97 | -4.5 dB |
| Peaking | 28212 Hz | 2.93 | -4.1 dB |
| Peaking | 2351 Hz  | 4.08 | -3.6 dB |
| Peaking | 2799 Hz  | 2.46 | 4.0 dB  |
| Peaking | 4553 Hz  | 3.4  | -3.1 dB |
| Peaking | 5809 Hz  | 5.66 | 2.5 dB  |
| Peaking | 6803 Hz  | 6.96 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D5000%20(balanced)/Denon%20AH-D5000%20(balanced).png)