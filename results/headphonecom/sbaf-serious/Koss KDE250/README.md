# Koss KDE250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 5.9; 153 5.4; 164 5.0; 175 4.5; 188 4.0; 201 3.7; 215 3.4; 230 3.0; 246 2.5; 263 2.1; 282 1.8; 301 1.6; 323 1.4; 345 1.4; 369 1.2; 395 1.3; 423 1.4; 452 1.3; 484 1.5; 518 1.4; 554 1.5; 593 1.6; 635 1.6; 679 1.4; 726 1.3; 777 1.4; 832 1.1; 890 0.8; 952 0.4; 1019 -0.0; 1090 -0.5; 1167 -1.0; 1248 -1.7; 1336 -2.7; 1429 -4.1; 1529 -5.7; 1636 -7.1; 1751 -8.0; 1873 -9.0; 2004 -10.7; 2145 -13.0; 2295 -15.4; 2455 -16.1; 2627 -14.8; 2811 -13.6; 3008 -11.8; 3219 -8.2; 3444 -3.9; 3685 -0.4; 3943 1.9; 4219 4.2; 4514 6.0; 4830 4.9; 5168 2.9; 5530 2.4; 5917 2.5; 6331 1.1; 6775 -1.9; 7249 -5.4; 7756 -7.9; 8299 -8.7; 8880 -7.5; 9502 -5.7; 10167 -4.9; 10879 -5.4; 11640 -6.0; 12455 -5.3; 13327 -2.8; 14260 -0.1; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KDE250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.24 | 6.5 dB   |
| Peaking | 981 Hz   | 0.95 | 4.8 dB   |
| Peaking | 2566 Hz  | 1.03 | -23.3 dB |
| Peaking | 4546 Hz  | 1.07 | 17.3 dB  |
| Peaking | 8557 Hz  | 1.27 | -10.2 dB |
| Peaking | 3 Hz     | 2.43 | 0.5 dB   |
| Peaking | 9889 Hz  | 5.78 | 2.6 dB   |
| Peaking | 14142 Hz | 1.92 | 3.0 dB   |
| Peaking | 12404 Hz | 2.39 | -4.3 dB  |
| Peaking | 24000 Hz | 1.37 | -0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20KDE250/Koss%20KDE250.png)