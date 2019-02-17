# Audeze LCD-4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -1.8; 25 -1.9; 28 -2.1; 31 -2.2; 34 -2.3; 37 -2.4; 41 -2.5; 45 -2.6; 49 -2.7; 54 -2.9; 60 -3.1; 66 -3.3; 72 -3.5; 79 -3.8; 87 -4.1; 96 -4.5; 106 -4.7; 116 -4.9; 128 -5.2; 141 -5.4; 155 -5.6; 170 -5.7; 187 -5.8; 206 -5.9; 227 -5.8; 249 -5.9; 274 -6.0; 302 -6.1; 332 -6.2; 365 -6.1; 402 -6.2; 442 -6.4; 486 -6.5; 535 -6.5; 588 -6.3; 647 -6.4; 712 -6.4; 783 -6.3; 861 -6.5; 947 -6.3; 1042 -6.4; 1146 -6.7; 1261 -6.7; 1387 -7.0; 1526 -7.7; 1678 -7.6; 1846 -7.1; 2031 -6.9; 2234 -6.6; 2457 -5.1; 2703 -4.5; 2973 -3.3; 3270 -1.5; 3597 -1.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.3; 6373 -2.6; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -10.1; 20000 -13.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.57 | 4.2 dB  |
| Peaking | 59 Hz   |  0.66 | 2.4 dB  |
| Peaking | 278 Hz  |  1.71 | 0.2 dB  |
| Peaking | 1773 Hz |  1.9  | -2.0 dB |
| Peaking | 4361 Hz |  1.24 | 6.8 dB  |
| Peaking | 2215 Hz | 10.68 | -0.7 dB |
| Peaking | 3265 Hz |  6.94 | 1.1 dB  |
| Peaking | 4428 Hz |  3.12 | -1.2 dB |
| Peaking | 6081 Hz |  1.69 | 3.5 dB  |
| Peaking | 7557 Hz |  1.27 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-4/Audeze%20LCD-4.png)