# Superlux HD 681 EVO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.1; 23 -3.6; 25 -4.1; 28 -4.8; 31 -5.4; 34 -5.7; 37 -6.0; 41 -6.2; 45 -6.3; 49 -6.3; 54 -6.3; 60 -6.1; 66 -6.0; 72 -5.7; 79 -5.5; 87 -5.3; 96 -5.2; 106 -5.2; 116 -5.1; 128 -4.8; 141 -4.1; 155 -3.1; 170 -2.6; 187 -2.3; 206 -1.8; 227 -1.5; 249 -1.2; 274 -0.9; 302 -0.6; 332 -0.3; 365 0.0; 402 0.2; 442 0.2; 486 0.2; 535 0.7; 588 0.6; 647 0.8; 712 0.4; 783 -0.0; 861 -0.4; 947 -0.3; 1042 0.3; 1146 0.8; 1261 0.9; 1387 0.6; 1526 -0.3; 1678 -2.1; 1846 -3.9; 2031 -5.0; 2234 -4.5; 2457 -3.6; 2703 -2.7; 2973 -2.3; 3270 -1.0; 3597 2.5; 3957 6.0; 4353 4.0; 4788 1.4; 5267 1.2; 5793 0.4; 6373 -0.4; 7010 -1.0; 7711 -3.3; 8482 -6.1; 9330 -8.4; 10263 -8.0; 11289 -4.6; 12418 -2.9; 13660 -3.4; 15026 -0.6; 16529 0.0; 18182 0.0; 20000 -1.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 EVO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 EVO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.61 | -6.2 dB |
| Peaking | 118 Hz   | 1.41 | -2.9 dB |
| Peaking | 2219 Hz  | 2.37 | -5.3 dB |
| Peaking | 4046 Hz  | 4.41 | 7.3 dB  |
| Peaking | 9763 Hz  | 2.26 | -9.1 dB |
| Peaking | 1680 Hz  | 1.09 | 2.6 dB  |
| Peaking | 1836 Hz  | 3.27 | -3.5 dB |
| Peaking | 3072 Hz  | 4.54 | -2.1 dB |
| Peaking | 6031 Hz  | 3.5  | 1.1 dB  |
| Peaking | 13685 Hz | 6.73 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Superlux%20HD%20681%20EVO/Superlux%20HD%20681%20EVO.png)