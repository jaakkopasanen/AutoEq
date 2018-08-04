# Phiaton MS 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.3; 52 4.8; 56 4.4; 59 4.1; 64 3.8; 68 3.6; 73 3.6; 78 3.7; 83 3.6; 89 3.6; 95 3.2; 102 2.9; 109 2.6; 117 2.5; 125 2.2; 134 1.9; 143 2.0; 153 1.9; 164 2.0; 175 2.1; 188 2.2; 201 2.5; 215 2.9; 230 3.0; 246 3.0; 263 3.0; 282 3.1; 301 3.0; 323 3.0; 345 3.1; 369 3.2; 395 3.6; 423 3.7; 452 3.7; 484 3.9; 518 4.2; 554 4.5; 593 4.7; 635 4.8; 679 4.5; 726 3.9; 777 3.2; 832 2.4; 890 1.5; 952 0.8; 1019 -0.2; 1090 -1.1; 1167 -1.8; 1248 -2.1; 1336 -1.9; 1429 -2.1; 1529 -1.4; 1636 -1.0; 1751 -1.0; 1873 -0.7; 2004 0.8; 2145 2.2; 2295 4.2; 2455 5.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.37 | 6.2 dB  |
| Peaking | 276 Hz  | 1.14 | 1.9 dB  |
| Peaking | 638 Hz  | 1.17 | 5.1 dB  |
| Peaking | 1410 Hz | 1.08 | -5.8 dB |
| Peaking | 3365 Hz | 0.74 | 7.8 dB  |
| Peaking | 1951 Hz | 5.55 | -1.4 dB |
| Peaking | 2461 Hz | 4.06 | 2.0 dB  |
| Peaking | 3474 Hz | 2.57 | -1.2 dB |
| Peaking | 6247 Hz | 2.2  | 5.5 dB  |
| Peaking | 7425 Hz | 1.48 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20300/Phiaton%20MS%20300.png)