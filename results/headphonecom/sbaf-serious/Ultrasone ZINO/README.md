# Ultrasone Zino

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.5; 30 4.8; 32 4.0; 35 2.9; 37 2.2; 40 1.4; 42 1.0; 45 0.4; 49 -0.2; 52 -0.6; 56 -1.0; 59 -1.2; 64 -1.3; 68 -1.4; 73 -1.6; 78 -1.6; 83 -1.6; 89 -1.6; 95 -1.5; 102 -1.4; 109 -1.3; 117 -1.2; 125 -0.9; 134 -0.8; 143 -0.7; 153 -0.5; 164 -0.2; 175 0.1; 188 0.6; 201 1.0; 215 1.6; 230 1.8; 246 1.3; 263 1.3; 282 1.7; 301 2.1; 323 2.7; 345 3.3; 369 3.7; 395 4.2; 423 4.7; 452 5.2; 484 5.7; 518 6.0; 554 6.0; 593 6.0; 635 6.0; 679 6.0; 726 6.0; 777 6.0; 832 6.0; 890 4.6; 952 1.9; 1019 -0.7; 1090 -2.8; 1167 -4.6; 1248 -6.5; 1336 -7.8; 1429 -8.9; 1529 -9.6; 1636 -11.2; 1751 -12.4; 1873 -13.7; 2004 -14.4; 2145 -14.7; 2295 -10.1; 2455 -5.4; 2627 -5.8; 2811 -5.8; 3008 -4.9; 3219 -4.1; 3444 -3.7; 3685 -2.2; 3943 0.3; 4219 -4.3; 4514 -4.0; 4830 -1.4; 5168 -0.6; 5530 -2.4; 5917 -5.0; 6331 -4.8; 6775 -0.7; 7249 -0.7; 7756 -2.5; 8299 -5.8; 8880 -9.4; 9502 -11.2; 10167 -9.9; 10879 -6.1; 11640 -2.2; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.1; 20000 -4.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Zino ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 2.34 | 7.1 dB   |
| Peaking | 661 Hz   | 0.99 | 9.0 dB   |
| Peaking | 1802 Hz  | 1.3  | -15.5 dB |
| Peaking | 9558 Hz  | 3.6  | -12.0 dB |
| Peaking | 20152 Hz | 3.72 | -3.4 dB  |
| Peaking | 31 Hz    | 1.76 | 1.7 dB   |
| Peaking | 78 Hz    | 1.02 | -2.2 dB  |
| Peaking | 863 Hz   | 7.08 | 2.7 dB   |
| Peaking | 1097 Hz  | 4.83 | -1.2 dB  |
| Peaking | 1259 Hz  | 7.59 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20Zino/Ultrasone%20Zino.png)