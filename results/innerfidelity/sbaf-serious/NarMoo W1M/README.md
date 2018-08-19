# NarMoo W1M

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.4; 22 -5.5; 23 -5.5; 25 -5.5; 26 -5.5; 28 -5.5; 30 -5.5; 32 -5.5; 35 -5.4; 37 -5.4; 40 -5.3; 42 -5.3; 45 -5.2; 49 -5.2; 52 -5.1; 56 -5.1; 59 -5.1; 64 -5.0; 68 -5.0; 73 -5.0; 78 -5.1; 83 -5.1; 89 -5.1; 95 -5.1; 102 -5.1; 109 -5.0; 117 -4.9; 125 -4.8; 134 -4.8; 143 -4.7; 153 -4.6; 164 -4.5; 175 -4.3; 188 -4.2; 201 -4.0; 215 -3.8; 230 -3.6; 246 -3.5; 263 -3.4; 282 -3.1; 301 -3.0; 323 -2.8; 345 -2.6; 369 -2.4; 395 -2.3; 423 -2.0; 452 -1.8; 484 -1.8; 518 -1.6; 554 -1.3; 593 -1.0; 635 -0.8; 679 -0.8; 726 -0.6; 777 -0.3; 832 -0.2; 890 -0.2; 952 -0.1; 1019 0.2; 1090 0.4; 1167 0.6; 1248 0.9; 1336 1.2; 1429 1.4; 1529 1.6; 1636 1.8; 1751 2.1; 1873 2.5; 2004 2.8; 2145 2.8; 2295 2.9; 2455 3.0; 2627 3.4; 2811 4.1; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.0; 4830 3.3; 5168 4.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998715981dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo W1M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  0.43 | -4.7 dB |
| Peaking | 129 Hz  |  0.36 | -4.3 dB |
| Peaking | 3654 Hz |  0.89 | 6.3 dB  |
| Peaking | 6160 Hz |  3.37 | 5.7 dB  |
| Peaking | 6968 Hz |  1.12 | -2.7 dB |
| Peaking | 2513 Hz |  3.27 | -2.1 dB |
| Peaking | 2588 Hz |  1.22 | 1.2 dB  |
| Peaking | 4898 Hz | 10.37 | -2.2 dB |
| Peaking | 5408 Hz |  8.1  | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20W1M/NarMoo%20W1M.png)