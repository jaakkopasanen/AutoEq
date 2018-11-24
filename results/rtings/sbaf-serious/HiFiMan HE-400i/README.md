# HiFiMan HE-400i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.3; 41 4.6; 45 4.0; 49 3.5; 54 3.0; 60 2.6; 66 2.3; 72 2.0; 79 1.8; 87 1.6; 96 1.2; 106 0.9; 116 0.7; 128 0.4; 141 0.2; 155 0.1; 170 0.1; 187 0.0; 206 -0.1; 227 -0.1; 249 -0.1; 274 -0.3; 302 -0.3; 332 -0.3; 365 -0.4; 402 -0.2; 442 0.5; 486 1.1; 535 0.8; 588 0.1; 647 -0.2; 712 -0.1; 783 -0.7; 861 -0.6; 947 -0.1; 1042 0.1; 1146 0.7; 1261 0.8; 1387 0.5; 1526 -0.2; 1678 -0.1; 1846 1.1; 2031 1.2; 2234 1.7; 2457 0.4; 2703 0.4; 2973 -0.2; 3270 0.8; 3597 1.0; 3957 0.4; 4353 0.0; 4788 1.3; 5267 3.9; 5793 5.6; 6373 1.2; 7010 -1.8; 7711 -3.2; 8482 -5.4; 9330 -4.6; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan HE-400i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan HE-400i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.59 | 6.2 dB  |
| Peaking | 207 Hz   | 1.12 | -0.5 dB |
| Peaking | 2125 Hz  | 3.76 | 1.6 dB  |
| Peaking | 5654 Hz  | 5.44 | 6.8 dB  |
| Peaking | 8502 Hz  | 3.52 | -6.2 dB |
| Peaking | 502 Hz   | 4.37 | 1.8 dB  |
| Peaking | 850 Hz   | 0.74 | -1.0 dB |
| Peaking | 1310 Hz  | 1.58 | 1.7 dB  |
| Peaking | 1557 Hz  | 4.94 | -1.4 dB |
| Peaking | 24000 Hz | 1.74 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/HiFiMan%20HE-400i/HiFiMan%20HE-400i.png)