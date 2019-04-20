# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.9; 28 -4.0; 31 -4.1; 34 -4.2; 37 -4.4; 41 -4.5; 45 -4.7; 49 -4.9; 54 -5.1; 60 -5.5; 66 -5.8; 72 -6.2; 79 -6.6; 87 -7.0; 96 -7.5; 106 -8.0; 116 -8.4; 128 -8.8; 141 -9.1; 155 -9.4; 170 -9.6; 187 -9.8; 206 -10.0; 227 -10.1; 249 -10.2; 274 -10.2; 302 -10.1; 332 -10.0; 365 -9.8; 402 -9.7; 442 -9.6; 486 -9.4; 535 -9.2; 588 -8.9; 647 -8.6; 712 -8.3; 783 -7.9; 861 -7.7; 947 -7.7; 1042 -7.8; 1146 -7.8; 1261 -7.6; 1387 -7.1; 1526 -6.4; 1678 -5.8; 1846 -5.2; 2031 -4.4; 2234 -3.1; 2457 -1.8; 2703 -1.2; 2973 -1.3; 3270 -1.5; 3597 -1.2; 3957 -0.6; 4353 -0.5; 4788 -0.6; 5267 -1.2; 5793 -1.7; 6373 -2.1; 7010 -4.1; 7711 -6.2; 8482 -6.6; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.8; 15026 -9.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.34 | 3.2 dB  |
| Peaking | 225 Hz   | 0.32 | -4.1 dB |
| Peaking | 2699 Hz  | 1.94 | 4.4 dB  |
| Peaking | 4715 Hz  | 1.49 | 5.8 dB  |
| Peaking | 14657 Hz | 3.62 | -3.6 dB |
| Peaking | 1111 Hz  | 1.11 | 1.1 dB  |
| Peaking | 1225 Hz  | 2.11 | -1.8 dB |
| Peaking | 5017 Hz  | 5.77 | -0.6 dB |
| Peaking | 6484 Hz  | 3.99 | 2.1 dB  |
| Peaking | 8073 Hz  | 2.35 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE535/Shure%20SE535.png)