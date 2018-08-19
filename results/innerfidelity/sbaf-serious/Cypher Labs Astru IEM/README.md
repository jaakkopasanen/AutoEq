# Cypher Labs Astru IEM

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 5.8; 22 5.2; 23 4.9; 25 4.5; 26 4.3; 28 3.9; 30 3.6; 32 3.2; 35 2.8; 37 2.5; 40 2.2; 42 1.9; 45 1.6; 49 1.2; 52 0.9; 56 0.6; 59 0.3; 64 -0.1; 68 -0.5; 73 -0.8; 78 -1.2; 83 -1.5; 89 -1.9; 95 -2.2; 102 -2.5; 109 -2.7; 117 -2.9; 125 -3.2; 134 -3.4; 143 -3.5; 153 -3.7; 164 -3.9; 175 -3.8; 188 -3.9; 201 -3.9; 215 -3.9; 230 -3.8; 246 -3.7; 263 -3.6; 282 -3.4; 301 -3.3; 323 -3.1; 345 -2.8; 369 -2.7; 395 -2.4; 423 -2.1; 452 -1.8; 484 -1.6; 518 -1.4; 554 -1.0; 593 -0.5; 635 -0.2; 679 -0.1; 726 0.2; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -2.1; 1529 -2.8; 1636 -3.5; 1751 -4.2; 1873 -4.8; 2004 -5.2; 2145 -5.3; 2295 -4.6; 2455 -3.1; 2627 -2.4; 2811 -1.7; 3008 -0.5; 3219 0.7; 3444 1.1; 3685 0.2; 3943 -1.8; 4219 -4.0; 4514 -3.5; 4830 -1.5; 5168 -0.6; 5530 -2.1; 5917 0.6; 6331 2.2; 6775 0.9; 7249 0.8; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.899052133336809dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cypher Labs Astru IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.41 | 6.5 dB  |
| Peaking | 189 Hz  | 0.47 | -4.3 dB |
| Peaking | 1980 Hz | 1.35 | -9.3 dB |
| Peaking | 2034 Hz | 0.44 | 4.1 dB  |
| Peaking | 4384 Hz | 4.92 | -5.4 dB |
| Peaking | 3067 Hz | 2.11 | -0.9 dB |
| Peaking | 3347 Hz | 5.55 | 2.4 dB  |
| Peaking | 5575 Hz | 9.73 | -3.3 dB |
| Peaking | 6147 Hz | 5.14 | 2.3 dB  |
| Peaking | 8768 Hz | 1.33 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cypher%20Labs%20Astru%20IEM/Cypher%20Labs%20Astru%20IEM.png)