# Audeze LCD-3 sn2312260
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.4; 25 -4.6; 28 -5.3; 31 -5.8; 34 -5.8; 37 -5.9; 41 -6.1; 45 -6.2; 49 -6.4; 54 -6.5; 60 -6.6; 66 -6.8; 72 -7.1; 79 -7.4; 87 -7.6; 96 -8.0; 106 -8.2; 116 -8.5; 128 -8.8; 141 -9.0; 155 -9.2; 170 -9.5; 187 -9.6; 206 -9.8; 227 -9.7; 249 -9.5; 274 -9.2; 302 -8.7; 332 -8.3; 365 -8.2; 402 -8.8; 442 -9.2; 486 -9.6; 535 -9.4; 588 -9.2; 647 -8.7; 712 -8.2; 783 -8.0; 861 -7.6; 947 -6.5; 1042 -5.5; 1146 -5.5; 1261 -5.6; 1387 -6.1; 1526 -5.9; 1678 -5.3; 1846 -4.5; 2031 -4.3; 2234 -4.4; 2457 -4.4; 2703 -4.5; 2973 -6.0; 3270 -4.5; 3597 -0.6; 3957 -0.5; 4353 -1.9; 4788 -3.3; 5267 -5.5; 5793 -7.7; 6373 -6.4; 7010 -5.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.5; 15026 -7.6; 16529 -10.5; 18182 -12.6; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312260 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312260 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 190 Hz   | 0.89 | -3.2 dB |
| Peaking | 545 Hz   | 1.8  | -2.7 dB |
| Peaking | 1989 Hz  | 1.53 | 2.0 dB  |
| Peaking | 3952 Hz  | 3.52 | 6.4 dB  |
| Peaking | 18143 Hz | 1.31 | -6.7 dB |
| Peaking | 21 Hz    | 1.3  | 2.1 dB  |
| Peaking | 1084 Hz  | 3.24 | 2.7 dB  |
| Peaking | 1096 Hz  | 1.48 | -1.5 dB |
| Peaking | 5779 Hz  | 5.66 | -3.9 dB |
| Peaking | 5788 Hz  | 2.12 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312260/Audeze%20LCD-3%20sn2312260.png)