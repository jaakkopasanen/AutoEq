# Samsung Level On Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.4; 28 4.8; 31 4.2; 34 3.6; 37 3.0; 41 2.2; 45 1.5; 49 1.1; 54 0.7; 60 0.3; 66 -0.1; 72 -0.3; 79 -0.6; 87 -1.0; 96 -1.4; 106 -1.9; 116 -2.4; 128 -2.9; 141 -3.3; 155 -3.5; 170 -3.7; 187 -3.8; 206 -3.7; 227 -3.4; 249 -3.0; 274 -2.4; 302 -1.7; 332 -1.0; 365 -0.2; 402 0.4; 442 0.8; 486 1.3; 535 1.1; 588 0.7; 647 0.4; 712 -0.2; 783 -0.5; 861 -0.2; 947 0.0; 1042 -0.0; 1146 0.5; 1261 1.9; 1387 2.2; 1526 2.2; 1678 2.1; 1846 2.0; 2031 2.1; 2234 2.3; 2457 2.7; 2703 2.6; 2973 2.7; 3270 3.1; 3597 3.1; 3957 0.4; 4353 1.3; 4788 5.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.5; 9330 -4.7; 10263 -3.7; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level On Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level On Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.08 | 6.0 dB  |
| Peaking | 171 Hz  | 1.09 | -4.2 dB |
| Peaking | 2226 Hz | 0.8  | 2.4 dB  |
| Peaking | 5733 Hz | 2.61 | 6.3 dB  |
| Peaking | 9571 Hz | 4.73 | -6.3 dB |
| Peaking | 494 Hz  | 2.76 | 1.8 dB  |
| Peaking | 821 Hz  | 2.81 | -1.1 dB |
| Peaking | 4077 Hz | 1.87 | 4.2 dB  |
| Peaking | 4120 Hz | 6.01 | -5.9 dB |
| Peaking | 4163 Hz | 0.87 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Samsung%20Level%20On%20Wireless/Samsung%20Level%20On%20Wireless.png)