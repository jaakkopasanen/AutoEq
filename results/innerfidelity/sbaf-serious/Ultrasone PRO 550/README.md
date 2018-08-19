# Ultrasone PRO 550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.7; 32 5.1; 35 4.2; 37 3.8; 40 3.2; 42 2.8; 45 2.5; 49 2.4; 52 2.3; 56 2.4; 59 2.9; 64 3.2; 68 2.7; 73 2.0; 78 1.8; 83 1.7; 89 1.6; 95 1.7; 102 2.0; 109 2.2; 117 2.4; 125 2.5; 134 2.9; 143 3.1; 153 3.4; 164 4.3; 175 4.8; 188 5.6; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 5.4; 345 3.8; 369 2.2; 395 1.2; 423 0.8; 452 0.7; 484 0.5; 518 0.5; 554 0.7; 593 1.8; 635 3.1; 679 2.6; 726 1.6; 777 1.2; 832 0.7; 890 0.3; 952 0.1; 1019 0.1; 1090 0.5; 1167 0.7; 1248 0.5; 1336 0.7; 1429 0.1; 1529 -0.4; 1636 -0.2; 1751 0.8; 1873 2.3; 2004 4.0; 2145 4.7; 2295 3.6; 2455 1.8; 2627 3.0; 2811 4.1; 3008 3.7; 3219 2.5; 3444 1.8; 3685 2.1; 3943 3.2; 4219 5.9; 4514 5.4; 4830 5.8; 5168 6.0; 5530 5.0; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -0.8; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -2.0; 18692 -0.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.57 | 6.2 dB  |
| Peaking | 234 Hz   | 1.16 | 6.4 dB  |
| Peaking | 2222 Hz  | 2.81 | 3.8 dB  |
| Peaking | 4654 Hz  | 2.35 | 5.6 dB  |
| Peaking | 6182 Hz  | 5.16 | 4.3 dB  |
| Peaking | 458 Hz   | 3.57 | -1.5 dB |
| Peaking | 654 Hz   | 5.83 | 2.7 dB  |
| Peaking | 2897 Hz  | 8.52 | 2.7 dB  |
| Peaking | 3850 Hz  | 0.2  | -0.4 dB |
| Peaking | 17687 Hz | 4.69 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20550/Ultrasone%20PRO%20550.png)