# Audeze LCD-3 Rev 2 sn2613375
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.1; 25 -3.2; 28 -3.5; 31 -4.3; 34 -4.7; 37 -4.7; 41 -4.4; 45 -4.5; 49 -4.7; 54 -5.6; 60 -5.9; 66 -5.8; 72 -5.9; 79 -6.1; 87 -6.4; 96 -6.8; 106 -6.8; 116 -7.0; 128 -7.3; 141 -7.6; 155 -7.7; 170 -7.9; 187 -8.1; 206 -8.2; 227 -8.2; 249 -8.3; 274 -8.3; 302 -8.4; 332 -8.3; 365 -8.2; 402 -8.1; 442 -8.0; 486 -8.4; 535 -8.7; 588 -8.3; 647 -8.2; 712 -8.0; 783 -7.7; 861 -7.8; 947 -7.6; 1042 -7.1; 1146 -7.1; 1261 -7.6; 1387 -8.3; 1526 -8.8; 1678 -8.6; 1846 -7.8; 2031 -8.0; 2234 -7.6; 2457 -6.6; 2703 -5.6; 2973 -5.7; 3270 -4.6; 3597 -1.4; 3957 -0.8; 4353 -0.5; 4788 -1.7; 5267 -2.3; 5793 -1.4; 6373 -0.7; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -7.4; 16529 -11.4; 18182 -13.2; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 Rev 2 sn2613375 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 Rev 2 sn2613375 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.21 | 3.4 dB  |
| Peaking | 551 Hz   | 0.06 | -2.3 dB |
| Peaking | 4714 Hz  | 1.13 | 7.6 dB  |
| Peaking | 14338 Hz | 1.51 | 3.8 dB  |
| Peaking | 17686 Hz | 0.66 | -7.7 dB |
| Peaking | 1157 Hz  | 1.81 | 2.6 dB  |
| Peaking | 1436 Hz  | 1.35 | -2.2 dB |
| Peaking | 3781 Hz  | 6.54 | 2.8 dB  |
| Peaking | 5818 Hz  | 1.68 | -2.5 dB |
| Peaking | 6277 Hz  | 4.91 | 5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -4.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20Rev%202%20sn2613375/Audeze%20LCD-3%20Rev%202%20sn2613375.png)