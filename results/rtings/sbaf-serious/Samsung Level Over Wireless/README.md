# Samsung Level Over Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.4; 28 1.9; 31 1.5; 34 1.1; 37 0.7; 41 0.2; 45 -0.2; 49 -0.5; 54 -0.9; 60 -1.3; 66 -1.7; 72 -1.9; 79 -2.1; 87 -2.4; 96 -2.8; 106 -3.2; 116 -3.4; 128 -3.6; 141 -3.6; 155 -3.5; 170 -3.3; 187 -3.0; 206 -2.5; 227 -2.2; 249 -2.6; 274 -3.9; 302 -4.5; 332 -3.7; 365 -2.9; 402 -2.0; 442 -1.4; 486 -1.0; 535 -1.0; 588 -1.2; 647 -1.5; 712 -1.2; 783 -1.2; 861 -1.7; 947 -0.3; 1042 -0.3; 1146 -0.2; 1261 -0.1; 1387 -1.0; 1526 -1.2; 1678 -0.2; 1846 1.4; 2031 1.6; 2234 0.7; 2457 3.4; 2703 5.9; 2973 6.0; 3270 5.5; 3597 1.9; 3957 -2.1; 4353 -2.8; 4788 -0.2; 5267 2.5; 5793 3.9; 6373 3.0; 7010 1.8; 7711 0.3; 8482 -0.3; 9330 -4.1; 10263 -0.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level Over Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level Over Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.4  | 4.1 dB  |
| Peaking | 118 Hz   | 0.3  | -3.6 dB |
| Peaking | 306 Hz   | 5.25 | -2.2 dB |
| Peaking | 2879 Hz  | 3.93 | 7.1 dB  |
| Peaking | 5964 Hz  | 6.13 | 4.4 dB  |
| Peaking | 225 Hz   | 7.55 | 1.0 dB  |
| Peaking | 1480 Hz  | 8    | -1.4 dB |
| Peaking | 3371 Hz  | 5.25 | 2.3 dB  |
| Peaking | 4139 Hz  | 5.36 | -4.6 dB |
| Peaking | 21148 Hz | 1.79 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Samsung%20Level%20Over%20Wireless/Samsung%20Level%20Over%20Wireless.png)