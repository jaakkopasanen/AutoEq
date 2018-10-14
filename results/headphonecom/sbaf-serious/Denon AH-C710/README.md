# Denon AH-C710

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.4dB
GraphicEQ: 21 -12.1; 23 -12.0; 25 -11.9; 28 -11.9; 31 -11.9; 34 -11.8; 37 -11.8; 41 -11.7; 45 -11.6; 49 -11.6; 54 -11.6; 60 -11.5; 66 -11.5; 72 -11.4; 79 -11.4; 87 -11.2; 96 -11.1; 106 -10.8; 116 -10.6; 128 -10.3; 141 -10.0; 155 -9.6; 170 -9.2; 187 -8.7; 206 -8.2; 227 -7.5; 249 -6.9; 274 -6.3; 302 -5.5; 332 -4.8; 365 -4.3; 402 -3.6; 442 -3.0; 486 -2.3; 535 -1.7; 588 -1.1; 647 -0.5; 712 -0.1; 783 0.2; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.7; 1387 -1.4; 1526 -2.2; 1678 -2.7; 1846 -3.0; 2031 -3.7; 2234 -4.3; 2457 -5.2; 2703 -6.1; 2973 -5.5; 3270 -3.0; 3597 -0.5; 3957 -0.7; 4353 -2.7; 4788 -4.4; 5267 -6.2; 5793 -10.3; 6373 -7.7; 7010 -3.3; 7711 -1.2; 8482 -1.3; 9330 -3.8; 10263 -4.1; 11289 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.4dB` and instead set Global volume in the UI for both channels to **-4**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.2  | -11.8 dB |
| Peaking | 171 Hz   | 0.67 | -4.4 dB  |
| Peaking | 2534 Hz  | 2.1  | -5.7 dB  |
| Peaking | 5869 Hz  | 3.59 | -10.4 dB |
| Peaking | 22223 Hz | 2.18 | -1.8 dB  |
| Peaking | 796 Hz   | 2.55 | 1.3 dB   |
| Peaking | 1526 Hz  | 1.11 | 1.4 dB   |
| Peaking | 1644 Hz  | 2.33 | -2.7 dB  |
| Peaking | 9774 Hz  | 4.4  | -6.8 dB  |
| Peaking | 9848 Hz  | 1.51 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C710/Denon%20AH-C710.png)