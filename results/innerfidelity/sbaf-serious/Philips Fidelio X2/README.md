# Philips Fidelio X2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.4; 22 3.5; 23 3.0; 25 2.1; 26 1.7; 28 1.0; 30 0.3; 32 -0.4; 35 -1.2; 37 -1.8; 40 -2.4; 42 -2.8; 45 -3.4; 49 -3.9; 52 -4.2; 56 -4.6; 59 -4.7; 64 -4.9; 68 -5.1; 73 -5.2; 78 -5.3; 83 -5.3; 89 -5.2; 95 -5.1; 102 -4.8; 109 -4.5; 117 -4.1; 125 -3.8; 134 -3.6; 143 -3.5; 153 -3.4; 164 -3.1; 175 -2.6; 188 -2.6; 201 -2.9; 215 -3.7; 230 -4.0; 246 -3.4; 263 -3.0; 282 -2.7; 301 -2.6; 323 -2.4; 345 -2.3; 369 -2.3; 395 -2.3; 423 -2.1; 452 -2.1; 484 -2.3; 518 -2.4; 554 -2.2; 593 -2.1; 635 -2.2; 679 -2.3; 726 -2.2; 777 -1.8; 832 -1.7; 890 -1.0; 952 -0.3; 1019 0.1; 1090 0.6; 1167 1.4; 1248 1.2; 1336 0.3; 1429 -1.0; 1529 -2.4; 1636 -2.7; 1751 -2.7; 1873 -2.1; 2004 -1.6; 2145 -1.5; 2295 -1.6; 2455 -0.9; 2627 0.6; 2811 3.7; 3008 3.0; 3219 1.5; 3444 1.6; 3685 0.6; 3943 -0.1; 4219 -1.6; 4514 -4.2; 4830 -3.5; 5168 1.0; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.2; 8299 -4.1; 8880 -6.8; 9502 -6.0; 10167 -1.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.084225018767812dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.23 | 5.9 dB  |
| Peaking | 69 Hz   |  0.92 | -3.1 dB |
| Peaking | 130 Hz  |  0.17 | -2.8 dB |
| Peaking | 6142 Hz |  4.63 | 7.3 dB  |
| Peaking | 8998 Hz |  5.14 | -8.2 dB |
| Peaking | 1222 Hz |  2.33 | 5.8 dB  |
| Peaking | 1488 Hz |  1.12 | -4.4 dB |
| Peaking | 2931 Hz |  4.19 | 4.8 dB  |
| Peaking | 4676 Hz |  6.22 | -5.8 dB |
| Peaking | 5446 Hz | 10.58 | 4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20X2/Philips%20Fidelio%20X2.png)