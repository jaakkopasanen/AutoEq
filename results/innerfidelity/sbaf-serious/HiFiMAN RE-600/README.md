# HiFiMAN RE-600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.5; 25 -4.6; 28 -4.7; 31 -4.8; 34 -4.9; 37 -5.0; 41 -5.1; 45 -5.2; 49 -5.4; 54 -5.7; 60 -6.0; 66 -6.3; 72 -6.6; 79 -7.0; 87 -7.4; 96 -7.8; 106 -8.1; 116 -8.2; 128 -8.5; 141 -8.8; 155 -8.9; 170 -9.0; 187 -9.1; 206 -9.1; 227 -9.0; 249 -8.9; 274 -8.8; 302 -8.6; 332 -8.4; 365 -8.2; 402 -8.0; 442 -7.6; 486 -7.6; 535 -7.4; 588 -7.1; 647 -7.0; 712 -7.1; 783 -7.1; 861 -7.6; 947 -8.1; 1042 -8.9; 1146 -9.7; 1261 -10.6; 1387 -11.9; 1526 -13.3; 1678 -14.5; 1846 -14.1; 2031 -13.3; 2234 -11.6; 2457 -7.8; 2703 -4.3; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -2.3; 5267 -3.0; 5793 -3.5; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.53 | 2.1 dB  |
| Peaking | 177 Hz  | 0.68 | -2.8 dB |
| Peaking | 1837 Hz | 1.44 | -9.8 dB |
| Peaking | 3003 Hz | 3.34 | 4.9 dB  |
| Peaking | 4034 Hz | 1.18 | 6.4 dB  |
| Peaking | 747 Hz  | 2.72 | 0.8 dB  |
| Peaking | 1367 Hz | 4.12 | -0.4 dB |
| Peaking | 5710 Hz | 2.85 | -0.6 dB |
| Peaking | 6534 Hz | 5.41 | 4.0 dB  |
| Peaking | 7697 Hz | 1.82 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -8.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-600/HiFiMAN%20RE-600.png)