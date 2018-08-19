# Denon AH-D2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 4.6; 22 3.7; 23 3.3; 25 2.6; 26 2.3; 28 1.9; 30 1.6; 32 1.4; 35 1.4; 37 1.5; 40 1.8; 42 1.8; 45 1.7; 49 1.5; 52 1.4; 56 1.4; 59 1.7; 64 2.0; 68 1.8; 73 1.5; 78 1.4; 83 1.2; 89 1.1; 95 0.9; 102 0.8; 109 0.7; 117 0.5; 125 0.6; 134 0.4; 143 0.3; 153 0.2; 164 0.4; 175 0.2; 188 0.2; 201 0.4; 215 0.4; 230 0.4; 246 0.4; 263 0.5; 282 0.7; 301 0.8; 323 0.8; 345 0.8; 369 1.0; 395 1.0; 423 0.9; 452 1.0; 484 0.9; 518 0.6; 554 0.0; 593 -0.2; 635 -0.4; 679 -0.4; 726 -0.4; 777 0.8; 832 0.8; 890 0.1; 952 -0.1; 1019 -0.0; 1090 0.1; 1167 0.6; 1248 1.2; 1336 1.6; 1429 1.9; 1529 1.9; 1636 1.8; 1751 1.5; 1873 1.5; 2004 2.1; 2145 3.2; 2295 4.7; 2455 5.3; 2627 5.3; 2811 4.7; 3008 3.8; 3219 2.7; 3444 2.0; 3685 1.2; 3943 1.0; 4219 1.8; 4514 2.0; 4830 1.5; 5168 2.1; 5530 2.7; 5917 0.7; 6331 -0.4; 6775 0.2; 7249 1.1; 7756 0.3; 8299 0.0; 8880 -0.2; 9502 -3.4; 10167 -4.8; 10879 -2.5; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -3.0; 18692 -5.1; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.51499799083071dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 2556 Hz  | 1.91 | 5.3 dB  |
| Peaking | 5333 Hz  | 5.33 | 2.2 dB  |
| Peaking | 10083 Hz | 6.5  | -5.5 dB |
| Peaking | 18734 Hz | 2.57 | -5.7 dB |
| Peaking | 17 Hz    | 1.38 | 5.1 dB  |
| Peaking | 63 Hz    | 1.08 | 1.6 dB  |
| Peaking | 371 Hz   | 2.19 | 1.0 dB  |
| Peaking | 1405 Hz  | 6.08 | 1.2 dB  |
| Peaking | 14980 Hz | 2.02 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D2000/Denon%20AH-D2000.png)