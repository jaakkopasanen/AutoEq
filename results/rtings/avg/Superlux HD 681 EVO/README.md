# Superlux HD 681 EVO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -3.1; 23 -3.6; 25 -4.1; 28 -4.8; 31 -5.4; 34 -5.7; 37 -6.0; 41 -6.2; 45 -6.3; 49 -6.3; 54 -6.3; 60 -6.1; 66 -6.0; 72 -5.7; 79 -5.5; 87 -5.3; 96 -5.2; 106 -5.2; 116 -5.1; 128 -4.8; 141 -4.1; 155 -3.1; 170 -2.6; 187 -2.3; 206 -1.8; 227 -1.5; 249 -1.2; 274 -0.9; 302 -0.6; 332 -0.3; 365 0.0; 402 0.2; 442 0.2; 486 0.2; 535 0.7; 588 0.6; 647 0.8; 712 0.4; 783 -0.0; 861 -0.4; 947 -0.3; 1042 0.3; 1146 0.8; 1261 0.9; 1387 0.6; 1526 -0.3; 1678 -2.1; 1846 -3.9; 2031 -5.0; 2234 -4.5; 2457 -3.7; 2703 -2.9; 2973 -2.8; 3270 -1.7; 3597 1.5; 3957 5.5; 4353 2.8; 4788 -0.4; 5267 -1.4; 5793 -2.0; 6373 -1.6; 7010 -1.8; 7711 -4.7; 8482 -6.7; 9330 -7.0; 10263 -6.2; 11289 -5.4; 12418 -6.1; 13660 -6.7; 15026 -2.9; 16529 -0.0; 18182 -1.5; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 EVO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 EVO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 55 Hz    |  0.45 | -6.6 dB |
| Peaking | 2217 Hz  |  2.37 | -5.1 dB |
| Peaking | 4017 Hz  |  7.05 | 7.5 dB  |
| Peaking | 9188 Hz  |  1.79 | -6.7 dB |
| Peaking | 13328 Hz |  2.62 | -5.8 dB |
| Peaking | 126 Hz   |  4.01 | -1.2 dB |
| Peaking | 488 Hz   |  1.14 | 1.0 dB  |
| Peaking | 1327 Hz  |  3.32 | 1.8 dB  |
| Peaking | 1840 Hz  |  5.87 | -1.5 dB |
| Peaking | 5534 Hz  | 11.11 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20681%20EVO/Superlux%20HD%20681%20EVO.png)