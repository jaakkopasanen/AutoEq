# InEar StageDriver 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -7.9; 25 -7.9; 28 -8.1; 31 -8.2; 34 -8.3; 37 -8.4; 41 -8.6; 45 -8.8; 49 -9.0; 54 -9.3; 60 -9.5; 66 -9.8; 72 -10.2; 79 -10.5; 87 -11.0; 96 -11.4; 106 -11.7; 116 -11.9; 128 -12.2; 141 -12.5; 155 -12.6; 170 -12.7; 187 -12.7; 206 -12.6; 227 -12.4; 249 -12.2; 274 -11.8; 302 -11.3; 332 -10.8; 365 -10.2; 402 -9.6; 442 -8.8; 486 -8.4; 535 -7.8; 588 -7.0; 647 -6.6; 712 -6.3; 783 -5.9; 861 -5.8; 947 -6.0; 1042 -6.3; 1146 -6.6; 1261 -7.1; 1387 -7.8; 1526 -8.8; 1678 -9.6; 1846 -10.3; 2031 -10.8; 2234 -10.6; 2457 -8.2; 2703 -5.3; 2973 -1.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -3.2; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.8
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
| Peaking | 113 Hz  | 0.56 | -4.7 dB |
| Peaking | 243 Hz  | 1.12 | -3.5 dB |
| Peaking | 2122 Hz | 2.02 | -7.7 dB |
| Peaking | 3501 Hz | 1.24 | 7.9 dB  |
| Peaking | 6094 Hz | 5.17 | 4.3 dB  |
| Peaking | 25 Hz   | 1.47 | -0.9 dB |
| Peaking | 832 Hz  | 2.25 | 1.4 dB  |
| Peaking | 1577 Hz | 5.53 | -1.0 dB |
| Peaking | 6664 Hz | 8.65 | 1.5 dB  |
| Peaking | 8069 Hz | 2.39 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/InEar%20StageDriver%203/InEar%20StageDriver%203.png)