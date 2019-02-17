# Audeze LCD-2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -2.9; 25 -3.0; 28 -3.0; 31 -3.0; 34 -3.0; 37 -3.0; 41 -3.2; 45 -3.4; 49 -3.6; 54 -3.8; 60 -4.1; 66 -4.5; 72 -4.8; 79 -5.0; 87 -5.3; 96 -5.6; 106 -5.8; 116 -6.1; 128 -6.4; 141 -6.6; 155 -6.8; 170 -6.9; 187 -7.0; 206 -7.2; 227 -7.3; 249 -7.4; 274 -7.4; 302 -7.4; 332 -7.4; 365 -7.4; 402 -7.3; 442 -7.1; 486 -7.2; 535 -7.0; 588 -7.0; 647 -7.3; 712 -7.6; 783 -7.5; 861 -7.7; 947 -7.1; 1042 -6.1; 1146 -5.3; 1261 -5.1; 1387 -5.5; 1526 -6.1; 1678 -5.5; 1846 -4.4; 2031 -4.1; 2234 -4.5; 2457 -3.9; 2703 -3.7; 2973 -3.1; 3270 -2.5; 3597 -1.2; 3957 -0.5; 4353 -0.8; 4788 -2.1; 5267 -2.4; 5793 -2.0; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.9; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.99 | 3.5 dB  |
| Peaking | 51 Hz   | 1.45 | 2.1 dB  |
| Peaking | 2139 Hz | 1.98 | 1.6 dB  |
| Peaking | 3988 Hz | 1.91 | 5.9 dB  |
| Peaking | 6200 Hz | 4.38 | 4.0 dB  |
| Peaking | 92 Hz   | 1.59 | 0.7 dB  |
| Peaking | 393 Hz  | 0.33 | -1.0 dB |
| Peaking | 1211 Hz | 4.78 | 1.7 dB  |
| Peaking | 8252 Hz | 4.25 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2/Audeze%20LCD-2.png)