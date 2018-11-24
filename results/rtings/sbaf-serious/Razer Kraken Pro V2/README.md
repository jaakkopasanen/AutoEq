# Razer Kraken Pro V2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.5; 28 4.6; 31 3.6; 34 2.7; 37 1.9; 41 0.9; 45 -0.2; 49 -1.1; 54 -2.1; 60 -3.1; 66 -3.8; 72 -4.3; 79 -4.7; 87 -5.0; 96 -5.3; 106 -5.5; 116 -5.7; 128 -5.8; 141 -5.8; 155 -5.8; 170 -5.6; 187 -5.4; 206 -5.1; 227 -4.6; 249 -3.7; 274 -2.9; 302 -5.3; 332 -5.3; 365 -4.3; 402 -3.4; 442 -2.8; 486 -2.5; 535 -2.4; 588 -1.7; 647 -1.6; 712 -0.6; 783 -0.7; 861 -1.4; 947 -0.6; 1042 0.5; 1146 2.0; 1261 3.4; 1387 3.8; 1526 2.9; 1678 3.2; 1846 3.4; 2031 2.9; 2234 4.4; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.8; 9330 -4.5; 10263 -0.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken Pro V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken Pro V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.75 | 7.2 dB  |
| Peaking | 108 Hz  | 0.44 | -6.3 dB |
| Peaking | 375 Hz  | 1.34 | -2.2 dB |
| Peaking | 2802 Hz | 0.9  | 6.0 dB  |
| Peaking | 5395 Hz | 2.87 | 4.6 dB  |
| Peaking | 897 Hz  | 4.72 | -1.7 dB |
| Peaking | 1305 Hz | 3.95 | 2.4 dB  |
| Peaking | 2061 Hz | 7.68 | -1.8 dB |
| Peaking | 6430 Hz | 7.17 | 2.4 dB  |
| Peaking | 9029 Hz | 4.67 | -6.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Razer%20Kraken%20Pro%20V2/Razer%20Kraken%20Pro%20V2.png)