# Samsung Level U Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 21 -6.2; 23 -6.1; 25 -6.1; 28 -6.1; 31 -6.0; 34 -5.9; 37 -5.8; 41 -5.7; 45 -5.6; 49 -5.5; 54 -5.4; 60 -5.6; 66 -5.7; 72 -5.9; 79 -6.0; 87 -6.3; 96 -6.6; 106 -7.0; 116 -7.4; 128 -7.6; 141 -7.7; 155 -7.7; 170 -7.6; 187 -7.4; 206 -7.1; 227 -6.9; 249 -6.5; 274 -5.9; 302 -5.3; 332 -4.6; 365 -4.0; 402 -3.3; 442 -2.6; 486 -1.9; 535 -1.2; 588 -0.4; 647 0.2; 712 0.7; 783 0.9; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.1; 1526 -1.1; 1678 -1.0; 1846 -1.0; 2031 -0.8; 2234 0.0; 2457 1.0; 2703 1.3; 2973 0.7; 3270 -0.5; 3597 -1.7; 3957 -2.6; 4353 -3.6; 4788 -3.4; 5267 -2.2; 5793 -0.3; 6373 -0.1; 7010 1.9; 7711 0.3; 8482 -1.4; 9330 -6.4; 10263 -3.9; 11289 -0.1; 12418 -0.4; 13660 -2.3; 15026 -2.5; 16529 -4.7; 18182 -7.9; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level U Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-20**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level U Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.83 | -5.5 dB |
| Peaking | 42 Hz    | 0.25 | -4.7 dB |
| Peaking | 188 Hz   | 0.77 | -5.5 dB |
| Peaking | 9395 Hz  | 6.81 | -6.7 dB |
| Peaking | 18685 Hz | 1.24 | -8.4 dB |
| Peaking | 774 Hz   | 1.33 | 3.7 dB  |
| Peaking | 1078 Hz  | 0.41 | -2.0 dB |
| Peaking | 2678 Hz  | 2.85 | 2.9 dB  |
| Peaking | 4470 Hz  | 2.59 | -3.6 dB |
| Peaking | 7073 Hz  | 3.58 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Samsung%20Level%20U%20Pro/Samsung%20Level%20U%20Pro.png)