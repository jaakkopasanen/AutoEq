# Ultrasone PRO 900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 -1.4; 22 -2.3; 23 -2.8; 25 -3.6; 26 -4.0; 28 -4.6; 30 -5.2; 32 -5.7; 35 -6.3; 37 -6.6; 40 -7.1; 42 -7.3; 45 -7.5; 49 -7.6; 52 -7.7; 56 -7.6; 59 -6.9; 64 -5.0; 68 -4.5; 73 -5.3; 78 -6.5; 83 -7.3; 89 -7.7; 95 -7.4; 102 -7.0; 109 -7.3; 117 -7.7; 125 -8.0; 134 -7.5; 143 -7.3; 153 -7.4; 164 -6.2; 175 -6.3; 188 -5.6; 201 -4.4; 215 -2.8; 230 -0.7; 246 1.6; 263 3.9; 282 4.5; 301 3.3; 323 1.8; 345 0.8; 369 0.1; 395 -0.5; 423 -0.8; 452 -0.8; 484 -0.8; 518 0.7; 554 4.7; 593 2.3; 635 0.5; 679 0.2; 726 0.2; 777 0.3; 832 0.0; 890 -0.3; 952 -0.1; 1019 0.2; 1090 0.7; 1167 1.3; 1248 1.4; 1336 0.7; 1429 -0.3; 1529 -1.0; 1636 -1.2; 1751 -1.1; 1873 0.0; 2004 1.1; 2145 0.6; 2295 0.7; 2455 -1.3; 2627 -5.1; 2811 -5.3; 3008 -4.3; 3219 -4.3; 3444 -4.4; 3685 -4.4; 3943 -4.5; 4219 -4.9; 4514 -3.4; 4830 0.9; 5168 4.4; 5530 0.1; 5917 -3.0; 6331 -8.6; 6775 -8.2; 7249 -3.9; 7756 -0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -1.3; 13327 -4.6; 14260 -7.8; 15258 -9.4; 16326 -9.0; 17469 -7.4; 18692 -5.7; 20000 -4.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 46 Hz    |  0.8  | -7.2 dB |
| Peaking | 129 Hz   |  1.71 | -7.1 dB |
| Peaking | 3423 Hz  |  1.87 | -5.1 dB |
| Peaking | 32916 Hz |  2.89 | -6.9 dB |
| Peaking | 17897 Hz |  1.14 | -6.4 dB |
| Peaking | 189 Hz   |  3.77 | -3.1 dB |
| Peaking | 275 Hz   |  4.09 | 6.4 dB  |
| Peaking | 563 Hz   | 11.36 | 5.2 dB  |
| Peaking | 5186 Hz  |  9.62 | 7.1 dB  |
| Peaking | 6534 Hz  |  7.39 | -9.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20900/Ultrasone%20PRO%20900.png)