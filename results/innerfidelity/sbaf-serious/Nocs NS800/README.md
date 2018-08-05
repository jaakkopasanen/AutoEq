# Nocs NS800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.8; 22 0.7; 23 0.7; 25 0.6; 26 0.6; 28 0.6; 30 0.5; 32 0.5; 35 0.5; 37 0.5; 40 0.5; 42 0.5; 45 0.5; 49 0.6; 52 0.6; 56 0.6; 59 0.5; 64 0.5; 68 0.5; 73 0.4; 78 0.3; 83 0.0; 89 -0.3; 95 -0.6; 102 -1.2; 109 -1.7; 117 -2.1; 125 -2.7; 134 -3.1; 143 -3.4; 153 -3.5; 164 -3.6; 175 -3.5; 188 -3.6; 201 -3.5; 215 -3.4; 230 -3.2; 246 -3.1; 263 -3.0; 282 -2.8; 301 -2.6; 323 -2.5; 345 -2.3; 369 -2.1; 395 -1.9; 423 -1.6; 452 -1.3; 484 -1.2; 518 -1.1; 554 -0.7; 593 -0.3; 635 -0.1; 679 -0.0; 726 0.2; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -0.9; 1529 -1.2; 1636 -1.3; 1751 -1.2; 1873 -0.9; 2004 -0.7; 2145 -0.6; 2295 -0.5; 2455 -0.3; 2627 -0.5; 2811 -0.6; 3008 0.3; 3219 2.2; 3444 4.9; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.0; 10167 -0.4; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 77 Hz   | 0.65 | 2.2 dB  |
| Peaking | 166 Hz  | 0.67 | -4.7 dB |
| Peaking | 2787 Hz | 4.05 | -3.3 dB |
| Peaking | 1778 Hz | 2.23 | -1.9 dB |
| Peaking | 4452 Hz | 1.25 | 7.2 dB  |
| Peaking | 17 Hz   | 1.43 | 0.5 dB  |
| Peaking | 785 Hz  | 3.27 | 0.9 dB  |
| Peaking | 7793 Hz | 1.03 | -1.3 dB |
| Peaking | 6391 Hz | 3.73 | 4.1 dB  |
| Peaking | 7353 Hz | 2.68 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS800/Nocs%20NS800.png)