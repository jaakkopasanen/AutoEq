# Marshall Major

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 5.6; 117 5.2; 125 4.7; 134 4.3; 143 4.0; 153 3.6; 164 3.5; 175 3.2; 188 3.0; 201 2.8; 215 2.6; 230 2.5; 246 2.5; 263 2.8; 282 2.8; 301 2.2; 323 2.0; 345 2.3; 369 2.3; 395 2.1; 423 2.0; 452 1.9; 484 2.2; 518 2.6; 554 3.1; 593 3.5; 635 3.7; 679 3.7; 726 3.5; 777 3.2; 832 2.6; 890 1.9; 952 1.0; 1019 -0.1; 1090 -0.7; 1167 -0.8; 1248 -2.0; 1336 -4.0; 1429 -5.8; 1529 -7.2; 1636 -7.8; 1751 -8.6; 1873 -8.2; 2004 -6.8; 2145 -4.9; 2295 -2.6; 2455 -0.5; 2627 1.4; 2811 2.9; 3008 4.0; 3219 4.7; 3444 4.9; 3685 5.5; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 4.2; 6331 1.5; 6775 -1.9; 7249 -3.2; 7756 -2.0; 8299 -1.3; 8880 -2.2; 9502 -3.1; 10167 -0.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall Major ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.14 | 6.0 dB   |
| Peaking | 94 Hz   | 2.01 | 1.2 dB   |
| Peaking | 699 Hz  | 1.37 | 3.9 dB   |
| Peaking | 1740 Hz | 1.93 | -10.6 dB |
| Peaking | 3869 Hz | 1.47 | 7.7 dB   |
| Peaking | 2128 Hz | 6.04 | -1.2 dB  |
| Peaking | 2923 Hz | 2.56 | 2.1 dB   |
| Peaking | 3656 Hz | 2.87 | -2.0 dB  |
| Peaking | 5706 Hz | 2.54 | 7.4 dB   |
| Peaking | 6868 Hz | 1.68 | -6.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Marshall%20Major/Marshall%20Major.png)