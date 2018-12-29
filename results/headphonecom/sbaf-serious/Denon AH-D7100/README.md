# Denon AH-D7100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -6.8; 23 -6.8; 25 -6.8; 28 -6.7; 31 -6.6; 34 -6.5; 37 -6.3; 41 -6.1; 45 -5.8; 49 -5.6; 54 -5.1; 60 -4.2; 66 -4.1; 72 -4.6; 79 -5.2; 87 -6.1; 96 -7.2; 106 -7.4; 116 -7.4; 128 -7.3; 141 -7.0; 155 -6.4; 170 -4.9; 187 -4.6; 206 -2.8; 227 -0.2; 249 2.8; 274 5.6; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 5.4; 486 4.6; 535 3.7; 588 2.9; 647 1.9; 712 1.4; 783 1.1; 861 0.7; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.9; 1387 -1.7; 1526 -2.8; 1678 -3.5; 1846 -3.3; 2031 -2.6; 2234 -1.2; 2457 1.1; 2703 2.6; 2973 2.7; 3270 3.6; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 4.8; 6373 3.6; 7010 2.5; 7711 0.3; 8482 -2.0; 9330 -4.8; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.3; 18182 -7.3; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.74 | -6.6 dB |
| Peaking | 141 Hz   | 0.75 | -8.7 dB |
| Peaking | 323 Hz   | 1.2  | 10.1 dB |
| Peaking | 4514 Hz  | 1.88 | 7.2 dB  |
| Peaking | 18158 Hz | 3.13 | -8.1 dB |
| Peaking | 508 Hz   | 3.3  | 1.3 dB  |
| Peaking | 1841 Hz  | 1.69 | -5.0 dB |
| Peaking | 2759 Hz  | 1.86 | 2.7 dB  |
| Peaking | 6546 Hz  | 4.59 | 2.0 dB  |
| Peaking | 9074 Hz  | 6.42 | -6.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7100/Denon%20AH-D7100.png)