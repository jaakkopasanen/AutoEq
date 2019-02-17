# InEar StageDriver 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.1; 25 -8.2; 28 -8.4; 31 -8.5; 34 -8.6; 37 -8.7; 41 -8.9; 45 -9.1; 49 -9.3; 54 -9.5; 60 -9.8; 66 -10.1; 72 -10.5; 79 -10.8; 87 -11.3; 96 -11.7; 106 -12.0; 116 -12.2; 128 -12.5; 141 -12.8; 155 -12.9; 170 -13.0; 187 -13.0; 206 -12.9; 227 -12.7; 249 -12.4; 274 -12.1; 302 -11.6; 332 -11.1; 365 -10.5; 402 -9.9; 442 -9.1; 486 -8.7; 535 -8.1; 588 -7.3; 647 -6.9; 712 -6.6; 783 -6.1; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.4; 1387 -8.1; 1526 -9.1; 1678 -9.9; 1846 -10.6; 2031 -11.1; 2234 -10.9; 2457 -8.4; 2703 -5.6; 2973 -2.2; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -3.5; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar StageDriver 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDriver 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.5  | -4.6 dB |
| Peaking | 239 Hz  | 1.01 | -3.8 dB |
| Peaking | 2123 Hz | 1.95 | -7.7 dB |
| Peaking | 3536 Hz | 1.31 | 7.9 dB  |
| Peaking | 6108 Hz | 5.23 | 4.4 dB  |
| Peaking | 21 Hz   | 1.61 | -0.9 dB |
| Peaking | 828 Hz  | 2.38 | 1.3 dB  |
| Peaking | 1560 Hz | 5.53 | -1.0 dB |
| Peaking | 6757 Hz | 7.23 | 1.4 dB  |
| Peaking | 7989 Hz | 2.39 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/InEar%20StageDriver%203/InEar%20StageDriver%203.png)