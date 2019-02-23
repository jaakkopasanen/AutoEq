# Focal Elear with Utopia Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.1; 25 -2.5; 28 -2.9; 31 -3.3; 34 -3.6; 37 -3.9; 41 -4.1; 45 -4.4; 49 -4.6; 54 -4.8; 60 -5.1; 66 -5.5; 72 -5.8; 79 -6.2; 87 -6.6; 96 -7.1; 106 -7.4; 116 -7.6; 128 -7.9; 141 -8.1; 155 -8.3; 170 -8.3; 187 -8.3; 206 -8.5; 227 -8.3; 249 -8.3; 274 -8.2; 302 -8.2; 332 -8.0; 365 -7.9; 402 -7.9; 442 -7.7; 486 -7.7; 535 -7.8; 588 -7.5; 647 -7.7; 712 -7.9; 783 -7.9; 861 -8.3; 947 -8.7; 1042 -9.1; 1146 -9.7; 1261 -10.2; 1387 -10.6; 1526 -10.5; 1678 -10.6; 1846 -9.8; 2031 -8.1; 2234 -6.9; 2457 -6.2; 2703 -6.0; 2973 -5.6; 3270 -4.9; 3597 -4.3; 3957 -0.8; 4353 -1.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear with Utopia Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear with Utopia Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.65 | 5.2 dB  |
| Peaking | 60 Hz    | 0.9  | 1.5 dB  |
| Peaking | 161 Hz   | 0.41 | -2.2 dB |
| Peaking | 1458 Hz  | 1.41 | -4.6 dB |
| Peaking | 4929 Hz  | 1.53 | 7.0 dB  |
| Peaking | 1793 Hz  | 7.13 | -1.0 dB |
| Peaking | 2279 Hz  | 2.75 | 0.7 dB  |
| Peaking | 6438 Hz  | 4.28 | 3.9 dB  |
| Peaking | 7243 Hz  | 1.76 | -2.5 dB |
| Peaking | 11519 Hz | 1.04 | -0.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Elear%20with%20Utopia%20Pads/Focal%20Elear%20with%20Utopia%20Pads.png)