# Sennheiser Momentum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.2; 25 -3.3; 28 -3.6; 31 -3.7; 34 -3.9; 37 -4.0; 41 -4.2; 45 -4.4; 49 -4.5; 54 -4.8; 60 -5.0; 66 -5.2; 72 -5.5; 79 -5.8; 87 -6.2; 96 -6.6; 106 -6.8; 116 -6.8; 128 -6.8; 141 -6.8; 155 -7.6; 170 -7.3; 187 -7.5; 206 -7.8; 227 -7.7; 249 -7.6; 274 -7.2; 302 -6.8; 332 -6.4; 365 -5.8; 402 -5.3; 442 -5.0; 486 -5.1; 535 -5.0; 588 -5.0; 647 -5.3; 712 -5.8; 783 -5.9; 861 -6.3; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.5; 1387 -7.3; 1526 -7.9; 1678 -7.9; 1846 -7.3; 2031 -6.3; 2234 -4.9; 2457 -2.8; 2703 -1.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.32 | 3.4 dB  |
| Peaking | 47 Hz   | 2.06 | 1.6 dB  |
| Peaking | 527 Hz  | 2.52 | 1.7 dB  |
| Peaking | 1705 Hz | 2.04 | -3.6 dB |
| Peaking | 3815 Hz | 0.86 | 7.1 dB  |
| Peaking | 204 Hz  | 1.84 | -1.5 dB |
| Peaking | 2831 Hz | 4.93 | 1.3 dB  |
| Peaking | 3847 Hz | 2.8  | -1.0 dB |
| Peaking | 6281 Hz | 2.37 | 5.4 dB  |
| Peaking | 7332 Hz | 1.48 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum/Sennheiser%20Momentum.png)