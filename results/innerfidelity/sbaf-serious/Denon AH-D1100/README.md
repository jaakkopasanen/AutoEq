# Denon AH-D1100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.7; 22 -4.5; 23 -4.9; 25 -5.6; 26 -5.8; 28 -6.2; 30 -6.6; 32 -7.0; 35 -7.5; 37 -7.9; 40 -8.3; 42 -8.6; 45 -8.9; 49 -9.3; 52 -9.6; 56 -9.9; 59 -10.1; 64 -10.4; 68 -10.6; 73 -10.8; 78 -11.0; 83 -11.2; 89 -11.4; 95 -11.4; 102 -11.3; 109 -11.1; 117 -10.8; 125 -11.1; 134 -11.4; 143 -11.5; 153 -11.9; 164 -11.3; 175 -10.0; 188 -10.9; 201 -11.3; 215 -11.5; 230 -11.0; 246 -10.4; 263 -9.7; 282 -8.4; 301 -7.1; 323 -5.5; 345 -3.7; 369 -2.0; 395 -0.0; 423 1.9; 452 2.7; 484 2.8; 518 2.3; 554 1.7; 593 0.9; 635 0.2; 679 -0.5; 726 -0.8; 777 -0.8; 832 -0.9; 890 -0.6; 952 -0.3; 1019 0.1; 1090 0.6; 1167 0.9; 1248 1.2; 1336 1.2; 1429 0.9; 1529 0.4; 1636 0.2; 1751 0.2; 1873 0.2; 2004 0.0; 2145 -2.1; 2295 -2.5; 2455 -2.0; 2627 -0.9; 2811 1.0; 3008 2.9; 3219 2.0; 3444 0.4; 3685 2.9; 3943 5.8; 4219 5.9; 4514 2.2; 4830 1.9; 5168 3.2; 5530 2.5; 5917 2.6; 6331 2.1; 6775 1.8; 7249 1.3; 7756 -0.0; 8299 -1.6; 8880 -2.8; 9502 -3.5; 10167 -3.6; 10879 -2.9; 11640 -1.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099998284527814dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -5.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.12 | -5.8 dB |
| Peaking | 101 Hz  | 0.75 | -8.4 dB |
| Peaking | 223 Hz  | 2.11 | -7.9 dB |
| Peaking | 4114 Hz | 3.5  | 5.6 dB  |
| Peaking | 17 Hz   | 2.87 | 2.6 dB  |
| Peaking | 472 Hz  | 3.67 | 5.2 dB  |
| Peaking | 2302 Hz | 7.09 | -3.3 dB |
| Peaking | 6354 Hz | 2.58 | 2.5 dB  |
| Peaking | 9675 Hz | 2.73 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D1100/Denon%20AH-D1100.png)