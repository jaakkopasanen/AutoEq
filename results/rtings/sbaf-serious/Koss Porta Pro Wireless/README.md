# Koss Porta Pro Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.8; 25 3.1; 28 2.0; 31 1.1; 34 0.3; 37 -0.4; 41 -1.1; 45 -1.8; 49 -2.3; 54 -2.8; 60 -3.2; 66 -3.6; 72 -3.8; 79 -4.0; 87 -4.3; 96 -4.5; 106 -4.8; 116 -5.0; 128 -5.2; 141 -5.2; 155 -5.2; 170 -5.0; 187 -4.8; 206 -4.5; 227 -4.1; 249 -3.7; 274 -3.4; 302 -3.0; 332 -2.7; 365 -2.3; 402 -2.0; 442 -1.6; 486 -1.3; 535 -0.9; 588 -0.7; 647 -0.4; 712 -0.1; 783 -0.1; 861 -0.1; 947 -0.0; 1042 0.1; 1146 0.2; 1261 0.2; 1387 -0.5; 1526 -1.4; 1678 -2.1; 1846 -2.4; 2031 -2.2; 2234 -0.8; 2457 1.2; 2703 3.2; 2973 4.1; 3270 4.2; 3597 5.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 1.6; 5793 4.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.99 | 5.7 dB  |
| Peaking | 56 Hz   | 0.84 | -1.9 dB |
| Peaking | 151 Hz  | 0.56 | -4.9 dB |
| Peaking | 4015 Hz | 2.1  | 6.6 dB  |
| Peaking | 6330 Hz | 6.72 | 4.8 dB  |
| Peaking | 1319 Hz | 0.99 | 1.5 dB  |
| Peaking | 1856 Hz | 1.69 | -4.2 dB |
| Peaking | 2787 Hz | 4.17 | 3.1 dB  |
| Peaking | 8049 Hz | 6.47 | -0.7 dB |
| Peaking | 9918 Hz | 2.57 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Koss%20Porta%20Pro%20Wireless/Koss%20Porta%20Pro%20Wireless.png)