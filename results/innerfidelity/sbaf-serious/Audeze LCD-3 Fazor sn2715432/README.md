# Audeze LCD-3 Fazor sn2715432
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.5; 31 -1.9; 34 -2.2; 37 -2.6; 41 -2.9; 45 -3.5; 49 -4.1; 54 -4.7; 60 -5.4; 66 -5.7; 72 -5.9; 79 -6.1; 87 -6.4; 96 -6.8; 106 -6.9; 116 -7.2; 128 -7.4; 141 -7.7; 155 -7.8; 170 -8.0; 187 -8.1; 206 -8.2; 227 -8.2; 249 -8.3; 274 -8.3; 302 -8.3; 332 -8.4; 365 -8.4; 402 -8.5; 442 -8.3; 486 -8.4; 535 -8.3; 588 -7.9; 647 -8.1; 712 -7.9; 783 -7.8; 861 -8.2; 947 -8.1; 1042 -7.8; 1146 -7.8; 1261 -7.9; 1387 -9.0; 1526 -9.6; 1678 -9.7; 1846 -8.8; 2031 -8.6; 2234 -7.7; 2457 -6.3; 2703 -5.6; 2973 -4.8; 3270 -4.0; 3597 -3.2; 3957 -2.0; 4353 -2.4; 4788 -4.2; 5267 -5.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.9; 20000 -11.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 Fazor sn2715432 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 Fazor sn2715432 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.53 | 5.9 dB  |
| Peaking | 286 Hz   | 0.31 | -2.0 dB |
| Peaking | 1666 Hz  | 2.22 | -3.0 dB |
| Peaking | 3817 Hz  | 2.38 | 4.4 dB  |
| Peaking | 6165 Hz  | 4.93 | 6.1 dB  |
| Peaking | 8136 Hz  | 5.3  | -0.7 dB |
| Peaking | 17873 Hz | 1.42 | 1.1 dB  |
| Peaking | 20080 Hz | 1.08 | -5.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20Fazor%20sn2715432/Audeze%20LCD-3%20Fazor%20sn2715432.png)