# Ultimate Ears UE500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -8.6; 22 -8.6; 23 -8.6; 25 -8.5; 26 -8.4; 28 -8.3; 30 -8.2; 32 -8.1; 35 -7.9; 37 -7.7; 40 -7.5; 42 -7.4; 45 -7.2; 49 -6.9; 52 -6.7; 56 -6.5; 59 -6.3; 64 -6.0; 68 -5.9; 73 -5.7; 78 -5.6; 83 -5.5; 89 -5.6; 95 -5.8; 102 -6.0; 109 -6.1; 117 -6.3; 125 -6.6; 134 -6.7; 143 -6.8; 153 -6.6; 164 -6.5; 175 -6.2; 188 -5.9; 201 -5.7; 215 -5.2; 230 -4.9; 246 -4.5; 263 -4.3; 282 -3.8; 301 -3.5; 323 -3.1; 345 -2.7; 369 -2.4; 395 -2.0; 423 -1.6; 452 -1.2; 484 -1.0; 518 -0.7; 554 -0.3; 593 0.2; 635 0.3; 679 0.3; 726 0.5; 777 0.8; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.1; 1336 -1.3; 1429 -1.3; 1529 -1.5; 1636 -2.0; 1751 -2.5; 1873 -2.7; 2004 -3.1; 2145 -3.5; 2295 -3.4; 2455 -2.9; 2627 -1.7; 2811 0.2; 3008 2.8; 3219 5.1; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.4; 6775 2.5; 7249 0.1; 7756 -0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 9 Hz    | 0.7  | -8.0 dB |
| Peaking | 33 Hz   | 0.44 | -6.2 dB |
| Peaking | 165 Hz  | 0.82 | -5.5 dB |
| Peaking | 2267 Hz | 1.73 | -6.7 dB |
| Peaking | 3965 Hz | 1.11 | 8.2 dB  |
| Peaking | 741 Hz  | 2.1  | 1.7 dB  |
| Peaking | 9490 Hz | 1.38 | -0.5 dB |
| Peaking | 2103 Hz | 0.12 | -0.3 dB |
| Peaking | 6240 Hz | 3.52 | 4.5 dB  |
| Peaking | 7189 Hz | 3.14 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE500/Ultimate%20Ears%20UE500.png)