# Ultrasone HFi 2400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.6; 22 2.2; 23 1.5; 25 0.4; 26 -0.2; 28 -1.1; 30 -2.0; 32 -2.7; 35 -3.7; 37 -4.2; 40 -4.9; 42 -5.3; 45 -5.7; 49 -5.9; 52 -6.1; 56 -6.6; 59 -6.8; 64 -6.8; 68 -6.8; 73 -6.9; 78 -7.1; 83 -7.3; 89 -7.2; 95 -6.9; 102 -6.8; 109 -6.5; 117 -6.2; 125 -5.9; 134 -5.5; 143 -5.3; 153 -5.0; 164 -4.5; 175 -4.2; 188 -3.9; 201 -3.4; 215 -3.1; 230 -3.9; 246 -4.5; 263 -4.0; 282 -3.4; 301 -3.0; 323 -2.5; 345 -1.8; 369 -1.6; 395 -1.5; 423 -1.0; 452 -1.0; 484 -1.1; 518 -0.7; 554 0.2; 593 0.3; 635 -0.1; 679 -0.3; 726 -0.4; 777 -0.2; 832 -0.4; 890 -0.0; 952 0.2; 1019 -0.1; 1090 -0.0; 1167 0.3; 1248 0.4; 1336 0.2; 1429 0.5; 1529 0.6; 1636 0.4; 1751 -0.4; 1873 -0.4; 2004 -0.1; 2145 -0.1; 2295 4.8; 2455 6.0; 2627 5.4; 2811 3.8; 3008 1.8; 3219 -0.1; 3444 -1.3; 3685 0.7; 3943 0.9; 4219 -0.9; 4514 1.2; 4830 4.3; 5168 5.3; 5530 4.5; 5917 -0.9; 6331 -8.2; 6775 -7.3; 7249 -1.8; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.4; 13327 -4.1; 14260 -7.5; 15258 -8.8; 16326 -7.5; 17469 -4.2; 18692 -0.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi 2400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 63 Hz    | 0.91 | -4.6 dB  |
| Peaking | 131 Hz   | 0.5  | -4.2 dB  |
| Peaking | 5283 Hz  | 0.44 | 2.9 dB   |
| Peaking | 6527 Hz  | 7.51 | -12.7 dB |
| Peaking | 15363 Hz | 1.94 | -10.2 dB |
| Peaking | 20 Hz    | 2.91 | 4.0 dB   |
| Peaking | 2118 Hz  | 3.82 | -4.2 dB  |
| Peaking | 2440 Hz  | 3.29 | 8.4 dB   |
| Peaking | 3884 Hz  | 1.05 | -4.2 dB  |
| Peaking | 5215 Hz  | 4.46 | 7.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi%202400/Ultrasone%20HFi%202400.png)