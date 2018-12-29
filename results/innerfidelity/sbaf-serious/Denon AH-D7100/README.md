# Denon AH-D7100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.6; 23 -4.7; 25 -4.7; 28 -4.6; 31 -4.5; 34 -4.4; 37 -4.3; 41 -4.0; 45 -3.7; 49 -3.3; 54 -2.8; 60 -2.7; 66 -3.1; 72 -3.6; 79 -4.0; 87 -4.6; 96 -5.4; 106 -5.7; 116 -5.5; 128 -5.5; 141 -5.3; 155 -4.7; 170 -3.5; 187 -3.3; 206 -1.8; 227 0.4; 249 2.7; 274 5.3; 302 6.0; 332 6.0; 365 5.9; 402 5.3; 442 4.8; 486 4.1; 535 3.5; 588 3.2; 647 2.3; 712 1.5; 783 1.1; 861 0.6; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.7; 1526 -2.9; 1678 -3.7; 1846 -3.6; 2031 -3.0; 2234 -1.5; 2457 1.6; 2703 2.2; 2973 1.9; 3270 2.7; 3597 5.5; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 3.6; 6373 2.9; 7010 2.5; 7711 0.3; 8482 -1.3; 9330 -4.1; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.6; 18182 -5.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.94 | -4.5 dB |
| Peaking | 142 Hz   | 0.69 | -7.0 dB |
| Peaking | 323 Hz   | 1.19 | 9.4 dB  |
| Peaking | 4518 Hz  | 2.07 | 7.1 dB  |
| Peaking | 17838 Hz | 2.71 | -6.3 dB |
| Peaking | 579 Hz   | 2.86 | 1.3 dB  |
| Peaking | 1888 Hz  | 1.68 | -5.5 dB |
| Peaking | 2533 Hz  | 2.45 | 3.2 dB  |
| Peaking | 8299 Hz  | 0.89 | 1.6 dB  |
| Peaking | 9044 Hz  | 4.63 | -6.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7100/Denon%20AH-D7100.png)