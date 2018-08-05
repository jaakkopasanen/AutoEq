# Sennheiser PX 200 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.9; 52 5.7; 56 5.5; 59 5.4; 64 5.2; 68 5.0; 73 4.8; 78 4.6; 83 4.5; 89 4.4; 95 5.0; 102 5.3; 109 4.3; 117 3.4; 125 2.9; 134 2.8; 143 2.4; 153 1.9; 164 1.7; 175 1.5; 188 1.3; 201 1.3; 215 1.4; 230 1.9; 246 2.4; 263 2.3; 282 1.9; 301 1.5; 323 1.7; 345 1.6; 369 1.5; 395 1.2; 423 1.1; 452 0.9; 484 0.7; 518 0.5; 554 0.6; 593 0.9; 635 1.0; 679 0.6; 726 0.4; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.7; 1248 -1.1; 1336 -1.9; 1429 -2.6; 1529 -2.5; 1636 -1.8; 1751 -2.3; 1873 -2.4; 2004 -2.2; 2145 -1.3; 2295 0.1; 2455 1.0; 2627 1.9; 2811 3.2; 3008 4.4; 3219 5.0; 3444 5.4; 3685 5.7; 3943 5.8; 4219 3.7; 4514 2.3; 4830 2.4; 5168 3.9; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.35 | 5.3 dB  |
| Peaking | 82 Hz   |  0.04 | 1.0 dB  |
| Peaking | 1721 Hz |  1.38 | -3.8 dB |
| Peaking | 3417 Hz |  1.97 | 6.2 dB  |
| Peaking | 5962 Hz |  4.07 | 5.8 dB  |
| Peaking | 99 Hz   |  7.02 | 1.7 dB  |
| Peaking | 201 Hz  |  1.52 | -1.5 dB |
| Peaking | 250 Hz  |  2.45 | 1.7 dB  |
| Peaking | 1647 Hz | 10.06 | 0.6 dB  |
| Peaking | 8291 Hz |  4.45 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20200%20II/Sennheiser%20PX%20200%20II.png)