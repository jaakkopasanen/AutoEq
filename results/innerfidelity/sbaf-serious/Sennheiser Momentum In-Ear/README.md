# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.5; 25 -11.5; 28 -11.6; 31 -11.7; 34 -11.7; 37 -11.8; 41 -11.8; 45 -11.9; 49 -12.0; 54 -12.1; 60 -12.2; 66 -12.4; 72 -12.5; 79 -12.7; 87 -12.9; 96 -13.0; 106 -13.0; 116 -12.9; 128 -12.8; 141 -12.7; 155 -12.5; 170 -12.2; 187 -11.9; 206 -11.5; 227 -11.0; 249 -10.6; 274 -10.0; 302 -9.5; 332 -8.9; 365 -8.3; 402 -7.7; 442 -7.0; 486 -6.6; 535 -6.0; 588 -5.3; 647 -4.8; 712 -4.6; 783 -4.2; 861 -4.2; 947 -4.4; 1042 -4.7; 1146 -4.9; 1261 -5.2; 1387 -5.7; 1526 -6.2; 1678 -6.5; 1846 -6.2; 2031 -5.6; 2234 -4.9; 2457 -3.5; 2703 -2.2; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -3.3; 5267 -3.9; 5793 -6.2; 6373 -9.8; 7010 -8.6; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.2; 12418 -7.9; 13660 -7.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.39 | -5.0 dB |
| Peaking | 115 Hz   | 0.98 | -4.2 dB |
| Peaking | 216 Hz   | 1.65 | -2.9 dB |
| Peaking | 3571 Hz  | 1.31 | 6.6 dB  |
| Peaking | 6518 Hz  | 4.71 | -5.2 dB |
| Peaking | 345 Hz   | 1.9  | -1.1 dB |
| Peaking | 804 Hz   | 1.09 | 2.5 dB  |
| Peaking | 1762 Hz  | 2.2  | -1.9 dB |
| Peaking | 6092 Hz  | 0.11 | 0.1 dB  |
| Peaking | 12696 Hz | 2.64 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)