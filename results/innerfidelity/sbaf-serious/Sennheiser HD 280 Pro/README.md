# Sennheiser HD 280 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.0; 25 -2.4; 28 -3.0; 31 -3.4; 34 -3.8; 37 -4.1; 41 -4.4; 45 -4.6; 49 -4.8; 54 -4.6; 60 -4.2; 66 -3.2; 72 -2.2; 79 -1.9; 87 -1.8; 96 -2.1; 106 -2.5; 116 -2.9; 128 -3.1; 141 -3.5; 155 -3.7; 170 -3.9; 187 -5.5; 206 -6.3; 227 -6.6; 249 -6.8; 274 -7.1; 302 -7.3; 332 -7.4; 365 -7.4; 402 -7.4; 442 -7.2; 486 -7.4; 535 -7.5; 588 -7.2; 647 -7.3; 712 -7.4; 783 -7.3; 861 -7.6; 947 -7.6; 1042 -7.8; 1146 -8.2; 1261 -8.2; 1387 -8.4; 1526 -9.1; 1678 -10.0; 1846 -10.1; 2031 -9.6; 2234 -8.7; 2457 -6.2; 2703 -3.2; 2973 -2.0; 3270 -2.7; 3597 -3.4; 3957 -3.0; 4353 -3.7; 4788 -4.3; 5267 -2.2; 5793 -0.9; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -9.4; 9330 -11.1; 10263 -7.4; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.35 | 4.3 dB   |
| Peaking | 94 Hz    | 1.25 | 4.2 dB   |
| Peaking | 2094 Hz  | 0.53 | -22.7 dB |
| Peaking | 2685 Hz  | 0.45 | 21.6 dB  |
| Peaking | 9188 Hz  | 3.85 | -8.2 dB  |
| Peaking | 162 Hz   | 7.2  | 2.1 dB   |
| Peaking | 277 Hz   | 1.5  | -1.1 dB  |
| Peaking | 4604 Hz  | 5.96 | -2.4 dB  |
| Peaking | 6171 Hz  | 4.74 | 3.9 dB   |
| Peaking | 14019 Hz | 0.75 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | 3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)