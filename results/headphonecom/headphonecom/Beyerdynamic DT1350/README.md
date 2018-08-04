# Beyerdynamic DT1350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.8; 22 -5.9; 23 -5.9; 25 -6.0; 26 -6.0; 28 -6.0; 30 -6.1; 32 -6.2; 35 -6.2; 37 -6.2; 40 -6.2; 42 -6.2; 45 -6.2; 49 -6.2; 52 -6.1; 56 -5.7; 59 -5.7; 64 -6.0; 68 -6.0; 73 -6.0; 78 -6.0; 83 -5.7; 89 -5.0; 95 -4.3; 102 -3.6; 109 -3.4; 117 -3.9; 125 -3.9; 134 -3.0; 143 -2.5; 153 -2.6; 164 -2.8; 175 -4.1; 188 -4.7; 201 -5.1; 215 -5.3; 230 -5.4; 246 -5.4; 263 -5.4; 282 -4.9; 301 -4.8; 323 -5.4; 345 -5.7; 369 -5.6; 395 -5.3; 423 -5.1; 452 -5.2; 484 -5.0; 518 -4.6; 554 -4.1; 593 -3.5; 635 -3.1; 679 -2.4; 726 -1.6; 777 -1.0; 832 -1.0; 890 -0.8; 952 -0.4; 1019 0.0; 1090 0.5; 1167 1.1; 1248 1.8; 1336 2.5; 1429 3.0; 1529 3.3; 1636 3.3; 1751 3.1; 1873 3.2; 2004 4.0; 2145 5.4; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.1; 8299 -4.4; 8880 -7.2; 9502 -5.6; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT1350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.42 | -6.5 dB  |
| Peaking | 374 Hz  | 0.66 | -5.6 dB  |
| Peaking | 2939 Hz | 0.58 | 6.1 dB   |
| Peaking | 5936 Hz | 1.91 | 3.5 dB   |
| Peaking | 8859 Hz | 4.13 | -10.1 dB |
| Peaking | 79 Hz   | 4.77 | -1.2 dB  |
| Peaking | 157 Hz  | 2.62 | 1.8 dB   |
| Peaking | 196 Hz  | 3.2  | -1.7 dB  |
| Peaking | 1857 Hz | 2.25 | 1.5 dB   |
| Peaking | 1868 Hz | 4.96 | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Beyerdynamic%20DT1350/Beyerdynamic%20DT1350.png)