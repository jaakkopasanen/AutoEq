# Razer Kraken Pro V2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.4; 28 4.4; 31 3.5; 34 2.7; 37 2.0; 41 1.1; 45 0.1; 49 -0.8; 54 -1.8; 60 -2.8; 66 -3.7; 72 -4.3; 79 -4.9; 87 -5.4; 96 -5.7; 106 -6.0; 116 -6.2; 128 -6.3; 141 -6.4; 155 -6.4; 170 -6.3; 187 -6.0; 206 -5.6; 227 -5.1; 249 -4.2; 274 -3.6; 302 -6.1; 332 -6.2; 365 -5.3; 402 -4.5; 442 -3.9; 486 -3.7; 535 -3.5; 588 -2.8; 647 -2.6; 712 -1.5; 783 -1.1; 861 -1.6; 947 -0.7; 1042 0.4; 1146 1.8; 1261 3.2; 1387 3.9; 1526 3.3; 1678 3.6; 1846 3.4; 2031 2.5; 2234 3.9; 2457 5.6; 2703 5.8; 2973 6.0; 3270 4.5; 3597 3.2; 3957 3.8; 4353 5.7; 4788 4.9; 5267 4.7; 5793 3.7; 6373 4.2; 7010 2.5; 7711 0.3; 8482 -2.3; 9330 -3.3; 10263 -0.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.1; 16529 -1.0; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken Pro V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken Pro V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.72 | 6.8 dB  |
| Peaking | 110 Hz  | 0.53 | -6.5 dB |
| Peaking | 416 Hz  | 0.81 | -3.5 dB |
| Peaking | 2333 Hz | 0.75 | 5.0 dB  |
| Peaking | 5006 Hz | 2.42 | 3.6 dB  |
| Peaking | 1329 Hz | 2.95 | 4.5 dB  |
| Peaking | 1345 Hz | 1.48 | -2.7 dB |
| Peaking | 6583 Hz | 7.7  | 2.4 dB  |
| Peaking | 6608 Hz | 5.28 | 0.4 dB  |
| Peaking | 9025 Hz | 3.9  | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Kraken%20Pro%20V2/Razer%20Kraken%20Pro%20V2.png)