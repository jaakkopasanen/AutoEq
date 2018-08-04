# Noontec Hammo S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.9; 22 0.7; 23 0.6; 25 0.4; 26 0.3; 28 0.2; 30 0.1; 32 0.0; 35 -0.1; 37 -0.2; 40 -0.2; 42 -0.2; 45 -0.2; 49 -0.3; 52 -0.3; 56 -0.3; 59 -0.3; 64 -0.3; 68 -0.3; 73 -0.3; 78 -0.2; 83 -0.3; 89 -0.3; 95 -0.3; 102 -0.1; 109 -0.1; 117 -0.3; 125 -1.1; 134 -2.1; 143 -2.8; 153 -3.4; 164 -2.6; 175 -2.3; 188 -3.1; 201 -3.0; 215 -2.9; 230 -2.6; 246 -2.1; 263 -1.7; 282 -1.2; 301 -0.7; 323 -0.2; 345 0.4; 369 0.9; 395 1.4; 423 1.9; 452 1.8; 484 2.1; 518 2.1; 554 2.1; 593 1.8; 635 1.2; 679 0.6; 726 0.5; 777 0.8; 832 1.0; 890 0.8; 952 0.7; 1019 -0.1; 1090 -0.7; 1167 -1.2; 1248 -1.7; 1336 -2.0; 1429 -2.4; 1529 -2.6; 1636 -2.6; 1751 -2.5; 1873 -2.2; 2004 -1.5; 2145 -0.8; 2295 -0.0; 2455 1.3; 2627 2.2; 2811 2.8; 3008 3.4; 3219 3.0; 3444 1.0; 3685 -0.5; 3943 1.2; 4219 0.4; 4514 0.8; 4830 3.5; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.3; 9502 -1.0; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 201 Hz  | 1.24 | -3.6 dB |
| Peaking | 485 Hz  | 1.08 | 2.7 dB  |
| Peaking | 1607 Hz | 1.68 | -3.2 dB |
| Peaking | 2872 Hz | 3.84 | 3.8 dB  |
| Peaking | 5758 Hz | 3.33 | 6.9 dB  |
| Peaking | 16 Hz   | 1.67 | 1.0 dB  |
| Peaking | 112 Hz  | 3.83 | 1.0 dB  |
| Peaking | 144 Hz  | 7.45 | -1.4 dB |
| Peaking | 6609 Hz | 7.42 | 2.0 dB  |
| Peaking | 8309 Hz | 1.61 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Hammo%20S/Noontec%20Hammo%20S.png)