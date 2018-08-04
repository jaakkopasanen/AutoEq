# JPS Labs Abyss AB-1266

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.7; 30 5.6; 32 5.6; 35 5.8; 37 6.0; 40 6.0; 42 5.8; 45 5.4; 49 5.2; 52 5.4; 56 5.8; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 5.8; 117 5.5; 125 5.1; 134 4.9; 143 4.7; 153 4.5; 164 4.4; 175 4.4; 188 4.3; 201 4.2; 215 4.2; 230 4.2; 246 4.0; 263 3.9; 282 3.8; 301 3.5; 323 3.2; 345 3.1; 369 3.2; 395 2.8; 423 2.2; 452 2.7; 484 5.7; 518 5.6; 554 5.4; 593 5.0; 635 3.9; 679 3.1; 726 2.4; 777 1.9; 832 0.9; 890 0.1; 952 -0.1; 1019 0.4; 1090 1.4; 1167 1.0; 1248 1.9; 1336 2.5; 1429 2.7; 1529 3.3; 1636 3.9; 1751 5.7; 1873 6.0; 2004 6.0; 2145 5.9; 2295 5.8; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 4.1; 6775 2.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.6; 9502 -0.6; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.0; 18692 -2.0; 20000 -1.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JPS Labs Abyss AB-1266 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.65 | 4.6 dB  |
| Peaking | 90 Hz   | 0.34 | 5.5 dB  |
| Peaking | 539 Hz  | 3.78 | 4.5 dB  |
| Peaking | 3788 Hz | 0.53 | 7.0 dB  |
| Peaking | 8843 Hz | 1.53 | -3.6 dB |
| Peaking | 743 Hz  | 2.03 | 1.7 dB  |
| Peaking | 909 Hz  | 2.38 | -2.8 dB |
| Peaking | 1923 Hz | 2.71 | 2.6 dB  |
| Peaking | 3183 Hz | 0.39 | -0.8 dB |
| Peaking | 5764 Hz | 4.89 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JPS%20Labs%20Abyss%20AB-1266/JPS%20Labs%20Abyss%20AB-1266.png)