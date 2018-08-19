# Ultrasone Edition 10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.4; 35 4.6; 37 4.1; 40 3.5; 42 3.2; 45 2.8; 49 2.5; 52 2.2; 56 1.7; 59 1.3; 64 0.9; 68 0.6; 73 0.2; 78 0.1; 83 0.1; 89 -0.3; 95 -0.6; 102 -0.8; 109 -0.9; 117 -0.9; 125 -0.9; 134 -0.9; 143 -0.9; 153 -0.8; 164 -0.6; 175 -0.5; 188 -0.4; 201 -0.2; 215 0.0; 230 0.2; 246 0.4; 263 0.5; 282 0.7; 301 0.8; 323 1.0; 345 1.2; 369 1.4; 395 1.4; 423 1.6; 452 1.7; 484 1.6; 518 1.6; 554 1.6; 593 1.6; 635 1.6; 679 1.5; 726 1.4; 777 1.4; 832 1.0; 890 0.5; 952 0.2; 1019 -0.2; 1090 -0.4; 1167 -1.1; 1248 -1.3; 1336 -1.2; 1429 -0.7; 1529 -0.0; 1636 1.1; 1751 3.4; 1873 6.0; 2004 6.0; 2145 6.0; 2295 5.9; 2455 6.0; 2627 6.0; 2811 5.5; 3008 3.8; 3219 1.2; 3444 -0.8; 3685 -2.8; 3943 -4.1; 4219 -4.2; 4514 -1.9; 4830 1.9; 5168 1.7; 5530 -1.6; 5917 -6.9; 6331 -10.0; 6775 -5.3; 7249 0.5; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -2.0; 14260 -6.2; 15258 -8.4; 16326 -7.0; 17469 -3.1; 18692 -0.3; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 1.24 | 6.6 dB   |
| Peaking | 2400 Hz  | 1.89 | 7.2 dB   |
| Peaking | 3916 Hz  | 5.08 | -6.1 dB  |
| Peaking | 6293 Hz  | 8.48 | -11.3 dB |
| Peaking | 15493 Hz | 2.86 | -9.4 dB  |
| Peaking | 134 Hz   | 1.22 | -1.5 dB  |
| Peaking | 745 Hz   | 0.49 | 2.5 dB   |
| Peaking | 1335 Hz  | 1.19 | -4.3 dB  |
| Peaking | 1874 Hz  | 6.51 | 3.9 dB   |
| Peaking | 9678 Hz  | 1.09 | 0.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Edition%2010/Ultrasone%20Edition%2010.png)