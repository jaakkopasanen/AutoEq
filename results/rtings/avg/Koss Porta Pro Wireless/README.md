# Koss Porta Pro Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.5; 25 2.8; 28 1.9; 31 1.0; 34 0.3; 37 -0.3; 41 -0.9; 45 -1.5; 49 -2.0; 54 -2.4; 60 -3.0; 66 -3.5; 72 -3.8; 79 -4.2; 87 -4.6; 96 -5.0; 106 -5.3; 116 -5.5; 128 -5.7; 141 -5.8; 155 -5.8; 170 -5.7; 187 -5.4; 206 -5.0; 227 -4.6; 249 -4.3; 274 -4.0; 302 -3.8; 332 -3.6; 365 -3.3; 402 -3.1; 442 -2.7; 486 -2.5; 535 -2.1; 588 -1.8; 647 -1.4; 712 -1.0; 783 -0.6; 861 -0.3; 947 -0.1; 1042 0.0; 1146 0.0; 1261 -0.1; 1387 -0.5; 1526 -1.0; 1678 -1.8; 1846 -2.5; 2031 -2.6; 2234 -1.3; 2457 0.7; 2703 2.4; 2973 2.6; 3270 1.6; 3597 1.9; 3957 3.8; 4353 6.0; 4788 5.7; 5267 -1.3; 5793 0.1; 6373 3.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 18 Hz    |  0.92 | 5.3 dB  |
| Peaking | 136 Hz   |  0.34 | -5.0 dB |
| Peaking | 137 Hz   |  1.17 | -0.9 dB |
| Peaking | 4340 Hz  |  3.56 | 6.4 dB  |
| Peaking | 22854 Hz |  2.26 | 1.1 dB  |
| Peaking | 1038 Hz  |  2.02 | 1.0 dB  |
| Peaking | 1959 Hz  |  2.65 | -3.1 dB |
| Peaking | 2766 Hz  |  4.47 | 3.1 dB  |
| Peaking | 5454 Hz  | 10.59 | -4.7 dB |
| Peaking | 6566 Hz  |  7.26 | 4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20Porta%20Pro%20Wireless/Koss%20Porta%20Pro%20Wireless.png)