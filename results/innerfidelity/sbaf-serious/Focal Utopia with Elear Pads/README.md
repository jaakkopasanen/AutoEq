# Focal Utopia with Elear Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.7; 25 -6.8; 28 -7.0; 31 -7.1; 34 -7.2; 37 -7.3; 41 -7.4; 45 -7.6; 49 -7.7; 54 -8.0; 60 -8.4; 66 -8.6; 72 -8.9; 79 -9.1; 87 -9.5; 96 -9.8; 106 -9.9; 116 -10.1; 128 -10.3; 141 -10.3; 155 -10.3; 170 -10.2; 187 -10.1; 206 -10.0; 227 -9.7; 249 -9.4; 274 -9.1; 302 -8.7; 332 -8.3; 365 -7.9; 402 -7.5; 442 -7.0; 486 -6.9; 535 -6.7; 588 -6.2; 647 -5.8; 712 -5.7; 783 -5.5; 861 -5.7; 947 -5.7; 1042 -5.5; 1146 -5.6; 1261 -5.7; 1387 -6.0; 1526 -6.2; 1678 -6.5; 1846 -6.0; 2031 -5.8; 2234 -6.3; 2457 -7.9; 2703 -8.0; 2973 -5.9; 3270 -4.4; 3597 -1.4; 3957 -2.4; 4353 -3.5; 4788 -2.2; 5267 -0.5; 5793 -2.9; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -7.7; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Utopia with Elear Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia with Elear Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 110 Hz  | 0.79 | -3.3 dB |
| Peaking | 219 Hz  | 1.47 | -2.1 dB |
| Peaking | 3687 Hz | 6.91 | 4.6 dB  |
| Peaking | 5377 Hz | 2.34 | 5.5 dB  |
| Peaking | 8786 Hz | 5.58 | -2.3 dB |
| Peaking | 345 Hz  | 2.26 | -0.5 dB |
| Peaking | 858 Hz  | 1.08 | 1.2 dB  |
| Peaking | 2113 Hz | 5.19 | 1.1 dB  |
| Peaking | 2600 Hz | 3.41 | -3.0 dB |
| Peaking | 3147 Hz | 3.25 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Utopia%20with%20Elear%20Pads/Focal%20Utopia%20with%20Elear%20Pads.png)