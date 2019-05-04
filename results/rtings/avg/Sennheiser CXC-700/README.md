# Sennheiser CXC-700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.2; 28 -8.6; 31 -8.9; 34 -9.1; 37 -9.2; 41 -9.3; 45 -9.4; 49 -9.5; 54 -9.5; 60 -9.6; 66 -9.6; 72 -9.7; 79 -9.7; 87 -9.7; 96 -9.8; 106 -9.7; 116 -9.6; 128 -9.5; 141 -9.2; 155 -8.9; 170 -8.5; 187 -8.1; 206 -7.6; 227 -7.1; 249 -6.5; 274 -6.1; 302 -5.8; 332 -5.3; 365 -4.7; 402 -4.1; 442 -3.4; 486 -2.8; 535 -2.1; 588 -1.4; 647 -0.8; 712 -0.5; 783 -0.6; 861 -1.1; 947 -1.8; 1042 -2.3; 1146 -2.9; 1261 -3.4; 1387 -3.8; 1526 -3.9; 1678 -4.1; 1846 -4.4; 2031 -4.5; 2234 -4.2; 2457 -3.3; 2703 -2.5; 2973 -2.1; 3270 -2.1; 3597 -2.6; 3957 -3.1; 4353 -3.9; 4788 -5.4; 5267 -7.0; 5793 -8.3; 6373 -8.1; 7010 -6.8; 7711 -5.8; 8482 -6.2; 9330 -6.6; 10263 -5.1; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CXC-700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CXC-700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.55 | -3.6 dB |
| Peaking | 123 Hz  | 0.63 | -3.8 dB |
| Peaking | 702 Hz  | 1.2  | 4.8 dB  |
| Peaking | 3397 Hz | 1.8  | 3.3 dB  |
| Peaking | 5997 Hz | 2.08 | -4.0 dB |
| Peaking | 2049 Hz | 3.72 | -0.8 dB |
| Peaking | 2679 Hz | 5.54 | 0.7 dB  |
| Peaking | 9154 Hz | 8.44 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20CXC-700/Sennheiser%20CXC-700.png)