# Beyerdynamic DT770

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.0; 22 -5.6; 23 -5.8; 25 -6.1; 26 -6.2; 28 -6.4; 30 -6.6; 32 -6.7; 35 -6.7; 37 -6.6; 40 -6.3; 42 -5.9; 45 -5.1; 49 -4.6; 52 -4.6; 56 -3.5; 59 -1.3; 64 1.0; 68 -0.9; 73 -3.9; 78 -5.5; 83 -6.2; 89 -6.5; 95 -6.6; 102 -6.6; 109 -6.4; 117 -5.9; 125 -5.4; 134 -4.5; 143 -3.5; 153 -2.2; 164 -1.4; 175 -1.3; 188 -0.3; 201 0.3; 215 0.7; 230 0.6; 246 0.5; 263 0.0; 282 -0.1; 301 -0.2; 323 -0.3; 345 -0.3; 369 -0.4; 395 -0.6; 423 -0.5; 452 -0.6; 484 -0.7; 518 -0.9; 554 -0.9; 593 -0.7; 635 -0.8; 679 -1.0; 726 -1.0; 777 -0.9; 832 -0.7; 890 -0.5; 952 0.1; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.4; 1336 0.5; 1429 0.5; 1529 0.2; 1636 -0.3; 1751 -0.7; 1873 -0.8; 2004 -0.8; 2145 -0.5; 2295 0.2; 2455 1.1; 2627 1.7; 2811 2.2; 3008 3.0; 3219 3.2; 3444 5.1; 3685 6.0; 3943 6.0; 4219 2.8; 4514 -1.2; 4830 -3.0; 5168 -2.0; 5530 -1.4; 5917 -3.9; 6331 -6.3; 6775 -4.9; 7249 -3.7; 7756 -4.5; 8299 -6.5; 8880 -7.9; 9502 -7.3; 10167 -5.3; 10879 -3.7; 11640 -3.9; 12455 -4.8; 13327 -4.1; 14260 -1.1; 15258 0.0; 16326 -0.7; 17469 -5.4; 18692 -9.4; 20000 -9.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT770 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.14 | -7.2 dB |
| Peaking | 103 Hz   | 2.03 | -6.7 dB |
| Peaking | 1717 Hz  | 0.74 | 3.1 dB  |
| Peaking | 3626 Hz  | 2.6  | 10.0 dB |
| Peaking | 17176 Hz | 0.04 | -5.2 dB |
| Peaking | 19 Hz    | 1.11 | -1.3 dB |
| Peaking | 28 Hz    | 2.67 | 1.3 dB  |
| Peaking | 220 Hz   | 4.17 | 1.7 dB  |
| Peaking | 8885 Hz  | 5.75 | -3.8 dB |
| Peaking | 15099 Hz | 3.39 | 6.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT770/Beyerdynamic%20DT770.png)