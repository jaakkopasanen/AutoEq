# Fidue A31s

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -7.7; 22 -7.7; 23 -7.8; 25 -7.9; 26 -7.9; 28 -8.1; 30 -8.2; 32 -8.2; 35 -8.3; 37 -8.3; 40 -8.3; 42 -8.2; 45 -8.2; 49 -8.1; 52 -8.1; 56 -8.0; 59 -7.9; 64 -7.8; 68 -7.7; 73 -7.6; 78 -7.6; 83 -7.6; 89 -7.7; 95 -8.0; 102 -8.2; 109 -8.4; 117 -8.6; 125 -8.9; 134 -9.0; 143 -9.0; 153 -8.9; 164 -8.7; 175 -8.3; 188 -7.9; 201 -7.6; 215 -7.2; 230 -6.7; 246 -6.3; 263 -5.8; 282 -5.3; 301 -4.9; 323 -4.4; 345 -3.9; 369 -3.5; 395 -3.0; 423 -2.3; 452 -1.9; 484 -1.7; 518 -1.2; 554 -0.8; 593 -0.2; 635 0.1; 679 0.3; 726 0.5; 777 0.9; 832 0.9; 890 0.5; 952 0.2; 1019 0.1; 1090 0.3; 1167 -0.3; 1248 -0.8; 1336 -1.4; 1429 -1.4; 1529 -1.7; 1636 -2.6; 1751 -3.7; 1873 -4.4; 2004 -4.9; 2145 -5.5; 2295 -5.5; 2455 -4.2; 2627 -2.5; 2811 -0.6; 3008 1.8; 3219 3.0; 3444 3.5; 3685 2.8; 3943 0.6; 4219 -3.1; 4514 -4.4; 4830 -0.7; 5168 4.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A31s ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.27 | -7.9 dB |
| Peaking | 172 Hz  | 0.84 | -6.2 dB |
| Peaking | 2169 Hz | 2.26 | -6.0 dB |
| Peaking | 3268 Hz | 5.39 | 5.1 dB  |
| Peaking | 5964 Hz | 4.6  | 7.2 dB  |
| Peaking | 337 Hz  | 2.72 | -0.8 dB |
| Peaking | 772 Hz  | 1.95 | 1.8 dB  |
| Peaking | 5235 Hz | 8.53 | 4.2 dB  |
| Peaking | 4450 Hz | 5    | -6.2 dB |
| Peaking | 3742 Hz | 6.85 | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A31s/Fidue%20A31s.png)