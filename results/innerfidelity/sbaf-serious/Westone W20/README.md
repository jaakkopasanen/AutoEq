# Westone W20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.2; 22 2.1; 23 2.0; 25 1.9; 26 1.8; 28 1.7; 30 1.6; 32 1.5; 35 1.3; 37 1.2; 40 1.1; 42 1.0; 45 0.8; 49 0.6; 52 0.5; 56 0.3; 59 0.1; 64 -0.2; 68 -0.4; 73 -0.7; 78 -1.0; 83 -1.3; 89 -1.6; 95 -1.9; 102 -2.1; 109 -2.3; 117 -2.5; 125 -2.7; 134 -3.0; 143 -3.1; 153 -3.1; 164 -3.3; 175 -3.4; 188 -3.4; 201 -3.5; 215 -3.5; 230 -3.4; 246 -3.4; 263 -3.3; 282 -3.2; 301 -3.1; 323 -2.9; 345 -2.7; 369 -2.6; 395 -2.4; 423 -2.1; 452 -1.8; 484 -1.7; 518 -1.5; 554 -1.0; 593 -0.6; 635 -0.3; 679 -0.3; 726 -0.0; 777 0.3; 832 0.3; 890 0.3; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -1.1; 1529 -1.4; 1636 -1.7; 1751 -1.8; 1873 -1.8; 2004 -1.6; 2145 -1.5; 2295 -1.0; 2455 0.4; 2627 1.9; 2811 3.9; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.2; 5168 4.2; 5530 5.2; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999990280935dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.52 | 2.2 dB  |
| Peaking | 192 Hz  | 0.6  | -3.8 dB |
| Peaking | 2074 Hz | 1.78 | -4.5 dB |
| Peaking | 3491 Hz | 1.26 | 7.5 dB  |
| Peaking | 6041 Hz | 4.67 | 4.3 dB  |
| Peaking | 814 Hz  | 3.05 | 0.9 dB  |
| Peaking | 1539 Hz | 5.7  | -0.7 dB |
| Peaking | 3712 Hz | 4.62 | -2.1 dB |
| Peaking | 4016 Hz | 1.95 | 1.5 dB  |
| Peaking | 8449 Hz | 2.46 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W20/Westone%20W20.png)