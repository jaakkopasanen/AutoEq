# Audeze LCD-3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.3; 25 -2.6; 28 -3.3; 31 -3.9; 34 -4.1; 37 -4.3; 41 -4.3; 45 -4.4; 49 -4.6; 54 -5.0; 60 -5.2; 66 -5.3; 72 -5.5; 79 -5.7; 87 -6.0; 96 -6.4; 106 -6.6; 116 -6.8; 128 -7.2; 141 -7.4; 155 -7.6; 170 -7.8; 187 -7.9; 206 -8.0; 227 -7.9; 249 -8.0; 274 -7.9; 302 -7.8; 332 -7.7; 365 -7.5; 402 -7.6; 442 -7.7; 486 -7.9; 535 -7.9; 588 -7.6; 647 -7.6; 712 -7.5; 783 -7.1; 861 -6.8; 947 -6.1; 1042 -5.4; 1146 -5.3; 1261 -5.0; 1387 -5.5; 1526 -5.9; 1678 -5.6; 1846 -4.8; 2031 -4.4; 2234 -4.7; 2457 -4.3; 2703 -4.3; 2973 -4.5; 3270 -4.1; 3597 -1.9; 3957 -0.5; 4353 -0.7; 4788 -1.4; 5267 -2.7; 5793 -4.8; 6373 -3.1; 7010 -3.3; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.8; 16529 -8.2; 18182 -11.1; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.34 | 4.1 dB  |
| Peaking | 266 Hz   | 0.45 | -2.4 dB |
| Peaking | 4275 Hz  | 1.59 | 5.1 dB  |
| Peaking | 15116 Hz | 1.43 | 2.4 dB  |
| Peaking | 18521 Hz | 0.71 | -6.0 dB |
| Peaking | 688 Hz   | 2.33 | -0.8 dB |
| Peaking | 1147 Hz  | 3.56 | 1.2 dB  |
| Peaking | 2152 Hz  | 2.84 | 0.7 dB  |
| Peaking | 3244 Hz  | 4.31 | -1.6 dB |
| Peaking | 3732 Hz  | 5.11 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3/Audeze%20LCD-3.png)