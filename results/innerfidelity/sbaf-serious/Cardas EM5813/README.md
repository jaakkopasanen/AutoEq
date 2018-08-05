# Cardas EM5813

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -6.2; 22 -6.2; 23 -6.2; 25 -6.2; 26 -6.2; 28 -6.2; 30 -6.2; 32 -6.2; 35 -6.2; 37 -6.2; 40 -6.2; 42 -6.2; 45 -6.2; 49 -6.2; 52 -6.2; 56 -6.2; 59 -6.2; 64 -6.3; 68 -6.3; 73 -6.4; 78 -6.5; 83 -6.7; 89 -7.0; 95 -7.4; 102 -7.9; 109 -8.3; 117 -8.8; 125 -9.3; 134 -9.7; 143 -9.9; 153 -10.1; 164 -10.0; 175 -10.0; 188 -9.8; 201 -9.8; 215 -9.6; 230 -9.3; 246 -9.1; 263 -8.9; 282 -8.5; 301 -8.3; 323 -7.9; 345 -7.6; 369 -7.3; 395 -7.0; 423 -6.5; 452 -6.1; 484 -5.8; 518 -5.4; 554 -4.8; 593 -4.3; 635 -3.9; 679 -3.7; 726 -3.3; 777 -2.9; 832 -2.6; 890 -0.6; 952 -0.2; 1019 -0.1; 1090 -0.7; 1167 -0.3; 1248 -0.5; 1336 -1.0; 1429 -1.3; 1529 -1.5; 1636 -1.6; 1751 -1.5; 1873 -1.2; 2004 -1.6; 2145 -2.0; 2295 -3.0; 2455 -4.2; 2627 -5.2; 2811 -2.9; 3008 0.1; 3219 1.7; 3444 2.3; 3685 1.3; 3943 -1.0; 4219 -4.6; 4514 -5.9; 4830 -2.5; 5168 2.4; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cardas EM5813 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.54 | -5.5 dB |
| Peaking | 191 Hz  | 0.45 | -9.8 dB |
| Peaking | 2536 Hz | 6.16 | -5.3 dB |
| Peaking | 4522 Hz | 6.93 | -8.5 dB |
| Peaking | 5821 Hz | 3.02 | 7.2 dB  |
| Peaking | 999 Hz  | 2.08 | 3.7 dB  |
| Peaking | 1002 Hz | 0.82 | -2.0 dB |
| Peaking | 3434 Hz | 4.38 | 5.2 dB  |
| Peaking | 3444 Hz | 1.94 | -1.9 dB |
| Peaking | 8213 Hz | 5.23 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cardas%20EM5813/Cardas%20EM5813.png)