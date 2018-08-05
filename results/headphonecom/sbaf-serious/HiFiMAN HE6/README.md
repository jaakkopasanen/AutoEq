# HiFiMAN HE6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 4.2; 22 3.2; 23 2.8; 25 2.1; 26 1.9; 28 1.5; 30 1.4; 32 1.3; 35 1.3; 37 1.4; 40 1.6; 42 1.7; 45 1.8; 49 1.9; 52 1.9; 56 1.9; 59 1.9; 64 2.0; 68 2.0; 73 2.0; 78 1.7; 83 1.6; 89 1.6; 95 1.4; 102 1.2; 109 1.1; 117 0.7; 125 0.3; 134 0.0; 143 -0.2; 153 -0.4; 164 -0.3; 175 -0.2; 188 -0.3; 201 -0.3; 215 -0.3; 230 -0.2; 246 -0.2; 263 -0.2; 282 -0.0; 301 0.3; 323 0.2; 345 0.3; 369 0.4; 395 0.3; 423 0.4; 452 0.3; 484 0.3; 518 0.2; 554 0.2; 593 0.3; 635 0.5; 679 0.5; 726 0.6; 777 0.6; 832 0.1; 890 -0.3; 952 0.1; 1019 0.0; 1090 0.2; 1167 1.2; 1248 0.8; 1336 0.9; 1429 0.9; 1529 0.6; 1636 1.0; 1751 2.5; 1873 3.3; 2004 3.3; 2145 2.4; 2295 1.5; 2455 2.6; 2627 2.5; 2811 0.8; 3008 -0.2; 3219 -0.3; 3444 -0.2; 3685 -0.7; 3943 -0.3; 4219 -2.4; 4514 -3.3; 4830 -1.3; 5168 2.3; 5530 5.2; 5917 -3.1; 6331 -4.5; 6775 -4.9; 7249 -4.2; 7756 -3.6; 8299 -4.2; 8880 -4.9; 9502 -3.6; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 -1.2; 13327 -4.2; 14260 -6.2; 15258 -5.9; 16326 -3.4; 17469 -0.5; 18692 -0.1; 20000 -3.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.3dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc         |     Q | Gain    |
|:--------|:-----------|:------|:--------|
| Peaking | 11 Hz      |  0.16 | 2.6 dB  |
| Peaking | 2035 Hz    |  1.97 | 3.1 dB  |
| Peaking | 4372 Hz    | 10.37 | -3.4 dB |
| Peaking | 7756 Hz    |  2.39 | -4.8 dB |
| Peaking | 33363 Hz   |  2.91 | -6.9 dB |
| Peaking | 10 Hz      |  2.48 | 1.1 dB  |
| Peaking | 168 Hz     |  2.81 | -0.8 dB |
| Peaking | 5479 Hz    |  8.99 | 8.6 dB  |
| Peaking | 6084 Hz    |  5.02 | -4.4 dB |
| Peaking | 3223049 Hz |  2.3  | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE6/HiFiMAN%20HE6.png)