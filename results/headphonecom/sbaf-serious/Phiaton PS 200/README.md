# Phiaton PS 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.6; 22 1.6; 23 1.6; 25 1.5; 26 1.5; 28 1.5; 30 1.4; 32 1.3; 35 1.2; 37 1.1; 40 1.0; 42 1.0; 45 0.9; 49 0.7; 52 0.6; 56 0.4; 59 0.3; 64 0.0; 68 -0.2; 73 -0.4; 78 -0.6; 83 -0.8; 89 -1.1; 95 -1.3; 102 -1.5; 109 -1.6; 117 -1.8; 125 -2.0; 134 -2.2; 143 -2.3; 153 -2.3; 164 -2.5; 175 -2.6; 188 -2.7; 201 -2.8; 215 -2.6; 230 -2.6; 246 -2.6; 263 -2.6; 282 -2.4; 301 -2.3; 323 -2.2; 345 -1.8; 369 -1.7; 395 -1.5; 423 -1.3; 452 -1.1; 484 -0.9; 518 -0.7; 554 -0.5; 593 -0.3; 635 0.0; 679 0.2; 726 0.3; 777 0.4; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.4; 1248 -0.7; 1336 -1.0; 1429 -1.3; 1529 -1.6; 1636 -1.8; 1751 -1.8; 1873 -1.5; 2004 -1.2; 2145 -0.7; 2295 0.0; 2455 1.1; 2627 2.7; 2811 4.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.3; 4514 3.7; 4830 3.3; 5168 3.1; 5530 2.7; 5917 1.8; 6331 0.4; 6775 -0.9; 7249 -2.0; 7756 -3.0; 8299 -4.0; 8880 -5.7; 9502 -7.4; 10167 -7.2; 10879 -3.6; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999437614dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.67 | 1.7 dB  |
| Peaking | 192 Hz   | 0.7  | -2.9 dB |
| Peaking | 2021 Hz  | 1.49 | -4.8 dB |
| Peaking | 3323 Hz  | 1.12 | 7.9 dB  |
| Peaking | 9384 Hz  | 2.66 | -8.4 dB |
| Peaking | 794 Hz   | 2.74 | 0.9 dB  |
| Peaking | 1457 Hz  | 5.06 | -0.6 dB |
| Peaking | 5574 Hz  | 7.02 | 0.9 dB  |
| Peaking | 7123 Hz  | 4.79 | -1.3 dB |
| Peaking | 11979 Hz | 5.9  | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20200/Phiaton%20PS%20200.png)