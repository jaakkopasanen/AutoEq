# Beyerdynamic T50p sn16912

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.6; 42 5.3; 45 5.0; 49 4.5; 52 4.2; 56 3.7; 59 3.4; 64 3.1; 68 2.8; 73 2.6; 78 2.6; 83 2.6; 89 2.5; 95 2.2; 102 2.5; 109 3.0; 117 3.3; 125 3.1; 134 3.1; 143 3.4; 153 3.5; 164 3.7; 175 2.7; 188 1.3; 201 -0.1; 215 -1.2; 230 -2.2; 246 -2.8; 263 -2.9; 282 -3.2; 301 -3.9; 323 -4.8; 345 -4.7; 369 -4.4; 395 -4.1; 423 -3.8; 452 -3.7; 484 -3.4; 518 -3.0; 554 -2.6; 593 -2.1; 635 -1.9; 679 -1.5; 726 -0.7; 777 -0.2; 832 -0.2; 890 -0.2; 952 -0.0; 1019 0.1; 1090 0.3; 1167 0.5; 1248 0.6; 1336 0.5; 1429 0.3; 1529 0.2; 1636 0.2; 1751 0.6; 1873 1.2; 2004 2.0; 2145 3.2; 2295 4.8; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -2.2; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sn16912 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.53 | 6.3 dB  |
| Peaking | 157 Hz   | 1.46 | 5.3 dB  |
| Peaking | 314 Hz   | 0.76 | -5.6 dB |
| Peaking | 4254 Hz  | 0.68 | 7.1 dB  |
| Peaking | 8780 Hz  | 2.63 | -4.6 dB |
| Peaking | 1756 Hz  | 2.98 | -2.0 dB |
| Peaking | 2500 Hz  | 3.48 | 2.4 dB  |
| Peaking | 4152 Hz  | 2.63 | -1.0 dB |
| Peaking | 6141 Hz  | 6.34 | 1.6 dB  |
| Peaking | 13664 Hz | 1.63 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sn16912/Beyerdynamic%20T50p%20sn16912.png)