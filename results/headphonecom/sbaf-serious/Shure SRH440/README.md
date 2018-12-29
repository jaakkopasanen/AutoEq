# Shure SRH440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.8; 87 4.0; 96 2.8; 106 2.0; 116 1.8; 128 1.5; 141 1.4; 155 1.1; 170 1.7; 187 1.5; 206 1.6; 227 1.8; 249 1.6; 274 1.1; 302 0.7; 332 0.3; 365 -0.5; 402 -0.5; 442 -0.4; 486 -0.4; 535 -0.4; 588 -0.4; 647 -0.4; 712 -0.4; 783 -0.3; 861 -0.4; 947 -0.2; 1042 0.7; 1146 0.2; 1261 -0.3; 1387 -1.0; 1526 -2.0; 1678 -2.7; 1846 -2.5; 2031 -1.3; 2234 -0.1; 2457 1.3; 2703 1.8; 2973 2.2; 3270 1.9; 3597 1.3; 3957 1.7; 4353 0.6; 4788 1.6; 5267 5.6; 5793 2.2; 6373 5.4; 7010 2.5; 7711 0.3; 8482 -1.6; 9330 -5.9; 10263 -6.4; 11289 -0.9; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.46 | 6.7 dB  |
| Peaking | 1760 Hz | 2.78 | -3.3 dB |
| Peaking | 2825 Hz | 2.35 | 2.4 dB  |
| Peaking | 6157 Hz | 2.17 | 5.0 dB  |
| Peaking | 9720 Hz | 3.94 | -8.3 dB |
| Peaking | 39 Hz   | 2.4  | -0.8 dB |
| Peaking | 76 Hz   | 2.69 | 2.5 dB  |
| Peaking | 105 Hz  | 1.27 | -1.5 dB |
| Peaking | 240 Hz  | 1.7  | 1.4 dB  |
| Peaking | 394 Hz  | 1.47 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH440/Shure%20SRH440.png)