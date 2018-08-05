# Massdrop x HiFiMAN HE4XX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 10 -84; 20 4.0; 22 3.5; 23 3.2; 25 2.8; 26 2.7; 28 2.4; 30 2.2; 32 2.1; 35 1.9; 37 1.8; 40 1.8; 42 1.8; 45 1.7; 49 1.7; 52 1.7; 56 1.5; 59 1.2; 64 1.0; 68 0.9; 73 0.8; 78 0.7; 83 0.6; 89 0.4; 95 0.1; 102 -0.2; 109 -0.4; 117 -0.7; 125 -1.2; 134 -1.4; 143 -1.5; 153 -1.8; 164 -1.8; 175 -1.9; 188 -2.0; 201 -2.1; 215 -1.9; 230 -1.7; 246 -1.6; 263 -1.5; 282 -1.5; 301 -1.6; 323 -1.9; 345 -2.1; 369 -2.2; 395 -2.0; 423 -1.7; 452 -1.0; 484 -0.7; 518 -1.2; 554 -1.3; 593 -1.1; 635 -1.2; 679 -1.3; 726 -1.2; 777 -0.3; 832 -0.3; 890 -0.3; 952 -0.3; 1019 0.1; 1090 0.4; 1167 0.6; 1248 1.0; 1336 0.9; 1429 1.0; 1529 1.1; 1636 1.4; 1751 1.8; 1873 1.9; 2004 1.7; 2145 1.2; 2295 0.9; 2455 -0.1; 2627 -0.7; 2811 -1.0; 3008 -1.3; 3219 -1.0; 3444 0.0; 3685 -0.2; 3943 -0.1; 4219 -2.3; 4514 -3.3; 4830 -2.0; 5168 0.5; 5530 1.3; 5917 0.3; 6331 -2.8; 6775 -5.5; 7249 -6.0; 7756 -5.4; 8299 -5.8; 8880 -6.8; 9502 -5.2; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -1.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.6dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x HiFiMAN HE4XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 9 Hz     | 0.18 | 3.5 dB  |
| Peaking | 171 Hz   | 1.22 | -2.1 dB |
| Peaking | 376 Hz   | 1.56 | -1.7 dB |
| Peaking | 4453 Hz  | 9.01 | -2.9 dB |
| Peaking | 8147 Hz  | 2.6  | -7.0 dB |
| Peaking | 1849 Hz  | 1.87 | 2.1 dB  |
| Peaking | 2832 Hz  | 3.88 | -1.6 dB |
| Peaking | 5613 Hz  | 6.98 | 3.2 dB  |
| Peaking | 6767 Hz  | 8.03 | -3.1 dB |
| Peaking | 10851 Hz | 6.29 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20HiFiMAN%20HE4XX/Massdrop%20x%20HiFiMAN%20HE4XX.png)