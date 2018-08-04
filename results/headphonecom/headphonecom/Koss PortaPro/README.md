# Koss PortaPro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.9; 22 4.0; 23 3.5; 25 2.6; 26 2.2; 28 1.5; 30 0.8; 32 0.2; 35 -0.7; 37 -1.3; 40 -2.0; 42 -2.5; 45 -3.1; 49 -3.9; 52 -4.5; 56 -5.2; 59 -5.6; 64 -6.3; 68 -6.8; 73 -7.3; 78 -7.7; 83 -8.0; 89 -8.3; 95 -8.5; 102 -8.6; 109 -8.7; 117 -8.5; 125 -8.4; 134 -8.2; 143 -8.0; 153 -7.9; 164 -7.6; 175 -7.3; 188 -6.9; 201 -6.5; 215 -6.1; 230 -5.8; 246 -5.4; 263 -5.1; 282 -4.9; 301 -4.5; 323 -4.2; 345 -4.0; 369 -3.4; 395 -2.8; 423 -2.5; 452 -2.1; 484 -1.8; 518 -1.3; 554 -1.0; 593 -0.6; 635 -0.2; 679 -0.2; 726 -0.0; 777 0.1; 832 0.2; 890 0.1; 952 0.0; 1019 -0.0; 1090 -0.0; 1167 -0.0; 1248 0.1; 1336 0.2; 1429 0.4; 1529 0.3; 1636 0.0; 1751 -0.6; 1873 -1.2; 2004 -1.7; 2145 -1.9; 2295 -1.4; 2455 -0.4; 2627 0.9; 2811 2.6; 3008 3.9; 3219 4.7; 3444 5.0; 3685 5.1; 3943 4.3; 4219 3.7; 4514 3.8; 4830 3.3; 5168 4.6; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.4; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss PortaPro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.22 | 5.7 dB  |
| Peaking | 82 Hz   | 0.76 | -5.6 dB |
| Peaking | 170 Hz  | 0.64 | -5.4 dB |
| Peaking | 3528 Hz | 3.11 | 5.3 dB  |
| Peaking | 5837 Hz | 3.2  | 6.1 dB  |
| Peaking | 344 Hz  | 2.05 | -1.1 dB |
| Peaking | 1075 Hz | 0.26 | 0.8 dB  |
| Peaking | 2163 Hz | 2.52 | -3.2 dB |
| Peaking | 2912 Hz | 6.39 | 1.5 dB  |
| Peaking | 8698 Hz | 3.06 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Koss%20PortaPro/Koss%20PortaPro.png)