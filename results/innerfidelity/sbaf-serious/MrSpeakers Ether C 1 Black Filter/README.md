# MrSpeakers Ether C 1 Black Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.7; 22 2.6; 23 2.5; 25 2.5; 26 2.5; 28 2.5; 30 2.6; 32 2.7; 35 3.0; 37 3.2; 40 3.6; 42 3.9; 45 4.5; 49 4.6; 52 4.1; 56 3.4; 59 3.2; 64 3.1; 68 3.7; 73 4.7; 78 4.5; 83 3.6; 89 3.4; 95 3.3; 102 2.5; 109 2.5; 117 2.5; 125 2.2; 134 2.4; 143 2.9; 153 3.4; 164 3.8; 175 2.0; 188 1.8; 201 1.5; 215 1.2; 230 1.0; 246 0.8; 263 0.7; 282 0.6; 301 0.5; 323 0.5; 345 0.7; 369 1.0; 395 1.4; 423 1.9; 452 2.3; 484 2.3; 518 2.0; 554 1.7; 593 1.5; 635 1.3; 679 1.0; 726 0.9; 777 0.8; 832 0.5; 890 -0.2; 952 -0.1; 1019 0.2; 1090 0.7; 1167 1.1; 1248 1.0; 1336 0.8; 1429 0.9; 1529 0.7; 1636 0.2; 1751 0.1; 1873 0.9; 2004 1.3; 2145 1.2; 2295 1.5; 2455 1.4; 2627 1.4; 2811 1.5; 3008 1.7; 3219 1.6; 3444 1.7; 3685 2.2; 3943 2.4; 4219 2.0; 4514 2.1; 4830 3.2; 5168 5.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C 1 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.3  | 1.9 dB  |
| Peaking | 65 Hz   | 0.73 | 3.2 dB  |
| Peaking | 159 Hz  | 4.61 | 2.4 dB  |
| Peaking | 500 Hz  | 1.8  | 2.0 dB  |
| Peaking | 5634 Hz | 2.3  | 6.2 dB  |
| Peaking | 2255 Hz | 3.93 | 0.5 dB  |
| Peaking | 5296 Hz | 0.77 | 3.2 dB  |
| Peaking | 4818 Hz | 2.2  | -3.5 dB |
| Peaking | 9091 Hz | 1.21 | -1.6 dB |
| Peaking | 7684 Hz | 4.95 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20C%201%20Black%20Filter/MrSpeakers%20Ether%20C%201%20Black%20Filter.png)