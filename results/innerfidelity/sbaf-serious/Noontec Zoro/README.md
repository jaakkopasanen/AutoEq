# Noontec Zoro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.2; 22 -0.2; 23 -0.4; 25 -0.7; 26 -0.8; 28 -1.0; 30 -1.2; 32 -1.3; 35 -1.5; 37 -1.6; 40 -1.8; 42 -1.8; 45 -1.9; 49 -2.0; 52 -2.0; 56 -2.1; 59 -2.1; 64 -2.2; 68 -2.4; 73 -2.5; 78 -2.6; 83 -2.8; 89 -3.0; 95 -3.2; 102 -3.6; 109 -3.8; 117 -4.1; 125 -4.5; 134 -4.7; 143 -4.8; 153 -4.9; 164 -5.1; 175 -4.8; 188 -4.9; 201 -5.0; 215 -4.8; 230 -4.8; 246 -4.7; 263 -4.5; 282 -4.1; 301 -3.9; 323 -4.0; 345 -3.8; 369 -3.8; 395 -3.6; 423 -3.3; 452 -3.3; 484 -3.3; 518 -3.1; 554 -2.8; 593 -2.4; 635 -2.1; 679 -1.9; 726 -1.4; 777 -0.9; 832 -0.5; 890 -0.2; 952 -0.0; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.1; 1336 -0.6; 1429 -1.3; 1529 -1.8; 1636 -1.7; 1751 -1.2; 1873 -0.4; 2004 1.0; 2145 2.3; 2295 3.7; 2455 5.5; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.2; 6331 4.3; 6775 3.5; 7249 0.9; 7756 -1.6; 8299 -2.5; 8880 -1.4; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 2.1  | -0.7 dB |
| Peaking | 211 Hz   | 0.37 | -4.9 dB |
| Peaking | 1681 Hz  | 2.18 | -5.5 dB |
| Peaking | 3534 Hz  | 0.51 | 7.3 dB  |
| Peaking | 8317 Hz  | 2.99 | -5.8 dB |
| Peaking | 540 Hz   | 5.52 | -0.5 dB |
| Peaking | 2584 Hz  | 6.62 | 1.4 dB  |
| Peaking | 3955 Hz  | 1.3  | -0.9 dB |
| Peaking | 5688 Hz  | 2.44 | 1.6 dB  |
| Peaking | 12838 Hz | 1.48 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro/Noontec%20Zoro.png)