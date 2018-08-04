# Aiaiai TMA-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.3; 30 4.7; 32 4.0; 35 3.0; 37 2.4; 40 1.7; 42 1.3; 45 0.8; 49 0.2; 52 -0.1; 56 -0.6; 59 -0.8; 64 -1.0; 68 -1.1; 73 -1.2; 78 -1.5; 83 -1.7; 89 -1.7; 95 -1.7; 102 -2.0; 109 -2.5; 117 -3.1; 125 -3.6; 134 -3.9; 143 -4.0; 153 -4.1; 164 -4.0; 175 -4.0; 188 -4.2; 201 -4.3; 215 -4.3; 230 -4.1; 246 -4.1; 263 -3.9; 282 -3.8; 301 -4.1; 323 -4.3; 345 -4.4; 369 -4.3; 395 -3.9; 423 -3.4; 452 -3.2; 484 -3.0; 518 -2.4; 554 -1.4; 593 -0.3; 635 1.0; 679 1.9; 726 2.6; 777 2.7; 832 1.8; 890 0.8; 952 0.1; 1019 0.1; 1090 0.5; 1167 1.1; 1248 1.8; 1336 2.0; 1429 2.3; 1529 3.0; 1636 3.7; 1751 4.6; 1873 5.7; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 4.6; 5168 4.4; 5530 5.2; 5917 4.7; 6331 2.1; 6775 1.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aiaiai TMA-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.43 | 6.5 dB  |
| Peaking | 373 Hz  | 2.14 | -3.2 dB |
| Peaking | 169 Hz  | 0.77 | -4.2 dB |
| Peaking | 2354 Hz | 0.95 | 5.7 dB  |
| Peaking | 4509 Hz | 1.63 | 4.0 dB  |
| Peaking | 14 Hz   | 1.95 | 1.4 dB  |
| Peaking | 515 Hz  | 4.32 | -1.6 dB |
| Peaking | 752 Hz  | 2.51 | 3.6 dB  |
| Peaking | 974 Hz  | 2.57 | -2.2 dB |
| Peaking | 8661 Hz | 3.12 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aiaiai%20TMA-1/Aiaiai%20TMA-1.png)