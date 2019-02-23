# Sennheiser HD 414
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.8; 72 -1.8; 79 -2.9; 87 -3.7; 96 -4.7; 106 -5.5; 116 -6.0; 128 -6.7; 141 -7.3; 155 -7.7; 170 -8.0; 187 -8.1; 206 -8.2; 227 -8.2; 249 -8.1; 274 -7.9; 302 -7.8; 332 -7.8; 365 -7.7; 402 -7.5; 442 -7.2; 486 -7.3; 535 -7.2; 588 -6.8; 647 -6.8; 712 -6.8; 783 -6.7; 861 -6.9; 947 -7.0; 1042 -7.1; 1146 -7.2; 1261 -7.5; 1387 -8.2; 1526 -9.0; 1678 -9.5; 1846 -9.4; 2031 -8.7; 2234 -9.1; 2457 -11.2; 2703 -13.4; 2973 -11.3; 3270 -8.7; 3597 -7.6; 3957 -6.1; 4353 -4.5; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 414 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 414 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.32 | 7.7 dB  |
| Peaking | 151 Hz  | 0.6  | -5.4 dB |
| Peaking | 1648 Hz | 2.85 | -2.6 dB |
| Peaking | 2748 Hz | 3.23 | -7.0 dB |
| Peaking | 5522 Hz | 2.45 | 7.2 dB  |
| Peaking | 57 Hz   | 1.1  | -0.9 dB |
| Peaking | 64 Hz   | 3.08 | 1.7 dB  |
| Peaking | 6541 Hz | 6.97 | 2.4 dB  |
| Peaking | 7648 Hz | 2.16 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20414/Sennheiser%20HD%20414.png)