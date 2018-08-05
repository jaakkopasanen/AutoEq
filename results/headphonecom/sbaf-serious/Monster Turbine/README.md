# Monster Turbine

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 -13.1; 22 -13.0; 23 -12.9; 25 -12.7; 26 -12.6; 28 -12.4; 30 -12.2; 32 -12.0; 35 -11.6; 37 -11.4; 40 -11.1; 42 -10.9; 45 -10.6; 49 -10.2; 52 -9.9; 56 -9.6; 59 -9.3; 64 -9.0; 68 -8.7; 73 -8.3; 78 -8.1; 83 -7.9; 89 -7.7; 95 -7.7; 102 -7.7; 109 -7.7; 117 -7.8; 125 -8.0; 134 -8.0; 143 -7.8; 153 -7.7; 164 -7.6; 175 -7.3; 188 -6.9; 201 -6.5; 215 -6.0; 230 -5.5; 246 -5.1; 263 -4.7; 282 -4.2; 301 -3.8; 323 -3.3; 345 -2.7; 369 -2.3; 395 -1.9; 423 -1.4; 452 -1.1; 484 -0.9; 518 -0.6; 554 -0.2; 593 0.3; 635 0.5; 679 0.5; 726 0.6; 777 0.9; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.6; 1336 -2.1; 1429 -2.1; 1529 -2.8; 1636 -3.6; 1751 -4.6; 1873 -5.3; 2004 -5.8; 2145 -6.4; 2295 -6.8; 2455 -7.2; 2627 -7.6; 2811 -7.4; 3008 -6.3; 3219 -5.1; 3444 -4.2; 3685 -4.3; 3943 -5.1; 4219 -7.0; 4514 -7.9; 4830 -6.4; 5168 -3.0; 5530 0.5; 5917 3.3; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.3; 8880 -2.6; 9502 -3.1; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -2.6; 16326 -0.9; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 0.65 | -12.7 dB |
| Peaking | 36 Hz   | 0.37 | -8.9 dB  |
| Peaking | 171 Hz  | 1    | -5.1 dB  |
| Peaking | 2464 Hz | 1.66 | -7.9 dB  |
| Peaking | 4458 Hz | 6.1  | -7.2 dB  |
| Peaking | 749 Hz  | 1.58 | 2.3 dB   |
| Peaking | 3096 Hz | 0.07 | -0.6 dB  |
| Peaking | 6310 Hz | 3.4  | 6.7 dB   |
| Peaking | 9208 Hz | 7.1  | -3.3 dB  |
| Peaking | 4976 Hz | 7.28 | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Turbine/Monster%20Turbine.png)