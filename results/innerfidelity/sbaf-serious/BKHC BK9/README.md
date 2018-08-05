# BKHC BK9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 4.2; 22 3.7; 23 3.4; 25 3.0; 26 2.8; 28 2.5; 30 2.3; 32 2.1; 35 1.9; 37 1.7; 40 1.6; 42 1.5; 45 1.4; 49 1.2; 52 1.2; 56 1.2; 59 1.2; 64 1.1; 68 1.1; 73 1.1; 78 1.0; 83 0.9; 89 1.0; 95 1.0; 102 0.3; 109 -0.0; 117 -0.1; 125 0.4; 134 0.3; 143 0.0; 153 -0.1; 164 -0.4; 175 -0.2; 188 -0.3; 201 -0.4; 215 -0.9; 230 -1.1; 246 -1.3; 263 -1.5; 282 -1.4; 301 -1.4; 323 -1.6; 345 -1.8; 369 -2.0; 395 -2.3; 423 -2.4; 452 -2.6; 484 -2.9; 518 -3.2; 554 -3.1; 593 -3.0; 635 -3.1; 679 -3.1; 726 -2.7; 777 -2.0; 832 -1.0; 890 -0.4; 952 -0.2; 1019 0.3; 1090 1.2; 1167 2.3; 1248 3.3; 1336 4.2; 1429 4.9; 1529 5.6; 1636 6.0; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BKHC BK9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.68 | 4.8 dB  |
| Peaking | 77 Hz   | 1.31 | 0.8 dB  |
| Peaking | 677 Hz  | 0.7  | -5.4 dB |
| Peaking | 1844 Hz | 0.61 | 7.6 dB  |
| Peaking | 5100 Hz | 1.83 | 4.4 dB  |
| Peaking | 2236 Hz | 2.73 | -1.0 dB |
| Peaking | 3935 Hz | 0.84 | 1.2 dB  |
| Peaking | 4833 Hz | 3.92 | -1.2 dB |
| Peaking | 6358 Hz | 4.01 | 3.7 dB  |
| Peaking | 7358 Hz | 1.42 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/BKHC%20BK9/BKHC%20BK9.png)