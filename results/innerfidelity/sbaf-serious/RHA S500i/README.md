# RHA S500i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 10 -84; 20 4.4; 22 3.8; 23 3.5; 25 3.1; 26 2.9; 28 2.6; 30 2.4; 32 2.2; 35 1.9; 37 1.7; 40 1.5; 42 1.4; 45 1.1; 49 0.9; 52 0.7; 56 0.4; 59 0.2; 64 -0.1; 68 -0.4; 73 -0.6; 78 -0.8; 83 -1.2; 89 -1.4; 95 -1.7; 102 -1.9; 109 -1.9; 117 -2.1; 125 -2.1; 134 -2.1; 143 -2.5; 153 -2.5; 164 -2.5; 175 -2.4; 188 -2.3; 201 -2.3; 215 -2.2; 230 -2.0; 246 -1.9; 263 -1.8; 282 -1.6; 301 -1.4; 323 -1.3; 345 -1.0; 369 -0.8; 395 -0.6; 423 -0.3; 452 -0.1; 484 -0.0; 518 0.1; 554 0.4; 593 0.8; 635 0.9; 679 0.8; 726 0.8; 777 1.0; 832 0.8; 890 0.6; 952 0.3; 1019 -0.2; 1090 -0.7; 1167 -1.2; 1248 -1.6; 1336 -2.2; 1429 -2.9; 1529 -3.6; 1636 -4.3; 1751 -4.7; 1873 -5.1; 2004 -5.5; 2145 -6.3; 2295 -7.2; 2455 -8.1; 2627 -9.6; 2811 -10.6; 3008 -8.6; 3219 -5.3; 3444 -2.0; 3685 -0.1; 3943 0.7; 4219 -0.0; 4514 -0.6; 4830 -0.4; 5168 0.3; 5530 0.2; 5917 -0.5; 6331 -2.6; 6775 -5.1; 7249 -6.6; 7756 -6.1; 8299 -4.7; 8880 -2.8; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 -0.0; 12455 -1.6; 13327 -3.5; 14260 -3.9; 15258 -2.2; 16326 -0.1; 17469 0.0; 18692 -0.0; 20000 -3.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.505463620427271dB` and instead set Global volume in the UI for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA S500i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.61 | 4.6 dB  |
| Peaking | 152 Hz   | 0.84 | -2.7 dB |
| Peaking | 2536 Hz  | 1.92 | -9.7 dB |
| Peaking | 13904 Hz | 2.14 | -3.6 dB |
| Peaking | 20152 Hz | 3.14 | -2.5 dB |
| Peaking | 736 Hz   | 2.09 | 1.2 dB  |
| Peaking | 1629 Hz  | 1.82 | -3.8 dB |
| Peaking | 2917 Hz  | 5.99 | -5.5 dB |
| Peaking | 4359 Hz  | 0.37 | 3.8 dB  |
| Peaking | 7408 Hz  | 2.46 | -9.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20S500i/RHA%20S500i.png)