# AKG N700NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.4dB
GraphicEQ: 21 -2.2; 23 -2.4; 25 -2.6; 28 -2.7; 31 -2.6; 34 -2.5; 37 -2.3; 41 -2.1; 45 -1.9; 49 -1.7; 54 -1.4; 60 -1.2; 66 -1.1; 72 -1.0; 79 -0.8; 87 -0.8; 96 -0.7; 106 -0.6; 116 -0.6; 128 -0.6; 141 -0.6; 155 -0.6; 170 -0.5; 187 -0.3; 206 -0.1; 227 0.1; 249 0.2; 274 0.3; 302 0.3; 332 0.3; 365 0.3; 402 0.1; 442 -0.1; 486 -0.4; 535 -0.9; 588 -1.3; 647 -1.3; 712 -1.0; 783 -0.7; 861 -0.3; 947 -0.0; 1042 -0.0; 1146 -0.0; 1261 -0.4; 1387 -1.5; 1526 -2.4; 1678 -2.8; 1846 -2.5; 2031 -2.5; 2234 -2.0; 2457 -3.5; 2703 -6.0; 2973 -7.6; 3270 -6.8; 3597 -5.0; 3957 -4.9; 4353 -5.3; 4788 -6.0; 5267 -5.4; 5793 -5.2; 6373 -5.8; 7010 -2.5; 7711 -1.2; 8482 -3.0; 9330 -3.4; 10263 -1.8; 11289 -3.9; 12418 -6.9; 13660 -5.3; 15026 -1.8; 16529 0.0; 18182 0.0; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N700NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-4**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N700NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 28 Hz    |  0.57 | -2.5 dB |
| Peaking | 614 Hz   |  3.99 | -1.0 dB |
| Peaking | 3883 Hz  |  0.74 | -6.3 dB |
| Peaking | 12738 Hz |  3.06 | -6.6 dB |
| Peaking | 20689 Hz |  2.86 | -3.7 dB |
| Peaking | 1102 Hz  |  3.38 | 1.4 dB  |
| Peaking | 2355 Hz  |  3.49 | 4.3 dB  |
| Peaking | 2855 Hz  |  1.54 | -4.6 dB |
| Peaking | 3727 Hz  |  3.05 | 3.9 dB  |
| Peaking | 6293 Hz  | 12.45 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20N700NC/AKG%20N700NC.png)