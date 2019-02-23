# Audeze LCD-X sn7456406
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.3; 28 -2.8; 31 -4.1; 34 -4.5; 37 -4.6; 41 -5.0; 45 -5.1; 49 -5.2; 54 -5.4; 60 -5.4; 66 -5.5; 72 -5.8; 79 -5.9; 87 -6.4; 96 -6.8; 106 -7.1; 116 -7.2; 128 -7.6; 141 -7.8; 155 -7.9; 170 -8.1; 187 -8.2; 206 -8.3; 227 -8.0; 249 -8.1; 274 -8.2; 302 -8.2; 332 -8.3; 365 -8.1; 402 -8.0; 442 -7.8; 486 -7.7; 535 -7.4; 588 -6.8; 647 -7.1; 712 -7.1; 783 -6.8; 861 -7.0; 947 -6.8; 1042 -6.3; 1146 -5.8; 1261 -5.5; 1387 -6.8; 1526 -7.0; 1678 -7.3; 1846 -7.7; 2031 -7.9; 2234 -8.3; 2457 -6.3; 2703 -4.5; 2973 -3.4; 3270 -2.6; 3597 -3.0; 3957 -3.3; 4353 -5.5; 4788 -6.2; 5267 -7.8; 5793 -4.1; 6373 -4.5; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -8.7; 18182 -9.0; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X sn7456406 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X sn7456406 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.72 | 8.2 dB  |
| Peaking | 252 Hz   | 0.6  | -1.9 dB |
| Peaking | 3414 Hz  | 3.36 | 4.4 dB  |
| Peaking | 15252 Hz | 0.4  | 1.0 dB  |
| Peaking | 18083 Hz | 0.74 | -3.6 dB |
| Peaking | 1201 Hz  | 5.55 | 1.5 dB  |
| Peaking | 2234 Hz  | 2.39 | -3.3 dB |
| Peaking | 2653 Hz  | 3.05 | 2.7 dB  |
| Peaking | 5326 Hz  | 6.31 | -2.6 dB |
| Peaking | 5965 Hz  | 8.62 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X%20sn7456406/Audeze%20LCD-X%20sn7456406.png)