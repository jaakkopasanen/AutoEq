# Reid and Heath Acoustics SA-850

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.5; 26 5.2; 28 4.4; 30 3.7; 32 3.1; 35 2.3; 37 2.0; 40 1.6; 42 1.3; 45 1.1; 49 0.9; 52 0.9; 56 0.8; 59 0.8; 64 0.8; 68 0.8; 73 0.7; 78 0.6; 83 0.6; 89 0.5; 95 0.5; 102 0.7; 109 0.7; 117 0.4; 125 0.1; 134 -0.1; 143 -0.5; 153 -0.7; 164 -0.7; 175 -0.9; 188 -1.2; 201 -1.5; 215 -2.0; 230 -2.7; 246 -3.0; 263 -3.2; 282 -3.3; 301 -3.2; 323 -2.9; 345 -2.9; 369 -3.1; 395 -3.5; 423 -3.6; 452 -3.9; 484 -4.4; 518 -4.7; 554 -4.7; 593 -4.5; 635 -4.3; 679 -4.1; 726 -3.2; 777 -2.1; 832 -1.2; 890 -0.2; 952 0.3; 1019 -0.1; 1090 -1.1; 1167 -2.2; 1248 -2.6; 1336 -2.8; 1429 -4.2; 1529 -4.6; 1636 -4.1; 1751 -3.0; 1873 -1.9; 2004 -0.4; 2145 0.7; 2295 2.0; 2455 3.8; 2627 5.1; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.9; 3685 5.9; 3943 6.0; 4219 6.0; 4514 5.6; 4830 -0.1; 5168 -2.7; 5530 -2.6; 5917 -1.9; 6331 -2.0; 6775 -2.4; 7249 -2.4; 7756 -0.9; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Reid and Heath Acoustics SA-850 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.96 | 6.3 dB  |
| Peaking | 274 Hz  | 1.69 | -2.8 dB |
| Peaking | 548 Hz  | 1.82 | -4.7 dB |
| Peaking | 1562 Hz | 2.93 | -5.4 dB |
| Peaking | 3177 Hz | 1.97 | 7.4 dB  |
| Peaking | 875 Hz  | 1.95 | -1.4 dB |
| Peaking | 927 Hz  | 4.33 | 3.1 dB  |
| Peaking | 4391 Hz | 3.62 | 8.8 dB  |
| Peaking | 5063 Hz | 1.92 | -7.2 dB |
| Peaking | 9047 Hz | 4.87 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Reid%20and%20Heath%20Acoustics%20SA-850/Reid%20and%20Heath%20Acoustics%20SA-850.png)