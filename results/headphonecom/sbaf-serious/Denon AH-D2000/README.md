# Denon AH-D2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 0.6; 22 -0.3; 23 -0.7; 25 -1.4; 26 -1.7; 28 -2.1; 30 -2.4; 32 -2.5; 35 -2.5; 37 -2.4; 40 -2.1; 42 -2.1; 45 -2.2; 49 -2.3; 52 -2.3; 56 -2.1; 59 -1.8; 64 -1.4; 68 -1.5; 73 -1.5; 78 -1.5; 83 -1.4; 89 -1.3; 95 -1.2; 102 -1.1; 109 -0.9; 117 -0.8; 125 -0.6; 134 -0.5; 143 -0.5; 153 -0.5; 164 -0.1; 175 -0.1; 188 -0.1; 201 0.1; 215 0.2; 230 0.3; 246 0.3; 263 0.4; 282 0.7; 301 0.8; 323 0.8; 345 0.8; 369 0.9; 395 1.0; 423 1.0; 452 1.0; 484 0.8; 518 0.4; 554 0.0; 593 -0.1; 635 -0.3; 679 -0.5; 726 -0.5; 777 0.9; 832 0.8; 890 0.1; 952 -0.1; 1019 -0.0; 1090 0.1; 1167 0.6; 1248 1.2; 1336 1.6; 1429 1.9; 1529 1.9; 1636 1.8; 1751 1.4; 1873 1.5; 2004 2.1; 2145 3.2; 2295 4.7; 2455 5.4; 2627 5.2; 2811 4.6; 3008 3.9; 3219 2.7; 3444 1.9; 3685 1.2; 3943 1.3; 4219 1.8; 4514 1.9; 4830 1.4; 5168 2.2; 5530 2.7; 5917 0.6; 6331 -0.5; 6775 0.3; 7249 1.1; 7756 0.3; 8299 0.0; 8880 -0.3; 9502 -3.3; 10167 -4.7; 10879 -2.7; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -2.9; 18692 -5.0; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.75 | -2.4 dB |
| Peaking | 2556 Hz  | 1.86 | 5.2 dB  |
| Peaking | 5331 Hz  | 6.18 | 2.3 dB  |
| Peaking | 10081 Hz | 6.31 | -5.3 dB |
| Peaking | 29149 Hz | 2.55 | -5.6 dB |
| Peaking | 358 Hz   | 0.98 | 1.7 dB  |
| Peaking | 1394 Hz  | 4.12 | 1.5 dB  |
| Peaking | 471 Hz   | 0.29 | -0.8 dB |
| Peaking | 15830 Hz | 5.09 | 0.8 dB  |
| Peaking | 12489 Hz | 4.08 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D2000/Denon%20AH-D2000.png)