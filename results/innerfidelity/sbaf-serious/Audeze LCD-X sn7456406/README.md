# Audeze LCD-X sn7456406
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.1; 28 -2.6; 31 -3.9; 34 -4.3; 37 -4.4; 41 -4.8; 45 -4.9; 49 -5.0; 54 -5.2; 60 -5.2; 66 -5.3; 72 -5.6; 79 -5.7; 87 -6.2; 96 -6.6; 106 -6.9; 116 -7.0; 128 -7.4; 141 -7.6; 155 -7.7; 170 -7.9; 187 -8.0; 206 -8.1; 227 -7.8; 249 -7.9; 274 -8.0; 302 -8.0; 332 -8.1; 365 -7.9; 402 -7.8; 442 -7.6; 486 -7.5; 535 -7.2; 588 -6.6; 647 -6.9; 712 -6.9; 783 -6.6; 861 -6.8; 947 -6.6; 1042 -6.1; 1146 -5.6; 1261 -5.3; 1387 -6.6; 1526 -6.8; 1678 -7.1; 1846 -7.5; 2031 -7.7; 2234 -8.1; 2457 -6.1; 2703 -4.3; 2973 -3.2; 3270 -2.4; 3597 -2.8; 3957 -3.1; 4353 -5.3; 4788 -6.0; 5267 -7.6; 5793 -3.9; 6373 -4.3; 7010 -6.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -8.5; 18182 -8.9; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X sn7456406 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X sn7456406 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 12 Hz    |  0.59 | 9.2 dB  |
| Peaking | 242 Hz   |  0.7  | -1.7 dB |
| Peaking | 3405 Hz  |  3.3  | 4.7 dB  |
| Peaking | 6079 Hz  | 11.1  | 4.1 dB  |
| Peaking | 18323 Hz |  1.13 | -2.7 dB |
| Peaking | 33 Hz    |  3.25 | -0.8 dB |
| Peaking | 1203 Hz  |  6.57 | 1.4 dB  |
| Peaking | 2094 Hz  |  3.39 | -2.5 dB |
| Peaking | 3459 Hz  |  0.69 | 0.7 dB  |
| Peaking | 5237 Hz  |  7.55 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X%20sn7456406/Audeze%20LCD-X%20sn7456406.png)