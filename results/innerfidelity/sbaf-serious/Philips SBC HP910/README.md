# Philips SBC HP910

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.6; 37 5.3; 40 4.7; 42 4.4; 45 4.0; 49 3.5; 52 3.1; 56 2.6; 59 2.5; 64 2.5; 68 2.2; 73 1.8; 78 2.1; 83 2.4; 89 1.6; 95 0.7; 102 -0.1; 109 -0.4; 117 -0.9; 125 -1.3; 134 -1.6; 143 -1.7; 153 -1.8; 164 -1.5; 175 -1.5; 188 -1.5; 201 -1.5; 215 -1.3; 230 -1.1; 246 -0.8; 263 -0.7; 282 -0.4; 301 -0.1; 323 0.0; 345 0.3; 369 0.5; 395 0.8; 423 1.1; 452 1.1; 484 1.2; 518 1.3; 554 1.1; 593 1.1; 635 1.7; 679 1.7; 726 1.1; 777 1.1; 832 0.7; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.6; 1336 -0.7; 1429 -0.8; 1529 -0.8; 1636 -1.1; 1751 -1.8; 1873 -1.9; 2004 -2.0; 2145 -2.6; 2295 -3.5; 2455 -4.0; 2627 -4.7; 2811 -5.4; 3008 -5.5; 3219 -4.6; 3444 -2.9; 3685 -1.4; 3943 -1.0; 4219 -0.1; 4514 -1.3; 4830 -4.4; 5168 -3.8; 5530 -0.9; 5917 -0.1; 6331 -2.8; 6775 -6.0; 7249 -6.8; 7756 -7.6; 8299 -8.5; 8880 -7.9; 9502 -4.4; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SBC HP910 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 22 Hz    |  0.42 | 6.2 dB  |
| Peaking | 146 Hz   |  1.57 | -2.7 dB |
| Peaking | 2515 Hz  |  2.04 | -3.4 dB |
| Peaking | 3021 Hz  |  4.56 | -3.3 dB |
| Peaking | 8021 Hz  |  2.78 | -9.0 dB |
| Peaking | 229 Hz   |  3.14 | -0.8 dB |
| Peaking | 576 Hz   |  1.47 | 1.6 dB  |
| Peaking | 5797 Hz  | 12.25 | 2.8 dB  |
| Peaking | 4962 Hz  | 10.43 | -3.8 dB |
| Peaking | 10707 Hz |  6.19 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SBC%20HP910/Philips%20SBC%20HP910.png)