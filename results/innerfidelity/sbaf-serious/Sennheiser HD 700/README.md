# Sennheiser HD 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.7; 31 -2.3; 34 -2.8; 37 -3.3; 41 -3.8; 45 -4.2; 49 -4.6; 54 -5.1; 60 -5.5; 66 -5.9; 72 -6.2; 79 -6.5; 87 -6.9; 96 -7.5; 106 -8.0; 116 -8.3; 128 -8.6; 141 -9.0; 155 -9.2; 170 -9.2; 187 -9.5; 206 -9.4; 227 -9.3; 249 -9.3; 274 -9.2; 302 -8.9; 332 -8.8; 365 -8.5; 402 -8.3; 442 -7.8; 486 -7.7; 535 -7.4; 588 -6.9; 647 -6.7; 712 -6.6; 783 -6.0; 861 -5.8; 947 -5.3; 1042 -4.7; 1146 -4.4; 1261 -3.6; 1387 -3.1; 1526 -2.2; 1678 -1.9; 1846 -1.0; 2031 -0.6; 2234 -1.0; 2457 -1.6; 2703 -2.3; 2973 -2.6; 3270 -2.3; 3597 -1.5; 3957 -2.9; 4353 -6.3; 4788 -8.9; 5267 -10.2; 5793 -11.4; 6373 -14.6; 7010 -9.8; 7711 -6.4; 8482 -6.7; 9330 -7.6; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.2; 20000 -14.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.43 | 6.8 dB  |
| Peaking | 202 Hz   | 0.53 | -3.2 dB |
| Peaking | 2008 Hz  | 1    | 5.9 dB  |
| Peaking | 3656 Hz  | 5.55 | 4.0 dB  |
| Peaking | 6083 Hz  | 2.92 | -8.0 dB |
| Peaking | 1702 Hz  | 6.01 | -0.4 dB |
| Peaking | 2497 Hz  | 0.58 | 0.2 dB  |
| Peaking | 4862 Hz  | 9.25 | -1.9 dB |
| Peaking | 7767 Hz  | 7.97 | 2.1 dB  |
| Peaking | 19835 Hz | 1.44 | -7.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)