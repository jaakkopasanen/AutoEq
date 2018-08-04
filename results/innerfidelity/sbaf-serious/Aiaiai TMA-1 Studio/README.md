# Aiaiai TMA-1 Studio

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.2; 30 4.6; 32 3.8; 35 2.8; 37 2.2; 40 1.5; 42 1.1; 45 0.5; 49 -0.1; 52 -0.5; 56 -0.8; 59 -1.0; 64 -1.2; 68 -1.4; 73 -1.6; 78 -1.7; 83 -1.8; 89 -1.9; 95 -2.1; 102 -2.1; 109 -2.1; 117 -2.4; 125 -2.8; 134 -3.1; 143 -3.4; 153 -3.6; 164 -3.5; 175 -3.3; 188 -3.2; 201 -3.2; 215 -3.2; 230 -3.0; 246 -2.9; 263 -2.7; 282 -2.3; 301 -1.9; 323 -1.6; 345 -1.9; 369 -1.9; 395 -1.6; 423 -1.5; 452 -1.4; 484 -1.3; 518 -1.0; 554 -0.5; 593 0.3; 635 0.9; 679 1.3; 726 1.7; 777 1.9; 832 1.5; 890 0.8; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 0.3; 1248 1.1; 1336 1.4; 1429 1.3; 1529 1.7; 1636 2.3; 1751 3.0; 1873 3.8; 2004 4.5; 2145 5.3; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.7; 3685 5.2; 3943 5.2; 4219 5.4; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 2.7; 7249 0.4; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aiaiai TMA-1 Studio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.3  | 6.7 dB  |
| Peaking | 167 Hz  | 0.43 | -3.3 dB |
| Peaking | 712 Hz  | 3.6  | 2.4 dB  |
| Peaking | 2698 Hz | 1.19 | 6.2 dB  |
| Peaking | 5302 Hz | 2.34 | 5.2 dB  |
| Peaking | 1086 Hz | 7.08 | -1.0 dB |
| Peaking | 2076 Hz | 6.14 | 0.6 dB  |
| Peaking | 6455 Hz | 7.79 | 2.1 dB  |
| Peaking | 6186 Hz | 6.85 | 1.3 dB  |
| Peaking | 7384 Hz | 2.14 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aiaiai%20TMA-1%20Studio/Aiaiai%20TMA-1%20Studio.png)