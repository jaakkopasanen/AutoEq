# Sennheiser PX 200 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.8; 22 5.1; 23 4.8; 25 4.2; 26 4.0; 28 3.7; 30 3.3; 32 3.0; 35 2.6; 37 2.4; 40 2.1; 42 1.9; 45 1.6; 49 1.4; 52 1.2; 56 1.0; 59 0.8; 64 0.7; 68 0.6; 73 0.4; 78 0.3; 83 0.3; 89 0.4; 95 1.2; 102 1.8; 109 1.1; 117 0.5; 125 0.5; 134 0.7; 143 0.5; 153 0.2; 164 0.1; 175 -0.0; 188 -0.1; 201 -0.2; 215 -0.1; 230 0.5; 246 1.0; 263 1.0; 282 0.5; 301 0.1; 323 0.3; 345 0.2; 369 0.1; 395 -0.0; 423 -0.1; 452 -0.1; 484 -0.1; 518 0.0; 554 0.2; 593 0.4; 635 0.7; 679 0.6; 726 0.4; 777 0.5; 832 0.5; 890 0.4; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.4; 1336 -0.5; 1429 -0.5; 1529 0.2; 1636 1.3; 1751 0.8; 1873 0.5; 2004 0.8; 2145 1.8; 2295 3.2; 2455 3.9; 2627 4.9; 2811 5.9; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.99 | 5.6 dB  |
| Peaking | 5 Hz    | 1.67 | 0.3 dB  |
| Peaking | 32 Hz   | 1.47 | 0.7 dB  |
| Peaking | 102 Hz  | 6.43 | 1.5 dB  |
| Peaking | 4069 Hz | 1.04 | 7.0 dB  |
| Peaking | 1389 Hz | 2.19 | -1.3 dB |
| Peaking | 2798 Hz | 4.51 | 2.1 dB  |
| Peaking | 4097 Hz | 3.34 | -1.2 dB |
| Peaking | 6351 Hz | 2.63 | 5.3 dB  |
| Peaking | 7239 Hz | 1.56 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20PX%20200%20II/Sennheiser%20PX%20200%20II.png)