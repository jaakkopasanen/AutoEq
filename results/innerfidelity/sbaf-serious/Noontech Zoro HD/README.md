# Noontech Zoro HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.7; 22 -3.8; 23 -3.9; 25 -4.0; 26 -4.0; 28 -4.1; 30 -4.2; 32 -4.3; 35 -4.4; 37 -4.4; 40 -4.5; 42 -4.5; 45 -4.5; 49 -4.5; 52 -4.6; 56 -4.6; 59 -4.6; 64 -4.7; 68 -4.8; 73 -4.9; 78 -5.0; 83 -5.1; 89 -5.3; 95 -5.6; 102 -6.0; 109 -6.2; 117 -6.6; 125 -6.8; 134 -6.9; 143 -6.8; 153 -7.0; 164 -7.1; 175 -6.6; 188 -6.7; 201 -6.7; 215 -6.5; 230 -6.1; 246 -5.7; 263 -5.2; 282 -4.8; 301 -4.6; 323 -4.4; 345 -3.9; 369 -3.6; 395 -3.3; 423 -2.8; 452 -2.7; 484 -2.6; 518 -2.1; 554 -1.7; 593 -1.5; 635 -1.2; 679 -1.1; 726 -0.8; 777 -0.6; 832 -0.4; 890 -0.3; 952 -0.2; 1019 0.1; 1090 0.4; 1167 0.8; 1248 1.1; 1336 0.9; 1429 0.9; 1529 0.7; 1636 0.7; 1751 0.9; 1873 1.3; 2004 1.5; 2145 1.6; 2295 1.7; 2455 2.4; 2627 2.8; 2811 3.1; 3008 2.5; 3219 1.8; 3444 2.4; 3685 3.5; 3943 5.4; 4219 6.0; 4514 6.0; 4830 5.9; 5168 4.5; 5530 5.3; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontech Zoro HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 5 Hz    | 1.59 | -3.1 dB |
| Peaking | 29 Hz   | 0.26 | -3.7 dB |
| Peaking | 182 Hz  | 0.63 | -5.9 dB |
| Peaking | 4308 Hz | 1.35 | 5.4 dB  |
| Peaking | 6095 Hz | 5.08 | 3.6 dB  |
| Peaking | 2839 Hz | 2.06 | 2.0 dB  |
| Peaking | 1236 Hz | 3.43 | 1.1 dB  |
| Peaking | 3324 Hz | 3.21 | -3.5 dB |
| Peaking | 4052 Hz | 2.31 | 1.1 dB  |
| Peaking | 8498 Hz | 2.73 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontech%20Zoro%20HD/Noontech%20Zoro%20HD.png)