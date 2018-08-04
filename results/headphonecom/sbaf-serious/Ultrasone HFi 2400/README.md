# Ultrasone HFi 2400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.5; 23 5.1; 25 4.3; 26 3.8; 28 2.9; 30 2.0; 32 1.3; 35 0.3; 37 -0.2; 40 -0.9; 42 -1.3; 45 -1.7; 49 -2.0; 52 -2.2; 56 -2.6; 59 -2.8; 64 -2.9; 68 -3.0; 73 -3.1; 78 -3.5; 83 -3.9; 89 -4.0; 95 -4.1; 102 -4.4; 109 -4.5; 117 -4.6; 125 -4.7; 134 -4.7; 143 -4.7; 153 -4.6; 164 -4.2; 175 -4.0; 188 -3.8; 201 -3.3; 215 -3.1; 230 -3.9; 246 -4.5; 263 -4.0; 282 -3.4; 301 -3.0; 323 -2.5; 345 -1.8; 369 -1.6; 395 -1.5; 423 -1.0; 452 -1.0; 484 -1.1; 518 -0.7; 554 0.2; 593 0.3; 635 -0.1; 679 -0.3; 726 -0.4; 777 -0.2; 832 -0.4; 890 -0.0; 952 0.2; 1019 -0.1; 1090 -0.0; 1167 0.3; 1248 0.4; 1336 0.2; 1429 0.5; 1529 0.6; 1636 0.4; 1751 -0.4; 1873 -0.4; 2004 -0.1; 2145 -0.1; 2295 4.8; 2455 6.0; 2627 5.4; 2811 3.8; 3008 1.8; 3219 -0.1; 3444 -1.3; 3685 0.7; 3943 0.9; 4219 -0.9; 4514 1.2; 4830 4.3; 5168 5.3; 5530 4.5; 5917 -0.9; 6331 -8.2; 6775 -7.3; 7249 -1.8; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.4; 13327 -4.1; 14260 -7.5; 15258 -8.8; 16326 -7.5; 17469 -4.2; 18692 -0.7; 20000 0.0
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
| Peaking | 21 Hz    | 1.61 | 6.4 dB   |
| Peaking | 126 Hz   | 0.46 | -4.7 dB  |
| Peaking | 5240 Hz  | 0.43 | 2.8 dB   |
| Peaking | 6552 Hz  | 7.64 | -12.7 dB |
| Peaking | 15356 Hz | 1.93 | -10.2 dB |
| Peaking | 576 Hz   | 5.65 | 1.3 dB   |
| Peaking | 2105 Hz  | 3.76 | -4.4 dB  |
| Peaking | 2454 Hz  | 3.09 | 8.9 dB   |
| Peaking | 3677 Hz  | 1.02 | -4.2 dB  |
| Peaking | 5200 Hz  | 4.77 | 6.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi%202400/Ultrasone%20HFi%202400.png)