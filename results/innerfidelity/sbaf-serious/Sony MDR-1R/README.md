# Sony MDR-1R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.5; 35 4.8; 37 4.4; 40 3.8; 42 3.5; 45 3.0; 49 2.4; 52 2.0; 56 1.6; 59 1.3; 64 0.9; 68 0.5; 73 -0.0; 78 -0.5; 83 -0.9; 89 -1.2; 95 -1.4; 102 -1.5; 109 -1.8; 117 -1.6; 125 -1.2; 134 -0.8; 143 -0.7; 153 -1.3; 164 -1.4; 175 0.3; 188 -0.5; 201 -1.0; 215 -1.2; 230 -1.2; 246 -0.8; 263 -0.6; 282 -0.3; 301 0.5; 323 1.3; 345 2.2; 369 3.0; 395 3.5; 423 3.9; 452 4.0; 484 3.7; 518 3.5; 554 3.4; 593 3.2; 635 2.7; 679 2.0; 726 2.0; 777 2.0; 832 1.4; 890 0.9; 952 0.4; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.8; 1429 -2.4; 1529 -3.1; 1636 -3.5; 1751 -3.4; 1873 -2.9; 2004 -2.3; 2145 -1.1; 2295 0.2; 2455 2.1; 2627 3.6; 2811 5.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.65 | 7.3 dB  |
| Peaking | 119 Hz  |  0.26 | -2.5 dB |
| Peaking | 470 Hz  |  1.11 | 5.4 dB  |
| Peaking | 1763 Hz |  1.64 | -6.3 dB |
| Peaking | 3746 Hz |  0.88 | 7.6 dB  |
| Peaking | 179 Hz  | 11.97 | 1.6 dB  |
| Peaking | 2974 Hz |  3.88 | 2.2 dB  |
| Peaking | 3449 Hz |  1.49 | -1.5 dB |
| Peaking | 6203 Hz |  2.24 | 5.7 dB  |
| Peaking | 7429 Hz |  1.53 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1R/Sony%20MDR-1R.png)