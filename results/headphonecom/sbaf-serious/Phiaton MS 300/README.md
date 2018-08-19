# Phiaton MS 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.8; 49 5.1; 52 4.5; 56 4.0; 59 3.7; 64 3.3; 68 3.0; 73 2.9; 78 2.9; 83 2.8; 89 2.8; 95 2.5; 102 2.4; 109 2.2; 117 2.2; 125 2.2; 134 2.0; 143 2.2; 153 2.2; 164 2.3; 175 2.3; 188 2.4; 201 2.7; 215 3.0; 230 3.1; 246 3.1; 263 3.1; 282 3.2; 301 3.1; 323 3.1; 345 3.1; 369 3.2; 395 3.6; 423 3.7; 452 3.7; 484 4.0; 518 4.3; 554 4.5; 593 4.6; 635 4.8; 679 4.6; 726 4.0; 777 3.1; 832 2.4; 890 1.5; 952 0.8; 1019 -0.2; 1090 -1.1; 1167 -1.8; 1248 -2.1; 1336 -1.9; 1429 -2.1; 1529 -1.4; 1636 -1.0; 1751 -0.9; 1873 -0.7; 2004 0.8; 2145 2.2; 2295 4.2; 2455 5.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.53 | 6.3 dB  |
| Peaking | 275 Hz  | 0.74 | 2.4 dB  |
| Peaking | 648 Hz  | 1.31 | 4.6 dB  |
| Peaking | 1423 Hz | 1.09 | -5.7 dB |
| Peaking | 3356 Hz | 0.74 | 7.8 dB  |
| Peaking | 1951 Hz | 5.79 | -1.4 dB |
| Peaking | 2464 Hz | 4.19 | 1.9 dB  |
| Peaking | 3477 Hz | 2.62 | -1.2 dB |
| Peaking | 6252 Hz | 2.19 | 5.6 dB  |
| Peaking | 7409 Hz | 1.47 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20300/Phiaton%20MS%20300.png)