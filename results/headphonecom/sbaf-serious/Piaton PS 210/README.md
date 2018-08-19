# Piaton PS 210

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.4; 52 5.1; 56 4.6; 59 4.3; 64 3.7; 68 3.4; 73 2.9; 78 2.5; 83 2.1; 89 1.7; 95 1.4; 102 1.0; 109 0.7; 117 0.5; 125 0.1; 134 -0.2; 143 -0.5; 153 -0.7; 164 -0.9; 175 -1.2; 188 -1.3; 201 -1.5; 215 -1.6; 230 -1.7; 246 -1.9; 263 -1.9; 282 -1.9; 301 -1.8; 323 -1.9; 345 -1.8; 369 -1.9; 395 -1.9; 423 -2.1; 452 -2.2; 484 -1.9; 518 -1.8; 554 -1.6; 593 -1.7; 635 -1.7; 679 -1.8; 726 -1.7; 777 -1.4; 832 -1.1; 890 -0.8; 952 -0.4; 1019 0.0; 1090 0.5; 1167 1.0; 1248 1.3; 1336 1.5; 1429 1.5; 1529 1.2; 1636 0.8; 1751 0.2; 1873 -0.7; 2004 -1.8; 2145 -3.0; 2295 -4.0; 2455 -4.1; 2627 -2.2; 2811 0.5; 3008 3.3; 3219 5.7; 3444 6.0; 3685 6.0; 3943 4.8; 4219 2.1; 4514 0.5; 4830 1.9; 5168 4.9; 5530 5.9; 5917 3.8; 6331 0.8; 6775 -0.0; 7249 -2.9; 7756 -6.2; 8299 -7.1; 8880 -3.8; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.104854686618013dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Piaton PS 210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 33 Hz   |  0.84 | 7.0 dB  |
| Peaking | 2398 Hz |  4.11 | -5.9 dB |
| Peaking | 3420 Hz |  3.12 | 7.2 dB  |
| Peaking | 5526 Hz |  5.93 | 6.3 dB  |
| Peaking | 8078 Hz |  5.19 | -8.3 dB |
| Peaking | 27 Hz   |  0.31 | 3.4 dB  |
| Peaking | 32 Hz   |  1.43 | -4.2 dB |
| Peaking | 321 Hz  |  0.31 | -2.4 dB |
| Peaking | 1330 Hz |  2.09 | 2.6 dB  |
| Peaking | 4531 Hz | 14.02 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Piaton%20PS%20210/Piaton%20PS%20210.png)