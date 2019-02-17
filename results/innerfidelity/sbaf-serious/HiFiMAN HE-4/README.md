# HiFiMAN HE-4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.3; 31 -1.5; 34 -1.6; 37 -1.8; 41 -1.9; 45 -2.0; 49 -2.0; 54 -2.1; 60 -2.3; 66 -2.5; 72 -2.7; 79 -3.0; 87 -3.4; 96 -3.6; 106 -4.0; 116 -4.1; 128 -4.3; 141 -4.6; 155 -4.9; 170 -5.1; 187 -5.4; 206 -5.7; 227 -5.9; 249 -6.0; 274 -6.0; 302 -5.5; 332 -4.7; 365 -4.2; 402 -4.2; 442 -4.4; 486 -4.8; 535 -4.5; 588 -4.2; 647 -4.0; 712 -1.8; 783 -1.6; 861 -2.4; 947 -3.2; 1042 -3.6; 1146 -1.8; 1261 -2.5; 1387 -2.4; 1526 -2.2; 1678 -1.6; 1846 -1.0; 2031 -1.3; 2234 -2.1; 2457 -1.7; 2703 -2.8; 2973 -3.8; 3270 -5.1; 3597 -5.8; 3957 -7.0; 4353 -8.7; 4788 -8.6; 5267 -1.0; 5793 -3.5; 6373 -9.4; 7010 -9.3; 7711 -9.1; 8482 -11.5; 9330 -12.5; 10263 -8.5; 11289 -6.0; 12418 -8.1; 13660 -9.7; 15026 -8.0; 16529 -7.1; 18182 -10.5; 20000 -16.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.76 | 3.2 dB   |
| Peaking | 1829 Hz  | 1.09 | 2.8 dB   |
| Peaking | 4255 Hz  | 4.82 | -5.0 dB  |
| Peaking | 8744 Hz  | 1.97 | -7.8 dB  |
| Peaking | 20397 Hz | 0.45 | -12.1 dB |
| Peaking | 237 Hz   | 1.37 | -2.1 dB  |
| Peaking | 758 Hz   | 6.74 | 2.5 dB   |
| Peaking | 5498 Hz  | 9.54 | 6.7 dB   |
| Peaking | 6421 Hz  | 6.64 | -3.5 dB  |
| Peaking | 13620 Hz | 5.25 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | -6.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-4/HiFiMAN%20HE-4.png)