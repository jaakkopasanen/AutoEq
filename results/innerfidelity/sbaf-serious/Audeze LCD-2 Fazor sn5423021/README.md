# Audeze LCD-2 Fazor sn5423021
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.2; 25 -2.3; 28 -2.4; 31 -2.5; 34 -2.6; 37 -2.8; 41 -3.3; 45 -3.6; 49 -3.7; 54 -4.0; 60 -4.8; 66 -5.4; 72 -5.6; 79 -5.7; 87 -5.9; 96 -6.1; 106 -6.5; 116 -6.6; 128 -6.8; 141 -7.1; 155 -7.3; 170 -7.4; 187 -7.6; 206 -7.7; 227 -7.7; 249 -7.8; 274 -7.9; 302 -7.9; 332 -7.9; 365 -8.1; 402 -8.1; 442 -8.0; 486 -8.2; 535 -8.1; 588 -7.6; 647 -7.5; 712 -7.6; 783 -7.7; 861 -8.3; 947 -8.5; 1042 -8.4; 1146 -8.5; 1261 -8.4; 1387 -9.3; 1526 -10.2; 1678 -10.3; 1846 -9.3; 2031 -8.3; 2234 -7.7; 2457 -6.7; 2703 -5.8; 2973 -4.7; 3270 -3.9; 3597 -2.4; 3957 -0.6; 4353 -0.5; 4788 -0.8; 5267 -1.0; 5793 -1.9; 6373 -2.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -6.7; 16529 -6.5; 18182 -6.7; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Fazor sn5423021 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Fazor sn5423021 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.48 | 4.2 dB  |
| Peaking | 43 Hz    | 1.32 | 0.8 dB  |
| Peaking | 341 Hz   | 0.37 | -1.5 dB |
| Peaking | 1663 Hz  | 1.6  | -3.8 dB |
| Peaking | 4511 Hz  | 1.45 | 6.8 dB  |
| Peaking | 671 Hz   | 4.61 | 0.5 dB  |
| Peaking | 926 Hz   | 6.3  | -0.6 dB |
| Peaking | 6604 Hz  | 3.54 | 2.6 dB  |
| Peaking | 7809 Hz  | 1.76 | -2.1 dB |
| Peaking | 20001 Hz | 1.69 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Fazor%20sn5423021/Audeze%20LCD-2%20Fazor%20sn5423021.png)