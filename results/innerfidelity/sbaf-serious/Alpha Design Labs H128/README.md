# Alpha Design Labs H128

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.6; 22 0.0; 23 -0.2; 25 -0.7; 26 -1.0; 28 -1.4; 30 -1.7; 32 -2.0; 35 -2.4; 37 -2.5; 40 -2.8; 42 -2.9; 45 -3.1; 49 -3.2; 52 -3.3; 56 -3.3; 59 -3.4; 64 -3.4; 68 -3.4; 73 -3.5; 78 -3.7; 83 -3.8; 89 -3.9; 95 -4.1; 102 -4.2; 109 -4.2; 117 -4.3; 125 -4.4; 134 -4.7; 143 -5.2; 153 -5.4; 164 -5.2; 175 -4.7; 188 -4.6; 201 -4.4; 215 -4.2; 230 -4.1; 246 -3.8; 263 -3.6; 282 -3.2; 301 -3.0; 323 -2.8; 345 -2.5; 369 -2.3; 395 -2.1; 423 -2.0; 452 -2.0; 484 -2.0; 518 -2.1; 554 -1.9; 593 -1.6; 635 -1.6; 679 -1.6; 726 -1.6; 777 -1.4; 832 -1.2; 890 -0.7; 952 0.0; 1019 -0.1; 1090 -0.7; 1167 -0.6; 1248 -0.3; 1336 -0.3; 1429 -0.2; 1529 -0.1; 1636 -0.1; 1751 0.2; 1873 0.5; 2004 0.9; 2145 0.8; 2295 0.7; 2455 1.5; 2627 2.2; 2811 2.9; 3008 3.3; 3219 3.7; 3444 4.9; 3685 5.9; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.3; 9502 -0.5; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Alpha Design Labs H128 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.2  | 2.3 dB  |
| Peaking | 47 Hz   | 0.52 | -2.8 dB |
| Peaking | 165 Hz  | 0.79 | -4.1 dB |
| Peaking | 565 Hz  | 0.61 | -1.2 dB |
| Peaking | 4517 Hz | 1.28 | 6.9 dB  |
| Peaking | 1647 Hz | 3.82 | -0.3 dB |
| Peaking | 3664 Hz | 2.83 | 1.1 dB  |
| Peaking | 4470 Hz | 3.44 | -1.4 dB |
| Peaking | 6350 Hz | 3.2  | 4.0 dB  |
| Peaking | 7579 Hz | 1.55 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Alpha%20Design%20Labs%20H128/Alpha%20Design%20Labs%20H128.png)