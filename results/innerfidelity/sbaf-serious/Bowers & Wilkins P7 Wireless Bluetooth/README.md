# Bowers & Wilkins P7 Wireless Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 0.0; 23 2.3; 25 1.8; 28 1.3; 31 0.8; 34 0.4; 37 0.1; 41 -0.2; 45 -0.4; 49 -0.6; 54 -0.8; 60 -1.0; 66 -1.2; 72 -1.4; 79 -1.6; 87 -1.8; 96 -2.2; 106 -2.3; 116 -2.3; 128 -2.4; 141 -2.5; 155 -2.7; 170 -2.7; 187 -2.4; 206 -2.5; 227 -2.3; 249 -2.0; 274 -1.5; 302 -0.5; 332 0.1; 365 0.5; 402 0.7; 442 0.7; 486 0.6; 535 0.6; 588 0.9; 647 0.8; 712 0.6; 783 0.6; 861 0.2; 947 -0.0; 1042 0.4; 1146 0.3; 1261 -0.2; 1387 -0.9; 1526 -1.8; 1678 -2.4; 1846 -2.5; 2031 -1.9; 2234 -1.8; 2457 -2.0; 2703 -1.0; 2973 2.5; 3270 5.5; 3597 3.2; 3957 0.1; 4353 -0.4; 4788 0.2; 5267 1.7; 5793 1.9; 6373 2.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.6dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.97 | 3.1 dB  |
| Peaking | 135 Hz  | 0.91 | -2.9 dB |
| Peaking | 2127 Hz | 1.66 | -2.8 dB |
| Peaking | 3276 Hz | 5.54 | 6.9 dB  |
| Peaking | 6501 Hz | 5.13 | 3.8 dB  |
| Peaking | 238 Hz  | 2.04 | -1.9 dB |
| Peaking | 410 Hz  | 0.66 | 1.5 dB  |
| Peaking | 1187 Hz | 3.36 | 1.1 dB  |
| Peaking | 1695 Hz | 1.4  | -1.4 dB |
| Peaking | 2099 Hz | 5.46 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7%20Wireless%20Bluetooth/Bowers%20&%20Wilkins%20P7%20Wireless%20Bluetooth.png)