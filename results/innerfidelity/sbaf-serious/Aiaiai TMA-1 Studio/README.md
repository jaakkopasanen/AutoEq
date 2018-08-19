# Aiaiai TMA-1 Studio

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.2; 30 4.5; 32 3.8; 35 2.8; 37 2.2; 40 1.4; 42 0.9; 45 0.3; 49 -0.4; 52 -0.8; 56 -1.2; 59 -1.4; 64 -1.8; 68 -2.0; 73 -2.3; 78 -2.5; 83 -2.6; 89 -2.7; 95 -2.8; 102 -2.7; 109 -2.5; 117 -2.6; 125 -2.8; 134 -3.0; 143 -3.2; 153 -3.4; 164 -3.2; 175 -3.0; 188 -3.0; 201 -3.0; 215 -3.0; 230 -2.9; 246 -2.8; 263 -2.6; 282 -2.3; 301 -1.9; 323 -1.6; 345 -1.9; 369 -1.9; 395 -1.6; 423 -1.5; 452 -1.4; 484 -1.3; 518 -1.0; 554 -0.4; 593 0.3; 635 0.9; 679 1.3; 726 1.7; 777 1.9; 832 1.5; 890 0.8; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 0.3; 1248 1.1; 1336 1.4; 1429 1.3; 1529 1.7; 1636 2.3; 1751 3.0; 1873 3.8; 2004 4.5; 2145 5.3; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.7; 3685 5.2; 3943 5.2; 4219 5.4; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 2.7; 7249 0.4; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aiaiai TMA-1 Studio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.92 | 8.1 dB  |
| Peaking | 100 Hz  | 0.23 | -3.5 dB |
| Peaking | 715 Hz  | 3.3  | 2.5 dB  |
| Peaking | 2695 Hz | 1.17 | 6.2 dB  |
| Peaking | 5304 Hz | 2.35 | 5.2 dB  |
| Peaking | 1083 Hz | 7.07 | -1.0 dB |
| Peaking | 2077 Hz | 6    | 0.6 dB  |
| Peaking | 6285 Hz | 7.19 | 2.0 dB  |
| Peaking | 6361 Hz | 5.86 | 1.2 dB  |
| Peaking | 7365 Hz | 2.17 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aiaiai%20TMA-1%20Studio/Aiaiai%20TMA-1%20Studio.png)