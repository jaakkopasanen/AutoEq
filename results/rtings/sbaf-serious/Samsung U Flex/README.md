# Samsung U Flex

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 0.0; 23 3.1; 25 2.9; 28 2.7; 31 2.4; 34 2.3; 37 2.1; 41 1.9; 45 1.8; 49 1.7; 54 1.5; 60 1.1; 66 0.9; 72 0.7; 79 0.5; 87 0.2; 96 -0.3; 106 -0.9; 116 -1.5; 128 -2.0; 141 -2.4; 155 -2.6; 170 -2.7; 187 -2.7; 206 -3.0; 227 -3.2; 249 -2.9; 274 -2.5; 302 -2.0; 332 -1.6; 365 -1.2; 402 -0.9; 442 -0.5; 486 -0.0; 535 0.4; 588 0.9; 647 1.2; 712 1.4; 783 1.3; 861 1.0; 947 0.5; 1042 -0.4; 1146 -1.4; 1261 -2.3; 1387 -3.2; 1526 -4.1; 1678 -4.7; 1846 -4.8; 2031 -5.0; 2234 -5.0; 2457 -5.2; 2703 -5.9; 2973 -6.1; 3270 -5.2; 3597 -4.4; 3957 -5.0; 4353 -6.0; 4788 -5.0; 5267 -3.2; 5793 -1.4; 6373 0.2; 7010 2.2; 7711 0.3; 8482 -1.2; 9330 -7.8; 10263 -8.4; 11289 -3.7; 12418 -0.1; 13660 0.0; 15026 -2.2; 16529 -5.7; 18182 -3.3; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung U Flex GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung U Flex ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  1.26 | 3.3 dB  |
| Peaking | 2390 Hz  |  1.11 | -5.9 dB |
| Peaking | 4407 Hz  |  4.2  | -4.4 dB |
| Peaking | 10006 Hz |  5.39 | -9.9 dB |
| Peaking | 16881 Hz |  2.92 | -6.4 dB |
| Peaking | 209 Hz   |  1.03 | -3.4 dB |
| Peaking | 749 Hz   |  1.44 | 2.4 dB  |
| Peaking | 1463 Hz  |  3.05 | -1.7 dB |
| Peaking | 7058 Hz  |  4.63 | 3.5 dB  |
| Peaking | 9217 Hz  | 11.93 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Samsung%20U%20Flex/Samsung%20U%20Flex.png)