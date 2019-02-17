# Audeze LCD-XC sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -2.5; 66 -3.7; 72 -3.9; 79 -4.1; 87 -4.4; 96 -4.6; 106 -4.6; 116 -4.7; 128 -4.9; 141 -4.9; 155 -4.7; 170 -5.0; 187 -5.1; 206 -4.9; 227 -4.6; 249 -4.4; 274 -4.2; 302 -4.1; 332 -4.0; 365 -4.0; 402 -4.2; 442 -4.2; 486 -4.7; 535 -4.7; 588 -4.4; 647 -4.4; 712 -5.1; 783 -5.4; 861 -6.0; 947 -6.3; 1042 -6.8; 1146 -7.6; 1261 -8.3; 1387 -9.2; 1526 -10.2; 1678 -10.8; 1846 -10.6; 2031 -9.5; 2234 -8.0; 2457 -5.9; 2703 -4.7; 2973 -3.6; 3270 -2.7; 3597 -2.0; 3957 -3.8; 4353 -8.0; 4788 -9.9; 5267 -3.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.9; 16529 -7.1; 18182 -8.7; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.62 | 6.6 dB  |
| Peaking | 410 Hz  | 0.61 | 2.4 dB  |
| Peaking | 1678 Hz | 1.79 | -5.0 dB |
| Peaking | 3253 Hz | 3.3  | 5.0 dB  |
| Peaking | 6068 Hz | 5.25 | 6.9 dB  |
| Peaking | 71 Hz   | 4.62 | -0.6 dB |
| Peaking | 2569 Hz | 9.11 | 1.5 dB  |
| Peaking | 3836 Hz | 7.53 | 3.0 dB  |
| Peaking | 4797 Hz | 4.13 | -6.0 dB |
| Peaking | 5427 Hz | 8.36 | 5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC%20sample%202/Audeze%20LCD-XC%20sample%202.png)