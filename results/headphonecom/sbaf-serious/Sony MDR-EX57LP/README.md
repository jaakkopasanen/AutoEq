# Sony MDR-EX57LP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 0.0; 23 0.3; 25 -0.1; 28 -0.7; 31 -1.2; 34 -1.7; 37 -2.1; 41 -2.6; 45 -3.0; 49 -3.3; 54 -3.8; 60 -4.3; 66 -4.7; 72 -5.2; 79 -5.5; 87 -5.8; 96 -6.1; 106 -6.4; 116 -6.6; 128 -6.9; 141 -6.9; 155 -7.0; 170 -7.0; 187 -6.9; 206 -6.7; 227 -6.4; 249 -6.1; 274 -5.7; 302 -5.2; 332 -4.6; 365 -4.0; 402 -3.4; 442 -2.9; 486 -2.3; 535 -1.7; 588 -1.0; 647 -0.5; 712 -0.2; 783 0.1; 861 0.7; 947 0.3; 1042 -0.1; 1146 -0.6; 1261 -1.2; 1387 -2.1; 1526 -3.2; 1678 -3.9; 1846 -4.1; 2031 -3.5; 2234 -3.1; 2457 -3.4; 2703 -3.9; 2973 -4.0; 3270 -2.6; 3597 -1.4; 3957 -2.2; 4353 -4.8; 4788 -7.2; 5267 -8.3; 5793 -4.4; 6373 0.2; 7010 2.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.8; 11289 -3.6; 12418 -2.1; 13660 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6dB` and instead set Global volume in the UI for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX57LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 109 Hz   | 0.57 | -5.9 dB |
| Peaking | 248 Hz   | 1.06 | -3.6 dB |
| Peaking | 1762 Hz  | 2.95 | -3.8 dB |
| Peaking | 2763 Hz  | 2.82 | -3.4 dB |
| Peaking | 5047 Hz  | 4.41 | -8.9 dB |
| Peaking | 19 Hz    | 2.39 | 1.6 dB  |
| Peaking | 855 Hz   | 3.53 | 1.6 dB  |
| Peaking | 5631 Hz  | 8.22 | -2.3 dB |
| Peaking | 6817 Hz  | 4.77 | 3.6 dB  |
| Peaking | 11523 Hz | 5.31 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-EX57LP/Sony%20MDR-EX57LP.png)