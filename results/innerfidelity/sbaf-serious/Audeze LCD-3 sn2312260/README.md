# Audeze LCD-3 sn2312260
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -4.9; 25 -5.2; 28 -5.9; 31 -6.3; 34 -6.4; 37 -6.4; 41 -6.6; 45 -6.7; 49 -6.9; 54 -7.0; 60 -7.1; 66 -7.3; 72 -7.7; 79 -7.9; 87 -8.2; 96 -8.6; 106 -8.8; 116 -9.0; 128 -9.3; 141 -9.5; 155 -9.7; 170 -10.0; 187 -10.2; 206 -10.3; 227 -10.2; 249 -10.1; 274 -9.7; 302 -9.3; 332 -8.9; 365 -8.7; 402 -9.3; 442 -9.8; 486 -10.1; 535 -10.0; 588 -9.8; 647 -9.3; 712 -8.7; 783 -8.6; 861 -8.2; 947 -7.1; 1042 -6.0; 1146 -6.0; 1261 -6.2; 1387 -6.6; 1526 -6.4; 1678 -5.8; 1846 -5.1; 2031 -4.9; 2234 -4.9; 2457 -5.0; 2703 -5.0; 2973 -6.5; 3270 -5.1; 3597 -0.7; 3957 -0.5; 4353 -2.4; 4788 -3.9; 5267 -6.0; 5793 -8.3; 6373 -6.9; 7010 -5.6; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.6; 13660 -8.0; 15026 -8.1; 16529 -11.1; 18182 -13.1; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312260 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312260 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 191 Hz   | 0.67 | -3.8 dB |
| Peaking | 346 Hz   | 2.84 | 0.5 dB  |
| Peaking | 545 Hz   | 1.76 | -2.9 dB |
| Peaking | 3886 Hz  | 3.67 | 6.6 dB  |
| Peaking | 18133 Hz | 1.14 | -7.3 dB |
| Peaking | 22 Hz    | 2    | 1.5 dB  |
| Peaking | 1091 Hz  | 7.61 | 1.1 dB  |
| Peaking | 1938 Hz  | 5.09 | 1.3 dB  |
| Peaking | 2595 Hz  | 2.5  | 1.2 dB  |
| Peaking | 3061 Hz  | 7.73 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312260/Audeze%20LCD-3%20sn2312260.png)