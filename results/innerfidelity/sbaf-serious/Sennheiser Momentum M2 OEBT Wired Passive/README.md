# Sennheiser Momentum M2 OEBT Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.4; 25 -8.7; 28 -9.1; 31 -9.5; 34 -9.8; 37 -10.0; 41 -10.3; 45 -10.7; 49 -11.0; 54 -11.3; 60 -11.5; 66 -11.5; 72 -11.2; 79 -12.3; 87 -12.9; 96 -12.4; 106 -11.9; 116 -13.1; 128 -14.1; 141 -14.3; 155 -13.9; 170 -13.3; 187 -12.9; 206 -11.5; 227 -9.7; 249 -7.8; 274 -6.2; 302 -5.3; 332 -5.1; 365 -5.5; 402 -6.3; 442 -6.1; 486 -6.0; 535 -5.9; 588 -5.6; 647 -5.7; 712 -5.8; 783 -5.8; 861 -6.1; 947 -6.2; 1042 -6.4; 1146 -6.5; 1261 -6.8; 1387 -7.5; 1526 -8.5; 1678 -9.2; 1846 -9.6; 2031 -9.9; 2234 -9.8; 2457 -9.1; 2703 -8.1; 2973 -6.6; 3270 -4.7; 3597 -2.9; 3957 -0.5; 4353 -0.6; 4788 -4.3; 5267 -5.6; 5793 -3.2; 6373 -4.4; 7010 -7.1; 7711 -8.0; 8482 -10.0; 9330 -11.7; 10263 -7.3; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum M2 OEBT Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.98 | -4.3 dB |
| Peaking | 68 Hz   | 0.75 | -5.1 dB |
| Peaking | 151 Hz  | 1.86 | -6.6 dB |
| Peaking | 4138 Hz | 4.42 | 6.9 dB  |
| Peaking | 9094 Hz | 4.77 | -5.9 dB |
| Peaking | 203 Hz  | 4.87 | -2.1 dB |
| Peaking | 308 Hz  | 2.95 | 2.4 dB  |
| Peaking | 816 Hz  | 0.68 | 1.0 dB  |
| Peaking | 2145 Hz | 1.19 | -6.2 dB |
| Peaking | 3023 Hz | 0.8  | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Passive/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Passive.png)