# Samsung Gear IconX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 3.4; 25 3.2; 28 2.9; 31 2.5; 34 2.1; 37 1.8; 41 1.5; 45 1.2; 49 0.9; 54 0.6; 60 0.2; 66 -0.2; 72 -0.4; 79 -0.6; 87 -0.9; 96 -1.3; 106 -1.8; 116 -2.3; 128 -2.7; 141 -3.0; 155 -3.2; 170 -3.4; 187 -3.6; 206 -3.8; 227 -3.6; 249 -3.1; 274 -2.5; 302 -1.9; 332 -1.4; 365 -1.0; 402 -0.6; 442 -0.1; 486 0.5; 535 1.0; 588 1.5; 647 2.0; 712 2.3; 783 2.2; 861 1.5; 947 0.5; 1042 -0.2; 1146 -0.9; 1261 -1.5; 1387 -2.0; 1526 -2.5; 1678 -2.6; 1846 -2.2; 2031 -1.8; 2234 -1.0; 2457 -0.1; 2703 0.4; 2973 0.7; 3270 1.2; 3597 1.6; 3957 1.0; 4353 0.2; 4788 1.5; 5267 3.8; 5793 5.2; 6373 4.2; 7010 2.5; 7711 0.3; 8482 -1.8; 9330 -4.6; 10263 -1.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Gear IconX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Gear IconX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.98 | 3.6 dB  |
| Peaking | 179 Hz  | 1.14 | -4.1 dB |
| Peaking | 1659 Hz | 3.01 | -3.0 dB |
| Peaking | 5944 Hz | 2.62 | 5.5 dB  |
| Peaking | 9299 Hz | 4.79 | -5.6 dB |
| Peaking | 282 Hz  | 2.29 | -0.8 dB |
| Peaking | 750 Hz  | 1.44 | 3.4 dB  |
| Peaking | 1102 Hz | 1.35 | -1.7 dB |
| Peaking | 3595 Hz | 2.74 | 1.4 dB  |
| Peaking | 4387 Hz | 5.95 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Samsung%20Gear%20IconX/Samsung%20Gear%20IconX.png)