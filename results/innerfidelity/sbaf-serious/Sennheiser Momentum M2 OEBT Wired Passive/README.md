# Sennheiser Momentum M2 OEBT Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.2; 25 -7.6; 28 -8.0; 31 -8.4; 34 -8.6; 37 -8.9; 41 -9.2; 45 -9.6; 49 -9.9; 54 -10.2; 60 -10.4; 66 -10.3; 72 -10.1; 79 -11.2; 87 -11.8; 96 -11.3; 106 -10.8; 116 -11.9; 128 -12.9; 141 -13.2; 155 -12.8; 170 -12.2; 187 -11.8; 206 -10.4; 227 -8.6; 249 -6.7; 274 -5.1; 302 -4.2; 332 -4.0; 365 -4.4; 402 -5.1; 442 -5.0; 486 -4.9; 535 -4.8; 588 -4.5; 647 -4.6; 712 -4.7; 783 -4.7; 861 -5.0; 947 -5.1; 1042 -5.2; 1146 -5.4; 1261 -5.7; 1387 -6.4; 1526 -7.3; 1678 -8.1; 1846 -8.5; 2031 -8.7; 2234 -8.7; 2457 -8.0; 2703 -6.9; 2973 -5.5; 3270 -3.6; 3597 -1.8; 3957 -0.5; 4353 -0.5; 4788 -3.2; 5267 -4.5; 5793 -2.1; 6373 -3.3; 7010 -6.0; 7711 -6.8; 8482 -8.9; 9330 -10.6; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum M2 OEBT Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 1.52 | -2.9 dB |
| Peaking | 71 Hz   | 0.97 | -4.2 dB |
| Peaking | 147 Hz  | 2.26 | -6.0 dB |
| Peaking | 4054 Hz | 3.62 | 6.9 dB  |
| Peaking | 5958 Hz | 6.89 | 4.3 dB  |
| Peaking | 199 Hz  | 3.77 | -2.8 dB |
| Peaking | 309 Hz  | 2.7  | 2.6 dB  |
| Peaking | 1263 Hz | 0.32 | 2.5 dB  |
| Peaking | 1980 Hz | 1.37 | -5.0 dB |
| Peaking | 9105 Hz | 4.66 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Passive/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Passive.png)