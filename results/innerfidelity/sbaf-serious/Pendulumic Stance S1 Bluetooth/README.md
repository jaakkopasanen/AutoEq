# Pendulumic Stance S1 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.6; 45 4.8; 49 3.5; 52 2.6; 56 1.6; 59 0.9; 64 -0.1; 68 -0.8; 73 -1.5; 78 -2.0; 83 -2.5; 89 -3.0; 95 -3.4; 102 -3.7; 109 -3.7; 117 -3.7; 125 -3.8; 134 -3.8; 143 -3.8; 153 -3.7; 164 -3.6; 175 -3.3; 188 -3.2; 201 -3.2; 215 -3.1; 230 -3.0; 246 -2.9; 263 -2.8; 282 -2.7; 301 -2.6; 323 -2.9; 345 -2.7; 369 -2.5; 395 -2.3; 423 -2.1; 452 -1.6; 484 -1.2; 518 -0.6; 554 0.1; 593 0.7; 635 0.9; 679 0.7; 726 0.5; 777 -0.0; 832 -0.6; 890 -0.5; 952 0.0; 1019 -0.1; 1090 -0.2; 1167 -1.3; 1248 -2.1; 1336 -2.2; 1429 -2.1; 1529 -2.0; 1636 -2.6; 1751 -2.2; 1873 -1.5; 2004 -0.0; 2145 1.6; 2295 2.9; 2455 4.0; 2627 4.8; 2811 3.8; 3008 3.1; 3219 3.4; 3444 5.7; 3685 6.0; 3943 4.0; 4219 2.0; 4514 1.2; 4830 2.7; 5168 5.8; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -0.9; 9502 -1.0; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pendulumic Stance S1 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.51 | 12.3 dB |
| Peaking | 77 Hz    | 0.38 | -8.9 dB |
| Peaking | 3319 Hz  | 2.2  | 4.9 dB  |
| Peaking | 5819 Hz  | 3.69 | 6.3 dB  |
| Peaking | 24000 Hz | 2.47 | 4.2 dB  |
| Peaking | 388 Hz   | 2.1  | -1.1 dB |
| Peaking | 629 Hz   | 2.41 | 1.9 dB  |
| Peaking | 1630 Hz  | 1.7  | -3.1 dB |
| Peaking | 2408 Hz  | 4.33 | 3.6 dB  |
| Peaking | 9079 Hz  | 4.72 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pendulumic%20Stance%20S1%20Bluetooth/Pendulumic%20Stance%20S1%20Bluetooth.png)