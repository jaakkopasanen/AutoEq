# Sennheiser HD650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.1; 22 0.4; 23 0.0; 25 -0.6; 26 -0.9; 28 -1.4; 30 -1.9; 32 -2.3; 35 -2.8; 37 -3.1; 40 -3.1; 42 -2.9; 45 -2.6; 49 -3.0; 52 -3.7; 56 -4.3; 59 -4.5; 64 -4.5; 68 -4.3; 73 -4.5; 78 -4.8; 83 -5.0; 89 -5.2; 95 -5.3; 102 -5.3; 109 -5.3; 117 -5.3; 125 -5.3; 134 -5.3; 143 -5.3; 153 -5.1; 164 -5.0; 175 -4.9; 188 -4.7; 201 -4.6; 215 -4.4; 230 -4.2; 246 -3.9; 263 -3.8; 282 -3.7; 301 -3.5; 323 -3.2; 345 -3.1; 369 -2.8; 395 -2.5; 423 -2.3; 452 -1.9; 484 -1.6; 518 -1.3; 554 -0.9; 593 -0.5; 635 -0.2; 679 -0.1; 726 -0.0; 777 0.3; 832 0.0; 890 -0.1; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.1; 1248 0.1; 1336 0.8; 1429 1.5; 1529 1.9; 1636 2.1; 1751 2.0; 1873 1.6; 2004 1.5; 2145 1.6; 2295 1.8; 2455 2.0; 2627 2.0; 2811 1.9; 3008 2.1; 3219 2.0; 3444 2.5; 3685 3.4; 3943 4.5; 4219 4.7; 4514 4.6; 4830 5.7; 5168 6.0; 5530 6.0; 5917 5.6; 6331 3.8; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.74 | 2.6 dB  |
| Peaking | 57 Hz   | 0.4  | -2.4 dB |
| Peaking | 161 Hz  | 0.46 | -3.9 dB |
| Peaking | 2013 Hz | 0.73 | 1.7 dB  |
| Peaking | 5134 Hz | 1.99 | 6.0 dB  |
| Peaking | 12 Hz   | 1.16 | 1.1 dB  |
| Peaking | 5865 Hz | 5.36 | 2.6 dB  |
| Peaking | 3971 Hz | 6.66 | 1.7 dB  |
| Peaking | 6784 Hz | 6.81 | 2.6 dB  |
| Peaking | 6580 Hz | 1.47 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD650/Sennheiser%20HD650.png)