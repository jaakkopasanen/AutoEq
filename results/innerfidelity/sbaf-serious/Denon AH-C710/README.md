# Denon AH-C710

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.4dB
GraphicEQ: 21 -10.8; 23 -10.8; 25 -10.9; 28 -10.8; 31 -10.8; 34 -10.8; 37 -10.8; 41 -10.8; 45 -10.7; 49 -10.7; 54 -10.7; 60 -10.6; 66 -10.6; 72 -10.6; 79 -10.7; 87 -10.7; 96 -10.7; 106 -10.5; 116 -10.2; 128 -10.0; 141 -9.8; 155 -9.5; 170 -9.1; 187 -8.6; 206 -8.1; 227 -7.5; 249 -6.9; 274 -6.3; 302 -5.7; 332 -5.0; 365 -4.3; 402 -3.7; 442 -2.9; 486 -2.4; 535 -1.8; 588 -1.0; 647 -0.5; 712 -0.2; 783 0.2; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 0.1; 1387 -0.7; 1526 -1.4; 1678 -2.0; 1846 -2.2; 2031 -2.5; 2234 -3.2; 2457 -4.2; 2703 -5.3; 2973 -4.8; 3270 -2.8; 3597 -1.3; 3957 -2.0; 4353 -4.7; 4788 -7.4; 5267 -10.9; 5793 -9.8; 6373 -4.5; 7010 -1.9; 7711 -2.7; 8482 -6.8; 9330 -6.8; 10263 -0.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C710 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.11 | -11.0 dB |
| Peaking | 643 Hz   | 0.78 | 2.9 dB   |
| Peaking | 2589 Hz  | 2.09 | -4.7 dB  |
| Peaking | 5389 Hz  | 3.89 | -11.8 dB |
| Peaking | 9018 Hz  | 5.54 | -7.5 dB  |
| Peaking | 1705 Hz  | 5.38 | -1.2 dB  |
| Peaking | 2970 Hz  | 4.98 | -2.6 dB  |
| Peaking | 3483 Hz  | 1.88 | 2.3 dB   |
| Peaking | 4532 Hz  | 5.46 | -2.1 dB  |
| Peaking | 10646 Hz | 6.99 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C710/Denon%20AH-C710.png)