# Sony MDR-V600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.4; 49 4.5; 52 3.9; 56 3.3; 59 2.9; 64 2.4; 68 2.3; 73 1.8; 78 1.0; 83 0.4; 89 -0.2; 95 -0.4; 102 -0.3; 109 0.2; 117 0.0; 125 -1.1; 134 -1.9; 143 -2.8; 153 -3.3; 164 -3.0; 175 -2.9; 188 -3.0; 201 -3.5; 215 -3.8; 230 -3.9; 246 -4.0; 263 -4.0; 282 -3.8; 301 -3.6; 323 -3.4; 345 -3.2; 369 -3.0; 395 -3.2; 423 -3.5; 452 -3.6; 484 -2.9; 518 -2.5; 554 -2.5; 593 -1.9; 635 -0.8; 679 -1.0; 726 -1.4; 777 -1.1; 832 -0.9; 890 -0.8; 952 -0.4; 1019 0.2; 1090 0.7; 1167 1.3; 1248 1.9; 1336 2.2; 1429 2.0; 1529 1.4; 1636 1.0; 1751 1.1; 1873 1.7; 2004 2.7; 2145 3.8; 2295 4.7; 2455 5.4; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.3; 3685 4.4; 3943 4.1; 4219 2.1; 4514 2.5; 4830 4.2; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -2.0; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.64 | 6.7 dB  |
| Peaking | 218 Hz  | 0.72 | -4.1 dB |
| Peaking | 467 Hz  | 2.06 | -1.8 dB |
| Peaking | 2828 Hz | 1.45 | 6.2 dB  |
| Peaking | 5762 Hz | 3.5  | 5.8 dB  |
| Peaking | 48 Hz   | 3.49 | 0.5 dB  |
| Peaking | 905 Hz  | 2.51 | -1.1 dB |
| Peaking | 1366 Hz | 1.73 | 2.3 dB  |
| Peaking | 1684 Hz | 3.33 | -2.2 dB |
| Peaking | 9409 Hz | 5.35 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-V600/Sony%20MDR-V600.png)