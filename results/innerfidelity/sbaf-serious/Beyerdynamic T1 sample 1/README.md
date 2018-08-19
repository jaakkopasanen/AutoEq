# Beyerdynamic T1 sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.8; 23 5.6; 25 5.2; 26 5.0; 28 4.6; 30 4.3; 32 4.0; 35 3.7; 37 3.4; 40 3.2; 42 3.0; 45 2.7; 49 2.4; 52 2.3; 56 2.7; 59 2.9; 64 2.2; 68 1.6; 73 1.0; 78 0.6; 83 0.2; 89 -0.1; 95 -0.5; 102 -0.7; 109 -1.0; 117 -1.1; 125 -1.4; 134 -1.6; 143 -1.7; 153 -1.8; 164 -2.0; 175 -2.0; 188 -2.1; 201 -2.2; 215 -2.2; 230 -2.2; 246 -2.2; 263 -2.2; 282 -2.1; 301 -2.1; 323 -1.9; 345 -1.8; 369 -1.8; 395 -1.7; 423 -1.5; 452 -1.3; 484 -1.2; 518 -1.2; 554 -1.0; 593 -0.8; 635 -0.7; 679 -0.7; 726 -0.6; 777 -0.2; 832 -0.2; 890 -0.2; 952 0.0; 1019 0.1; 1090 0.3; 1167 0.4; 1248 0.6; 1336 0.7; 1429 0.2; 1529 -0.6; 1636 -1.3; 1751 -2.1; 1873 -1.6; 2004 -0.3; 2145 1.2; 2295 1.3; 2455 -0.4; 2627 0.2; 2811 0.0; 3008 0.7; 3219 1.4; 3444 1.2; 3685 1.1; 3943 1.0; 4219 0.3; 4514 0.4; 4830 4.3; 5168 6.0; 5530 1.3; 5917 -4.6; 6331 -5.7; 6775 -1.2; 7249 -4.3; 7756 -8.0; 8299 -11.6; 8880 -12.5; 9502 -9.5; 10167 -4.2; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 -0.0; 14260 -0.9; 15258 -2.0; 16326 -2.1; 17469 -0.9; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 20 Hz    |  0.6  | 6.0 dB   |
| Peaking | 60 Hz    |  3.36 | 1.7 dB   |
| Peaking | 215 Hz   |  0.59 | -2.4 dB  |
| Peaking | 5067 Hz  |  8.94 | 7.9 dB   |
| Peaking | 8613 Hz  |  3.36 | -13.6 dB |
| Peaking | 1752 Hz  |  5.4  | -3.1 dB  |
| Peaking | 2434 Hz  |  0.58 | 1.1 dB   |
| Peaking | 6093 Hz  | 11.53 | -5.8 dB  |
| Peaking | 11336 Hz |  5.06 | 2.7 dB   |
| Peaking | 15990 Hz |  3.48 | -2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1%20sample%201/Beyerdynamic%20T1%20sample%201.png)