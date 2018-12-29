# Fidue A65
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 0.0; 23 2.5; 25 1.9; 28 1.1; 31 0.4; 34 -0.2; 37 -0.7; 41 -1.4; 45 -1.9; 49 -2.4; 54 -2.9; 60 -3.5; 66 -4.0; 72 -4.5; 79 -5.0; 87 -5.5; 96 -6.1; 106 -6.3; 116 -6.5; 128 -6.7; 141 -7.0; 155 -7.0; 170 -7.0; 187 -6.9; 206 -6.7; 227 -6.4; 249 -6.2; 274 -5.8; 302 -5.3; 332 -4.9; 365 -4.3; 402 -3.8; 442 -3.1; 486 -2.7; 535 -2.2; 588 -1.4; 647 -0.9; 712 -0.9; 783 -0.4; 861 0.0; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.8; 1387 -2.0; 1526 -3.6; 1678 -4.4; 1846 -4.3; 2031 -4.1; 2234 -3.9; 2457 -2.9; 2703 -2.2; 2973 -0.1; 3270 2.0; 3597 3.5; 3957 3.3; 4353 1.7; 4788 1.2; 5267 2.1; 5793 2.5; 6373 1.8; 7010 1.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A65 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A65 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.4  | 3.9 dB  |
| Peaking | 122 Hz  | 0.59 | -6.2 dB |
| Peaking | 271 Hz  | 1.09 | -3.1 dB |
| Peaking | 2112 Hz | 1.55 | -6.0 dB |
| Peaking | 3715 Hz | 1.14 | 4.2 dB  |
| Peaking | 996 Hz  | 2.14 | 1.3 dB  |
| Peaking | 1583 Hz | 5.96 | -1.7 dB |
| Peaking | 4656 Hz | 5.62 | -2.3 dB |
| Peaking | 6128 Hz | 1.32 | 1.8 dB  |
| Peaking | 8088 Hz | 1.46 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A65/Fidue%20A65.png)