# Beyerdynamic DT 770

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -1.0; 22 -1.6; 23 -1.8; 25 -2.3; 26 -2.5; 28 -2.9; 30 -3.2; 32 -3.5; 35 -3.8; 37 -3.9; 40 -4.1; 42 -4.2; 45 -4.3; 49 -4.3; 52 -4.1; 56 -3.8; 59 -3.3; 64 -1.9; 68 -0.5; 73 1.5; 78 1.8; 83 0.2; 89 -2.3; 95 -4.1; 102 -5.3; 109 -5.5; 117 -5.6; 125 -5.5; 134 -5.1; 143 -4.5; 153 -3.2; 164 -2.3; 175 -2.3; 188 -1.3; 201 -0.8; 215 -0.5; 230 -0.5; 246 -1.0; 263 -1.3; 282 -1.6; 301 -1.8; 323 -2.0; 345 -2.0; 369 -2.0; 395 -2.0; 423 -1.8; 452 -1.7; 484 -1.7; 518 -1.6; 554 -1.3; 593 -0.8; 635 -0.6; 679 -0.6; 726 -0.4; 777 -0.2; 832 -0.1; 890 -0.1; 952 -0.1; 1019 0.1; 1090 0.2; 1167 0.2; 1248 -0.0; 1336 -0.4; 1429 -0.8; 1529 -1.1; 1636 -1.5; 1751 -1.9; 1873 -1.8; 2004 -1.3; 2145 -1.4; 2295 -2.0; 2455 -1.9; 2627 -1.3; 2811 -0.4; 3008 0.8; 3219 1.9; 3444 3.3; 3685 4.5; 3943 4.5; 4219 3.9; 4514 5.6; 4830 4.7; 5168 -3.1; 5530 -7.2; 5917 -7.1; 6331 -7.6; 6775 -6.5; 7249 -5.8; 7756 -7.5; 8299 -9.6; 8880 -10.2; 9502 -7.9; 10167 -3.8; 10879 -1.0; 11640 -1.6; 12455 -4.2; 13327 -5.7; 14260 -4.7; 15258 -3.0; 16326 -3.7; 17469 -6.6; 18692 -8.3; 20000 -6.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 121 Hz   | 1.55 | -5.6 dB  |
| Peaking | 4603 Hz  | 1.7  | 22.9 dB  |
| Peaking | 8737 Hz  | 5.88 | -6.5 dB  |
| Peaking | 5440 Hz  | 1.05 | -20.4 dB |
| Peaking | 29123 Hz | 1.23 | -8.1 dB  |
| Peaking | 42 Hz    | 1.07 | -4.4 dB  |
| Peaking | 76 Hz    | 4.71 | 5.7 dB   |
| Peaking | 404 Hz   | 2.06 | -1.8 dB  |
| Peaking | 3587 Hz  | 7.82 | 2.8 dB   |
| Peaking | 36929 Hz | 8.89 | 3.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20770/Beyerdynamic%20DT%20770.png)