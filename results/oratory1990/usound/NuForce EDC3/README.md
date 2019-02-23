# NuForce EDC3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.9; 28 -4.0; 31 -4.1; 34 -4.3; 37 -4.4; 41 -4.5; 45 -4.7; 49 -4.9; 54 -5.1; 60 -5.4; 66 -5.7; 72 -5.9; 79 -6.3; 87 -6.7; 96 -7.1; 106 -7.5; 116 -7.8; 128 -8.1; 141 -8.4; 155 -8.5; 170 -8.6; 187 -8.7; 206 -8.8; 227 -9.3; 249 -9.8; 274 -10.0; 302 -10.0; 332 -9.8; 365 -9.6; 402 -9.6; 442 -9.6; 486 -9.5; 535 -9.3; 588 -9.0; 647 -8.8; 712 -8.4; 783 -8.1; 861 -7.9; 947 -8.0; 1042 -8.4; 1146 -9.0; 1261 -9.8; 1387 -10.3; 1526 -10.0; 1678 -9.1; 1846 -8.0; 2031 -6.9; 2234 -5.8; 2457 -4.9; 2703 -4.2; 2973 -3.1; 3270 -1.4; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.9; 5793 -2.1; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce EDC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce EDC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.45 | 2.8 dB  |
| Peaking | 301 Hz  | 0.48 | -3.4 dB |
| Peaking | 1461 Hz | 2.14 | -3.9 dB |
| Peaking | 3924 Hz | 1.48 | 6.7 dB  |
| Peaking | 6301 Hz | 5.94 | 3.7 dB  |
| Peaking | 510 Hz  | 4.42 | -0.2 dB |
| Peaking | 3086 Hz | 2.97 | 0.2 dB  |
| Peaking | 6809 Hz | 3.31 | 1.4 dB  |
| Peaking | 7698 Hz | 2.28 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/NuForce%20EDC3/NuForce%20EDC3.png)