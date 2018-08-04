# Audeze LCD 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.8; 42 5.7; 45 5.4; 49 5.1; 52 5.0; 56 4.9; 59 4.8; 64 4.9; 68 4.9; 73 4.9; 78 4.7; 83 4.1; 89 3.5; 95 3.1; 102 2.7; 109 2.4; 117 2.0; 125 1.6; 134 1.4; 143 1.2; 153 1.0; 164 1.0; 175 0.9; 188 0.8; 201 0.6; 215 0.6; 230 0.7; 246 0.8; 263 0.8; 282 0.9; 301 1.1; 323 1.2; 345 1.2; 369 1.1; 395 0.9; 423 0.8; 452 0.7; 484 0.6; 518 0.5; 554 0.7; 593 0.9; 635 0.9; 679 0.5; 726 0.5; 777 0.8; 832 0.9; 890 0.8; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.9; 1248 -1.3; 1336 -1.4; 1429 -1.3; 1529 -1.8; 1636 -2.3; 1751 -2.4; 1873 -2.0; 2004 -2.2; 2145 -2.5; 2295 -2.2; 2455 -1.6; 2627 -1.8; 2811 -1.6; 3008 -1.4; 3219 -1.7; 3444 -1.8; 3685 -2.5; 3943 -3.5; 4219 -5.4; 4514 -6.2; 4830 -6.1; 5168 -4.7; 5530 -3.6; 5917 -2.9; 6331 -0.8; 6775 0.8; 7249 1.2; 7756 -0.1; 8299 -2.5; 8880 -4.0; 9502 -4.0; 10167 -3.3; 10879 -2.4; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.7; 18692 -0.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.41 | 6.2 dB  |
| Peaking | 833 Hz   | 0.69 | 1.4 dB  |
| Peaking | 1685 Hz  | 0.97 | -2.8 dB |
| Peaking | 4670 Hz  | 2.72 | -6.1 dB |
| Peaking | 26344 Hz | 1.58 | -2.7 dB |
| Peaking | 3 Hz     | 1.6  | -0.3 dB |
| Peaking | 76 Hz    | 4.42 | 1.1 dB  |
| Peaking | 144 Hz   | 2.18 | -0.6 dB |
| Peaking | 7207 Hz  | 4.75 | 3.4 dB  |
| Peaking | 9264 Hz  | 2.91 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD%201/Audeze%20LCD%201.png)