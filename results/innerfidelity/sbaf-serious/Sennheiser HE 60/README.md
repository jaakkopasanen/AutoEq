# Sennheiser HE 60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.8; 41 5.7; 45 5.7; 49 5.7; 54 5.8; 60 5.6; 66 5.2; 72 4.8; 79 2.9; 87 2.1; 96 2.1; 106 2.1; 116 2.1; 128 1.8; 141 1.8; 155 1.6; 170 1.4; 187 1.4; 206 1.3; 227 1.2; 249 1.1; 274 1.1; 302 1.1; 332 1.1; 365 1.1; 402 1.0; 442 1.0; 486 0.9; 535 1.3; 588 2.1; 647 2.0; 712 1.3; 783 1.8; 861 1.8; 947 0.5; 1042 0.1; 1146 0.2; 1261 0.5; 1387 0.0; 1526 -0.6; 1678 -0.8; 1846 -1.0; 2031 -0.6; 2234 -0.1; 2457 0.6; 2703 0.8; 2973 0.8; 3270 0.8; 3597 2.1; 3957 2.0; 4353 0.9; 4788 -0.3; 5267 -2.6; 5793 -3.8; 6373 -1.5; 7010 1.8; 7711 0.3; 8482 -0.2; 9330 -2.5; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.2; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HE 60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HE 60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.28 | 6.1 dB  |
| Peaking | 58 Hz   | 3.13 | 1.7 dB  |
| Peaking | 628 Hz  | 1.53 | 1.9 dB  |
| Peaking | 3789 Hz | 3.6  | 2.5 dB  |
| Peaking | 5691 Hz | 5.41 | -4.4 dB |
| Peaking | 89 Hz   | 3.64 | -1.3 dB |
| Peaking | 139 Hz  | 0.35 | 0.3 dB  |
| Peaking | 1761 Hz | 3.8  | -1.3 dB |
| Peaking | 7017 Hz | 9.59 | 2.5 dB  |
| Peaking | 9205 Hz | 9.21 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HE%2060/Sennheiser%20HE%2060.png)