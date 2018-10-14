# Denon AH-D1100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.0; 23 -7.5; 25 -7.9; 28 -8.4; 31 -8.9; 34 -9.2; 37 -9.5; 41 -9.8; 45 -10.1; 49 -10.4; 54 -10.7; 60 -11.0; 66 -11.3; 72 -11.4; 79 -11.6; 87 -11.6; 96 -11.4; 106 -11.0; 116 -11.1; 128 -12.1; 141 -13.1; 155 -12.3; 170 -11.1; 187 -12.1; 206 -11.9; 227 -11.2; 249 -9.8; 274 -8.2; 302 -6.0; 332 -3.7; 365 -1.1; 402 1.4; 442 3.1; 486 3.4; 535 2.6; 588 1.5; 647 0.5; 712 -0.2; 783 -0.6; 861 -0.5; 947 -0.2; 1042 0.3; 1146 0.5; 1261 0.5; 1387 0.2; 1526 -0.9; 1678 -1.9; 1846 -3.0; 2031 -3.1; 2234 -1.9; 2457 0.4; 2703 2.8; 2973 4.9; 3270 2.2; 3597 3.5; 3957 6.0; 4353 3.6; 4788 -0.7; 5267 0.9; 5793 2.5; 6373 3.3; 7010 2.1; 7711 0.3; 8482 -0.5; 9330 -3.1; 10263 -3.9; 11289 -1.8; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 3 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 73 Hz    | 0.88 | -7.6 dB |
| Peaking | 146 Hz   | 1.85 | -7.9 dB |
| Peaking | 226 Hz   | 2.7  | -8.3 dB |
| Peaking | 23 Hz    | 0.34 | -6.5 dB |
| Peaking | 473 Hz   | 3.6  | 5.3 dB  |
| Peaking | 3885 Hz  | 4.51 | 6.3 dB  |
| Peaking | 6256 Hz  | 5.58 | 4.1 dB  |
| Peaking | 10086 Hz | 4.01 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D1100/Denon%20AH-D1100.png)