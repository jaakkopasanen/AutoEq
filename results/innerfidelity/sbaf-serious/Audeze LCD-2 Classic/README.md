# Audeze LCD-2 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.4; 25 -3.5; 28 -3.6; 31 -3.7; 34 -3.8; 37 -3.9; 41 -4.0; 45 -4.1; 49 -4.2; 54 -4.5; 60 -4.7; 66 -5.0; 72 -5.3; 79 -5.7; 87 -6.1; 96 -6.5; 106 -6.6; 116 -6.8; 128 -7.1; 141 -7.3; 155 -7.5; 170 -7.6; 187 -7.8; 206 -7.9; 227 -8.0; 249 -8.1; 274 -8.2; 302 -8.3; 332 -8.4; 365 -8.4; 402 -8.5; 442 -8.3; 486 -8.3; 535 -8.3; 588 -8.0; 647 -8.7; 712 -9.3; 783 -9.5; 861 -9.6; 947 -8.8; 1042 -8.9; 1146 -8.5; 1261 -8.7; 1387 -9.0; 1526 -9.6; 1678 -9.9; 1846 -8.8; 2031 -7.7; 2234 -7.9; 2457 -5.9; 2703 -5.6; 2973 -4.1; 3270 -3.0; 3597 -1.2; 3957 -0.5; 4353 -0.9; 4788 -2.1; 5267 -1.7; 5793 -4.7; 6373 -5.9; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.31 | 3.2 dB  |
| Peaking | 252 Hz  |  0.33 | -2.0 dB |
| Peaking | 813 Hz  |  2.56 | -1.8 dB |
| Peaking | 1668 Hz |  1.68 | -3.2 dB |
| Peaking | 4053 Hz |  1.64 | 6.5 dB  |
| Peaking | 91 Hz   |  4.17 | -0.2 dB |
| Peaking | 5318 Hz | 13.87 | 2.1 dB  |
| Peaking | 8235 Hz |  0.64 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)