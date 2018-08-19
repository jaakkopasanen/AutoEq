# Philips Fidelio L1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 -5.7; 22 -6.1; 23 -6.3; 25 -6.6; 26 -6.7; 28 -6.9; 30 -7.1; 32 -7.3; 35 -7.5; 37 -7.6; 40 -7.8; 42 -7.8; 45 -7.9; 49 -7.9; 52 -8.0; 56 -8.0; 59 -8.0; 64 -8.1; 68 -8.1; 73 -8.1; 78 -8.1; 83 -8.1; 89 -8.1; 95 -8.0; 102 -7.9; 109 -7.7; 117 -7.7; 125 -7.9; 134 -8.1; 143 -8.0; 153 -7.9; 164 -7.5; 175 -6.8; 188 -6.6; 201 -6.6; 215 -6.7; 230 -6.5; 246 -6.5; 263 -6.4; 282 -6.0; 301 -5.7; 323 -5.4; 345 -4.9; 369 -4.5; 395 -4.0; 423 -3.4; 452 -3.2; 484 -2.9; 518 -2.3; 554 -1.8; 593 -1.2; 635 -0.7; 679 -0.4; 726 -0.1; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.0; 1167 -0.4; 1248 -0.9; 1336 -2.2; 1429 -3.7; 1529 -5.2; 1636 -6.6; 1751 -7.4; 1873 -7.6; 2004 -7.5; 2145 -7.5; 2295 -8.5; 2455 -8.1; 2627 -7.4; 2811 -6.8; 3008 -5.4; 3219 -3.6; 3444 -1.9; 3685 -1.2; 3943 -0.3; 4219 0.6; 4514 1.8; 4830 3.2; 5168 4.7; 5530 5.0; 5917 4.6; 6331 3.4; 6775 -0.2; 7249 -3.1; 7756 -4.0; 8299 -4.2; 8880 -2.5; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.2; 18692 -0.5; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.1617556767928265dB` and instead set Global volume in the UI for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio L1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.36 | -7.6 dB |
| Peaking | 147 Hz  | 0.94 | -3.9 dB |
| Peaking | 298 Hz  | 1.56 | -3.6 dB |
| Peaking | 2237 Hz | 1.53 | -9.0 dB |
| Peaking | 5318 Hz | 3.8  | 6.8 dB  |
| Peaking | 1023 Hz | 1.63 | 2.0 dB  |
| Peaking | 1627 Hz | 4.89 | -2.8 dB |
| Peaking | 6292 Hz | 7.14 | 3.3 dB  |
| Peaking | 7823 Hz | 2.53 | -7.1 dB |
| Peaking | 8073 Hz | 1.03 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20L1/Philips%20Fidelio%20L1.png)