# Samsung Level U Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 21 -5.8; 23 -5.8; 25 -5.9; 28 -5.9; 31 -5.9; 34 -5.9; 37 -5.9; 41 -5.9; 45 -5.8; 49 -5.8; 54 -5.8; 60 -5.9; 66 -5.9; 72 -5.9; 79 -5.8; 87 -5.9; 96 -6.2; 106 -6.5; 116 -6.9; 128 -7.1; 141 -7.2; 155 -7.1; 170 -7.0; 187 -6.8; 206 -6.6; 227 -6.4; 249 -5.9; 274 -5.2; 302 -4.4; 332 -3.7; 365 -3.0; 402 -2.3; 442 -1.5; 486 -0.7; 535 0.0; 588 0.7; 647 1.3; 712 1.6; 783 1.4; 861 1.0; 947 0.4; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -1.1; 1526 -1.4; 1678 -1.4; 1846 -1.0; 2031 -0.4; 2234 0.5; 2457 1.5; 2703 1.9; 2973 1.8; 3270 1.4; 3597 0.5; 3957 -1.4; 4353 -3.6; 4788 -3.6; 5267 -1.8; 5793 1.1; 6373 2.4; 7010 2.5; 7711 0.3; 8482 -1.1; 9330 -4.9; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.4; 18182 -4.7; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level U Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level U Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.24 | -5.8 dB |
| Peaking | 185 Hz   | 0.95 | -5.4 dB |
| Peaking | 4571 Hz  | 3.43 | -2.3 dB |
| Peaking | 7376 Hz  | 3.17 | -1.9 dB |
| Peaking | 18864 Hz | 2.02 | -5.4 dB |
| Peaking | 749 Hz   | 0.98 | 5.1 dB  |
| Peaking | 1584 Hz  | 0.26 | -3.8 dB |
| Peaking | 2767 Hz  | 1.69 | 5.4 dB  |
| Peaking | 6810 Hz  | 2.96 | 6.2 dB  |
| Peaking | 9287 Hz  | 8.06 | -5.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Samsung%20Level%20U%20Pro/Samsung%20Level%20U%20Pro.png)