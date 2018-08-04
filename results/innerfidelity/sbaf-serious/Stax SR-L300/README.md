# Stax SR-L300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.4; 49 4.6; 52 4.1; 56 3.6; 59 3.3; 64 2.9; 68 2.7; 73 2.5; 78 2.3; 83 2.1; 89 1.9; 95 1.7; 102 1.2; 109 1.1; 117 1.1; 125 0.8; 134 0.7; 143 0.7; 153 0.7; 164 0.8; 175 0.9; 188 0.9; 201 1.0; 215 1.2; 230 1.3; 246 1.3; 263 1.5; 282 1.6; 301 1.6; 323 1.7; 345 1.7; 369 1.7; 395 1.8; 423 1.8; 452 1.8; 484 1.6; 518 1.5; 554 1.6; 593 1.9; 635 1.8; 679 1.4; 726 1.2; 777 1.2; 832 0.8; 890 0.3; 952 -0.1; 1019 0.2; 1090 0.3; 1167 -0.2; 1248 -1.0; 1336 -1.4; 1429 -0.6; 1529 0.2; 1636 1.5; 1751 2.4; 1873 3.0; 2004 2.8; 2145 2.1; 2295 1.4; 2455 0.9; 2627 0.6; 2811 1.0; 3008 2.1; 3219 2.5; 3444 3.0; 3685 2.6; 3943 2.1; 4219 1.0; 4514 0.6; 4830 0.4; 5168 1.5; 5530 1.5; 5917 0.3; 6331 0.2; 6775 0.5; 7249 0.6; 7756 -0.3; 8299 -2.4; 8880 -3.7; 9502 -2.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.7; 20000 -3.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.63 | 6.5 dB  |
| Peaking | 407 Hz  | 0.97 | 1.8 dB  |
| Peaking | 3151 Hz | 1.01 | 2.1 dB  |
| Peaking | 8867 Hz | 2.03 | 1.4 dB  |
| Peaking | 8837 Hz | 4.63 | -5.7 dB |
| Peaking | 641 Hz  | 5.05 | 0.8 dB  |
| Peaking | 1351 Hz | 3.72 | -2.3 dB |
| Peaking | 1910 Hz | 2.57 | 3.5 dB  |
| Peaking | 2625 Hz | 1.39 | -2.5 dB |
| Peaking | 3376 Hz | 3.49 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-L300/Stax%20SR-L300.png)