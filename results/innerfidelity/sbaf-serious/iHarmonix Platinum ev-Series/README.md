# iHarmonix Platinum ev-Series

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 -10.0; 22 -9.9; 23 -9.9; 25 -9.9; 26 -9.9; 28 -9.9; 30 -9.8; 32 -9.8; 35 -9.7; 37 -9.7; 40 -9.6; 42 -9.6; 45 -9.5; 49 -9.4; 52 -9.3; 56 -9.2; 59 -9.1; 64 -9.0; 68 -9.0; 73 -8.9; 78 -8.9; 83 -9.0; 89 -9.1; 95 -9.3; 102 -9.7; 109 -9.9; 117 -10.2; 125 -10.5; 134 -10.8; 143 -10.8; 153 -10.7; 164 -10.5; 175 -10.3; 188 -10.0; 201 -9.6; 215 -9.2; 230 -8.8; 246 -8.5; 263 -8.1; 282 -7.6; 301 -7.1; 323 -6.8; 345 -6.2; 369 -5.8; 395 -5.4; 423 -4.8; 452 -4.1; 484 -3.7; 518 -3.3; 554 -2.8; 593 -2.1; 635 -1.8; 679 -1.2; 726 -1.2; 777 -0.4; 832 -0.4; 890 -0.2; 952 -0.3; 1019 -0.3; 1090 -0.5; 1167 -0.6; 1248 -0.6; 1336 -0.9; 1429 -1.2; 1529 -1.5; 1636 -1.7; 1751 -1.9; 1873 -2.0; 2004 -1.9; 2145 -2.1; 2295 -2.2; 2455 -2.1; 2627 -2.1; 2811 -1.4; 3008 0.8; 3219 2.9; 3444 4.2; 3685 4.2; 3943 2.9; 4219 0.2; 4514 -3.0; 4830 -6.2; 5168 -7.4; 5530 -4.1; 5917 0.1; 6331 2.1; 6775 2.9; 7249 1.3; 7756 0.0; 8299 -1.7; 8880 -1.3; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.9dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iHarmonix Platinum ev-Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 1.51 | -9.6 dB |
| Peaking | 30 Hz   | 0.44 | -7.9 dB |
| Peaking | 172 Hz  | 0.54 | -9.2 dB |
| Peaking | 3617 Hz | 5.6  | 5.6 dB  |
| Peaking | 5026 Hz | 6.57 | -8.7 dB |
| Peaking | 849 Hz  | 2.37 | 1.4 dB  |
| Peaking | 2143 Hz | 1.82 | -2.4 dB |
| Peaking | 5468 Hz | 6.46 | -3.4 dB |
| Peaking | 6520 Hz | 2.21 | 4.0 dB  |
| Peaking | 8338 Hz | 4.68 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/iHarmonix%20Platinum%20ev-Series/iHarmonix%20Platinum%20ev-Series.png)