# NuForce EDC3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.0; 25 -2.1; 28 -2.3; 31 -2.4; 34 -2.6; 37 -2.7; 41 -2.8; 45 -3.0; 49 -3.2; 54 -3.4; 60 -3.7; 66 -4.0; 72 -4.2; 79 -4.6; 87 -5.0; 96 -5.4; 106 -5.8; 116 -6.1; 128 -6.4; 141 -6.6; 155 -6.8; 170 -6.9; 187 -7.0; 206 -7.1; 227 -7.6; 249 -8.1; 274 -8.3; 302 -8.3; 332 -8.1; 365 -7.9; 402 -7.9; 442 -7.9; 486 -7.8; 535 -7.6; 588 -7.3; 647 -7.1; 712 -6.7; 783 -6.4; 861 -6.2; 947 -6.3; 1042 -6.7; 1146 -7.3; 1261 -8.1; 1387 -8.5; 1526 -8.3; 1678 -7.4; 1846 -6.3; 2031 -5.2; 2234 -4.1; 2457 -3.2; 2703 -2.5; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.2; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce EDC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce EDC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.6  | 4.3 dB  |
| Peaking | 58 Hz   | 1.12 | 1.6 dB  |
| Peaking | 312 Hz  | 0.94 | -1.9 dB |
| Peaking | 1471 Hz | 2.6  | -3.3 dB |
| Peaking | 4009 Hz | 0.94 | 6.8 dB  |
| Peaking | 1882 Hz | 3.75 | -0.5 dB |
| Peaking | 3998 Hz | 3.44 | -1.5 dB |
| Peaking | 4050 Hz | 0.85 | 1.2 dB  |
| Peaking | 6330 Hz | 3.51 | 4.7 dB  |
| Peaking | 7235 Hz | 1.33 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/NuForce%20EDC3/NuForce%20EDC3.png)