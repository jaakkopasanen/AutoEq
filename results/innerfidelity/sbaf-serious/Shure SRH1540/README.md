# Shure SRH1540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.8; 25 -6.3; 28 -7.0; 31 -7.6; 34 -8.0; 37 -8.4; 41 -8.8; 45 -9.1; 49 -9.2; 54 -9.4; 60 -9.5; 66 -9.4; 72 -9.2; 79 -8.8; 87 -8.5; 96 -8.2; 106 -8.2; 116 -8.2; 128 -8.1; 141 -7.6; 155 -6.5; 170 -5.3; 187 -5.6; 206 -5.1; 227 -4.7; 249 -4.7; 274 -4.6; 302 -4.9; 332 -5.1; 365 -4.8; 402 -4.5; 442 -3.9; 486 -3.5; 535 -3.0; 588 -2.2; 647 -1.8; 712 -1.4; 783 -1.0; 861 -0.9; 947 -0.9; 1042 -1.1; 1146 -1.0; 1261 -0.9; 1387 -1.4; 1526 -2.2; 1678 -3.2; 1846 -4.2; 2031 -4.4; 2234 -4.1; 2457 -3.8; 2703 -3.1; 2973 -2.3; 3270 -2.5; 3597 -2.3; 3957 -2.0; 4353 -1.9; 4788 -1.5; 5267 -0.5; 5793 -3.2; 6373 -4.9; 7010 -2.7; 7711 -1.5; 8482 -3.5; 9330 -4.9; 10263 -1.7; 11289 -1.0; 12418 -1.0; 13660 -1.0; 15026 -1.0; 16529 -1.0; 18182 -1.0; 20000 -1.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.53 | -7.8 dB |
| Peaking | 130 Hz   | 1.05 | -3.2 dB |
| Peaking | 353 Hz   | 1.69 | -3.0 dB |
| Peaking | 2232 Hz  | 1.6  | -3.3 dB |
| Peaking | 505 Hz   | 3.53 | -0.8 dB |
| Peaking | 1428 Hz  | 0.64 | 1.2 dB  |
| Peaking | 1813 Hz  | 3.04 | -1.8 dB |
| Peaking | 7882 Hz  | 1.2  | -2.3 dB |
| Peaking | 22050 Hz | 2.17 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB |
| Peaking | 62 Hz    | 1.41 | -7.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1540/Shure%20SRH1540.png)