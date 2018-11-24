# HiFiMan HE-400i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.4; 41 4.8; 45 4.3; 49 3.8; 54 3.3; 60 2.9; 66 2.4; 72 2.0; 79 1.6; 87 1.2; 96 0.8; 106 0.4; 116 0.2; 128 -0.1; 141 -0.3; 155 -0.5; 170 -0.6; 187 -0.6; 206 -0.6; 227 -0.6; 249 -0.7; 274 -1.0; 302 -1.1; 332 -1.3; 365 -1.4; 402 -1.3; 442 -0.7; 486 -0.1; 535 -0.4; 588 -1.0; 647 -1.3; 712 -0.9; 783 -1.2; 861 -0.8; 947 -0.1; 1042 0.1; 1146 0.5; 1261 0.6; 1387 0.5; 1526 0.2; 1678 0.3; 1846 1.1; 2031 0.8; 2234 1.2; 2457 -0.0; 2703 -0.2; 2973 -1.3; 3270 -1.1; 3597 -1.2; 3957 -0.8; 4353 -0.0; 4788 1.5; 5267 3.5; 5793 4.2; 6373 -1.3; 7010 -4.3; 7711 -4.4; 8482 -5.7; 9330 -6.1; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.1; 16529 -0.9; 18182 -0.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan HE-400i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan HE-400i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.57 | 6.3 dB  |
| Peaking | 249 Hz   | 0.5  | -1.2 dB |
| Peaking | 3421 Hz  | 4.97 | -1.4 dB |
| Peaking | 5551 Hz  | 5.1  | 6.5 dB  |
| Peaking | 8185 Hz  | 2.16 | -6.4 dB |
| Peaking | 502 Hz   | 5.29 | 1.5 dB  |
| Peaking | 646 Hz   | 1.27 | -1.1 dB |
| Peaking | 1443 Hz  | 1.02 | 1.0 dB  |
| Peaking | 9390 Hz  | 7.37 | -3.5 dB |
| Peaking | 10560 Hz | 3.04 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/HiFiMan%20HE-400i/HiFiMan%20HE-400i.png)