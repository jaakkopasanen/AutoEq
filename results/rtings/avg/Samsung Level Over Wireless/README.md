# Samsung Level Over Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 2.1; 28 1.7; 31 1.4; 34 1.1; 37 0.8; 41 0.5; 45 0.1; 49 -0.2; 54 -0.6; 60 -1.0; 66 -1.5; 72 -1.9; 79 -2.3; 87 -2.8; 96 -3.2; 106 -3.6; 116 -3.9; 128 -4.1; 141 -4.2; 155 -4.1; 170 -3.9; 187 -3.6; 206 -3.0; 227 -2.7; 249 -3.2; 274 -4.6; 302 -5.4; 332 -4.6; 365 -3.9; 402 -3.1; 442 -2.5; 486 -2.2; 535 -2.2; 588 -2.3; 647 -2.5; 712 -2.1; 783 -1.7; 861 -1.9; 947 -0.4; 1042 -0.3; 1146 -0.4; 1261 -0.3; 1387 -1.0; 1526 -0.8; 1678 0.2; 1846 1.4; 2031 1.1; 2234 0.3; 2457 2.9; 2703 5.8; 2973 5.2; 3270 2.9; 3597 -1.3; 3957 -4.5; 4353 -4.2; 4788 -1.8; 5267 -0.5; 5793 0.0; 6373 -0.8; 7010 -1.0; 7711 0.3; 8482 -0.9; 9330 -4.2; 10263 -2.3; 11289 -0.9; 12418 -3.1; 13660 -5.0; 15026 -5.0; 16529 -3.4; 18182 -3.3; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level Over Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level Over Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 119 Hz   | 1.27 | -3.3 dB |
| Peaking | 331 Hz   | 0.74 | -3.8 dB |
| Peaking | 2864 Hz  | 3.31 | 7.0 dB  |
| Peaking | 4047 Hz  | 4.48 | -5.9 dB |
| Peaking | 21672 Hz | 0.17 | -5.8 dB |
| Peaking | 22 Hz    | 1.4  | 2.7 dB  |
| Peaking | 451 Hz   | 6.61 | 0.9 dB  |
| Peaking | 14509 Hz | 2.27 | -3.6 dB |
| Peaking | 17777 Hz | 0.74 | 3.2 dB  |
| Peaking | 20008 Hz | 2.47 | -5.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20Over%20Wireless/Samsung%20Level%20Over%20Wireless.png)