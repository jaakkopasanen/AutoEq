# WalMart Three DOllar Buds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 5.7; 206 4.0; 227 2.4; 249 0.8; 274 -0.5; 302 -1.9; 332 -3.0; 365 -3.9; 402 -4.3; 442 -3.8; 486 -3.2; 535 -2.3; 588 -0.3; 647 0.1; 712 -0.1; 783 -0.0; 861 0.3; 947 0.7; 1042 0.3; 1146 0.6; 1261 0.6; 1387 0.6; 1526 0.5; 1678 0.5; 1846 1.6; 2031 3.4; 2234 5.7; 2457 6.0; 2703 5.1; 2973 3.7; 3270 3.6; 3597 5.0; 3957 5.0; 4353 3.6; 4788 3.5; 5267 3.4; 5793 3.5; 6373 1.1; 7010 1.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`WalMart Three DOllar Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `WalMart Three DOllar Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 71 Hz   | 0.16 | 6.6 dB  |
| Peaking | 306 Hz  | 2.28 | -4.0 dB |
| Peaking | 427 Hz  | 1.63 | -6.6 dB |
| Peaking | 2379 Hz | 3.66 | 5.1 dB  |
| Peaking | 4066 Hz | 1.39 | 4.4 dB  |
| Peaking | 176 Hz  | 5.62 | 1.4 dB  |
| Peaking | 1633 Hz | 5.8  | -0.8 dB |
| Peaking | 5765 Hz | 8.65 | 1.7 dB  |
| Peaking | 8600 Hz | 1.3  | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/WalMart%20Three%20DOllar%20Buds/WalMart%20Three%20DOllar%20Buds.png)