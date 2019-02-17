# Audeze LCD-2 Fazor sn5423021
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.8; 41 -1.2; 45 -1.6; 49 -1.6; 54 -1.9; 60 -2.8; 66 -3.4; 72 -3.6; 79 -3.6; 87 -3.8; 96 -4.1; 106 -4.4; 116 -4.5; 128 -4.8; 141 -5.0; 155 -5.2; 170 -5.4; 187 -5.6; 206 -5.7; 227 -5.6; 249 -5.7; 274 -5.8; 302 -5.8; 332 -5.9; 365 -6.0; 402 -6.0; 442 -5.9; 486 -6.1; 535 -6.0; 588 -5.5; 647 -5.4; 712 -5.5; 783 -5.7; 861 -6.2; 947 -6.4; 1042 -6.3; 1146 -6.4; 1261 -6.3; 1387 -7.3; 1526 -8.1; 1678 -8.2; 1846 -7.3; 2031 -6.3; 2234 -5.7; 2457 -4.7; 2703 -3.7; 2973 -2.7; 3270 -1.9; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Fazor sn5423021 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Fazor sn5423021 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.29 | 6.2 dB  |
| Peaking | 656 Hz  | 2.25 | 0.9 dB  |
| Peaking | 1654 Hz | 2.86 | -2.8 dB |
| Peaking | 4396 Hz | 1.14 | 6.9 dB  |
| Peaking | 71 Hz   | 5.27 | -0.6 dB |
| Peaking | 3541 Hz | 3.05 | 1.0 dB  |
| Peaking | 4300 Hz | 3.38 | -1.2 dB |
| Peaking | 6318 Hz | 2.94 | 4.6 dB  |
| Peaking | 7359 Hz | 1.57 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Fazor%20sn5423021/Audeze%20LCD-2%20Fazor%20sn5423021.png)