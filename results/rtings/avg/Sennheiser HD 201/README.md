# Sennheiser HD 201
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.9; 37 -1.2; 41 -1.5; 45 -1.7; 49 -1.8; 54 -1.9; 60 -2.0; 66 -2.2; 72 -2.4; 79 -2.7; 87 -3.1; 96 -3.4; 106 -3.6; 116 -3.9; 128 -4.1; 141 -4.3; 155 -4.4; 170 -4.3; 187 -4.3; 206 -4.3; 227 -4.1; 249 -3.9; 274 -3.8; 302 -5.3; 332 -6.0; 365 -6.5; 402 -7.2; 442 -7.8; 486 -8.2; 535 -8.3; 588 -8.0; 647 -7.7; 712 -7.6; 783 -7.9; 861 -8.2; 947 -8.4; 1042 -8.6; 1146 -8.7; 1261 -8.4; 1387 -8.7; 1526 -9.8; 1678 -6.5; 1846 -9.0; 2031 -9.7; 2234 -9.2; 2457 -7.7; 2703 -6.7; 2973 -7.2; 3270 -8.4; 3597 -8.6; 3957 -6.3; 4353 -0.7; 4788 -0.5; 5267 -6.6; 5793 -3.7; 6373 -5.5; 7010 -7.5; 7711 -9.5; 8482 -10.5; 9330 -9.9; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 201 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 16 Hz   |  0.39 | 4.0 dB  |
| Peaking | 66 Hz   |  0.16 | 3.0 dB  |
| Peaking | 1096 Hz |  0.32 | -2.6 dB |
| Peaking | 4611 Hz |  4.88 | 7.9 dB  |
| Peaking | 8588 Hz |  4.1  | -4.5 dB |
| Peaking | 264 Hz  |  5.17 | 1.8 dB  |
| Peaking | 466 Hz  |  3.68 | -1.2 dB |
| Peaking | 2778 Hz |  7.82 | 1.7 dB  |
| Peaking | 3534 Hz |  6.33 | -2.2 dB |
| Peaking | 6020 Hz | 10.79 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.4 dB  |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)