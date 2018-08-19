# Polk Audio UltraFit 3000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -9.2; 22 -9.3; 23 -9.3; 25 -9.4; 26 -9.5; 28 -9.6; 30 -9.7; 32 -9.7; 35 -9.8; 37 -9.8; 40 -9.9; 42 -9.9; 45 -9.9; 49 -10.0; 52 -10.1; 56 -10.3; 59 -10.3; 64 -10.4; 68 -10.6; 73 -10.7; 78 -10.8; 83 -10.9; 89 -10.9; 95 -11.0; 102 -10.9; 109 -10.9; 117 -10.9; 125 -10.8; 134 -10.8; 143 -10.7; 153 -10.7; 164 -10.4; 175 -10.2; 188 -10.0; 201 -9.7; 215 -9.4; 230 -9.1; 246 -8.7; 263 -8.3; 282 -7.9; 301 -7.4; 323 -6.9; 345 -6.3; 369 -5.8; 395 -5.3; 423 -4.9; 452 -4.4; 484 -3.9; 518 -3.4; 554 -2.9; 593 -2.4; 635 -1.9; 679 -1.5; 726 -1.2; 777 -0.7; 832 -0.6; 890 -0.5; 952 -0.4; 1019 0.0; 1090 0.2; 1167 0.0; 1248 -0.2; 1336 -0.6; 1429 -1.0; 1529 -1.5; 1636 -1.8; 1751 -1.8; 1873 -1.7; 2004 -1.5; 2145 -1.1; 2295 -0.4; 2455 0.7; 2627 2.0; 2811 3.6; 3008 5.3; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.9; 4219 3.8; 4514 1.1; 4830 -0.1; 5168 1.9; 5530 5.4; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09999999703621dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 12 Hz   |  1.3  | -8.9 dB |
| Peaking | 54 Hz   |  0.28 | -9.0 dB |
| Peaking | 205 Hz  |  0.58 | -5.4 dB |
| Peaking | 3442 Hz |  3.11 | 7.0 dB  |
| Peaking | 6062 Hz |  4.78 | 6.3 dB  |
| Peaking | 1037 Hz |  1.52 | 1.3 dB  |
| Peaking | 1814 Hz |  1.88 | -2.4 dB |
| Peaking | 2863 Hz |  5.48 | 1.8 dB  |
| Peaking | 4759 Hz | 13.03 | -2.5 dB |
| Peaking | 8264 Hz |  6.13 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%203000/Polk%20Audio%20UltraFit%203000.png)