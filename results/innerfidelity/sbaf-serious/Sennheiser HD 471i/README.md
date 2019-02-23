# Sennheiser HD 471i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -8.0; 25 -8.3; 28 -8.6; 31 -8.8; 34 -8.9; 37 -9.0; 41 -9.0; 45 -8.9; 49 -8.9; 54 -8.7; 60 -8.5; 66 -8.3; 72 -8.1; 79 -7.9; 87 -7.6; 96 -7.6; 106 -6.8; 116 -6.0; 128 -7.3; 141 -10.1; 155 -10.1; 170 -9.7; 187 -11.1; 206 -10.9; 227 -11.0; 249 -11.0; 274 -10.6; 302 -10.2; 332 -9.7; 365 -8.9; 402 -8.8; 442 -8.9; 486 -8.9; 535 -9.0; 588 -8.9; 647 -9.0; 712 -9.2; 783 -8.8; 861 -8.6; 947 -8.6; 1042 -8.3; 1146 -8.6; 1261 -8.7; 1387 -9.1; 1526 -9.6; 1678 -9.5; 1846 -9.0; 2031 -7.7; 2234 -5.7; 2457 -5.4; 2703 -4.3; 2973 -3.6; 3270 -3.2; 3597 -3.2; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 471i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 471i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 1.03 | -2.7 dB |
| Peaking | 222 Hz  | 1.28 | -4.5 dB |
| Peaking | 696 Hz  | 0.81 | -2.2 dB |
| Peaking | 1629 Hz | 2.66 | -3.3 dB |
| Peaking | 4693 Hz | 1.28 | 6.7 dB  |
| Peaking | 120 Hz  | 5.37 | 2.7 dB  |
| Peaking | 144 Hz  | 5.85 | -2.1 dB |
| Peaking | 2785 Hz | 4    | 1.1 dB  |
| Peaking | 6301 Hz | 3.46 | 4.8 dB  |
| Peaking | 7078 Hz | 1.39 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20471i/Sennheiser%20HD%20471i.png)