# Ultrasone Zino

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.8; 26 5.6; 28 5.1; 30 4.4; 32 3.8; 35 2.9; 37 2.4; 40 1.7; 42 1.2; 45 0.6; 49 -0.1; 52 -0.6; 56 -1.1; 59 -1.4; 64 -1.8; 68 -2.1; 73 -2.3; 78 -2.4; 83 -2.4; 89 -2.3; 95 -2.2; 102 -2.2; 109 -2.0; 117 -1.8; 125 -1.6; 134 -1.3; 143 -1.1; 153 -0.7; 164 -0.3; 175 0.3; 188 0.6; 201 1.1; 215 1.7; 230 2.3; 246 2.5; 263 2.8; 282 3.4; 301 4.3; 323 4.9; 345 5.0; 369 5.0; 395 4.4; 423 4.1; 452 4.1; 484 4.3; 518 4.9; 554 5.7; 593 6.0; 635 6.0; 679 6.0; 726 6.0; 777 6.0; 832 5.5; 890 3.5; 952 1.5; 1019 -0.6; 1090 -2.2; 1167 -3.6; 1248 -4.2; 1336 -5.2; 1429 -6.1; 1529 -7.1; 1636 -8.0; 1751 -8.7; 1873 -9.2; 2004 -9.6; 2145 -9.2; 2295 -7.4; 2455 -3.2; 2627 0.1; 2811 0.3; 3008 1.2; 3219 2.6; 3444 2.2; 3685 5.0; 3943 5.4; 4219 -0.4; 4514 -0.6; 4830 1.3; 5168 2.2; 5530 -0.2; 5917 -2.8; 6331 -2.6; 6775 -1.0; 7249 0.7; 7756 0.3; 8299 -0.3; 8880 -1.8; 9502 -2.6; 10167 -2.7; 10879 -1.8; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Zino ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 24 Hz    |  1.24 | 6.8 dB   |
| Peaking | 319 Hz   |  0.65 | 10.2 dB  |
| Peaking | 744 Hz   |  1.25 | 10.9 dB  |
| Peaking | 2054 Hz  |  0.23 | -39.9 dB |
| Peaking | 2997 Hz  |  0.3  | 34.8 dB  |
| Peaking | 3842 Hz  | 16.33 | 4.2 dB   |
| Peaking | 6167 Hz  |  6.96 | -3.6 dB  |
| Peaking | 7588 Hz  |  4.87 | 1.5 dB   |
| Peaking | 9828 Hz  |  3.52 | -2.9 dB  |
| Peaking | 14538 Hz |  0.73 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Zino/Ultrasone%20Zino.png)