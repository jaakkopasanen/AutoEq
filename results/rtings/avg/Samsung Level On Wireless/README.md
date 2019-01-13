# Samsung Level On Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.5; 25 5.2; 28 4.7; 31 4.2; 34 3.6; 37 3.1; 41 2.4; 45 1.8; 49 1.4; 54 1.0; 60 0.6; 66 0.1; 72 -0.3; 79 -0.7; 87 -1.3; 96 -1.8; 106 -2.4; 116 -2.9; 128 -3.4; 141 -3.8; 155 -4.1; 170 -4.4; 187 -4.4; 206 -4.2; 227 -3.9; 249 -3.5; 274 -3.1; 302 -2.5; 332 -1.9; 365 -1.2; 402 -0.7; 442 -0.3; 486 0.1; 535 -0.1; 588 -0.3; 647 -0.7; 712 -1.0; 783 -1.0; 861 -0.3; 947 -0.0; 1042 -0.1; 1146 0.3; 1261 1.6; 1387 2.2; 1526 2.5; 1678 2.4; 1846 2.0; 2031 1.7; 2234 1.8; 2457 2.2; 2703 1.8; 2973 1.1; 3270 0.6; 3597 -0.0; 3957 -2.0; 4353 -0.0; 4788 3.7; 5267 5.9; 5793 6.0; 6373 4.4; 7010 1.9; 7711 0.3; 8482 -1.2; 9330 -4.8; 10263 -5.3; 11289 -3.2; 12418 -3.4; 13660 -4.5; 15026 -3.5; 16529 -1.2; 18182 -0.2; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level On Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level On Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.81 | 5.8 dB  |
| Peaking | 172 Hz   | 0.91 | -4.8 dB |
| Peaking | 5728 Hz  | 2.91 | 7.0 dB  |
| Peaking | 9830 Hz  | 3.67 | -5.6 dB |
| Peaking | 13924 Hz | 1.91 | -4.4 dB |
| Peaking | 498 Hz   | 1.76 | 2.5 dB  |
| Peaking | 600 Hz   | 0.82 | -2.0 dB |
| Peaking | 1466 Hz  | 2.71 | 1.9 dB  |
| Peaking | 2198 Hz  | 0.81 | 1.7 dB  |
| Peaking | 4012 Hz  | 6.01 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20On%20Wireless/Samsung%20Level%20On%20Wireless.png)