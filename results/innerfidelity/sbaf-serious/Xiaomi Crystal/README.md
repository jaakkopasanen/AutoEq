# Xiaomi Crystal

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.3dB
GraphicEQ: 10 -84; 20 -7.0; 22 -7.2; 23 -7.3; 25 -7.5; 26 -7.6; 28 -7.8; 30 -8.0; 32 -8.1; 35 -8.3; 37 -8.3; 40 -8.4; 42 -8.5; 45 -8.6; 49 -8.7; 52 -8.9; 56 -9.0; 59 -9.1; 64 -9.2; 68 -9.3; 73 -9.4; 78 -9.5; 83 -9.6; 89 -9.7; 95 -9.8; 102 -9.8; 109 -9.8; 117 -9.7; 125 -9.6; 134 -9.6; 143 -9.5; 153 -9.3; 164 -9.1; 175 -8.8; 188 -8.6; 201 -8.3; 215 -7.9; 230 -7.6; 246 -7.3; 263 -6.9; 282 -6.4; 301 -6.0; 323 -5.6; 345 -5.1; 369 -4.7; 395 -4.3; 423 -3.7; 452 -3.2; 484 -2.9; 518 -2.5; 554 -1.9; 593 -1.3; 635 -0.9; 679 -0.7; 726 -0.3; 777 0.1; 832 0.1; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.5; 1429 -0.5; 1529 -0.7; 1636 -0.8; 1751 -1.4; 1873 -2.3; 2004 -2.6; 2145 -2.7; 2295 -2.6; 2455 -2.2; 2627 -2.0; 2811 -2.0; 3008 -1.4; 3219 -1.0; 3444 -0.4; 3685 -0.4; 3943 -1.0; 4219 -2.7; 4514 -4.1; 4830 -4.8; 5168 -5.4; 5530 -6.7; 5917 -7.6; 6331 -6.9; 6775 -5.1; 7249 -3.9; 7756 -3.4; 8299 -4.0; 8880 -5.2; 9502 -6.0; 10167 -5.2; 10879 -2.5; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.25342780084276995dB` and instead set Global volume in the UI for both channels to **-2**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.3  | -7.4 dB |
| Peaking | 136 Hz   | 0.66 | -5.5 dB |
| Peaking | 283 Hz   | 1.16 | -2.8 dB |
| Peaking | 5817 Hz  | 1.86 | -7.1 dB |
| Peaking | 9607 Hz  | 4.33 | -5.3 dB |
| Peaking | 484 Hz   | 1.75 | -0.9 dB |
| Peaking | 783 Hz   | 1    | 1.2 dB  |
| Peaking | 2160 Hz  | 2.03 | -2.5 dB |
| Peaking | 3650 Hz  | 5.51 | 1.9 dB  |
| Peaking | 12107 Hz | 4.97 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Crystal/Xiaomi%20Crystal.png)