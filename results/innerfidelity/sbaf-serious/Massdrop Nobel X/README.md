# Massdrop Nobel X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.7; 22 -0.8; 23 -0.9; 25 -1.0; 26 -1.0; 28 -1.1; 30 -1.2; 32 -1.2; 35 -1.4; 37 -1.5; 40 -1.6; 42 -1.7; 45 -1.8; 49 -1.9; 52 -2.1; 56 -2.3; 59 -2.5; 64 -2.7; 68 -2.9; 73 -3.2; 78 -3.4; 83 -3.6; 89 -3.9; 95 -4.2; 102 -4.5; 109 -4.6; 117 -4.7; 125 -4.9; 134 -5.1; 143 -5.1; 153 -5.3; 164 -5.3; 175 -5.4; 188 -5.3; 201 -5.3; 215 -5.2; 230 -5.1; 246 -5.0; 263 -4.8; 282 -4.6; 301 -4.4; 323 -4.2; 345 -3.9; 369 -3.6; 395 -3.3; 423 -2.9; 452 -2.5; 484 -2.3; 518 -2.1; 554 -1.6; 593 -1.1; 635 -0.7; 679 -0.6; 726 -0.3; 777 0.1; 832 0.2; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.5; 1429 -0.8; 1529 -1.1; 1636 -1.3; 1751 -1.3; 1873 -1.1; 2004 -0.9; 2145 -0.7; 2295 -0.3; 2455 0.6; 2627 1.3; 2811 2.2; 3008 3.6; 3219 4.9; 3444 6.0; 3685 6.0; 3943 5.2; 4219 3.1; 4514 1.0; 4830 0.5; 5168 1.6; 5530 2.9; 5917 4.1; 6331 4.3; 6775 3.7; 7249 1.3; 7756 -1.0; 8299 -3.9; 8880 -4.8; 9502 -4.0; 10167 -1.9; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999529967255dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Nobel X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 134 Hz   | 0.52 | -4.5 dB |
| Peaking | 284 Hz   | 1.04 | -2.1 dB |
| Peaking | 3528 Hz  | 3.55 | 6.6 dB  |
| Peaking | 6386 Hz  | 3.6  | 5.2 dB  |
| Peaking | 8811 Hz  | 3.7  | -6.0 dB |
| Peaking | 862 Hz   | 2.3  | 1.0 dB  |
| Peaking | 1920 Hz  | 1.49 | -2.4 dB |
| Peaking | 2606 Hz  | 0.97 | 1.2 dB  |
| Peaking | 4722 Hz  | 9.69 | -1.8 dB |
| Peaking | 11047 Hz | 8.52 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20Nobel%20X/Massdrop%20Nobel%20X.png)