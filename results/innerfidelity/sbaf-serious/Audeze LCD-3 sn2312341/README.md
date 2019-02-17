# Audeze LCD-3 sn2312341
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.6; 25 -5.0; 28 -5.8; 31 -6.2; 34 -6.0; 37 -5.9; 41 -6.1; 45 -6.4; 49 -6.7; 54 -6.9; 60 -7.0; 66 -7.1; 72 -7.2; 79 -7.5; 87 -7.8; 96 -8.3; 106 -8.4; 116 -8.6; 128 -9.0; 141 -9.3; 155 -9.4; 170 -9.6; 187 -9.6; 206 -9.6; 227 -9.4; 249 -9.4; 274 -9.4; 302 -9.2; 332 -9.0; 365 -8.8; 402 -8.9; 442 -9.1; 486 -9.5; 535 -9.6; 588 -9.4; 647 -9.7; 712 -9.0; 783 -8.1; 861 -7.6; 947 -6.8; 1042 -6.1; 1146 -5.9; 1261 -5.7; 1387 -5.9; 1526 -6.0; 1678 -5.5; 1846 -5.1; 2031 -5.1; 2234 -5.7; 2457 -5.7; 2703 -5.8; 2973 -5.7; 3270 -6.0; 3597 -3.4; 3957 -0.5; 4353 -0.9; 4788 -2.6; 5267 -4.2; 5793 -6.1; 6373 -4.8; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.0; 18182 -12.8; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312341 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312341 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 1    | 3.2 dB  |
| Peaking | 194 Hz   | 0.66 | -3.1 dB |
| Peaking | 579 Hz   | 2.16 | -2.7 dB |
| Peaking | 4211 Hz  | 2.7  | 6.2 dB  |
| Peaking | 18916 Hz | 1.21 | -7.4 dB |
| Peaking | 723 Hz   | 3.92 | -0.9 dB |
| Peaking | 1555 Hz  | 0.93 | 1.1 dB  |
| Peaking | 3221 Hz  | 6.63 | -1.9 dB |
| Peaking | 6969 Hz  | 9.81 | 1.6 dB  |
| Peaking | 22050 Hz | 3.37 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312341/Audeze%20LCD-3%20sn2312341.png)