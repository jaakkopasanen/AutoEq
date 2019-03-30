# Sennheiser HD 280-13
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.6; 45 -2.3; 49 -2.8; 54 -3.2; 60 -3.2; 66 -2.7; 72 -2.2; 79 -1.9; 87 -1.8; 96 -1.8; 106 -1.8; 116 -1.4; 128 -0.9; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -1.5; 227 -5.4; 249 -8.1; 274 -9.8; 302 -10.5; 332 -10.6; 365 -10.4; 402 -10.0; 442 -9.6; 486 -9.3; 535 -9.1; 588 -8.8; 647 -8.6; 712 -8.6; 783 -8.6; 861 -8.6; 947 -8.8; 1042 -9.2; 1146 -9.7; 1261 -9.9; 1387 -9.7; 1526 -9.3; 1678 -9.2; 1846 -8.8; 2031 -7.9; 2234 -6.6; 2457 -4.1; 2703 -1.6; 2973 -1.6; 3270 -3.1; 3597 -4.5; 3957 -5.6; 4353 -7.4; 4788 -9.2; 5267 -10.1; 5793 -10.0; 6373 -8.3; 7010 -5.0; 7711 -6.2; 8482 -6.5; 9330 -8.8; 10263 -11.5; 11289 -12.3; 12418 -10.1; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280-13 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280-13 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.33 | 6.3 dB  |
| Peaking | 125 Hz   | 1.46 | 6.3 dB  |
| Peaking | 187 Hz   | 3.67 | 6.4 dB  |
| Peaking | 1096 Hz  | 0.07 | -3.7 dB |
| Peaking | 2922 Hz  | 2.02 | 8.9 dB  |
| Peaking | 304 Hz   | 3.89 | -2.5 dB |
| Peaking | 5693 Hz  | 2.67 | -4.6 dB |
| Peaking | 7260 Hz  | 1.44 | 5.7 dB  |
| Peaking | 11221 Hz | 1.9  | -6.7 dB |
| Peaking | 13624 Hz | 1.48 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | 7.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20280-13/Sennheiser%20HD%20280-13.png)