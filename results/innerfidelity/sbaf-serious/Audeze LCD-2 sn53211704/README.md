# Audeze LCD-2 sn53211704
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.3; 25 -3.3; 28 -3.3; 31 -3.2; 34 -3.1; 37 -3.1; 41 -3.5; 45 -3.7; 49 -3.6; 54 -3.7; 60 -4.3; 66 -4.7; 72 -5.0; 79 -5.1; 87 -5.3; 96 -5.8; 106 -6.1; 116 -6.3; 128 -6.6; 141 -6.7; 155 -7.0; 170 -7.2; 187 -7.3; 206 -7.5; 227 -7.7; 249 -7.8; 274 -7.7; 302 -7.8; 332 -7.8; 365 -7.5; 402 -7.2; 442 -6.8; 486 -6.6; 535 -6.7; 588 -6.9; 647 -7.3; 712 -7.9; 783 -8.0; 861 -8.1; 947 -6.8; 1042 -5.2; 1146 -5.0; 1261 -4.7; 1387 -5.8; 1526 -6.5; 1678 -6.1; 1846 -5.0; 2031 -4.5; 2234 -4.4; 2457 -3.8; 2703 -3.4; 2973 -3.3; 3270 -2.8; 3597 -1.7; 3957 -0.5; 4353 -1.1; 4788 -1.8; 5267 -2.9; 5793 -4.2; 6373 -1.5; 7010 -3.3; 7711 -5.5; 8482 -6.3; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -6.7; 18182 -10.4; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 sn53211704 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sn53211704 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.59 | 2.8 dB  |
| Peaking | 241 Hz   | 0.71 | -2.1 dB |
| Peaking | 781 Hz   | 3.85 | -2.3 dB |
| Peaking | 3975 Hz  | 1.55 | 5.0 dB  |
| Peaking | 6585 Hz  | 9.59 | 3.7 dB  |
| Peaking | 1215 Hz  | 2.8  | 3.1 dB  |
| Peaking | 1494 Hz  | 1.32 | -2.9 dB |
| Peaking | 2003 Hz  | 1.84 | 2.0 dB  |
| Peaking | 15760 Hz | 1.26 | 3.2 dB  |
| Peaking | 18887 Hz | 0.54 | -5.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sn53211704/Audeze%20LCD-2%20sn53211704.png)