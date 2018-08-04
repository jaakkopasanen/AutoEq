# Ultrasone HFi 2400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.1; 22 1.7; 23 1.0; 25 -0.2; 26 -0.7; 28 -1.7; 30 -2.5; 32 -3.2; 35 -4.2; 37 -4.8; 40 -5.5; 42 -5.9; 45 -6.3; 49 -6.5; 52 -6.7; 56 -7.1; 59 -7.4; 64 -7.4; 68 -7.4; 73 -7.5; 78 -7.8; 83 -8.0; 89 -8.0; 95 -7.8; 102 -7.8; 109 -7.6; 117 -7.4; 125 -7.1; 134 -6.8; 143 -6.6; 153 -6.3; 164 -5.8; 175 -5.5; 188 -5.3; 201 -4.8; 215 -4.5; 230 -5.3; 246 -5.9; 263 -5.4; 282 -4.8; 301 -4.4; 323 -3.8; 345 -3.3; 369 -2.9; 395 -2.7; 423 -2.2; 452 -2.0; 484 -1.9; 518 -1.2; 554 -0.2; 593 -0.1; 635 -0.4; 679 -0.4; 726 -0.4; 777 -0.4; 832 -0.5; 890 -0.0; 952 0.2; 1019 -0.1; 1090 0.1; 1167 0.6; 1248 1.0; 1336 1.6; 1429 2.6; 1529 3.3; 1636 3.4; 1751 2.6; 1873 2.5; 2004 2.9; 2145 2.9; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 4.4; 3219 2.2; 3444 0.8; 3685 2.8; 3943 3.2; 4219 2.7; 4514 5.4; 4830 6.0; 5168 6.0; 5530 6.0; 5917 2.6; 6331 -5.9; 6775 -5.9; 7249 -0.8; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.0; 14260 -1.1; 15258 -1.1; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi 2400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 49 Hz   |  1.48 | -3.8 dB |
| Peaking | 100 Hz  |  0.75 | -7.1 dB |
| Peaking | 272 Hz  |  1.41 | -3.3 dB |
| Peaking | 2472 Hz |  1.75 | 5.8 dB  |
| Peaking | 4963 Hz |  5.33 | 6.5 dB  |
| Peaking | 1536 Hz |  4.95 | 2.1 dB  |
| Peaking | 3400 Hz | 12.37 | -1.9 dB |
| Peaking | 2094 Hz |  8.71 | -1.7 dB |
| Peaking | 5705 Hz |  8.09 | 5.2 dB  |
| Peaking | 6519 Hz |  7.6  | -9.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Ultrasone%20HFi%202400/Ultrasone%20HFi%202400.png)