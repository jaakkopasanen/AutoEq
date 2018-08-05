# Piaton Moderna MS200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.4; 22 0.8; 23 0.5; 25 -0.1; 26 -0.4; 28 -0.9; 30 -1.3; 32 -1.7; 35 -2.2; 37 -2.5; 40 -2.9; 42 -3.2; 45 -3.5; 49 -3.9; 52 -4.1; 56 -4.4; 59 -4.6; 64 -4.9; 68 -5.2; 73 -5.4; 78 -5.8; 83 -6.2; 89 -6.6; 95 -7.2; 102 -7.8; 109 -8.4; 117 -8.9; 125 -9.4; 134 -10.0; 143 -10.3; 153 -10.5; 164 -10.6; 175 -10.5; 188 -10.6; 201 -10.5; 215 -10.4; 230 -10.1; 246 -10.0; 263 -9.8; 282 -9.5; 301 -9.2; 323 -8.9; 345 -8.5; 369 -8.2; 395 -7.6; 423 -6.9; 452 -6.3; 484 -6.5; 518 -6.4; 554 -5.6; 593 -4.8; 635 -4.0; 679 -3.5; 726 -2.7; 777 -1.9; 832 -1.2; 890 -0.7; 952 -0.3; 1019 0.1; 1090 0.3; 1167 0.4; 1248 0.4; 1336 0.0; 1429 -1.0; 1529 -1.8; 1636 -2.3; 1751 -2.9; 1873 -3.3; 2004 -3.5; 2145 -3.6; 2295 -3.3; 2455 -2.0; 2627 -0.4; 2811 1.6; 3008 3.5; 3219 5.0; 3444 5.9; 3685 6.0; 3943 5.6; 4219 3.8; 4514 2.3; 4830 1.8; 5168 2.1; 5530 2.3; 5917 1.2; 6331 -0.8; 6775 -1.9; 7249 -2.9; 7756 -3.5; 8299 -3.7; 8880 -3.6; 9502 -3.2; 10167 -2.5; 10879 -1.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Piaton Moderna MS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 186 Hz  | 0.45 | -10.9 dB |
| Peaking | 507 Hz  | 1.12 | -3.1 dB  |
| Peaking | 2183 Hz | 0.92 | -19.0 dB |
| Peaking | 3050 Hz | 0.39 | 19.0 dB  |
| Peaking | 7697 Hz | 0.82 | -10.9 dB |
| Peaking | 18 Hz   | 2.6  | 2.0 dB   |
| Peaking | 2706 Hz | 6.3  | -1.1 dB  |
| Peaking | 3784 Hz | 2.49 | 2.0 dB   |
| Peaking | 4541 Hz | 3.43 | -3.0 dB  |
| Peaking | 5641 Hz | 6.31 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Piaton%20Moderna%20MS200/Piaton%20Moderna%20MS200.png)