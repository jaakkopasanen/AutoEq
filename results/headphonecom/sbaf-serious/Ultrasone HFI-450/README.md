# Ultrasone HFI-450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.6; 42 5.1; 45 4.2; 49 3.0; 52 2.2; 56 1.3; 59 0.7; 64 -0.3; 68 -0.7; 73 -0.5; 78 0.2; 83 0.1; 89 -0.9; 95 -1.7; 102 -2.1; 109 -2.1; 117 -1.9; 125 -1.1; 134 -0.8; 143 -0.7; 153 -0.5; 164 0.1; 175 0.8; 188 0.8; 201 1.0; 215 1.1; 230 1.2; 246 0.8; 263 -0.1; 282 -1.1; 301 -1.7; 323 -2.2; 345 -2.3; 369 -1.9; 395 -1.5; 423 -1.8; 452 -1.7; 484 -1.2; 518 -0.8; 554 -0.5; 593 -0.2; 635 -0.1; 679 -0.3; 726 -0.3; 777 0.0; 832 0.1; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.0; 1248 0.0; 1336 -0.0; 1429 0.2; 1529 0.3; 1636 0.1; 1751 -1.3; 1873 -2.2; 2004 -2.0; 2145 -1.5; 2295 -0.7; 2455 0.3; 2627 1.5; 2811 2.5; 3008 2.9; 3219 2.4; 3444 1.5; 3685 2.4; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.6; 5168 3.3; 5530 1.2; 5917 4.8; 6331 5.5; 6775 2.0; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -2.0; 9502 -3.1; 10167 -2.4; 10879 -1.0; 11640 -0.3; 12455 -1.0; 13327 -1.2; 14260 -0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.43 | 7.2 dB  |
| Peaking | 6325 Hz | 4.07 | 7.4 dB  |
| Peaking | 2897 Hz | 3.9  | 4.0 dB  |
| Peaking | 4350 Hz | 2.37 | 10.5 dB |
| Peaking | 4796 Hz | 0.56 | -4.8 dB |
| Peaking | 14 Hz   | 1.13 | 2.4 dB  |
| Peaking | 4 Hz    | 1.35 | -0.7 dB |
| Peaking | 107 Hz  | 1.97 | -2.6 dB |
| Peaking | 228 Hz  | 1.72 | 2.3 dB  |
| Peaking | 331 Hz  | 1.88 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFI-450/Ultrasone%20HFI-450.png)