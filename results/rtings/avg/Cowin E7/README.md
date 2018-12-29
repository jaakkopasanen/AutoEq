# Cowin E7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.4; 23 -0.8; 25 -0.3; 28 0.2; 31 0.5; 34 0.9; 37 1.1; 41 1.3; 45 1.4; 49 1.4; 54 1.3; 60 1.1; 66 0.8; 72 0.4; 79 0.1; 87 -0.2; 96 -0.7; 106 -1.1; 116 -1.5; 128 -1.9; 141 -2.3; 155 -2.6; 170 -2.9; 187 -3.1; 206 -3.2; 227 -3.4; 249 -3.4; 274 -3.4; 302 -3.7; 332 -3.8; 365 -3.5; 402 -3.4; 442 -3.2; 486 -2.9; 535 -2.6; 588 -2.3; 647 -2.1; 712 -1.9; 783 -1.6; 861 -0.1; 947 0.4; 1042 -0.5; 1146 -0.0; 1261 2.1; 1387 4.1; 1526 5.8; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.9; 4788 3.7; 5267 4.2; 5793 5.3; 6373 4.1; 7010 2.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -1.4; 13660 -1.9; 15026 0.0; 16529 0.0; 18182 -1.1; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 1.13 | -2.7 dB |
| Peaking | 53 Hz    | 0.56 | 2.8 dB  |
| Peaking | 272 Hz   | 0.29 | -4.0 dB |
| Peaking | 1775 Hz  | 1.32 | 5.9 dB  |
| Peaking | 3804 Hz  | 1.02 | 5.5 dB  |
| Peaking | 1075 Hz  | 2.26 | 2.2 dB  |
| Peaking | 1129 Hz  | 4.94 | -3.8 dB |
| Peaking | 6029 Hz  | 5.95 | 3.5 dB  |
| Peaking | 9625 Hz  | 0.61 | -1.2 dB |
| Peaking | 19762 Hz | 3    | -5.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E7/Cowin%20E7.png)