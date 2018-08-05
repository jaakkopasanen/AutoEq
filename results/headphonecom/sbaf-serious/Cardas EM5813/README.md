# Cardas EM5813

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -8.4; 22 -8.4; 23 -8.4; 25 -8.4; 26 -8.4; 28 -8.4; 30 -8.4; 32 -8.4; 35 -8.3; 37 -8.2; 40 -8.1; 42 -8.1; 45 -8.1; 49 -8.2; 52 -8.2; 56 -8.1; 59 -8.1; 64 -8.1; 68 -8.1; 73 -8.1; 78 -8.1; 83 -8.3; 89 -8.5; 95 -8.8; 102 -9.1; 109 -9.5; 117 -9.9; 125 -10.3; 134 -10.6; 143 -10.8; 153 -10.9; 164 -10.8; 175 -10.6; 188 -10.4; 201 -10.2; 215 -9.9; 230 -9.5; 246 -9.1; 263 -8.9; 282 -8.4; 301 -7.9; 323 -7.5; 345 -7.0; 369 -6.5; 395 -6.1; 423 -5.5; 452 -5.2; 484 -4.9; 518 -4.4; 554 -3.9; 593 -3.2; 635 -2.8; 679 -2.7; 726 -2.4; 777 -2.0; 832 -2.0; 890 0.1; 952 1.3; 1019 -0.1; 1090 -0.7; 1167 -1.0; 1248 -1.3; 1336 -1.7; 1429 -2.2; 1529 -2.7; 1636 -3.1; 1751 -3.4; 1873 -3.6; 2004 -4.0; 2145 -4.6; 2295 -5.7; 2455 -7.0; 2627 -6.7; 2811 -4.0; 3008 -1.2; 3219 0.5; 3444 1.4; 3685 0.8; 3943 -1.2; 4219 -5.1; 4514 -6.9; 4830 -3.5; 5168 1.5; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cardas EM5813 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.31 | -7.9 dB |
| Peaking | 183 Hz  | 0.52 | -9.8 dB |
| Peaking | 2373 Hz | 2.98 | -6.8 dB |
| Peaking | 4539 Hz | 6.87 | -9.1 dB |
| Peaking | 5857 Hz | 3.17 | 7.4 dB  |
| Peaking | 955 Hz  | 4.71 | 3.5 dB  |
| Peaking | 1440 Hz | 0.68 | -1.0 dB |
| Peaking | 4156 Hz | 7.24 | -1.7 dB |
| Peaking | 3471 Hz | 4.23 | 3.4 dB  |
| Peaking | 8128 Hz | 4.94 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Cardas%20EM5813/Cardas%20EM5813.png)