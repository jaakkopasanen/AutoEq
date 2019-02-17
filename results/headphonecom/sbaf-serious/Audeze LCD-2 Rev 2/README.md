# Audeze LCD-2 Rev 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.5; 25 -3.5; 28 -3.4; 31 -3.4; 34 -3.3; 37 -3.4; 41 -3.5; 45 -3.5; 49 -3.4; 54 -3.4; 60 -4.5; 66 -4.8; 72 -4.9; 79 -5.1; 87 -5.1; 96 -5.5; 106 -5.8; 116 -6.0; 128 -6.2; 141 -6.4; 155 -6.8; 170 -6.9; 187 -7.3; 206 -7.3; 227 -7.3; 249 -7.0; 274 -7.1; 302 -7.0; 332 -6.5; 365 -6.1; 402 -6.2; 442 -6.3; 486 -6.4; 535 -6.4; 588 -6.4; 647 -6.4; 712 -6.3; 783 -6.3; 861 -6.0; 947 -4.8; 1042 -3.8; 1146 -2.6; 1261 -3.4; 1387 -4.6; 1526 -5.9; 1678 -6.5; 1846 -5.4; 2031 -4.1; 2234 -4.9; 2457 -4.4; 2703 -2.8; 2973 -3.4; 3270 -3.1; 3597 -1.3; 3957 -0.5; 4353 -0.7; 4788 -2.7; 5267 -3.9; 5793 -4.2; 6373 -3.7; 7010 -2.5; 7711 -3.7; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.5; 18182 -7.6; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Rev 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 214 Hz   | 0.7  | -3.3 dB |
| Peaking | 645 Hz   | 2.04 | -1.9 dB |
| Peaking | 1689 Hz  | 6.2  | -2.8 dB |
| Peaking | 4003 Hz  | 3.33 | 3.9 dB  |
| Peaking | 19021 Hz | 1.34 | -4.4 dB |
| Peaking | 36 Hz    | 1.43 | 1.0 dB  |
| Peaking | 830 Hz   | 6.9  | -1.0 dB |
| Peaking | 1140 Hz  | 6.12 | 2.1 dB  |
| Peaking | 5554 Hz  | 5.01 | -0.8 dB |
| Peaking | 7094 Hz  | 9.89 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)