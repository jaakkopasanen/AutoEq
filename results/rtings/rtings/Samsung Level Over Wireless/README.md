# Samsung Level Over Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 2.1; 28 1.7; 31 1.4; 34 1.1; 37 0.8; 41 0.5; 45 0.1; 49 -0.2; 54 -0.6; 60 -1.0; 66 -1.5; 72 -1.9; 79 -2.3; 87 -2.8; 96 -3.2; 106 -3.6; 116 -3.9; 128 -4.1; 141 -4.2; 155 -4.1; 170 -3.9; 187 -3.6; 206 -3.0; 227 -2.7; 249 -3.2; 274 -4.6; 302 -5.4; 332 -4.6; 365 -3.9; 402 -3.1; 442 -2.5; 486 -2.2; 535 -2.2; 588 -2.3; 647 -2.5; 712 -2.1; 783 -1.7; 861 -1.9; 947 -0.4; 1042 -0.3; 1146 -0.4; 1261 -0.3; 1387 -1.0; 1526 -0.8; 1678 0.2; 1846 1.4; 2031 1.1; 2234 0.2; 2457 3.0; 2703 5.8; 2973 5.6; 3270 3.6; 3597 -0.3; 3957 -3.3; 4353 -2.9; 4788 -0.1; 5267 2.1; 5793 2.5; 6373 0.4; 7010 -0.1; 7711 0.3; 8482 -0.6; 9330 -5.6; 10263 -4.1; 11289 -0.2; 12418 -0.1; 13660 -1.7; 15026 -2.4; 16529 -0.4; 18182 0.0; 20000 -3.4
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
| Peaking | 119 Hz   | 1.28 | -3.3 dB |
| Peaking | 331 Hz   | 0.71 | -3.7 dB |
| Peaking | 2888 Hz  | 3.1  | 6.6 dB  |
| Peaking | 4017 Hz  | 6.02 | -5.2 dB |
| Peaking | 9664 Hz  | 6.02 | -6.6 dB |
| Peaking | 22 Hz    | 1.43 | 2.7 dB  |
| Peaking | 233 Hz   | 6.07 | 1.2 dB  |
| Peaking | 297 Hz   | 7.15 | -1.6 dB |
| Peaking | 5599 Hz  | 5.53 | 3.0 dB  |
| Peaking | 18993 Hz | 0.43 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Samsung%20Level%20Over%20Wireless/Samsung%20Level%20Over%20Wireless.png)