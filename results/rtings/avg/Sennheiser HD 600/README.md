# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.4; 45 -2.0; 49 -2.5; 54 -3.0; 60 -3.7; 66 -4.3; 72 -4.9; 79 -5.5; 87 -6.1; 96 -6.6; 106 -7.1; 116 -7.5; 128 -7.9; 141 -8.2; 155 -8.4; 170 -8.5; 187 -8.5; 206 -8.3; 227 -8.1; 249 -7.9; 274 -7.7; 302 -7.6; 332 -7.7; 365 -7.7; 402 -7.6; 442 -7.6; 486 -7.7; 535 -7.6; 588 -7.5; 647 -7.4; 712 -7.2; 783 -7.2; 861 -7.2; 947 -6.9; 1042 -6.8; 1146 -7.4; 1261 -7.9; 1387 -8.6; 1526 -9.1; 1678 -9.5; 1846 -9.9; 2031 -10.3; 2234 -9.3; 2457 -9.1; 2703 -9.0; 2973 -9.7; 3270 -10.4; 3597 -10.3; 3957 -9.4; 4353 -8.0; 4788 -8.0; 5267 -8.0; 5793 -7.2; 6373 -7.6; 7010 -7.7; 7711 -7.9; 8482 -8.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.6; 15026 -9.4; 16529 -8.8; 18182 -10.2; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.38 | 7.1 dB  |
| Peaking | 118 Hz   | 0.44 | -3.7 dB |
| Peaking | 1824 Hz  | 1.87 | -3.0 dB |
| Peaking | 3455 Hz  | 1.7  | -3.3 dB |
| Peaking | 20316 Hz | 0.56 | -8.8 dB |
| Peaking | 1398 Hz  | 6.37 | -0.2 dB |
| Peaking | 4466 Hz  | 9.41 | 0.8 dB  |
| Peaking | 8298 Hz  | 2.42 | -2.2 dB |
| Peaking | 9787 Hz  | 3.19 | 2.0 dB  |
| Peaking | 11613 Hz | 5.08 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)