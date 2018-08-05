# Cypher Labs Astru IEM

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 5.9; 22 5.3; 23 5.0; 25 4.6; 26 4.4; 28 4.0; 30 3.7; 32 3.5; 35 3.1; 37 2.9; 40 2.6; 42 2.4; 45 2.2; 49 1.9; 52 1.7; 56 1.5; 59 1.4; 64 1.1; 68 1.0; 73 0.7; 78 0.4; 83 0.1; 89 -0.4; 95 -0.8; 102 -1.4; 109 -2.0; 117 -2.6; 125 -3.2; 134 -3.7; 143 -3.9; 153 -4.2; 164 -4.4; 175 -4.4; 188 -4.4; 201 -4.4; 215 -4.2; 230 -4.1; 246 -4.0; 263 -3.8; 282 -3.6; 301 -3.4; 323 -3.2; 345 -2.9; 369 -2.8; 395 -2.5; 423 -2.1; 452 -1.8; 484 -1.7; 518 -1.4; 554 -1.0; 593 -0.5; 635 -0.2; 679 -0.1; 726 0.2; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -2.1; 1529 -2.8; 1636 -3.5; 1751 -4.2; 1873 -4.8; 2004 -5.2; 2145 -5.3; 2295 -4.6; 2455 -3.1; 2627 -2.4; 2811 -1.7; 3008 -0.5; 3219 0.7; 3444 1.1; 3685 0.2; 3943 -1.8; 4219 -4.0; 4514 -3.5; 4830 -1.5; 5168 -0.6; 5530 -2.1; 5917 0.6; 6331 2.2; 6775 0.9; 7249 0.8; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cypher Labs Astru IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.45 | 6.5 dB  |
| Peaking | 74 Hz   | 1.45 | 1.3 dB  |
| Peaking | 186 Hz  | 0.72 | -4.9 dB |
| Peaking | 2004 Hz | 2.58 | -5.7 dB |
| Peaking | 4360 Hz | 7.85 | -4.2 dB |
| Peaking | 829 Hz  | 1.33 | 2.3 dB  |
| Peaking | 920 Hz  | 0.48 | -1.2 dB |
| Peaking | 5620 Hz | 7.33 | -3.1 dB |
| Peaking | 3361 Hz | 6.81 | 2.5 dB  |
| Peaking | 6163 Hz | 4.97 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cypher%20Labs%20Astru%20IEM/Cypher%20Labs%20Astru%20IEM.png)