# Audeze LCD-2 Rev 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.5; 25 -3.5; 28 -3.4; 31 -3.4; 34 -3.3; 37 -3.4; 41 -3.5; 45 -3.5; 49 -3.4; 54 -3.4; 60 -4.5; 66 -4.8; 72 -4.9; 79 -5.1; 87 -5.1; 96 -5.5; 106 -5.8; 116 -6.0; 128 -6.2; 141 -6.4; 155 -6.8; 170 -6.9; 187 -7.3; 206 -7.3; 227 -7.3; 249 -7.0; 274 -7.1; 302 -7.0; 332 -6.5; 365 -6.1; 402 -6.2; 442 -6.3; 486 -6.4; 535 -6.4; 588 -6.4; 647 -6.4; 712 -6.3; 783 -6.3; 861 -6.0; 947 -4.8; 1042 -3.8; 1146 -2.6; 1261 -3.4; 1387 -4.6; 1526 -5.9; 1678 -6.5; 1846 -5.4; 2031 -4.1; 2234 -4.9; 2457 -4.4; 2703 -2.8; 2973 -3.4; 3270 -3.1; 3597 -1.3; 3957 -0.5; 4353 -0.7; 4788 -2.7; 5267 -3.9; 5793 -4.2; 6373 -3.7; 7010 -2.8; 7711 -4.3; 8482 -4.6; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.8; 18182 -7.6; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Rev 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 210 Hz   |  0.93 | -2.6 dB |
| Peaking | 1060 Hz  |  0.79 | -3.2 dB |
| Peaking | 1132 Hz  |  2.61 | 5.1 dB  |
| Peaking | 3932 Hz  |  2.03 | 4.4 dB  |
| Peaking | 19069 Hz |  1.39 | -3.7 dB |
| Peaking | 34 Hz    |  1.12 | 1.6 dB  |
| Peaking | 1695 Hz  |  5.46 | -2.3 dB |
| Peaking | 1907 Hz  |  2.37 | 1.4 dB  |
| Peaking | 3223 Hz  | 11.46 | -0.9 dB |
| Peaking | 15844 Hz |  3.49 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)