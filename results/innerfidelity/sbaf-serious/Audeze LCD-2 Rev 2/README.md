# Audeze LCD-2 Rev 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -3.8; 25 -3.8; 28 -3.8; 31 -3.7; 34 -3.8; 37 -3.9; 41 -3.9; 45 -3.9; 49 -3.8; 54 -4.3; 60 -5.1; 66 -5.3; 72 -5.3; 79 -5.6; 87 -5.9; 96 -6.3; 106 -6.5; 116 -6.7; 128 -7.0; 141 -7.4; 155 -7.6; 170 -7.8; 187 -7.9; 206 -8.1; 227 -8.0; 249 -7.8; 274 -7.7; 302 -7.8; 332 -7.8; 365 -7.8; 402 -7.7; 442 -7.6; 486 -7.8; 535 -7.7; 588 -7.4; 647 -7.9; 712 -8.2; 783 -7.8; 861 -7.6; 947 -6.8; 1042 -5.8; 1146 -4.6; 1261 -4.8; 1387 -5.5; 1526 -6.7; 1678 -6.8; 1846 -5.7; 2031 -5.4; 2234 -5.2; 2457 -4.6; 2703 -4.4; 2973 -3.2; 3270 -3.7; 3597 -1.9; 3957 -0.5; 4353 -1.6; 4788 -3.8; 5267 -5.1; 5793 -4.1; 6373 -5.0; 7010 -4.0; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -6.1; 18182 -10.3; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Rev 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.49 | 3.0 dB  |
| Peaking | 250 Hz   | 0.2  | -2.4 dB |
| Peaking | 1193 Hz  | 4.52 | 2.7 dB  |
| Peaking | 3867 Hz  | 2.19 | 5.1 dB  |
| Peaking | 6951 Hz  | 4.6  | 0.7 dB  |
| Peaking | 1642 Hz  | 5.66 | -1.3 dB |
| Peaking | 1940 Hz  | 2.22 | 0.7 dB  |
| Peaking | 3163 Hz  | 3.31 | 1.1 dB  |
| Peaking | 3346 Hz  | 7.98 | -2.2 dB |
| Peaking | 19287 Hz | 1.25 | -6.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)