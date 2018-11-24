# Superlux HD 681

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 0.0; 23 0.1; 25 -0.5; 28 -1.4; 31 -2.1; 34 -2.5; 37 -2.9; 41 -3.2; 45 -3.4; 49 -3.4; 54 -3.4; 60 -3.2; 66 -3.0; 72 -2.8; 79 -2.6; 87 -2.5; 96 -2.5; 106 -2.5; 116 -2.3; 128 -2.2; 141 -2.0; 155 -1.6; 170 -1.1; 187 -0.5; 206 0.3; 227 -0.1; 249 -0.4; 274 -0.1; 302 0.2; 332 0.4; 365 0.5; 402 0.6; 442 0.5; 486 0.4; 535 0.9; 588 1.4; 647 1.1; 712 0.9; 783 0.5; 861 0.2; 947 0.0; 1042 0.0; 1146 0.2; 1261 0.2; 1387 -0.3; 1526 -1.2; 1678 -2.3; 1846 -4.0; 2031 -4.9; 2234 -5.0; 2457 -3.8; 2703 -2.2; 2973 -1.4; 3270 -0.5; 3597 2.3; 3957 4.7; 4353 -0.3; 4788 -4.8; 5267 -4.4; 5793 -1.0; 6373 -0.7; 7010 -1.3; 7711 -5.4; 8482 -9.1; 9330 -10.7; 10263 -8.9; 11289 -3.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 60 Hz    | 0.67 | -3.4 dB  |
| Peaking | 2149 Hz  | 2.64 | -5.5 dB  |
| Peaking | 3934 Hz  | 5.29 | 6.6 dB   |
| Peaking | 4870 Hz  | 5.7  | -6.0 dB  |
| Peaking | 9282 Hz  | 3.06 | -11.9 dB |
| Peaking | 136 Hz   | 1.55 | -2.4 dB  |
| Peaking | 146 Hz   | 0.83 | 1.6 dB   |
| Peaking | 613 Hz   | 1.69 | 1.3 dB   |
| Peaking | 6517 Hz  | 7.41 | 1.7 dB   |
| Peaking | 12398 Hz | 6.14 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Superlux%20HD%20681/Superlux%20HD%20681.png)