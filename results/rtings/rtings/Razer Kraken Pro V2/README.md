# Razer Kraken Pro V2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.4; 28 4.4; 31 3.5; 34 2.7; 37 2.0; 41 1.1; 45 0.1; 49 -0.8; 54 -1.8; 60 -2.8; 66 -3.7; 72 -4.3; 79 -4.9; 87 -5.4; 96 -5.7; 106 -6.0; 116 -6.2; 128 -6.3; 141 -6.4; 155 -6.4; 170 -6.3; 187 -6.0; 206 -5.6; 227 -5.1; 249 -4.2; 274 -3.6; 302 -6.1; 332 -6.2; 365 -5.3; 402 -4.5; 442 -3.9; 486 -3.7; 535 -3.5; 588 -2.8; 647 -2.6; 712 -1.5; 783 -1.1; 861 -1.6; 947 -0.7; 1042 0.4; 1146 1.8; 1261 3.2; 1387 3.9; 1526 3.3; 1678 3.6; 1846 3.4; 2031 2.5; 2234 3.9; 2457 5.6; 2703 5.9; 2973 6.0; 3270 5.2; 3597 4.2; 3957 5.1; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.9; 6373 5.3; 7010 2.5; 7711 0.3; 8482 -3.2; 9330 -6.0; 10263 -3.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken Pro V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken Pro V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.72 | 6.8 dB  |
| Peaking | 112 Hz  | 0.52 | -6.6 dB |
| Peaking | 409 Hz  | 0.92 | -3.5 dB |
| Peaking | 2496 Hz | 0.83 | 5.3 dB  |
| Peaking | 5225 Hz | 2.71 | 5.1 dB  |
| Peaking | 173 Hz  | 4.96 | -0.4 dB |
| Peaking | 1334 Hz | 5.05 | 2.1 dB  |
| Peaking | 2045 Hz | 8    | -2.4 dB |
| Peaking | 6421 Hz | 5.76 | 2.7 dB  |
| Peaking | 9218 Hz | 4.17 | -7.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Razer%20Kraken%20Pro%20V2/Razer%20Kraken%20Pro%20V2.png)