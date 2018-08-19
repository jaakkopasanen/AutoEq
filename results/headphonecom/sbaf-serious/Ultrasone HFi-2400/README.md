# Ultrasone HFi-2400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.5; 23 5.1; 25 4.3; 26 3.8; 28 2.9; 30 2.0; 32 1.3; 35 0.3; 37 -0.3; 40 -1.1; 42 -1.5; 45 -1.9; 49 -2.2; 52 -2.4; 56 -3.0; 59 -3.3; 64 -3.5; 68 -3.5; 73 -3.8; 78 -4.3; 83 -4.7; 89 -4.8; 95 -4.8; 102 -4.9; 109 -4.9; 117 -4.8; 125 -4.7; 134 -4.6; 143 -4.5; 153 -4.3; 164 -4.0; 175 -3.8; 188 -3.6; 201 -3.1; 215 -2.9; 230 -3.8; 246 -4.4; 263 -3.9; 282 -3.4; 301 -2.9; 323 -2.4; 345 -1.8; 369 -1.5; 395 -1.4; 423 -1.1; 452 -1.0; 484 -1.1; 518 -0.6; 554 0.3; 593 0.2; 635 -0.2; 679 -0.3; 726 -0.3; 777 -0.3; 832 -0.4; 890 0.0; 952 0.2; 1019 -0.1; 1090 -0.0; 1167 0.3; 1248 0.4; 1336 0.2; 1429 0.5; 1529 0.5; 1636 0.4; 1751 -0.4; 1873 -0.4; 2004 -0.1; 2145 -0.1; 2295 4.8; 2455 6.0; 2627 5.4; 2811 3.9; 3008 1.7; 3219 -0.1; 3444 -1.2; 3685 0.8; 3943 0.6; 4219 -0.9; 4514 1.3; 4830 4.4; 5168 5.3; 5530 4.4; 5917 -0.8; 6331 -8.2; 6775 -7.4; 7249 -1.9; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.5; 13327 -4.4; 14260 -7.5; 15258 -8.6; 16326 -7.4; 17469 -4.3; 18692 -0.6; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999999dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi-2400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.23 | 6.9 dB   |
| Peaking | 106 Hz   | 0.4  | -5.0 dB  |
| Peaking | 5338 Hz  | 0.43 | 2.9 dB   |
| Peaking | 6556 Hz  | 7.49 | -12.7 dB |
| Peaking | 15333 Hz | 1.85 | -10.0 dB |
| Peaking | 188 Hz   | 5    | 0.5 dB   |
| Peaking | 2101 Hz  | 3.72 | -4.5 dB  |
| Peaking | 2449 Hz  | 3.16 | 8.7 dB   |
| Peaking | 3826 Hz  | 1.08 | -4.3 dB  |
| Peaking | 5185 Hz  | 4.56 | 6.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi-2400/Ultrasone%20HFi-2400.png)