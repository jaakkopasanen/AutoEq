# Sennheiser CXC-700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.2; 25 -3.5; 28 -3.9; 31 -4.1; 34 -4.3; 37 -4.5; 41 -4.6; 45 -4.7; 49 -4.7; 54 -4.9; 60 -5.2; 66 -5.5; 72 -5.8; 79 -6.0; 87 -6.4; 96 -6.7; 106 -7.1; 116 -7.5; 128 -7.8; 141 -8.0; 155 -8.1; 170 -8.0; 187 -7.9; 206 -7.6; 227 -7.2; 249 -6.7; 274 -6.3; 302 -5.9; 332 -5.5; 365 -4.9; 402 -4.2; 442 -3.5; 486 -2.9; 535 -2.1; 588 -1.4; 647 -0.8; 712 -0.5; 783 -0.6; 861 -1.1; 947 -1.8; 1042 -2.3; 1146 -2.8; 1261 -3.4; 1387 -3.7; 1526 -3.8; 1678 -4.0; 1846 -4.2; 2031 -4.2; 2234 -3.5; 2457 -2.5; 2703 -2.1; 2973 -2.1; 3270 -2.5; 3597 -3.0; 3957 -3.5; 4353 -4.4; 4788 -5.2; 5267 -6.7; 5793 -8.5; 6373 -9.2; 7010 -6.9; 7711 -5.1; 8482 -6.6; 9330 -8.4; 10263 -5.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CXC-700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CXC-700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 165 Hz  | 0.84 | -3.6 dB |
| Peaking | 710 Hz  | 1.27 | 4.6 dB  |
| Peaking | 3022 Hz | 2    | 2.8 dB  |
| Peaking | 6082 Hz | 3.65 | -4.9 dB |
| Peaking | 9352 Hz | 6.16 | -3.8 dB |
| Peaking | 16 Hz   | 1.16 | 2.4 dB  |
| Peaking | 1940 Hz | 6.14 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20CXC-700/Sennheiser%20CXC-700.png)