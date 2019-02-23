# Sennheiser HD 424
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.6; 96 -2.0; 106 -3.4; 116 -4.5; 128 -5.9; 141 -7.0; 155 -7.9; 170 -8.3; 187 -8.3; 206 -8.3; 227 -8.0; 249 -7.7; 274 -7.3; 302 -6.9; 332 -6.5; 365 -6.2; 402 -5.9; 442 -5.5; 486 -5.5; 535 -5.4; 588 -5.3; 647 -5.3; 712 -5.5; 783 -5.5; 861 -5.9; 947 -6.3; 1042 -6.8; 1146 -7.2; 1261 -7.9; 1387 -9.2; 1526 -10.4; 1678 -11.4; 1846 -12.0; 2031 -11.6; 2234 -10.5; 2457 -8.9; 2703 -7.8; 2973 -7.1; 3270 -7.1; 3597 -7.5; 3957 -7.4; 4353 -6.8; 4788 -4.5; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 424 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 424 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 58 Hz    | 0.27 | 7.4 dB  |
| Peaking | 174 Hz   | 0.97 | -6.9 dB |
| Peaking | 693 Hz   | 1.02 | 1.4 dB  |
| Peaking | 1841 Hz  | 1.68 | -5.9 dB |
| Peaking | 5810 Hz  | 3.5  | 7.2 dB  |
| Peaking | 17 Hz    | 1.18 | 1.7 dB  |
| Peaking | 42 Hz    | 0.53 | -0.9 dB |
| Peaking | 84 Hz    | 3.6  | 1.6 dB  |
| Peaking | 4096 Hz  | 6.42 | -1.3 dB |
| Peaking | 20743 Hz | 1.85 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20424/Sennheiser%20HD%20424.png)