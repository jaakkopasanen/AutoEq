# Shure SRH940

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.6; 30 5.2; 32 4.7; 35 4.0; 37 3.6; 40 3.0; 42 2.6; 45 2.2; 49 1.7; 52 1.4; 56 1.1; 59 1.0; 64 0.8; 68 1.0; 73 1.6; 78 2.5; 83 3.1; 89 2.5; 95 1.3; 102 0.4; 109 0.2; 117 0.5; 125 1.0; 134 0.3; 143 -0.1; 153 -0.3; 164 0.1; 175 -0.7; 188 -1.6; 201 -2.0; 215 -2.4; 230 -2.7; 246 -2.9; 263 -3.0; 282 -2.7; 301 -2.7; 323 -3.7; 345 -3.6; 369 -2.7; 395 -2.3; 423 -2.1; 452 -1.9; 484 -1.6; 518 -1.4; 554 -1.2; 593 -0.8; 635 -0.7; 679 -0.5; 726 -0.4; 777 -0.1; 832 0.4; 890 0.0; 952 -0.1; 1019 0.0; 1090 0.1; 1167 -0.1; 1248 -0.3; 1336 -0.7; 1429 -1.1; 1529 -1.7; 1636 -2.0; 1751 -2.1; 1873 -2.0; 2004 -1.9; 2145 -1.8; 2295 -1.5; 2455 -0.2; 2627 -0.2; 2811 -0.4; 3008 -0.5; 3219 -0.8; 3444 -1.3; 3685 -1.7; 3943 -2.5; 4219 -2.7; 4514 -2.8; 4830 -2.0; 5168 0.0; 5530 2.5; 5917 3.1; 6331 3.5; 6775 3.9; 7249 1.3; 7756 -0.9; 8299 -5.8; 8880 -9.6; 9502 -9.0; 10167 -2.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.2; 14260 -3.0; 15258 -2.9; 16326 -1.7; 17469 -2.4; 18692 -4.5; 20000 -7.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH940 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 0.3  | 7.6 dB   |
| Peaking | 298 Hz   | 1.26 | -3.5 dB  |
| Peaking | 5649 Hz  | 0.68 | -4.3 dB  |
| Peaking | 6417 Hz  | 2.19 | 9.0 dB   |
| Peaking | 9002 Hz  | 5.31 | -10.6 dB |
| Peaking | 59 Hz    | 2.45 | -1.3 dB  |
| Peaking | 84 Hz    | 4.94 | 2.5 dB   |
| Peaking | 1827 Hz  | 2.96 | -1.7 dB  |
| Peaking | 2761 Hz  | 3.7  | 1.7 dB   |
| Peaking | 10966 Hz | 6.68 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH940/Shure%20SRH940.png)