# Master Dynamic ME05

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 10 -84; 20 -5.4; 22 -5.8; 23 -6.0; 25 -6.3; 26 -6.4; 28 -6.7; 30 -6.9; 32 -7.1; 35 -7.3; 37 -7.4; 40 -7.5; 42 -7.5; 45 -7.6; 49 -7.5; 52 -7.5; 56 -7.4; 59 -7.4; 64 -7.4; 68 -7.3; 73 -7.2; 78 -7.2; 83 -7.3; 89 -7.4; 95 -7.6; 102 -7.9; 109 -8.1; 117 -8.3; 125 -8.6; 134 -8.7; 143 -8.7; 153 -8.6; 164 -8.4; 175 -8.1; 188 -7.8; 201 -7.5; 215 -7.0; 230 -6.5; 246 -6.1; 263 -5.8; 282 -5.3; 301 -4.9; 323 -4.4; 345 -3.9; 369 -3.6; 395 -3.2; 423 -2.6; 452 -2.1; 484 -1.8; 518 -1.5; 554 -1.0; 593 -0.5; 635 -0.2; 679 -0.1; 726 0.1; 777 0.5; 832 0.5; 890 0.3; 952 0.1; 1019 -0.2; 1090 -0.5; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.6; 1529 -2.1; 1636 -2.6; 1751 -2.9; 1873 -3.0; 2004 -3.1; 2145 -3.3; 2295 -3.5; 2455 -3.4; 2627 -3.5; 2811 -3.6; 3008 -2.5; 3219 -1.3; 3444 -0.0; 3685 -0.1; 3943 -0.9; 4219 -2.9; 4514 -5.0; 4830 -5.8; 5168 -5.2; 5530 -3.5; 5917 -1.2; 6331 0.2; 6775 1.3; 7249 1.2; 7756 0.2; 8299 -0.9; 8880 -1.4; 9502 -0.7; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.9dB` and instead set Global volume in the UI for both channels to **-19**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic ME05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 4 Hz    | 1.59 | -4.7 dB |
| Peaking | 39 Hz   | 0.35 | -6.7 dB |
| Peaking | 172 Hz  | 0.77 | -6.3 dB |
| Peaking | 2226 Hz | 1.82 | -3.7 dB |
| Peaking | 4885 Hz | 4.98 | -6.2 dB |
| Peaking | 792 Hz  | 1.55 | 1.9 dB  |
| Peaking | 1437 Hz | 0.2  | -0.6 dB |
| Peaking | 3620 Hz | 6.75 | 2.2 dB  |
| Peaking | 6859 Hz | 5.05 | 2.5 dB  |
| Peaking | 8691 Hz | 6.95 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20ME05/Master%20Dynamic%20ME05.png)