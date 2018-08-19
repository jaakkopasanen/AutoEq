# Phiaton MS 400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.7; 37 5.4; 40 5.0; 42 4.8; 45 4.4; 49 3.6; 52 3.2; 56 2.6; 59 2.3; 64 2.4; 68 2.9; 73 2.8; 78 1.9; 83 1.3; 89 0.8; 95 0.4; 102 0.1; 109 -0.2; 117 -0.3; 125 -0.3; 134 0.1; 143 1.3; 153 2.6; 164 2.2; 175 2.0; 188 2.1; 201 2.2; 215 2.0; 230 1.5; 246 1.4; 263 1.6; 282 1.8; 301 1.9; 323 2.1; 345 2.2; 369 2.5; 395 2.7; 423 2.8; 452 2.7; 484 2.5; 518 2.5; 554 2.5; 593 2.5; 635 2.5; 679 2.5; 726 2.4; 777 2.3; 832 2.2; 890 1.5; 952 0.4; 1019 -0.2; 1090 -0.5; 1167 -0.4; 1248 -0.5; 1336 -0.8; 1429 -1.2; 1529 -1.7; 1636 -2.0; 1751 -1.9; 1873 -1.4; 2004 -0.3; 2145 1.4; 2295 3.1; 2455 4.7; 2627 5.6; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.82 | 6.5 dB  |
| Peaking | 182 Hz  | 3.37 | 1.6 dB  |
| Peaking | 496 Hz  | 0.85 | 2.8 dB  |
| Peaking | 1676 Hz | 1.61 | -5.5 dB |
| Peaking | 3467 Hz | 0.77 | 7.5 dB  |
| Peaking | 114 Hz  | 4.73 | -1.5 dB |
| Peaking | 2647 Hz | 3.78 | 2.2 dB  |
| Peaking | 3201 Hz | 1.29 | -1.4 dB |
| Peaking | 6202 Hz | 2.14 | 5.6 dB  |
| Peaking | 7473 Hz | 1.49 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20400/Phiaton%20MS%20400.png)