# Massdrop NuForce Every Day Car

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -12.8; 22 -12.8; 23 -12.8; 25 -12.7; 26 -12.6; 28 -12.5; 30 -12.4; 32 -12.2; 35 -12.1; 37 -11.9; 40 -11.8; 42 -11.6; 45 -11.5; 49 -11.2; 52 -11.1; 56 -10.9; 59 -10.8; 64 -10.6; 68 -10.4; 73 -10.2; 78 -10.1; 83 -9.9; 89 -9.9; 95 -9.7; 102 -9.5; 109 -9.2; 117 -8.9; 125 -8.8; 134 -8.6; 143 -8.4; 153 -8.2; 164 -8.0; 175 -7.6; 188 -7.3; 201 -7.0; 215 -6.6; 230 -6.1; 246 -5.8; 263 -5.5; 282 -5.0; 301 -4.6; 323 -4.2; 345 -3.8; 369 -3.4; 395 -2.9; 423 -2.3; 452 -1.9; 484 -1.6; 518 -1.4; 554 -0.9; 593 -0.4; 635 -0.1; 679 -0.1; 726 0.1; 777 0.3; 832 0.1; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.5; 1429 -2.1; 1529 -2.5; 1636 -3.0; 1751 -3.1; 1873 -3.2; 2004 -3.1; 2145 -3.0; 2295 -2.8; 2455 -2.2; 2627 -1.5; 2811 -0.5; 3008 1.3; 3219 3.3; 3444 5.5; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -0.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999892437422dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop NuForce Every Day Car ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.17 | -12.5 dB |
| Peaking | 181 Hz  | 0.8  | -3.4 dB  |
| Peaking | 2158 Hz | 1.53 | -5.2 dB  |
| Peaking | 4324 Hz | 1.2  | 7.8 dB   |
| Peaking | 787 Hz  | 1.01 | 3.9 dB   |
| Peaking | 844 Hz  | 0.57 | -2.6 dB  |
| Peaking | 2103 Hz | 5.73 | 1.2 dB   |
| Peaking | 6305 Hz | 3.61 | 4.1 dB   |
| Peaking | 7632 Hz | 1.48 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20NuForce%20Every%20Day%20Car/Massdrop%20NuForce%20Every%20Day%20Car.png)