# iHarmonix Platinum ev-Series

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 -10.0; 22 -10.0; 23 -10.0; 25 -10.0; 26 -10.0; 28 -10.0; 30 -10.0; 32 -10.0; 35 -10.0; 37 -10.0; 40 -10.0; 42 -10.0; 45 -10.1; 49 -10.1; 52 -10.2; 56 -10.2; 59 -10.2; 64 -10.3; 68 -10.4; 73 -10.4; 78 -10.5; 83 -10.6; 89 -10.7; 95 -10.7; 102 -10.8; 109 -10.6; 117 -10.6; 125 -10.5; 134 -10.5; 143 -10.3; 153 -10.2; 164 -10.0; 175 -9.7; 188 -9.5; 201 -9.2; 215 -8.9; 230 -8.5; 246 -8.2; 263 -7.9; 282 -7.4; 301 -6.9; 323 -6.6; 345 -6.1; 369 -5.7; 395 -5.3; 423 -4.7; 452 -4.1; 484 -3.6; 518 -3.2; 554 -2.8; 593 -2.0; 635 -1.8; 679 -1.1; 726 -1.2; 777 -0.4; 832 -0.4; 890 -0.2; 952 -0.3; 1019 -0.3; 1090 -0.5; 1167 -0.6; 1248 -0.6; 1336 -0.9; 1429 -1.2; 1529 -1.5; 1636 -1.7; 1751 -1.9; 1873 -2.0; 2004 -1.9; 2145 -2.1; 2295 -2.2; 2455 -2.1; 2627 -2.1; 2811 -1.4; 3008 0.8; 3219 2.9; 3444 4.2; 3685 4.2; 3943 2.9; 4219 0.2; 4514 -3.0; 4830 -6.2; 5168 -7.4; 5530 -4.1; 5917 0.1; 6331 2.1; 6775 2.9; 7249 1.3; 7756 0.0; 8299 -1.7; 8880 -1.3; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.4211924542934256dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iHarmonix Platinum ev-Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 30 Hz   | 0.16 | -9.8 dB  |
| Peaking | 198 Hz  | 0.58 | -4.7 dB  |
| Peaking | 2656 Hz | 1.34 | -9.7 dB  |
| Peaking | 3389 Hz | 1.12 | 11.3 dB  |
| Peaking | 4962 Hz | 4.26 | -11.8 dB |
| Peaking | 393 Hz  | 2.53 | -0.7 dB  |
| Peaking | 839 Hz  | 1.88 | 1.1 dB   |
| Peaking | 1606 Hz | 3.8  | -0.9 dB  |
| Peaking | 6661 Hz | 6.65 | 3.2 dB   |
| Peaking | 8448 Hz | 5.27 | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/iHarmonix%20Platinum%20ev-Series/iHarmonix%20Platinum%20ev-Series.png)