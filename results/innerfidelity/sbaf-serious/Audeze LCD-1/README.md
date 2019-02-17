# Audeze LCD-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.9; 45 -1.3; 49 -1.6; 54 -1.9; 60 -2.1; 66 -2.1; 72 -2.3; 79 -2.6; 87 -3.6; 96 -4.1; 106 -4.5; 116 -4.6; 128 -4.9; 141 -5.1; 155 -5.3; 170 -5.3; 187 -5.5; 206 -5.7; 227 -5.7; 249 -5.6; 274 -5.5; 302 -5.4; 332 -5.2; 365 -5.4; 402 -5.6; 442 -5.7; 486 -5.9; 535 -5.9; 588 -5.6; 647 -5.7; 712 -6.0; 783 -5.7; 861 -5.6; 947 -6.2; 1042 -6.7; 1146 -7.3; 1261 -7.8; 1387 -7.8; 1526 -8.2; 1678 -8.9; 1846 -8.6; 2031 -8.8; 2234 -8.9; 2457 -8.1; 2703 -8.3; 2973 -7.9; 3270 -8.2; 3597 -8.7; 3957 -10.1; 4353 -12.4; 4788 -12.7; 5267 -10.8; 5793 -9.5; 6373 -7.0; 7010 -5.5; 7711 -6.4; 8482 -9.7; 9330 -10.6; 10263 -9.7; 11289 -7.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.4  | 6.2 dB  |
| Peaking | 784 Hz   | 0.51 | 1.2 dB  |
| Peaking | 1724 Hz  | 1.04 | -2.8 dB |
| Peaking | 4668 Hz  | 2.65 | -6.2 dB |
| Peaking | 17917 Hz | 2.04 | -0.8 dB |
| Peaking | 74 Hz    | 3.13 | 1.4 dB  |
| Peaking | 79 Hz    | 1.34 | -0.7 dB |
| Peaking | 7199 Hz  | 4.6  | 3.4 dB  |
| Peaking | 9266 Hz  | 2.73 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-1/Audeze%20LCD-1.png)