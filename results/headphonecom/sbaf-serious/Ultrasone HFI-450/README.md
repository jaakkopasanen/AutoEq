# Ultrasone HFI-450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.9; 56 5.3; 59 4.6; 64 3.6; 68 3.1; 73 3.2; 78 3.8; 83 3.6; 89 2.3; 95 1.2; 102 0.3; 109 -0.1; 117 -0.3; 125 0.0; 134 0.0; 143 -0.1; 153 -0.1; 164 0.3; 175 1.0; 188 0.9; 201 1.1; 215 1.1; 230 1.2; 246 0.8; 263 -0.1; 282 -1.0; 301 -1.7; 323 -2.2; 345 -2.3; 369 -1.9; 395 -1.5; 423 -1.8; 452 -1.7; 484 -1.2; 518 -0.8; 554 -0.5; 593 -0.2; 635 -0.1; 679 -0.3; 726 -0.3; 777 0.0; 832 0.1; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.0; 1248 0.0; 1336 -0.0; 1429 0.2; 1529 0.3; 1636 0.1; 1751 -1.3; 1873 -2.2; 2004 -2.0; 2145 -1.5; 2295 -0.7; 2455 0.3; 2627 1.5; 2811 2.5; 3008 2.9; 3219 2.4; 3444 1.5; 3685 2.4; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.6; 5168 3.3; 5530 1.2; 5917 4.8; 6331 5.5; 6775 2.0; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -2.0; 9502 -3.1; 10167 -2.4; 10879 -1.0; 11640 -0.3; 12455 -1.0; 13327 -1.2; 14260 -0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 34 Hz   | 0.72 | 6.9 dB  |
| Peaking | 6335 Hz | 4.04 | 7.4 dB  |
| Peaking | 2897 Hz | 4.06 | 4.1 dB  |
| Peaking | 4337 Hz | 2.31 | 10.8 dB |
| Peaking | 4796 Hz | 0.58 | -5.0 dB |
| Peaking | 117 Hz  | 4.26 | -1.5 dB |
| Peaking | 232 Hz  | 2.65 | 2.1 dB  |
| Peaking | 333 Hz  | 1.64 | -2.8 dB |
| Peaking | 1609 Hz | 1.52 | 1.7 dB  |
| Peaking | 1914 Hz | 3.98 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFI-450/Ultrasone%20HFI-450.png)