# Audeze LCD-X sn7454971
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.5; 25 -2.5; 28 -2.8; 31 -3.5; 34 -4.3; 37 -4.4; 41 -4.2; 45 -4.2; 49 -4.5; 54 -4.9; 60 -5.2; 66 -5.3; 72 -5.5; 79 -5.6; 87 -6.0; 96 -6.3; 106 -6.5; 116 -6.6; 128 -7.0; 141 -7.2; 155 -7.4; 170 -7.5; 187 -7.7; 206 -7.8; 227 -7.8; 249 -7.7; 274 -7.7; 302 -7.6; 332 -7.3; 365 -7.2; 402 -7.3; 442 -6.7; 486 -7.2; 535 -7.2; 588 -6.7; 647 -6.6; 712 -6.5; 783 -6.2; 861 -6.3; 947 -6.5; 1042 -6.2; 1146 -6.3; 1261 -6.4; 1387 -7.0; 1526 -7.3; 1678 -7.6; 1846 -7.5; 2031 -7.7; 2234 -7.2; 2457 -5.5; 2703 -3.9; 2973 -2.4; 3270 -1.3; 3597 -2.1; 3957 -5.1; 4353 -1.7; 4788 -0.5; 5267 -0.6; 5793 -1.1; 6373 -3.1; 7010 -4.0; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.7; 18182 -8.3; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X sn7454971 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X sn7454971 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.41 | 3.5 dB  |
| Peaking | 49 Hz   | 0.6  | 1.5 dB  |
| Peaking | 203 Hz  | 0.6  | -1.6 dB |
| Peaking | 3234 Hz | 4.54 | 4.7 dB  |
| Peaking | 5234 Hz | 2.52 | 6.4 dB  |
| Peaking | 1891 Hz | 1.64 | -4.0 dB |
| Peaking | 2021 Hz | 0.9  | 2.3 dB  |
| Peaking | 6692 Hz | 3.67 | 2.3 dB  |
| Peaking | 7190 Hz | 1.52 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X%20sn7454971/Audeze%20LCD-X%20sn7454971.png)