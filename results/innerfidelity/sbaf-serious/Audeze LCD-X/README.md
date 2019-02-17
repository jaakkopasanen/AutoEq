# Audeze LCD-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.2; 25 -2.3; 28 -2.7; 31 -3.2; 34 -3.9; 37 -4.6; 41 -5.0; 45 -5.1; 49 -5.2; 54 -5.3; 60 -5.4; 66 -5.4; 72 -5.6; 79 -5.8; 87 -6.1; 96 -6.4; 106 -6.6; 116 -6.8; 128 -7.1; 141 -7.4; 155 -7.5; 170 -7.7; 187 -7.9; 206 -8.0; 227 -7.9; 249 -8.0; 274 -7.9; 302 -7.8; 332 -7.6; 365 -7.3; 402 -7.2; 442 -6.9; 486 -7.4; 535 -7.3; 588 -6.8; 647 -6.9; 712 -6.9; 783 -6.6; 861 -6.4; 947 -6.2; 1042 -6.1; 1146 -6.0; 1261 -6.2; 1387 -6.8; 1526 -7.0; 1678 -7.0; 1846 -7.0; 2031 -7.1; 2234 -6.8; 2457 -5.5; 2703 -3.8; 2973 -2.1; 3270 -1.0; 3597 -0.9; 3957 -2.7; 4353 -3.0; 4788 -3.6; 5267 -0.5; 5793 -0.5; 6373 -2.7; 7010 -3.8; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.3; 16529 -7.8; 18182 -9.5; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.75 | 4.2 dB  |
| Peaking | 218 Hz   | 0.82 | -1.8 dB |
| Peaking | 3341 Hz  | 2.79 | 6.3 dB  |
| Peaking | 5689 Hz  | 2.43 | 6.5 dB  |
| Peaking | 20685 Hz | 0.03 | -1.3 dB |
| Peaking | 72 Hz    | 3.75 | 0.4 dB  |
| Peaking | 520 Hz   | 3.91 | -0.7 dB |
| Peaking | 2016 Hz  | 2.15 | -1.5 dB |
| Peaking | 11781 Hz | 2.68 | 1.0 dB  |
| Peaking | 14368 Hz | 4.21 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X/Audeze%20LCD-X.png)