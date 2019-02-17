# Sennheiser Momentum Wireless Wired Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.7; 25 -4.1; 28 -4.2; 31 -3.9; 34 -3.5; 37 -3.2; 41 -3.0; 45 -2.7; 49 -2.5; 54 -2.2; 60 -2.1; 66 -1.9; 72 -1.9; 79 -1.9; 87 -1.8; 96 -1.9; 106 -1.8; 116 -1.6; 128 -1.5; 141 -1.5; 155 -1.3; 170 -1.1; 187 -0.8; 206 -0.6; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.7; 535 -1.6; 588 -2.2; 647 -3.1; 712 -4.0; 783 -4.5; 861 -5.4; 947 -6.1; 1042 -6.7; 1146 -7.1; 1261 -8.1; 1387 -9.2; 1526 -10.7; 1678 -11.4; 1846 -12.2; 2031 -12.2; 2234 -10.8; 2457 -8.0; 2703 -5.7; 2973 -2.8; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -4.7; 5267 -2.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum Wireless Wired Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum Wireless Wired Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 100 Hz   | 0.23 | 4.4 dB  |
| Peaking | 413 Hz   | 0.73 | 3.9 dB  |
| Peaking | 1947 Hz  | 1.25 | -8.3 dB |
| Peaking | 3463 Hz  | 1.6  | 8.7 dB  |
| Peaking | 6075 Hz  | 4.85 | 5.3 dB  |
| Peaking | 102 Hz   | 3.21 | -0.1 dB |
| Peaking | 4620 Hz  | 5.41 | -1.7 dB |
| Peaking | 4680 Hz  | 6.52 | 2.1 dB  |
| Peaking | 8408 Hz  | 4.06 | -0.7 dB |
| Peaking | 10849 Hz | 2.12 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 3.5 dB  |
| Peaking | 250 Hz   | 1.41 | 5.0 dB  |
| Peaking | 500 Hz   | 1.41 | 5.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20Wireless%20Wired%20Active/Sennheiser%20Momentum%20Wireless%20Wired%20Active.png)