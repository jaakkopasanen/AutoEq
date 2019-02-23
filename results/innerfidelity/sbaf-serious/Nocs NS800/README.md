# Nocs NS800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.5; 25 -6.5; 28 -6.7; 31 -6.8; 34 -6.8; 37 -6.9; 41 -7.0; 45 -7.1; 49 -7.2; 54 -7.4; 60 -7.7; 66 -7.9; 72 -8.2; 79 -8.5; 87 -8.9; 96 -9.1; 106 -9.5; 116 -9.5; 128 -9.8; 141 -10.0; 155 -10.0; 170 -10.1; 187 -10.1; 206 -10.1; 227 -10.0; 249 -9.9; 274 -9.7; 302 -9.5; 332 -9.3; 365 -9.1; 402 -8.8; 442 -8.4; 486 -8.2; 535 -8.0; 588 -7.3; 647 -7.1; 712 -6.9; 783 -6.6; 861 -6.7; 947 -6.9; 1042 -7.1; 1146 -7.3; 1261 -7.5; 1387 -7.9; 1526 -8.2; 1678 -8.3; 1846 -8.0; 2031 -7.7; 2234 -7.6; 2457 -7.4; 2703 -7.7; 2973 -7.0; 3270 -4.3; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 141 Hz  | 0.69 | -3.1 dB |
| Peaking | 305 Hz  | 1.05 | -1.8 dB |
| Peaking | 1774 Hz | 1.62 | -2.4 dB |
| Peaking | 2815 Hz | 4.11 | -3.5 dB |
| Peaking | 4479 Hz | 1.27 | 7.3 dB  |
| Peaking | 790 Hz  | 4.71 | 0.6 dB  |
| Peaking | 3635 Hz | 6.84 | 2.1 dB  |
| Peaking | 4433 Hz | 2.12 | -1.0 dB |
| Peaking | 6307 Hz | 2.95 | 4.5 dB  |
| Peaking | 7444 Hz | 1.26 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS800/Nocs%20NS800.png)