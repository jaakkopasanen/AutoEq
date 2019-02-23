# Audeze LCD-X sn7454971
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.6; 25 -2.6; 28 -2.9; 31 -3.7; 34 -4.4; 37 -4.6; 41 -4.3; 45 -4.4; 49 -4.6; 54 -5.0; 60 -5.4; 66 -5.4; 72 -5.6; 79 -5.8; 87 -6.1; 96 -6.5; 106 -6.6; 116 -6.8; 128 -7.2; 141 -7.3; 155 -7.5; 170 -7.7; 187 -7.9; 206 -8.0; 227 -7.9; 249 -7.9; 274 -7.8; 302 -7.7; 332 -7.5; 365 -7.4; 402 -7.4; 442 -6.8; 486 -7.3; 535 -7.4; 588 -6.9; 647 -6.7; 712 -6.6; 783 -6.4; 861 -6.5; 947 -6.6; 1042 -6.4; 1146 -6.4; 1261 -6.6; 1387 -7.2; 1526 -7.4; 1678 -7.8; 1846 -7.7; 2031 -7.8; 2234 -7.3; 2457 -5.7; 2703 -4.1; 2973 -2.6; 3270 -1.5; 3597 -2.3; 3957 -5.2; 4353 -1.8; 4788 -0.5; 5267 -0.7; 5793 -1.2; 6373 -3.3; 7010 -3.5; 7711 -5.4; 8482 -5.6; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.9; 16529 -6.8; 18182 -8.5; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X sn7454971 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X sn7454971 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.41 | 3.5 dB  |
| Peaking | 230 Hz   | 0.5  | -2.3 dB |
| Peaking | 1904 Hz  | 1.55 | -2.6 dB |
| Peaking | 3155 Hz  | 3.42 | 4.4 dB  |
| Peaking | 5227 Hz  | 2.63 | 5.5 dB  |
| Peaking | 347 Hz   | 5.16 | 0.2 dB  |
| Peaking | 3985 Hz  | 9.79 | -3.9 dB |
| Peaking | 4088 Hz  | 3.53 | 1.7 dB  |
| Peaking | 19610 Hz | 0.88 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X%20sn7454971/Audeze%20LCD-X%20sn7454971.png)