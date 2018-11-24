# Samsung Level U Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 21 -6.2; 23 -6.1; 25 -6.1; 28 -6.1; 31 -6.0; 34 -5.9; 37 -5.8; 41 -5.7; 45 -5.6; 49 -5.5; 54 -5.4; 60 -5.6; 66 -5.7; 72 -5.9; 79 -6.0; 87 -6.3; 96 -6.6; 106 -7.0; 116 -7.4; 128 -7.6; 141 -7.7; 155 -7.7; 170 -7.6; 187 -7.4; 206 -7.1; 227 -6.9; 249 -6.5; 274 -5.9; 302 -5.3; 332 -4.6; 365 -4.0; 402 -3.3; 442 -2.6; 486 -1.9; 535 -1.2; 588 -0.4; 647 0.2; 712 0.7; 783 0.9; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.1; 1526 -1.1; 1678 -1.0; 1846 -1.0; 2031 -0.8; 2234 0.0; 2457 1.0; 2703 1.1; 2973 0.3; 3270 -1.2; 3597 -2.7; 3957 -3.8; 4353 -4.9; 4788 -5.2; 5267 -4.8; 5793 -2.8; 6373 -1.4; 7010 1.7; 7711 0.3; 8482 -0.6; 9330 -3.7; 10263 -1.6; 11289 -0.5; 12418 -3.6; 13660 -5.6; 15026 -5.1; 16529 -7.8; 18182 -12.2; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level U Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level U Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 11 Hz    |  0.91 | -5.7 dB  |
| Peaking | 44 Hz    |  0.27 | -4.7 dB  |
| Peaking | 188 Hz   |  0.78 | -5.6 dB  |
| Peaking | 4621 Hz  |  2.98 | -5.6 dB  |
| Peaking | 18940 Hz |  0.87 | -13.3 dB |
| Peaking | 768 Hz   |  1.4  | 3.4 dB   |
| Peaking | 1300 Hz  |  0.3  | -1.8 dB  |
| Peaking | 2619 Hz  |  2.91 | 3.2 dB   |
| Peaking | 7288 Hz  |  4.24 | 3.1 dB   |
| Peaking | 9283 Hz  | 10    | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20U%20Pro/Samsung%20Level%20U%20Pro.png)