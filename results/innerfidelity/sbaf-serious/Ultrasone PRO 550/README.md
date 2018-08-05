# Ultrasone PRO 550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.7; 32 5.1; 35 4.3; 37 3.9; 40 3.3; 42 3.0; 45 2.7; 49 2.6; 52 2.6; 56 2.8; 59 3.3; 64 3.7; 68 3.3; 73 2.7; 78 2.6; 83 2.5; 89 2.4; 95 2.4; 102 2.6; 109 2.6; 117 2.6; 125 2.6; 134 2.7; 143 2.9; 153 3.2; 164 4.1; 175 4.6; 188 5.4; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 5.4; 345 3.7; 369 2.1; 395 1.2; 423 0.8; 452 0.7; 484 0.5; 518 0.5; 554 0.7; 593 1.8; 635 3.1; 679 2.6; 726 1.6; 777 1.2; 832 0.7; 890 0.3; 952 0.1; 1019 0.1; 1090 0.5; 1167 0.7; 1248 0.5; 1336 0.7; 1429 0.1; 1529 -0.4; 1636 -0.2; 1751 0.8; 1873 2.3; 2004 4.0; 2145 4.7; 2295 3.6; 2455 1.8; 2627 3.0; 2811 4.1; 3008 3.7; 3219 2.5; 3444 1.8; 3685 2.1; 3943 3.2; 4219 5.9; 4514 5.4; 4830 5.8; 5168 6.0; 5530 5.0; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -0.8; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -2.0; 18692 -0.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 9 Hz     | 0.2  | 6.7 dB  |
| Peaking | 238 Hz   | 1.23 | 6.3 dB  |
| Peaking | 2255 Hz  | 2.49 | 3.6 dB  |
| Peaking | 4630 Hz  | 2.53 | 5.4 dB  |
| Peaking | 6144 Hz  | 4.54 | 4.4 dB  |
| Peaking | 457 Hz   | 3.51 | -1.5 dB |
| Peaking | 652 Hz   | 6.36 | 2.6 dB  |
| Peaking | 1581 Hz  | 7.51 | -1.7 dB |
| Peaking | 8765 Hz  | 4.5  | -1.4 dB |
| Peaking | 30423 Hz | 4.31 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20550/Ultrasone%20PRO%20550.png)