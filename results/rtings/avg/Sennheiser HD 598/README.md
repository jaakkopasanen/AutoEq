# Sennheiser HD 598
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.1; 49 -1.8; 54 -2.5; 60 -3.3; 66 -4.0; 72 -4.6; 79 -5.1; 87 -5.8; 96 -6.4; 106 -6.9; 116 -7.4; 128 -7.9; 141 -8.2; 155 -8.4; 170 -8.5; 187 -8.4; 206 -8.2; 227 -8.0; 249 -7.8; 274 -7.6; 302 -7.5; 332 -7.3; 365 -7.1; 402 -6.8; 442 -6.7; 486 -6.8; 535 -6.5; 588 -5.6; 647 -5.6; 712 -5.4; 783 -5.2; 861 -5.0; 947 -4.9; 1042 -4.8; 1146 -4.7; 1261 -4.8; 1387 -4.9; 1526 -4.8; 1678 -4.8; 1846 -5.0; 2031 -5.6; 2234 -6.0; 2457 -5.9; 2703 -6.0; 2973 -6.1; 3270 -7.1; 3597 -7.7; 3957 -8.2; 4353 -9.4; 4788 -7.5; 5267 -5.9; 5793 -6.2; 6373 -5.1; 7010 -4.1; 7711 -6.2; 8482 -7.6; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -11.2; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 31 Hz   |  0.44 | 6.7 dB  |
| Peaking | 139 Hz  |  0.59 | -3.2 dB |
| Peaking | 1146 Hz |  0.76 | 2.0 dB  |
| Peaking | 4217 Hz |  4.36 | -3.2 dB |
| Peaking | 6791 Hz |  8.07 | 3.1 dB  |
| Peaking | 3423 Hz | 10.76 | -0.8 dB |
| Peaking | 5278 Hz |  8.19 | 1.0 dB  |
| Peaking | 9015 Hz |  7.77 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)