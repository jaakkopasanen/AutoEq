# Audeze LCD XC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.5; 22 -3.4; 23 -3.4; 25 -3.3; 26 -3.2; 28 -3.1; 30 -3.0; 32 -3.1; 35 -3.1; 37 -3.1; 40 -3.0; 42 -2.9; 45 -2.8; 49 -2.8; 52 -3.0; 56 -3.6; 59 -3.9; 64 -4.1; 68 -4.1; 73 -4.0; 78 -4.0; 83 -3.9; 89 -3.8; 95 -3.8; 102 -3.6; 109 -3.4; 117 -3.1; 125 -3.1; 134 -3.1; 143 -2.9; 153 -2.8; 164 -2.6; 175 -2.7; 188 -2.6; 201 -2.4; 215 -2.2; 230 -1.8; 246 -1.5; 263 -1.0; 282 -0.7; 301 -0.8; 323 -0.4; 345 0.7; 369 1.1; 395 1.0; 423 1.1; 452 1.2; 484 1.0; 518 1.4; 554 2.0; 593 2.2; 635 2.5; 679 2.4; 726 2.3; 777 2.0; 832 1.4; 890 0.9; 952 0.4; 1019 -0.0; 1090 -0.6; 1167 -1.1; 1248 -1.6; 1336 -2.5; 1429 -3.2; 1529 -3.8; 1636 -4.3; 1751 -4.2; 1873 -3.8; 2004 -3.0; 2145 -1.6; 2295 -0.3; 2455 0.9; 2627 2.1; 2811 2.3; 3008 2.6; 3219 2.8; 3444 0.9; 3685 -1.1; 3943 -1.6; 4219 0.6; 4514 4.9; 4830 5.6; 5168 4.9; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -2.7; 14260 -5.1; 15258 -5.6; 16326 -6.3; 17469 -7.2; 18692 -5.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.23 | -3.2 dB |
| Peaking | 100 Hz   | 0.83 | -3.0 dB |
| Peaking | 1667 Hz  | 3.35 | -5.1 dB |
| Peaking | 5615 Hz  | 2.14 | 6.7 dB  |
| Peaking | 17078 Hz | 1.23 | -7.7 dB |
| Peaking | 657 Hz   | 2.53 | 2.9 dB  |
| Peaking | 402 Hz   | 3.96 | 1.3 dB  |
| Peaking | 2986 Hz  | 3.85 | 2.9 dB  |
| Peaking | 3859 Hz  | 7.41 | -4.1 dB |
| Peaking | 29462 Hz | 7.3  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD%20XC/Audeze%20LCD%20XC.png)