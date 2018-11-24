# Razer Man O' War

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 0.0; 23 -0.0; 25 -1.1; 28 -2.5; 31 -3.6; 34 -4.5; 37 -5.1; 41 -5.7; 45 -6.1; 49 -6.4; 54 -6.5; 60 -6.6; 66 -6.7; 72 -6.8; 79 -7.0; 87 -7.2; 96 -7.4; 106 -7.5; 116 -7.6; 128 -7.7; 141 -7.7; 155 -7.6; 170 -7.2; 187 -6.7; 206 -6.3; 227 -7.4; 249 -7.0; 274 -6.2; 302 -5.4; 332 -4.1; 365 -3.4; 402 -3.3; 442 -3.6; 486 -3.1; 535 -1.1; 588 0.4; 647 0.1; 712 -1.3; 783 -1.1; 861 -0.6; 947 -0.2; 1042 0.0; 1146 0.2; 1261 0.6; 1387 0.9; 1526 1.3; 1678 1.0; 1846 1.3; 2031 2.0; 2234 4.2; 2457 3.1; 2703 1.7; 2973 1.1; 3270 1.8; 3597 4.6; 3957 4.3; 4353 0.7; 4788 1.3; 5267 1.9; 5793 1.9; 6373 -0.4; 7010 1.4; 7711 -1.1; 8482 -6.0; 9330 -7.2; 10263 -3.4; 11289 0.0; 12418 0.0; 13660 -0.8; 15026 -4.3; 16529 -2.8; 18182 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Man O' War GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Man O' War ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 46 Hz    |  1.27 | -4.2 dB |
| Peaking | 110 Hz   |  0.7  | -6.2 dB |
| Peaking | 254 Hz   |  0.99 | -4.2 dB |
| Peaking | 3260 Hz  |  0.65 | 3.0 dB  |
| Peaking | 9094 Hz  |  3.93 | -8.8 dB |
| Peaking | 604 Hz   | 10.33 | 2.0 dB  |
| Peaking | 2296 Hz  | 10.14 | 2.6 dB  |
| Peaking | 2950 Hz  |  6.83 | -2.0 dB |
| Peaking | 12781 Hz |  1.93 | 1.8 dB  |
| Peaking | 15313 Hz |  2.56 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Razer%20Man%20O'%20War/Razer%20Man%20O'%20War.png)