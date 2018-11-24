# Superlux HD 681

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 0.0; 23 -0.2; 25 -0.7; 28 -1.5; 31 -2.1; 34 -2.5; 37 -2.8; 41 -3.0; 45 -3.1; 49 -3.1; 54 -3.0; 60 -2.9; 66 -2.9; 72 -2.8; 79 -2.8; 87 -2.9; 96 -2.9; 106 -3.0; 116 -2.9; 128 -2.7; 141 -2.5; 155 -2.2; 170 -1.7; 187 -1.1; 206 -0.2; 227 -0.6; 249 -0.9; 274 -0.8; 302 -0.7; 332 -0.6; 365 -0.5; 402 -0.5; 442 -0.6; 486 -0.8; 535 -0.3; 588 0.4; 647 0.0; 712 0.1; 783 0.0; 861 0.1; 947 0.0; 1042 -0.0; 1146 -0.0; 1261 -0.1; 1387 -0.2; 1526 -0.8; 1678 -2.0; 1846 -4.1; 2031 -5.3; 2234 -5.5; 2457 -4.2; 2703 -2.8; 2973 -2.5; 3270 -2.3; 3597 0.2; 3957 3.5; 4353 -0.3; 4788 -4.6; 5267 -4.8; 5793 -2.5; 6373 -3.2; 7010 -3.8; 7711 -6.5; 8482 -9.4; 9330 -12.2; 10263 -12.3; 11289 -7.5; 12418 -2.2; 13660 -2.2; 15026 -3.2; 16529 -1.6; 18182 -1.0; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 70 Hz    | 0.5  | -3.2 dB |
| Peaking | 2161 Hz  | 2.85 | -5.8 dB |
| Peaking | 9097 Hz  | 1.83 | -9.8 dB |
| Peaking | 10317 Hz | 4.62 | -5.5 dB |
| Peaking | 15341 Hz | 3.89 | -2.2 dB |
| Peaking | 134 Hz   | 4.84 | -0.6 dB |
| Peaking | 3271 Hz  | 4.56 | -2.2 dB |
| Peaking | 3984 Hz  | 4.79 | 6.5 dB  |
| Peaking | 4921 Hz  | 3.81 | -5.9 dB |
| Peaking | 5860 Hz  | 1.98 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Superlux%20HD%20681/Superlux%20HD%20681.png)