# HyperX Cloud Stinger

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 -5.5; 23 -5.7; 25 -5.9; 28 -6.1; 31 -6.2; 34 -6.1; 37 -6.0; 41 -6.0; 45 -6.2; 49 -6.3; 54 -6.3; 60 -6.3; 66 -6.4; 72 -6.3; 79 -6.3; 87 -6.5; 96 -6.7; 106 -6.9; 116 -7.0; 128 -6.9; 141 -6.6; 155 -6.3; 170 -5.8; 187 -5.0; 206 -3.9; 227 -2.8; 249 -1.6; 274 -0.5; 302 0.9; 332 2.4; 365 4.2; 402 5.4; 442 5.1; 486 3.4; 535 1.5; 588 -0.2; 647 -1.2; 712 -1.5; 783 -1.1; 861 -0.3; 947 0.0; 1042 -0.1; 1146 -0.6; 1261 -1.5; 1387 -2.7; 1526 -3.9; 1678 -5.1; 1846 -5.7; 2031 -6.6; 2234 -6.0; 2457 -5.5; 2703 -5.0; 2973 -5.2; 3270 -4.4; 3597 -2.6; 3957 -0.4; 4353 0.3; 4788 0.8; 5267 2.0; 5793 -1.1; 6373 -3.3; 7010 -1.0; 7711 -2.2; 8482 -5.4; 9330 -6.9; 10263 -4.3; 11289 -0.2; 12418 0.0; 13660 -0.4; 15026 -4.7; 16529 -7.4; 18182 -8.5; 20000 -9.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Stinger GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Stinger ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.59 | -6.5 dB  |
| Peaking | 105 Hz   | 1.66 | -5.0 dB  |
| Peaking | 165 Hz   | 3.02 | -4.2 dB  |
| Peaking | 2182 Hz  | 1.52 | -6.8 dB  |
| Peaking | 20515 Hz | 0.43 | -10.3 dB |
| Peaking | 409 Hz   | 2.67 | 7.1 dB   |
| Peaking | 3786 Hz  | 0.02 | -0.5 dB  |
| Peaking | 4949 Hz  | 3.96 | 3.7 dB   |
| Peaking | 9263 Hz  | 3.56 | -6.2 dB  |
| Peaking | 12466 Hz | 2.24 | 4.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Stinger/HyperX%20Cloud%20Stinger.png)