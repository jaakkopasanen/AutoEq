# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.9; 54 -1.4; 60 -2.1; 66 -2.7; 72 -3.3; 79 -3.9; 87 -4.5; 96 -5.0; 106 -5.5; 116 -5.9; 128 -6.3; 141 -6.6; 155 -6.8; 170 -6.9; 187 -6.9; 206 -6.7; 227 -6.5; 249 -6.3; 274 -6.1; 302 -6.0; 332 -6.1; 365 -6.1; 402 -6.0; 442 -6.0; 486 -6.1; 535 -6.0; 588 -5.9; 647 -5.8; 712 -5.6; 783 -5.6; 861 -5.6; 947 -5.3; 1042 -5.2; 1146 -5.8; 1261 -6.3; 1387 -7.0; 1526 -7.5; 1678 -7.9; 1846 -8.3; 2031 -8.7; 2234 -7.7; 2457 -7.5; 2703 -7.4; 2973 -8.1; 3270 -8.8; 3597 -8.7; 3957 -7.8; 4353 -6.4; 4788 -6.4; 5267 -6.5; 5793 -5.6; 6373 -6.0; 7010 -6.1; 7711 -6.3; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.8; 16529 -7.3; 18182 -8.6; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.71 | 6.8 dB  |
| Peaking | 959 Hz  | 1.25 | 1.4 dB  |
| Peaking | 1839 Hz | 1.93 | -2.2 dB |
| Peaking | 3430 Hz | 3.6  | -2.4 dB |
| Peaking | 5851 Hz | 2.64 | 0.8 dB  |
| Peaking | 23 Hz   | 0.31 | 2.5 dB  |
| Peaking | 32 Hz   | 1.46 | -3.2 dB |
| Peaking | 159 Hz  | 0.85 | -1.6 dB |
| Peaking | 285 Hz  | 1.12 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)