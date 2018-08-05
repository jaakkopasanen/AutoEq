# Audeze LCD-2 Rev 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 10 -84; 20 0.5; 22 0.5; 23 0.5; 25 0.5; 26 0.5; 28 0.6; 30 0.6; 32 0.7; 35 0.7; 37 0.7; 40 0.6; 42 0.6; 45 0.7; 49 0.9; 52 1.0; 56 0.6; 59 0.1; 64 -0.2; 68 -0.2; 73 -0.3; 78 -0.3; 83 -0.3; 89 -0.4; 95 -0.7; 102 -1.2; 109 -1.4; 117 -1.7; 125 -2.1; 134 -2.5; 143 -2.7; 153 -3.0; 164 -3.1; 175 -3.2; 188 -3.5; 201 -3.5; 215 -3.4; 230 -3.3; 246 -3.1; 263 -3.1; 282 -3.2; 301 -3.1; 323 -2.7; 345 -2.3; 369 -2.2; 395 -2.3; 423 -2.2; 452 -2.3; 484 -2.5; 518 -2.6; 554 -2.4; 593 -2.3; 635 -2.3; 679 -2.5; 726 -2.3; 777 -2.2; 832 -2.2; 890 -1.7; 952 -0.7; 1019 0.1; 1090 0.6; 1167 1.4; 1248 0.7; 1336 -0.1; 1429 -1.0; 1529 -1.8; 1636 -2.3; 1751 -2.6; 1873 -1.1; 2004 -0.3; 2145 -0.1; 2295 -1.4; 2455 -0.4; 2627 1.0; 2811 0.8; 3008 0.7; 3219 0.6; 3444 2.0; 3685 2.9; 3943 3.8; 4219 3.4; 4514 2.7; 4830 1.0; 5168 0.2; 5530 0.0; 5917 -0.2; 6331 0.2; 6775 0.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -2.5; 18692 -3.8; 20000 -3.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.3dB` and instead set Global volume in the UI for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 212 Hz   | 0.9  | -3.6 dB |
| Peaking | 618 Hz   | 1.69 | -2.1 dB |
| Peaking | 1701 Hz  | 6.31 | -2.8 dB |
| Peaking | 4001 Hz  | 3.53 | 4.0 dB  |
| Peaking | 28919 Hz | 2    | -4.3 dB |
| Peaking | 42 Hz    | 1.21 | 1.1 dB  |
| Peaking | 836 Hz   | 6.27 | -1.1 dB |
| Peaking | 1149 Hz  | 6.09 | 2.1 dB  |
| Peaking | 5676 Hz  | 4.56 | -0.7 dB |
| Peaking | 7087 Hz  | 9.26 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)