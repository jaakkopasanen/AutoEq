# AKG K271 MK II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.7; 45 5.0; 49 4.1; 52 4.3; 56 5.6; 59 6.0; 64 5.6; 68 4.8; 73 3.9; 78 3.3; 83 2.7; 89 2.1; 95 1.7; 102 1.3; 109 1.1; 117 0.8; 125 0.4; 134 -0.0; 143 -0.3; 153 -0.6; 164 -0.1; 175 0.0; 188 -0.3; 201 -0.6; 215 -0.3; 230 0.0; 246 -0.2; 263 -0.0; 282 0.2; 301 -0.3; 323 -0.6; 345 -0.6; 369 -0.7; 395 -0.8; 423 -0.9; 452 -1.3; 484 -1.5; 518 -1.6; 554 -1.7; 593 -2.0; 635 -2.9; 679 -3.1; 726 0.6; 777 1.2; 832 0.8; 890 1.0; 952 0.5; 1019 -0.2; 1090 -0.7; 1167 -1.1; 1248 -1.4; 1336 -2.1; 1429 -2.7; 1529 -3.0; 1636 -3.2; 1751 -3.1; 1873 -2.4; 2004 -0.8; 2145 2.2; 2295 1.4; 2455 0.4; 2627 -0.3; 2811 -0.3; 3008 0.6; 3219 2.3; 3444 3.3; 3685 3.0; 3943 2.5; 4219 0.8; 4514 0.7; 4830 2.4; 5168 4.3; 5530 5.4; 5917 5.5; 6331 4.6; 6775 3.7; 7249 0.2; 7756 -4.1; 8299 -7.5; 8880 -8.8; 9502 -7.7; 10167 -5.1; 10879 -1.8; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MK II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.65 | 6.6 dB   |
| Peaking | 1568 Hz  | 3.02 | -3.6 dB  |
| Peaking | 3494 Hz  | 5.23 | 3.0 dB   |
| Peaking | 6085 Hz  | 2.36 | 7.3 dB   |
| Peaking | 8783 Hz  | 3    | -11.1 dB |
| Peaking | 64 Hz    | 5.91 | 2.4 dB   |
| Peaking | 712 Hz   | 1.66 | -5.1 dB  |
| Peaking | 861 Hz   | 2.65 | 4.1 dB   |
| Peaking | 750 Hz   | 8.14 | 3.9 dB   |
| Peaking | 11884 Hz | 6.05 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K271%20MK%20II/AKG%20K271%20MK%20II.png)