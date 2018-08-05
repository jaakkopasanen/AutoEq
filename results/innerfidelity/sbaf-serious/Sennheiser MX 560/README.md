# Sennheiser MX 560

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.7; 95 5.0; 102 4.6; 109 4.2; 117 3.9; 125 3.6; 134 3.3; 143 3.2; 153 3.0; 164 2.8; 175 2.7; 188 2.7; 201 2.5; 215 2.5; 230 2.4; 246 2.3; 263 2.2; 282 2.3; 301 2.3; 323 2.6; 345 1.9; 369 1.3; 395 1.5; 423 1.7; 452 1.8; 484 2.1; 518 2.1; 554 2.0; 593 1.9; 635 1.7; 679 1.4; 726 1.2; 777 1.2; 832 0.9; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.3; 1336 -2.2; 1429 -3.2; 1529 -4.5; 1636 -5.7; 1751 -7.2; 1873 -8.6; 2004 -9.9; 2145 -11.1; 2295 -12.0; 2455 -12.1; 2627 -12.3; 2811 -11.9; 3008 -10.3; 3219 -8.5; 3444 -6.9; 3685 -6.1; 3943 -6.3; 4219 -7.7; 4514 -8.8; 4830 -9.5; 5168 -9.9; 5530 -10.7; 5917 -10.3; 6331 -9.1; 6775 -7.7; 7249 -7.2; 7756 -7.6; 8299 -7.4; 8880 -5.3; 9502 -1.8; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.8; 14260 -3.7; 15258 -3.1; 16326 -0.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 560 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.3  | 6.4 dB   |
| Peaking | 734 Hz   | 0.55 | 2.3 dB   |
| Peaking | 2358 Hz  | 1.34 | -12.4 dB |
| Peaking | 5926 Hz  | 1.44 | -9.1 dB  |
| Peaking | 33345 Hz | 6.77 | -3.9 dB  |
| Peaking | 2929 Hz  | 4.95 | -2.3 dB  |
| Peaking | 4035 Hz  | 1.63 | 2.7 dB   |
| Peaking | 4523 Hz  | 3.39 | -3.2 dB  |
| Peaking | 8483 Hz  | 4.43 | -5.2 dB  |
| Peaking | 9845 Hz  | 1.86 | 3.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20MX%20560/Sennheiser%20MX%20560.png)