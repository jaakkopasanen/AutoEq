# Samsung Level On

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -4.7; 22 -4.9; 23 -5.0; 25 -5.2; 26 -5.2; 28 -5.4; 30 -5.6; 32 -5.7; 35 -5.8; 37 -5.9; 40 -6.0; 42 -6.1; 45 -6.1; 49 -6.2; 52 -6.3; 56 -6.4; 59 -6.5; 64 -6.7; 68 -6.8; 73 -6.9; 78 -7.1; 83 -7.3; 89 -7.4; 95 -7.5; 102 -7.4; 109 -7.6; 117 -7.9; 125 -8.3; 134 -8.4; 143 -8.2; 153 -8.2; 164 -7.9; 175 -7.5; 188 -7.5; 201 -7.2; 215 -6.5; 230 -5.9; 246 -5.4; 263 -4.7; 282 -3.8; 301 -3.1; 323 -2.8; 345 -2.8; 369 -3.0; 395 -3.0; 423 -3.1; 452 -3.2; 484 -3.3; 518 -3.6; 554 -3.5; 593 -3.2; 635 -3.1; 679 -2.7; 726 -1.8; 777 -1.1; 832 -1.0; 890 -0.8; 952 -0.3; 1019 0.2; 1090 0.5; 1167 0.9; 1248 1.2; 1336 0.4; 1429 -0.2; 1529 -1.0; 1636 -1.9; 1751 -2.9; 1873 -3.4; 2004 -4.4; 2145 -5.2; 2295 -5.6; 2455 -4.9; 2627 -3.7; 2811 -2.4; 3008 -0.5; 3219 0.2; 3444 -0.4; 3685 -1.3; 3943 -1.1; 4219 -0.0; 4514 1.3; 4830 3.0; 5168 4.8; 5530 5.6; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.82373123174118dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.53 | -4.1 dB |
| Peaking | 138 Hz   | 0.49 | -7.5 dB |
| Peaking | 2256 Hz  | 2.81 | -5.9 dB |
| Peaking | 5767 Hz  | 3.14 | 6.7 dB  |
| Peaking | 314 Hz   | 3.84 | 1.7 dB  |
| Peaking | 579 Hz   | 2.3  | -2.0 dB |
| Peaking | 1211 Hz  | 2.44 | 2.1 dB  |
| Peaking | 1719 Hz  | 4.08 | -1.2 dB |
| Peaking | 24000 Hz | 1.8  | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Samsung%20Level%20On/Samsung%20Level%20On.png)