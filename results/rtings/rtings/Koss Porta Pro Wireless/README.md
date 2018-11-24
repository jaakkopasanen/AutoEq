# Koss Porta Pro Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.5; 25 2.8; 28 1.9; 31 1.0; 34 0.3; 37 -0.3; 41 -0.9; 45 -1.5; 49 -2.0; 54 -2.4; 60 -3.0; 66 -3.5; 72 -3.8; 79 -4.2; 87 -4.6; 96 -5.0; 106 -5.3; 116 -5.5; 128 -5.7; 141 -5.8; 155 -5.8; 170 -5.7; 187 -5.4; 206 -5.0; 227 -4.6; 249 -4.3; 274 -4.0; 302 -3.8; 332 -3.6; 365 -3.3; 402 -3.1; 442 -2.7; 486 -2.5; 535 -2.1; 588 -1.8; 647 -1.4; 712 -1.0; 783 -0.6; 861 -0.3; 947 -0.1; 1042 0.0; 1146 0.0; 1261 -0.1; 1387 -0.5; 1526 -1.0; 1678 -1.8; 1846 -2.5; 2031 -2.6; 2234 -1.3; 2457 0.7; 2703 2.6; 2973 3.1; 3270 2.4; 3597 2.9; 3957 5.0; 4353 6.0; 4788 6.0; 5267 1.2; 5793 2.5; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 18 Hz    |  0.85 | 5.5 dB  |
| Peaking | 136 Hz   |  0.31 | -4.6 dB |
| Peaking | 137 Hz   |  1.02 | -1.4 dB |
| Peaking | 4399 Hz  |  1.95 | 6.0 dB  |
| Peaking | 24000 Hz |  2.48 | 1.4 dB  |
| Peaking | 1026 Hz  |  1.81 | 1.0 dB  |
| Peaking | 1962 Hz  |  2.5  | -3.3 dB |
| Peaking | 2759 Hz  |  5.25 | 2.7 dB  |
| Peaking | 5387 Hz  | 11.65 | -3.5 dB |
| Peaking | 6430 Hz  |  7.7  | 3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Koss%20Porta%20Pro%20Wireless/Koss%20Porta%20Pro%20Wireless.png)