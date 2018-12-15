# Samsung Gear IconX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 0.0; 23 3.1; 25 3.0; 28 2.7; 31 2.4; 34 2.2; 37 1.9; 41 1.7; 45 1.4; 49 1.2; 54 0.9; 60 0.4; 66 -0.0; 72 -0.4; 79 -0.7; 87 -1.2; 96 -1.8; 106 -2.3; 116 -2.8; 128 -3.3; 141 -3.6; 155 -3.8; 170 -4.0; 187 -4.2; 206 -4.3; 227 -4.0; 249 -3.6; 274 -3.2; 302 -2.8; 332 -2.4; 365 -2.0; 402 -1.6; 442 -1.2; 486 -0.7; 535 -0.2; 588 0.4; 647 0.9; 712 1.5; 783 1.7; 861 1.3; 947 0.5; 1042 -0.3; 1146 -1.1; 1261 -1.7; 1387 -2.0; 1526 -2.1; 1678 -2.2; 1846 -2.3; 2031 -2.2; 2234 -1.5; 2457 -0.6; 2703 -0.5; 2973 -0.9; 3270 -1.4; 3597 -1.6; 3957 -1.4; 4353 -1.1; 4788 -0.1; 5267 0.8; 5793 1.3; 6373 0.4; 7010 -0.0; 7711 -0.6; 8482 -2.8; 9330 -4.7; 10263 -3.5; 11289 -0.4; 12418 0.0; 13660 0.0; 15026 -0.3; 16529 -5.1; 18182 -8.2; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Gear IconX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Gear IconX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.66 | 3.2 dB  |
| Peaking | 180 Hz   | 0.89 | -4.6 dB |
| Peaking | 1774 Hz  | 1.99 | -2.5 dB |
| Peaking | 9464 Hz  | 4.88 | -5.1 dB |
| Peaking | 18066 Hz | 2.09 | -9.2 dB |
| Peaking | 769 Hz   | 2.56 | 2.4 dB  |
| Peaking | 1259 Hz  | 4.34 | -1.1 dB |
| Peaking | 3795 Hz  | 2.96 | -1.5 dB |
| Peaking | 5712 Hz  | 4.13 | 1.8 dB  |
| Peaking | 14086 Hz | 3.06 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Gear%20IconX/Samsung%20Gear%20IconX.png)