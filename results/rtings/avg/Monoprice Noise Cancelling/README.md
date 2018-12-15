# Monoprice Noise Cancelling

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.1; 28 -0.5; 31 -1.0; 34 -1.4; 37 -1.7; 41 -2.1; 45 -2.4; 49 -2.7; 54 -2.9; 60 -3.3; 66 -3.7; 72 -4.0; 79 -4.4; 87 -4.9; 96 -5.4; 106 -5.9; 116 -6.2; 128 -6.5; 141 -6.7; 155 -6.7; 170 -6.7; 187 -6.6; 206 -6.3; 227 -6.0; 249 -5.8; 274 -5.7; 302 -5.7; 332 -5.6; 365 -5.6; 402 -5.5; 442 -5.8; 486 -6.2; 535 -5.8; 588 -5.0; 647 -4.9; 712 -4.9; 783 -4.5; 861 -2.8; 947 -0.8; 1042 0.4; 1146 -0.2; 1261 -1.0; 1387 -0.0; 1526 0.0; 1678 -0.9; 1846 -0.9; 2031 0.2; 2234 0.7; 2457 1.7; 2703 2.5; 2973 1.9; 3270 0.7; 3597 1.4; 3957 2.8; 4353 2.2; 4788 3.0; 5267 1.5; 5793 -1.0; 6373 1.6; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.5; 15026 -3.7; 16529 -4.7; 18182 -3.1; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Noise Cancelling GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Noise Cancelling ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 108 Hz   |  0.56 | -1.4 dB |
| Peaking | 168 Hz   |  0.48 | -5.3 dB |
| Peaking | 553 Hz   |  1.25 | -4.1 dB |
| Peaking | 3961 Hz  |  0.76 | 2.2 dB  |
| Peaking | 16813 Hz |  1.5  | -5.0 dB |
| Peaking | 19 Hz    |  2.3  | 1.4 dB  |
| Peaking | 781 Hz   |  6.48 | -1.7 dB |
| Peaking | 1032 Hz  |  5.16 | 2.1 dB  |
| Peaking | 1802 Hz  |  7.2  | -1.5 dB |
| Peaking | 6854 Hz  | 14.75 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monoprice%20Noise%20Cancelling/Monoprice%20Noise%20Cancelling.png)