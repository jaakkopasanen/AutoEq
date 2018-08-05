# Philips TX2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 10 -84; 20 -6.5; 22 -6.4; 23 -6.4; 25 -6.4; 26 -6.4; 28 -6.3; 30 -6.3; 32 -6.2; 35 -6.1; 37 -6.1; 40 -6.0; 42 -5.9; 45 -5.8; 49 -5.7; 52 -5.6; 56 -5.5; 59 -5.4; 64 -5.2; 68 -5.2; 73 -5.1; 78 -5.1; 83 -5.1; 89 -5.3; 95 -5.5; 102 -5.8; 109 -6.0; 117 -6.3; 125 -6.6; 134 -6.8; 143 -6.8; 153 -6.7; 164 -6.6; 175 -6.3; 188 -6.0; 201 -5.7; 215 -5.3; 230 -4.9; 246 -4.6; 263 -4.2; 282 -3.8; 301 -3.4; 323 -3.0; 345 -2.6; 369 -2.3; 395 -2.0; 423 -1.5; 452 -1.2; 484 -0.5; 518 -0.5; 554 -0.1; 593 0.3; 635 0.5; 679 0.6; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -1.0; 1336 -1.5; 1429 -2.1; 1529 -2.6; 1636 -3.2; 1751 -3.6; 1873 -3.8; 2004 -4.1; 2145 -4.3; 2295 -4.0; 2455 -3.0; 2627 -1.8; 2811 -0.5; 3008 1.2; 3219 2.5; 3444 3.5; 3685 3.4; 3943 2.6; 4219 0.6; 4514 -1.2; 4830 -2.4; 5168 -3.3; 5530 -3.7; 5917 -4.0; 6331 -3.6; 6775 -2.0; 7249 -1.0; 7756 -0.8; 8299 -1.3; 8880 -1.6; 9502 -1.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.1dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips TX2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 8 Hz    | 0.85 | -5.9 dB |
| Peaking | 29 Hz   | 0.35 | -5.4 dB |
| Peaking | 164 Hz  | 0.88 | -5.6 dB |
| Peaking | 1958 Hz | 2.9  | -4.7 dB |
| Peaking | 5890 Hz | 3.94 | -4.5 dB |
| Peaking | 734 Hz  | 1.27 | 2.6 dB  |
| Peaking | 2559 Hz | 3.8  | -2.8 dB |
| Peaking | 1885 Hz | 0.2  | -1.5 dB |
| Peaking | 3623 Hz | 1.42 | 6.4 dB  |
| Peaking | 4692 Hz | 3.43 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20TX2/Philips%20TX2.png)