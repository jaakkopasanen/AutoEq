# Ultrasone HFI-580

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.6; 23 5.3; 25 4.6; 26 4.2; 28 3.3; 30 2.6; 32 1.8; 35 0.9; 37 0.3; 40 -0.4; 42 -0.8; 45 -1.2; 49 -1.6; 52 -1.9; 56 -2.0; 59 -2.0; 64 -1.9; 68 -1.9; 73 -0.8; 78 0.6; 83 0.5; 89 -0.0; 95 -0.3; 102 -0.5; 109 -0.4; 117 -0.2; 125 0.2; 134 0.7; 143 1.0; 153 1.4; 164 2.6; 175 3.8; 188 3.9; 201 1.2; 215 0.2; 230 0.2; 246 -0.2; 263 -0.8; 282 -1.5; 301 -1.8; 323 -1.8; 345 -1.5; 369 -1.2; 395 -0.8; 423 -0.6; 452 -0.4; 484 -0.3; 518 -0.3; 554 -0.3; 593 -0.1; 635 0.0; 679 0.2; 726 0.2; 777 0.2; 832 0.2; 890 0.1; 952 -0.0; 1019 -0.0; 1090 0.4; 1167 1.1; 1248 0.3; 1336 -0.3; 1429 -0.9; 1529 -1.4; 1636 -2.1; 1751 -3.3; 1873 -4.0; 2004 -4.3; 2145 -4.3; 2295 -4.2; 2455 -3.9; 2627 -4.1; 2811 -4.9; 3008 -5.9; 3219 -7.3; 3444 -7.0; 3685 -6.2; 3943 -5.1; 4219 -3.7; 4514 -2.5; 4830 -0.1; 5168 2.3; 5530 4.3; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.1; 7756 -2.3; 8299 -4.7; 8880 -6.2; 9502 -7.0; 10167 -5.9; 10879 -2.5; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 2.6  | 5.5 dB  |
| Peaking | 1984 Hz  | 3.45 | -3.2 dB |
| Peaking | 3458 Hz  | 1.77 | -7.7 dB |
| Peaking | 6055 Hz  | 2.52 | 8.7 dB  |
| Peaking | 9133 Hz  | 2.82 | -8.4 dB |
| Peaking | 57 Hz    | 2.6  | -2.5 dB |
| Peaking | 178 Hz   | 4.7  | 4.5 dB  |
| Peaking | 310 Hz   | 2.56 | -2.0 dB |
| Peaking | 1168 Hz  | 5.67 | 1.6 dB  |
| Peaking | 11873 Hz | 6.28 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFI-580/Ultrasone%20HFI-580.png)