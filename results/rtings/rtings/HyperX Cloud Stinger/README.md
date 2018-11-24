# HyperX Cloud Stinger

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 -5.5; 23 -5.7; 25 -5.9; 28 -6.1; 31 -6.2; 34 -6.1; 37 -6.0; 41 -6.0; 45 -6.2; 49 -6.3; 54 -6.3; 60 -6.3; 66 -6.4; 72 -6.3; 79 -6.3; 87 -6.5; 96 -6.7; 106 -6.9; 116 -7.0; 128 -6.9; 141 -6.6; 155 -6.3; 170 -5.8; 187 -5.0; 206 -3.9; 227 -2.8; 249 -1.6; 274 -0.5; 302 0.9; 332 2.4; 365 4.2; 402 5.4; 442 5.1; 486 3.4; 535 1.5; 588 -0.2; 647 -1.2; 712 -1.5; 783 -1.1; 861 -0.3; 947 0.0; 1042 -0.1; 1146 -0.6; 1261 -1.5; 1387 -2.7; 1526 -3.9; 1678 -5.1; 1846 -5.7; 2031 -6.6; 2234 -6.1; 2457 -5.5; 2703 -4.8; 2973 -4.7; 3270 -3.7; 3597 -1.6; 3957 0.8; 4353 1.6; 4788 2.6; 5267 4.6; 5793 1.4; 6373 -2.0; 7010 -0.1; 7711 -0.8; 8482 -4.8; 9330 -8.3; 10263 -6.0; 11289 -0.3; 12418 0.0; 13660 0.0; 15026 -2.1; 16529 -4.4; 18182 -4.2; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Stinger GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Stinger ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.59 | -6.5 dB |
| Peaking | 106 Hz   | 1.66 | -4.9 dB |
| Peaking | 165 Hz   | 3.02 | -4.2 dB |
| Peaking | 2098 Hz  | 1.85 | -7.0 dB |
| Peaking | 22146 Hz | 0.11 | -4.1 dB |
| Peaking | 409 Hz   | 3.25 | 6.7 dB  |
| Peaking | 3077 Hz  | 5.06 | -2.8 dB |
| Peaking | 5054 Hz  | 3.2  | 5.4 dB  |
| Peaking | 9496 Hz  | 3.82 | -8.7 dB |
| Peaking | 12210 Hz | 2.02 | 3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/HyperX%20Cloud%20Stinger/HyperX%20Cloud%20Stinger.png)