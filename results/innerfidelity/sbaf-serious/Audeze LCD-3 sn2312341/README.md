# Audeze LCD-3 sn2312341
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.3; 25 -4.8; 28 -5.6; 31 -5.9; 34 -5.8; 37 -5.7; 41 -5.8; 45 -6.1; 49 -6.4; 54 -6.6; 60 -6.7; 66 -6.8; 72 -6.9; 79 -7.2; 87 -7.5; 96 -8.0; 106 -8.1; 116 -8.4; 128 -8.7; 141 -9.0; 155 -9.2; 170 -9.3; 187 -9.3; 206 -9.3; 227 -9.1; 249 -9.1; 274 -9.1; 302 -8.9; 332 -8.8; 365 -8.5; 402 -8.6; 442 -8.9; 486 -9.2; 535 -9.3; 588 -9.2; 647 -9.4; 712 -8.8; 783 -7.8; 861 -7.3; 947 -6.6; 1042 -5.9; 1146 -5.6; 1261 -5.4; 1387 -5.7; 1526 -5.7; 1678 -5.3; 1846 -4.8; 2031 -4.8; 2234 -5.4; 2457 -5.4; 2703 -5.5; 2973 -5.4; 3270 -5.7; 3597 -3.1; 3957 -0.5; 4353 -0.7; 4788 -2.3; 5267 -3.9; 5793 -5.8; 6373 -4.6; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.7; 18182 -12.5; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312341 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312341 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.73 | 3.7 dB  |
| Peaking | 191 Hz   | 0.69 | -2.9 dB |
| Peaking | 573 Hz   | 2.3  | -2.5 dB |
| Peaking | 4228 Hz  | 2.31 | 6.1 dB  |
| Peaking | 18921 Hz | 1.22 | -7.1 dB |
| Peaking | 716 Hz   | 3.81 | -1.0 dB |
| Peaking | 1579 Hz  | 0.83 | 1.3 dB  |
| Peaking | 3225 Hz  | 6.49 | -2.1 dB |
| Peaking | 5426 Hz  | 3.12 | -0.7 dB |
| Peaking | 6776 Hz  | 8.7  | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312341/Audeze%20LCD-3%20sn2312341.png)