# Monster Beats Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.1; 22 1.2; 23 0.8; 25 0.1; 26 -0.3; 28 -0.9; 30 -1.4; 32 -1.9; 35 -2.6; 37 -3.0; 40 -3.6; 42 -3.9; 45 -4.3; 49 -4.6; 52 -4.8; 56 -5.1; 59 -5.1; 64 -5.2; 68 -5.3; 73 -5.3; 78 -5.5; 83 -5.5; 89 -5.8; 95 -6.0; 102 -6.1; 109 -6.2; 117 -6.3; 125 -6.4; 134 -6.5; 143 -6.7; 153 -6.7; 164 -6.7; 175 -6.5; 188 -6.4; 201 -6.4; 215 -6.3; 230 -6.2; 246 -6.0; 263 -5.7; 282 -5.4; 301 -5.1; 323 -4.8; 345 -4.2; 369 -3.7; 395 -3.5; 423 -3.6; 452 -3.3; 484 -3.3; 518 -3.3; 554 -3.0; 593 -2.6; 635 -2.4; 679 -2.4; 726 -2.2; 777 -1.8; 832 -1.5; 890 -0.9; 952 -0.3; 1019 0.0; 1090 -0.1; 1167 0.0; 1248 0.1; 1336 0.3; 1429 0.1; 1529 -0.5; 1636 -1.3; 1751 -2.2; 1873 -3.1; 2004 -4.1; 2145 -5.3; 2295 -6.6; 2455 -7.5; 2627 -7.8; 2811 -7.9; 3008 -6.7; 3219 -5.5; 3444 -4.0; 3685 -2.5; 3943 -1.6; 4219 -3.1; 4514 -4.6; 4830 -4.1; 5168 -0.8; 5530 3.2; 5917 5.9; 6331 2.9; 6775 0.5; 7249 -0.1; 7756 -0.4; 8299 -1.4; 8880 -3.5; 9502 -5.0; 10167 -4.2; 10879 -1.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.062282316564842dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 1.28 | -2.7 dB |
| Peaking | 169 Hz  | 0.47 | -6.6 dB |
| Peaking | 2704 Hz | 1.9  | -8.1 dB |
| Peaking | 5927 Hz | 8.28 | 7.6 dB  |
| Peaking | 9597 Hz | 4.69 | -5.4 dB |
| Peaking | 20 Hz   | 2.58 | 2.7 dB  |
| Peaking | 1329 Hz | 2.46 | 1.8 dB  |
| Peaking | 2169 Hz | 3.15 | -1.2 dB |
| Peaking | 4592 Hz | 1.81 | 2.5 dB  |
| Peaking | 4624 Hz | 5.1  | -6.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Pro/Monster%20Beats%20Pro.png)