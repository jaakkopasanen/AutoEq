# Logitech G930

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 1.9; 28 1.3; 31 0.9; 34 0.7; 37 0.7; 41 0.8; 45 1.0; 49 1.1; 54 1.3; 60 1.7; 66 1.7; 72 1.6; 79 1.2; 87 0.7; 96 0.1; 106 -0.3; 116 -0.5; 128 -0.5; 141 -0.3; 155 0.2; 170 1.0; 187 2.0; 206 3.4; 227 5.4; 249 6.0; 274 6.0; 302 5.9; 332 3.8; 365 1.9; 402 0.7; 442 0.2; 486 -0.4; 535 -0.8; 588 -0.9; 647 -1.0; 712 -0.8; 783 -0.7; 861 -0.5; 947 -0.2; 1042 0.1; 1146 0.9; 1261 1.7; 1387 2.5; 1526 1.8; 1678 1.5; 1846 1.6; 2031 1.9; 2234 2.8; 2457 4.0; 2703 5.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 0.1; 4788 -1.8; 5267 0.4; 5793 0.8; 6373 -3.3; 7010 1.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.8; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G930 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G930 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.64 | 3.3 dB  |
| Peaking | 63 Hz   | 3.18 | 1.8 dB  |
| Peaking | 263 Hz  | 2.53 | 7.0 dB  |
| Peaking | 2828 Hz | 2.29 | 5.8 dB  |
| Peaking | 3730 Hz | 6.08 | 4.6 dB  |
| Peaking | 126 Hz  | 3.49 | -1.2 dB |
| Peaking | 549 Hz  | 3.37 | -1.2 dB |
| Peaking | 768 Hz  | 2.19 | -1.0 dB |
| Peaking | 1377 Hz | 3.63 | 2.1 dB  |
| Peaking | 4695 Hz | 9.05 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G930/Logitech%20G930.png)