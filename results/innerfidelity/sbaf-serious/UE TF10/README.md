# UE TF10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.1; 22 0.0; 23 0.0; 25 -0.1; 26 -0.1; 28 -0.2; 30 -0.2; 32 -0.3; 35 -0.4; 37 -0.5; 40 -0.6; 42 -0.7; 45 -0.8; 49 -0.9; 52 -1.0; 56 -1.2; 59 -1.4; 64 -1.6; 68 -1.8; 73 -2.1; 78 -2.4; 83 -2.6; 89 -2.8; 95 -3.0; 102 -3.3; 109 -3.4; 117 -3.5; 125 -3.6; 134 -3.8; 143 -3.8; 153 -3.9; 164 -4.0; 175 -3.9; 188 -3.9; 201 -3.8; 215 -3.7; 230 -3.5; 246 -3.4; 263 -3.3; 282 -2.9; 301 -2.8; 323 -2.6; 345 -2.5; 369 -2.3; 395 -2.1; 423 -1.7; 452 -1.4; 484 -1.3; 518 -1.1; 554 -0.7; 593 -0.3; 635 -0.2; 679 -0.0; 726 0.1; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 -0.1; 1336 -0.2; 1429 -0.3; 1529 -0.3; 1636 -0.1; 1751 0.3; 1873 1.0; 2004 1.6; 2145 2.1; 2295 2.9; 2455 4.0; 2627 5.2; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999893069dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `UE TF10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 3 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 99 Hz   | 1.03 | -1.4 dB |
| Peaking | 198 Hz  | 0.64 | -3.5 dB |
| Peaking | 4009 Hz | 1.01 | 7.0 dB  |
| Peaking | 1603 Hz | 2.83 | -1.5 dB |
| Peaking | 2782 Hz | 4.07 | 2.1 dB  |
| Peaking | 4035 Hz | 2.99 | -1.3 dB |
| Peaking | 6226 Hz | 2.51 | 4.5 dB  |
| Peaking | 7482 Hz | 1.54 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/UE%20TF10/UE%20TF10.png)