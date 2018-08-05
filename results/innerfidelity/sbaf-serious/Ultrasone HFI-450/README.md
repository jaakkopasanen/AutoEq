# Ultrasone HFI-450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.4; 78 4.7; 83 4.2; 89 4.0; 95 3.6; 102 2.7; 109 2.1; 117 1.8; 125 1.5; 134 1.3; 143 1.3; 153 1.3; 164 1.7; 175 1.9; 188 1.7; 201 1.8; 215 1.6; 230 1.4; 246 1.1; 263 0.6; 282 -0.0; 301 -0.9; 323 -1.5; 345 -1.8; 369 -1.8; 395 -1.7; 423 -1.7; 452 -1.5; 484 -1.5; 518 -1.4; 554 -0.7; 593 -0.1; 635 0.2; 679 0.2; 726 0.3; 777 0.4; 832 0.3; 890 0.1; 952 0.0; 1019 -0.0; 1090 -0.0; 1167 -0.2; 1248 -0.3; 1336 -0.3; 1429 -0.1; 1529 -0.6; 1636 -0.4; 1751 -0.6; 1873 -0.4; 2004 0.3; 2145 1.0; 2295 1.9; 2455 2.9; 2627 4.1; 2811 4.1; 3008 4.5; 3219 4.6; 3444 4.5; 3685 5.2; 3943 6.0; 4219 6.0; 4514 4.2; 4830 1.3; 5168 0.9; 5530 4.1; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.3; 9502 -1.1; 10167 -0.8; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.31 | 6.0 dB  |
| Peaking | 66 Hz   | 2.42 | 1.8 dB  |
| Peaking | 393 Hz  | 2.21 | -2.4 dB |
| Peaking | 3570 Hz | 1.8  | 5.7 dB  |
| Peaking | 6202 Hz | 5.77 | 5.5 dB  |
| Peaking | 213 Hz  | 3.93 | 1.2 dB  |
| Peaking | 1730 Hz | 2.5  | -1.3 dB |
| Peaking | 2590 Hz | 6.05 | 1.9 dB  |
| Peaking | 6739 Hz | 9.25 | 0.8 dB  |
| Peaking | 9365 Hz | 2.7  | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20HFI-450/Ultrasone%20HFI-450.png)