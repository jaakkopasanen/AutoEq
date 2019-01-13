# InEar StageDriver 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.6; 23 -1.6; 25 -1.7; 28 -1.9; 31 -2.0; 34 -2.1; 37 -2.2; 41 -2.4; 45 -2.6; 49 -2.8; 54 -3.0; 60 -3.3; 66 -3.6; 72 -4.0; 79 -4.3; 87 -4.8; 96 -5.2; 106 -5.5; 116 -5.7; 128 -6.0; 141 -6.3; 155 -6.4; 170 -6.5; 187 -6.5; 206 -6.4; 227 -6.2; 249 -5.9; 274 -5.6; 302 -5.1; 332 -4.6; 365 -4.0; 402 -3.4; 442 -2.6; 486 -2.2; 535 -1.6; 588 -0.8; 647 -0.4; 712 -0.1; 783 0.4; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.9; 1387 -1.6; 1526 -2.6; 1678 -3.4; 1846 -4.1; 2031 -4.6; 2234 -4.4; 2457 -1.9; 2703 0.9; 2973 4.3; 3270 5.9; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.6; 5267 3.0; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar StageDriver 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDriver 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.5  | -4.6 dB |
| Peaking | 239 Hz  | 1.01 | -3.8 dB |
| Peaking | 2120 Hz | 1.96 | -7.6 dB |
| Peaking | 3540 Hz | 1.34 | 7.9 dB  |
| Peaking | 6107 Hz | 5.28 | 4.4 dB  |
| Peaking | 24 Hz   | 1.53 | -0.9 dB |
| Peaking | 828 Hz  | 2.39 | 1.3 dB  |
| Peaking | 1559 Hz | 5.55 | -1.0 dB |
| Peaking | 6665 Hz | 6.88 | 1.4 dB  |
| Peaking | 7958 Hz | 2.44 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/InEar%20StageDriver%203/InEar%20StageDriver%203.png)