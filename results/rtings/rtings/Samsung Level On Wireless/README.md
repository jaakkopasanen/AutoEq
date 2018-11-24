# Samsung Level On Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.5; 25 5.2; 28 4.7; 31 4.2; 34 3.6; 37 3.1; 41 2.4; 45 1.8; 49 1.4; 54 1.0; 60 0.6; 66 0.1; 72 -0.3; 79 -0.7; 87 -1.3; 96 -1.8; 106 -2.4; 116 -2.9; 128 -3.4; 141 -3.8; 155 -4.1; 170 -4.4; 187 -4.4; 206 -4.2; 227 -3.9; 249 -3.5; 274 -3.1; 302 -2.5; 332 -1.9; 365 -1.2; 402 -0.7; 442 -0.3; 486 0.1; 535 -0.1; 588 -0.3; 647 -0.7; 712 -1.0; 783 -1.0; 861 -0.3; 947 -0.0; 1042 -0.1; 1146 0.3; 1261 1.6; 1387 2.2; 1526 2.5; 1678 2.4; 1846 2.0; 2031 1.7; 2234 1.8; 2457 2.2; 2703 2.0; 2973 1.6; 3270 1.3; 3597 1.0; 3957 -0.8; 4353 1.3; 4788 5.3; 5267 6.0; 5793 6.0; 6373 5.3; 7010 2.3; 7711 0.3; 8482 -0.8; 9330 -6.2; 10263 -7.1; 11289 -2.4; 12418 -0.1; 13660 -1.2; 15026 -0.9; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level On Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level On Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.72 | 5.9 dB  |
| Peaking | 172 Hz  | 0.83 | -4.7 dB |
| Peaking | 1728 Hz | 1.5  | 2.5 dB  |
| Peaking | 5699 Hz | 2.5  | 7.0 dB  |
| Peaking | 9888 Hz | 3.92 | -8.8 dB |
| Peaking | 486 Hz  | 3.05 | 1.1 dB  |
| Peaking | 753 Hz  | 2.67 | -1.1 dB |
| Peaking | 2718 Hz | 4.39 | 1.1 dB  |
| Peaking | 4054 Hz | 7.35 | -3.0 dB |
| Peaking | 4810 Hz | 9.9  | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Samsung%20Level%20On%20Wireless/Samsung%20Level%20On%20Wireless.png)