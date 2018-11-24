# Razer Man O' War

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.3; 25 -0.8; 28 -2.3; 31 -3.6; 34 -4.5; 37 -5.2; 41 -5.9; 45 -6.4; 49 -6.7; 54 -6.8; 60 -6.8; 66 -6.9; 72 -6.8; 79 -6.8; 87 -6.8; 96 -6.9; 106 -7.0; 116 -7.1; 128 -7.2; 141 -7.2; 155 -7.0; 170 -6.6; 187 -6.1; 206 -5.7; 227 -6.9; 249 -6.4; 274 -5.5; 302 -4.6; 332 -3.2; 365 -2.4; 402 -2.3; 442 -2.5; 486 -1.9; 535 0.1; 588 1.5; 647 1.2; 712 -0.4; 783 -0.6; 861 -0.4; 947 -0.2; 1042 0.1; 1146 0.4; 1261 0.8; 1387 0.9; 1526 0.9; 1678 0.7; 1846 1.3; 2031 2.4; 2234 4.7; 2457 3.6; 2703 2.3; 2973 2.2; 3270 3.7; 3597 6.0; 3957 5.4; 4353 0.7; 4788 1.2; 5267 2.3; 5793 3.3; 6373 2.2; 7010 2.5; 7711 -0.3; 8482 -5.6; 9330 -5.7; 10263 -0.6; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.0; 16529 -0.1; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Man O' War GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Man O' War ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 84 Hz   | 0.46 | -7.3 dB |
| Peaking | 240 Hz  | 1.73 | -3.4 dB |
| Peaking | 3180 Hz | 0.9  | 4.0 dB  |
| Peaking | 6779 Hz | 3.55 | 2.8 dB  |
| Peaking | 8836 Hz | 4.45 | -8.2 dB |
| Peaking | 21 Hz   | 2.76 | 3.5 dB  |
| Peaking | 468 Hz  | 4.44 | -2.1 dB |
| Peaking | 486 Hz  | 2.04 | 0.6 dB  |
| Peaking | 608 Hz  | 3.34 | 3.4 dB  |
| Peaking | 717 Hz  | 2.36 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Razer%20Man%20O'%20War/Razer%20Man%20O'%20War.png)