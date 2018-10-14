# Denon AH-C360

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.7dB
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.2; 28 -7.5; 31 -7.7; 34 -7.9; 37 -8.1; 41 -8.3; 45 -8.4; 49 -8.7; 54 -8.9; 60 -9.2; 66 -9.4; 72 -9.7; 79 -10.0; 87 -10.1; 96 -10.2; 106 -10.3; 116 -10.3; 128 -10.4; 141 -10.3; 155 -10.2; 170 -10.1; 187 -9.8; 206 -9.4; 227 -9.0; 249 -8.5; 274 -8.0; 302 -7.3; 332 -6.5; 365 -5.9; 402 -5.4; 442 -4.8; 486 -4.2; 535 -3.3; 588 -2.5; 647 -1.5; 712 -0.8; 783 -0.2; 861 0.2; 947 0.0; 1042 0.2; 1146 0.3; 1261 0.5; 1387 0.3; 1526 -0.5; 1678 -0.6; 1846 0.5; 2031 -0.1; 2234 -0.2; 2457 0.1; 2703 0.5; 2973 0.6; 3270 0.4; 3597 -0.3; 3957 -2.1; 4353 -4.4; 4788 -5.9; 5267 -6.5; 5793 -7.8; 6373 -7.4; 7010 -5.7; 7711 -6.2; 8482 -8.1; 9330 -6.8; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.2; 16529 -0.1; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.7dB` and instead set Global volume in the UI for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.3  | -7.8 dB |
| Peaking | 155 Hz   | 0.73 | -5.6 dB |
| Peaking | 318 Hz   | 1.24 | -3.2 dB |
| Peaking | 5758 Hz  | 2.19 | -7.8 dB |
| Peaking | 8646 Hz  | 4.16 | -7.4 dB |
| Peaking | 501 Hz   | 2.89 | -1.2 dB |
| Peaking | 876 Hz   | 1.27 | 1.2 dB  |
| Peaking | 3213 Hz  | 2.4  | 1.7 dB  |
| Peaking | 4463 Hz  | 5.55 | -2.2 dB |
| Peaking | 10932 Hz | 6.35 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C360/Denon%20AH-C360.png)