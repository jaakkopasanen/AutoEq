# Audeze LCD-3 Rev 2 sn2613375
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.2; 25 -2.2; 28 -2.6; 31 -3.3; 34 -3.8; 37 -3.7; 41 -3.5; 45 -3.5; 49 -3.8; 54 -4.6; 60 -4.9; 66 -4.8; 72 -4.9; 79 -5.1; 87 -5.5; 96 -5.8; 106 -5.8; 116 -6.0; 128 -6.4; 141 -6.6; 155 -6.8; 170 -7.0; 187 -7.2; 206 -7.3; 227 -7.3; 249 -7.4; 274 -7.3; 302 -7.4; 332 -7.4; 365 -7.2; 402 -7.1; 442 -7.1; 486 -7.5; 535 -7.8; 588 -7.3; 647 -7.2; 712 -7.1; 783 -6.8; 861 -6.8; 947 -6.7; 1042 -6.1; 1146 -6.1; 1261 -6.6; 1387 -7.3; 1526 -7.8; 1678 -7.6; 1846 -6.9; 2031 -7.0; 2234 -6.7; 2457 -5.6; 2703 -4.7; 2973 -4.7; 3270 -3.7; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -1.3; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.8; 16529 -10.5; 18182 -12.2; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 Rev 2 sn2613375 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 Rev 2 sn2613375 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.38 | 4.1 dB  |
| Peaking | 47 Hz    | 1.35 | 2.0 dB  |
| Peaking | 4808 Hz  | 1.38 | 6.9 dB  |
| Peaking | 14660 Hz | 1.37 | 4.8 dB  |
| Peaking | 17259 Hz | 0.59 | -6.9 dB |
| Peaking | 351 Hz   | 0.73 | -1.0 dB |
| Peaking | 1680 Hz  | 2.55 | -1.6 dB |
| Peaking | 3715 Hz  | 5.82 | 2.6 dB  |
| Peaking | 6117 Hz  | 1.52 | -2.8 dB |
| Peaking | 6269 Hz  | 4.24 | 5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20Rev%202%20sn2613375/Audeze%20LCD-3%20Rev%202%20sn2613375.png)