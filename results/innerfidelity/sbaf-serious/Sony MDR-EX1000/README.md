# Sony MDR-EX1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.6; 22 4.4; 23 4.3; 25 4.1; 26 4.0; 28 3.9; 30 3.8; 32 3.7; 35 3.5; 37 3.5; 40 3.4; 42 3.4; 45 3.3; 49 3.2; 52 3.1; 56 3.1; 59 3.0; 64 2.9; 68 2.7; 73 2.6; 78 2.4; 83 2.2; 89 1.8; 95 1.3; 102 0.7; 109 0.2; 117 -0.3; 125 -1.0; 134 -1.5; 143 -1.8; 153 -2.1; 164 -2.3; 175 -2.2; 188 -2.2; 201 -2.3; 215 -2.3; 230 -2.1; 246 -2.1; 263 -2.0; 282 -1.8; 301 -1.7; 323 -1.6; 345 -1.4; 369 -1.3; 395 -1.2; 423 -0.9; 452 -0.7; 484 -0.7; 518 -0.5; 554 -0.1; 593 0.3; 635 0.4; 679 0.4; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.8; 1429 -2.5; 1529 -3.1; 1636 -3.6; 1751 -3.8; 1873 -3.6; 2004 -3.1; 2145 -2.4; 2295 -1.3; 2455 0.3; 2627 1.7; 2811 3.1; 3008 5.1; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.0; 4219 1.8; 4514 -1.2; 4830 -5.0; 5168 -6.3; 5530 -3.7; 5917 -0.3; 6331 1.3; 6775 1.3; 7249 -1.0; 7756 -4.0; 8299 -4.8; 8880 -2.7; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.79 | 4.4 dB  |
| Peaking | 1835 Hz | 1.89 | -4.9 dB |
| Peaking | 3439 Hz | 2.12 | 8.0 dB  |
| Peaking | 5095 Hz | 4.92 | -5.5 dB |
| Peaking | 4919 Hz | 4.59 | -3.2 dB |
| Peaking | 81 Hz   | 0.93 | 5.2 dB  |
| Peaking | 122 Hz  | 0.46 | -4.5 dB |
| Peaking | 755 Hz  | 1.83 | 1.5 dB  |
| Peaking | 6543 Hz | 5.56 | 2.8 dB  |
| Peaking | 8110 Hz | 5.22 | -5.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-EX1000/Sony%20MDR-EX1000.png)