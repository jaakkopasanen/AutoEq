# Audeze LCD-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.0; 54 -1.3; 60 -1.5; 66 -1.5; 72 -1.7; 79 -2.0; 87 -3.0; 96 -3.5; 106 -3.9; 116 -4.0; 128 -4.3; 141 -4.5; 155 -4.7; 170 -4.7; 187 -4.9; 206 -5.1; 227 -5.1; 249 -5.0; 274 -4.9; 302 -4.8; 332 -4.6; 365 -4.8; 402 -5.0; 442 -5.1; 486 -5.3; 535 -5.3; 588 -5.0; 647 -5.1; 712 -5.4; 783 -5.1; 861 -5.0; 947 -5.6; 1042 -6.1; 1146 -6.7; 1261 -7.2; 1387 -7.2; 1526 -7.6; 1678 -8.3; 1846 -8.0; 2031 -8.2; 2234 -8.3; 2457 -7.5; 2703 -7.7; 2973 -7.3; 3270 -7.6; 3597 -8.1; 3957 -9.5; 4353 -11.8; 4788 -12.1; 5267 -10.2; 5793 -8.9; 6373 -6.4; 7010 -5.0; 7711 -6.3; 8482 -9.1; 9330 -10.0; 10263 -9.1; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.37 | 6.2 dB  |
| Peaking | 1851 Hz  | 0.67 | -6.3 dB |
| Peaking | 2357 Hz  | 0.23 | 4.9 dB  |
| Peaking | 4680 Hz  | 2.31 | -8.1 dB |
| Peaking | 9512 Hz  | 2.61 | -5.4 dB |
| Peaking | 73 Hz    | 5.85 | 0.6 dB  |
| Peaking | 323 Hz   | 5.31 | 0.5 dB  |
| Peaking | 5997 Hz  | 7.56 | -1.8 dB |
| Peaking | 6778 Hz  | 5.05 | 2.2 dB  |
| Peaking | 13898 Hz | 0.41 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-1/Audeze%20LCD-1.png)