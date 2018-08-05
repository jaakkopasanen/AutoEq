# Nocs NS800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.2; 22 -0.2; 23 -0.2; 25 -0.2; 26 -0.2; 28 -0.2; 30 -0.2; 32 -0.2; 35 -0.1; 37 -0.1; 40 -0.1; 42 -0.1; 45 -0.1; 49 -0.2; 52 -0.2; 56 -0.2; 59 -0.2; 64 -0.2; 68 -0.1; 73 -0.2; 78 -0.4; 83 -0.6; 89 -0.7; 95 -1.0; 102 -1.6; 109 -1.9; 117 -2.3; 125 -2.9; 134 -3.3; 143 -3.5; 153 -3.8; 164 -3.8; 175 -3.8; 188 -3.8; 201 -3.7; 215 -3.6; 230 -3.4; 246 -3.3; 263 -3.2; 282 -3.0; 301 -2.8; 323 -2.5; 345 -2.2; 369 -2.0; 395 -1.8; 423 -1.5; 452 -1.3; 484 -1.3; 518 -1.2; 554 -0.8; 593 -0.3; 635 -0.1; 679 -0.0; 726 0.2; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.6; 1336 -0.9; 1429 -1.3; 1529 -1.5; 1636 -1.7; 1751 -1.6; 1873 -1.4; 2004 -1.2; 2145 -1.1; 2295 -1.0; 2455 -0.7; 2627 -0.9; 2811 -1.1; 3008 -0.1; 3219 2.0; 3444 4.9; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 200 Hz  | 0.8  | -4.0 dB |
| Peaking | 820 Hz  | 2.33 | 1.1 dB  |
| Peaking | 2796 Hz | 4.86 | -3.3 dB |
| Peaking | 1863 Hz | 1.32 | -2.5 dB |
| Peaking | 4422 Hz | 1.24 | 7.4 dB  |
| Peaking | 99 Hz   | 0.9  | 0.9 dB  |
| Peaking | 128 Hz  | 2.28 | -1.3 dB |
| Peaking | 7676 Hz | 1.1  | -1.4 dB |
| Peaking | 6323 Hz | 3.74 | 3.9 dB  |
| Peaking | 7502 Hz | 3.23 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS800/Nocs%20NS800.png)