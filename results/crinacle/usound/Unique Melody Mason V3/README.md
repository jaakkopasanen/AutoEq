# Unique Melody Mason V3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.3; 28 -6.6; 31 -6.9; 34 -7.1; 37 -7.2; 41 -7.4; 45 -7.5; 49 -7.5; 54 -7.6; 60 -7.7; 66 -7.8; 72 -7.9; 79 -8.1; 87 -8.2; 96 -8.3; 106 -8.4; 116 -8.4; 128 -8.4; 141 -8.3; 155 -8.3; 170 -8.1; 187 -7.9; 206 -7.7; 227 -7.5; 249 -7.2; 274 -7.0; 302 -6.7; 332 -6.5; 365 -6.4; 402 -6.3; 442 -6.2; 486 -6.1; 535 -6.0; 588 -5.9; 647 -5.9; 712 -5.9; 783 -5.8; 861 -5.8; 947 -6.0; 1042 -6.5; 1146 -7.2; 1261 -8.1; 1387 -8.7; 1526 -8.7; 1678 -8.3; 1846 -7.6; 2031 -7.1; 2234 -6.5; 2457 -5.5; 2703 -4.3; 2973 -3.1; 3270 -3.1; 3597 -1.9; 3957 -0.5; 4353 -1.0; 4788 -4.7; 5267 -9.6; 5793 -11.5; 6373 -8.1; 7010 -8.2; 7711 -9.0; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -8.3; 18182 -9.5; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Mason V3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Mason V3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 83 Hz    | 0.9  | -1.5 dB  |
| Peaking | 155 Hz   | 1.69 | -1.3 dB  |
| Peaking | 1570 Hz  | 2.44 | -3.0 dB  |
| Peaking | 4372 Hz  | 1.57 | 11.3 dB  |
| Peaking | 5394 Hz  | 1.99 | -11.0 dB |
| Peaking | 18 Hz    | 1.79 | 1.0 dB   |
| Peaking | 759 Hz   | 1.17 | 0.9 dB   |
| Peaking | 1263 Hz  | 4.61 | -1.0 dB  |
| Peaking | 2954 Hz  | 9.87 | 0.9 dB   |
| Peaking | 19431 Hz | 0.86 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%20Mason%20V3/Unique%20Melody%20Mason%20V3.png)