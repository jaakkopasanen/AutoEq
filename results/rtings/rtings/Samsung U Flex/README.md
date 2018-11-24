# Samsung U Flex

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.7; 28 2.5; 31 2.4; 34 2.3; 37 2.2; 41 2.1; 45 2.1; 49 2.0; 54 1.8; 60 1.4; 66 1.0; 72 0.7; 79 0.3; 87 -0.2; 96 -0.7; 106 -1.4; 116 -2.0; 128 -2.5; 141 -3.0; 155 -3.3; 170 -3.3; 187 -3.3; 206 -3.5; 227 -3.7; 249 -3.4; 274 -3.2; 302 -2.8; 332 -2.5; 365 -2.2; 402 -1.9; 442 -1.6; 486 -1.2; 535 -0.8; 588 -0.2; 647 0.1; 712 0.5; 783 0.8; 861 0.8; 947 0.5; 1042 -0.5; 1146 -1.6; 1261 -2.6; 1387 -3.2; 1526 -3.8; 1678 -4.3; 1846 -4.9; 2031 -5.4; 2234 -5.5; 2457 -5.6; 2703 -6.5; 2973 -7.2; 3270 -7.0; 3597 -6.6; 3957 -6.1; 4353 -6.1; 4788 -4.8; 5267 -3.6; 5793 -2.8; 6373 -2.4; 7010 0.7; 7711 0.3; 8482 -1.5; 9330 -9.3; 10263 -11.8; 11289 -8.2; 12418 -4.2; 13660 -2.6; 15026 -5.5; 16529 -9.1; 18182 -6.5; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung U Flex GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung U Flex ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.38 | 2.8 dB   |
| Peaking | 187 Hz   | 0.82 | -4.2 dB  |
| Peaking | 2949 Hz  | 0.96 | -7.3 dB  |
| Peaking | 10268 Hz | 4.27 | -12.0 dB |
| Peaking | 16884 Hz | 1.89 | -9.6 dB  |
| Peaking | 844 Hz   | 2.3  | 2.3 dB   |
| Peaking | 1468 Hz  | 2.44 | -1.5 dB  |
| Peaking | 4504 Hz  | 4.38 | -1.6 dB  |
| Peaking | 7727 Hz  | 3.53 | 4.1 dB   |
| Peaking | 9343 Hz  | 8.45 | -3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Samsung%20U%20Flex/Samsung%20U%20Flex.png)