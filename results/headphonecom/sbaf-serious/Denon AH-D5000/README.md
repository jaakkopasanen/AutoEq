# Denon AH-D5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 10 -84; 20 2.5; 22 1.7; 23 1.4; 25 0.8; 26 0.6; 28 0.2; 30 -0.0; 32 -0.2; 35 -0.5; 37 -0.7; 40 -0.9; 42 -0.9; 45 -0.7; 49 -0.7; 52 -0.8; 56 -1.0; 59 -1.0; 64 -1.2; 68 -1.3; 73 -1.4; 78 -1.6; 83 -1.7; 89 -1.9; 95 -2.0; 102 -2.0; 109 -2.1; 117 -2.2; 125 -2.4; 134 -2.5; 143 -2.5; 153 -2.6; 164 -2.5; 175 -2.5; 188 -2.2; 201 -2.1; 215 -2.2; 230 -2.1; 246 -2.1; 263 -2.1; 282 -2.0; 301 -2.0; 323 -1.7; 345 -1.4; 369 -1.1; 395 -0.8; 423 -0.6; 452 -0.3; 484 0.0; 518 0.4; 554 0.9; 593 1.4; 635 1.6; 679 1.1; 726 -0.0; 777 -1.6; 832 -1.9; 890 0.4; 952 1.0; 1019 -0.3; 1090 -1.0; 1167 -1.4; 1248 -1.8; 1336 -2.3; 1429 -2.7; 1529 -3.2; 1636 -3.5; 1751 -3.8; 1873 -3.7; 2004 -3.3; 2145 -2.9; 2295 -2.3; 2455 -1.4; 2627 0.5; 2811 1.4; 3008 1.0; 3219 0.5; 3444 -0.1; 3685 -0.7; 3943 -2.0; 4219 -3.5; 4514 -3.7; 4830 -3.1; 5168 -2.0; 5530 -0.9; 5917 -0.2; 6331 -1.8; 6775 -3.8; 7249 -4.5; 7756 -3.8; 8299 -3.3; 8880 -4.5; 9502 -5.0; 10167 -1.5; 10879 0.0; 11640 0.0; 12455 -0.0; 13327 -1.2; 14260 -0.1; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.7; 20000 -7.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6392418532763258dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 2.67 | 2.7 dB  |
| Peaking | 142 Hz   | 0.64 | -2.6 dB |
| Peaking | 1729 Hz  | 2.33 | -4.0 dB |
| Peaking | 7902 Hz  | 1.58 | -4.3 dB |
| Peaking | 20039 Hz | 4.25 | -7.2 dB |
| Peaking | 606 Hz   | 4.83 | 2.3 dB  |
| Peaking | 3177 Hz  | 2.14 | 5.3 dB  |
| Peaking | 4185 Hz  | 1.02 | -4.9 dB |
| Peaking | 5815 Hz  | 3.54 | 4.4 dB  |
| Peaking | 11185 Hz | 4.89 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D5000/Denon%20AH-D5000.png)