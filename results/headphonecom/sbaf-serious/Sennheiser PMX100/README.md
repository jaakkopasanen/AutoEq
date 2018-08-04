# Sennheiser PMX100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.3; 22 -2.1; 23 -2.4; 25 -3.0; 26 -3.3; 28 -3.7; 30 -4.1; 32 -4.5; 35 -5.0; 37 -5.2; 40 -5.5; 42 -5.7; 45 -6.0; 49 -6.3; 52 -6.5; 56 -6.6; 59 -6.7; 64 -6.9; 68 -7.0; 73 -7.0; 78 -7.0; 83 -7.1; 89 -7.0; 95 -6.9; 102 -6.8; 109 -6.4; 117 -6.3; 125 -6.3; 134 -6.0; 143 -6.0; 153 -5.8; 164 -5.6; 175 -5.2; 188 -4.9; 201 -4.8; 215 -4.5; 230 -4.2; 246 -3.8; 263 -3.4; 282 -3.0; 301 -2.8; 323 -2.4; 345 -2.1; 369 -1.9; 395 -1.7; 423 -1.4; 452 -1.2; 484 -1.1; 518 -0.9; 554 -0.5; 593 -0.3; 635 -0.1; 679 -0.2; 726 -0.0; 777 0.3; 832 0.3; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.1; 1167 -0.3; 1248 -0.6; 1336 -1.0; 1429 -1.6; 1529 -2.3; 1636 -2.9; 1751 -3.3; 1873 -3.4; 2004 -3.3; 2145 -2.3; 2295 -1.0; 2455 0.3; 2627 1.1; 2811 3.2; 3008 5.3; 3219 6.0; 3444 6.0; 3685 5.6; 3943 0.9; 4219 -5.9; 4514 -6.6; 4830 -2.1; 5168 2.3; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PMX100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 81 Hz   | 0.38 | -7.2 dB  |
| Peaking | 1917 Hz | 2.39 | -4.7 dB  |
| Peaking | 3489 Hz | 2.18 | 9.3 dB   |
| Peaking | 4376 Hz | 4.57 | -13.3 dB |
| Peaking | 5842 Hz | 3.51 | 7.2 dB   |
| Peaking | 216 Hz  | 2.71 | -0.6 dB  |
| Peaking | 782 Hz  | 1.24 | 0.8 dB   |
| Peaking | 1519 Hz | 5.57 | -0.8 dB  |
| Peaking | 8253 Hz | 4.71 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PMX100/Sennheiser%20PMX100.png)