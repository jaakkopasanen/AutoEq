# Sennheiser IE 80 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.2; 25 -11.2; 28 -11.3; 31 -11.3; 34 -11.4; 37 -11.4; 41 -11.4; 45 -11.5; 49 -11.6; 54 -11.7; 60 -11.8; 66 -11.9; 72 -12.1; 79 -12.2; 87 -12.4; 96 -12.6; 106 -12.7; 116 -12.7; 128 -12.7; 141 -12.6; 155 -12.4; 170 -12.1; 187 -11.8; 206 -11.4; 227 -10.9; 249 -10.4; 274 -9.8; 302 -9.3; 332 -8.6; 365 -8.0; 402 -7.3; 442 -6.7; 486 -6.0; 535 -5.2; 588 -4.5; 647 -3.8; 712 -2.9; 783 -2.2; 861 -1.6; 947 -1.0; 1042 -0.7; 1146 -0.8; 1261 -0.8; 1387 -0.9; 1526 -1.2; 1678 -1.3; 1846 -1.3; 2031 -1.2; 2234 -1.3; 2457 -1.6; 2703 -2.2; 2973 -2.9; 3270 -3.5; 3597 -4.1; 3957 -4.9; 4353 -6.5; 4788 -9.1; 5267 -9.0; 5793 -4.7; 6373 -1.3; 7010 -0.5; 7711 -1.7; 8482 -1.0; 9330 -0.8; 10263 -0.8; 11289 -0.9; 12418 -2.4; 13660 -2.1; 15026 -0.8; 16529 -0.8; 18182 -0.8; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 80 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 80 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.89 | -10.2 dB |
| Peaking | 66 Hz    | 0.29 | -9.7 dB  |
| Peaking | 227 Hz   | 0.6  | -5.1 dB  |
| Peaking | 4848 Hz  | 2.91 | -9.0 dB  |
| Peaking | 13126 Hz | 5.58 | -2.0 dB  |
| Peaking | 12 Hz    | 1.17 | 1.6 dB   |
| Peaking | 496 Hz   | 2.01 | -0.9 dB  |
| Peaking | 1010 Hz  | 1.68 | 1.4 dB   |
| Peaking | 3251 Hz  | 3.43 | -1.4 dB  |
| Peaking | 6691 Hz  | 6.7  | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -7.7 dB  |
| Peaking | 125 Hz   | 1.41 | -9.7 dB  |
| Peaking | 250 Hz   | 1.41 | -7.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20IE%2080%20S/Sennheiser%20IE%2080%20S.png)