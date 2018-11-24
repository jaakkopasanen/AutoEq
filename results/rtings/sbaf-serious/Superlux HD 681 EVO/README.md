# Superlux HD 681 EVO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.7; 23 -3.3; 25 -3.9; 28 -4.7; 31 -5.3; 34 -5.8; 37 -6.1; 41 -6.4; 45 -6.6; 49 -6.7; 54 -6.6; 60 -6.4; 66 -6.1; 72 -5.7; 79 -5.3; 87 -5.0; 96 -4.8; 106 -4.8; 116 -4.6; 128 -4.2; 141 -3.5; 155 -2.5; 170 -1.9; 187 -1.7; 206 -1.3; 227 -1.0; 249 -0.6; 274 -0.3; 302 0.2; 332 0.6; 365 1.0; 402 1.2; 442 1.3; 486 1.4; 535 1.9; 588 1.6; 647 1.9; 712 1.3; 783 0.5; 861 -0.2; 947 -0.2; 1042 0.4; 1146 1.0; 1261 1.2; 1387 0.6; 1526 -0.7; 1678 -2.5; 1846 -3.9; 2031 -4.6; 2234 -4.1; 2457 -3.2; 2703 -2.1; 2973 -1.2; 3270 0.8; 3597 4.7; 3957 6.0; 4353 4.0; 4788 1.2; 5267 1.6; 5793 1.8; 6373 2.1; 7010 1.6; 7711 -2.2; 8482 -5.7; 9330 -6.9; 10263 -4.6; 11289 -0.4; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 EVO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 EVO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.73 | -6.9 dB |
| Peaking | 116 Hz  | 1.91 | -2.7 dB |
| Peaking | 2178 Hz | 2.5  | -5.2 dB |
| Peaking | 3951 Hz | 3.33 | 6.9 dB  |
| Peaking | 9224 Hz | 4.18 | -8.0 dB |
| Peaking | 543 Hz  | 0.85 | 4.6 dB  |
| Peaking | 693 Hz  | 0.42 | -2.8 dB |
| Peaking | 1271 Hz | 3.17 | 2.8 dB  |
| Peaking | 6654 Hz | 3.49 | 3.1 dB  |
| Peaking | 8108 Hz | 5.95 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Superlux%20HD%20681%20EVO/Superlux%20HD%20681%20EVO.png)