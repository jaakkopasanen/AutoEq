# Monster Jamz

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 -8.3; 22 -8.3; 23 -8.2; 25 -8.1; 26 -8.1; 28 -7.9; 30 -7.8; 32 -7.7; 35 -7.5; 37 -7.3; 40 -7.1; 42 -7.0; 45 -6.8; 49 -6.5; 52 -6.3; 56 -6.1; 59 -5.9; 64 -5.6; 68 -5.4; 73 -5.2; 78 -5.0; 83 -5.0; 89 -5.0; 95 -5.1; 102 -5.3; 109 -5.5; 117 -5.7; 125 -5.9; 134 -5.9; 143 -6.1; 153 -5.9; 164 -5.7; 175 -5.4; 188 -5.1; 201 -4.8; 215 -4.3; 230 -4.1; 246 -3.6; 263 -3.4; 282 -3.0; 301 -2.6; 323 -2.3; 345 -1.9; 369 -1.6; 395 -1.3; 423 -0.9; 452 -0.6; 484 -0.4; 518 -0.2; 554 0.2; 593 0.6; 635 0.8; 679 0.8; 726 0.9; 777 1.1; 832 0.9; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -1.1; 1248 -1.2; 1336 -1.0; 1429 -2.0; 1529 -2.8; 1636 -3.4; 1751 -4.0; 1873 -4.4; 2004 -4.8; 2145 -5.3; 2295 -5.0; 2455 -4.7; 2627 -4.4; 2811 -3.1; 3008 -0.5; 3219 1.6; 3444 3.2; 3685 3.6; 3943 2.9; 4219 0.9; 4514 -0.7; 4830 -1.6; 5168 -1.3; 5530 -0.3; 5917 1.8; 6331 3.6; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.6; 15258 -1.8; 16326 -0.1; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.9dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.61 | -7.5 dB |
| Peaking | 35 Hz    | 0.44 | -5.6 dB |
| Peaking | 161 Hz   | 1    | -4.7 dB |
| Peaking | 2227 Hz  | 1.78 | -6.0 dB |
| Peaking | 3558 Hz  | 3.91 | 5.5 dB  |
| Peaking | 742 Hz   | 2.06 | 1.7 dB  |
| Peaking | 1608 Hz  | 5.16 | -1.1 dB |
| Peaking | 4966 Hz  | 5.46 | -2.4 dB |
| Peaking | 6502 Hz  | 5.62 | 4.7 dB  |
| Peaking | 15085 Hz | 6.85 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Jamz/Monster%20Jamz.png)