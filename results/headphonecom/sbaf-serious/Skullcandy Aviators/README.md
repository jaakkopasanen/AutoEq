# Skullcandy Aviators

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.1; 28 0.7; 31 -0.5; 34 -1.7; 37 -2.7; 41 -3.9; 45 -5.0; 49 -5.8; 54 -6.7; 60 -7.6; 66 -8.5; 72 -9.2; 79 -9.7; 87 -10.1; 96 -10.4; 106 -10.7; 116 -10.9; 128 -11.0; 141 -11.1; 155 -11.1; 170 -11.0; 187 -11.0; 206 -10.9; 227 -10.8; 249 -10.5; 274 -9.9; 302 -9.2; 332 -9.3; 365 -8.9; 402 -8.7; 442 -8.4; 486 -8.1; 535 -7.8; 588 -6.6; 647 -5.6; 712 -5.9; 783 -3.7; 861 -1.3; 947 0.3; 1042 -0.2; 1146 -1.3; 1261 -3.5; 1387 -5.6; 1526 -6.7; 1678 -7.4; 1846 -7.4; 2031 -6.8; 2234 -6.3; 2457 -5.6; 2703 -5.6; 2973 -6.6; 3270 -7.2; 3597 -6.6; 3957 -8.4; 4353 -12.4; 4788 -12.1; 5267 -8.1; 5793 -4.2; 6373 -1.3; 7010 -1.1; 7711 -2.0; 8482 -6.7; 9330 -10.0; 10263 -8.9; 11289 -7.1; 12418 -6.5; 13660 -6.0; 15026 -3.9; 16529 -0.1; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.0dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Aviators ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 133 Hz   | 0.47 | -11.3 dB |
| Peaking | 422 Hz   | 1.17 | -4.7 dB  |
| Peaking | 1991 Hz  | 1.43 | -6.7 dB  |
| Peaking | 4474 Hz  | 3.13 | -11.8 dB |
| Peaking | 10730 Hz | 1.51 | -8.9 dB  |
| Peaking | 22 Hz    | 2.32 | 5.6 dB   |
| Peaking | 992 Hz   | 2.69 | 7.3 dB   |
| Peaking | 998 Hz   | 1.04 | -3.4 dB  |
| Peaking | 7155 Hz  | 3.65 | 3.8 dB   |
| Peaking | 9040 Hz  | 6.37 | -4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Aviators/Skullcandy%20Aviators.png)