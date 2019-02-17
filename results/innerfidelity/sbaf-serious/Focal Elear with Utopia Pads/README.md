# Focal Elear with Utopia Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.0; 37 -1.3; 41 -1.6; 45 -1.8; 49 -2.0; 54 -2.3; 60 -2.6; 66 -2.9; 72 -3.2; 79 -3.6; 87 -4.1; 96 -4.6; 106 -4.8; 116 -5.0; 128 -5.3; 141 -5.6; 155 -5.8; 170 -5.7; 187 -5.8; 206 -5.9; 227 -5.7; 249 -5.8; 274 -5.6; 302 -5.6; 332 -5.5; 365 -5.3; 402 -5.3; 442 -5.1; 486 -5.1; 535 -5.2; 588 -4.9; 647 -5.1; 712 -5.3; 783 -5.3; 861 -5.8; 947 -6.2; 1042 -6.5; 1146 -7.1; 1261 -7.7; 1387 -8.0; 1526 -8.0; 1678 -8.1; 1846 -7.2; 2031 -5.6; 2234 -4.3; 2457 -3.7; 2703 -3.4; 2973 -3.0; 3270 -2.4; 3597 -1.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear with Utopia Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear with Utopia Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.69 | 5.7 dB  |
| Peaking | 60 Hz   | 0.93 | 2.1 dB  |
| Peaking | 552 Hz  | 0.8  | 1.4 dB  |
| Peaking | 1470 Hz | 2.17 | -2.9 dB |
| Peaking | 4438 Hz | 1.1  | 6.7 dB  |
| Peaking | 1787 Hz | 8.22 | -1.1 dB |
| Peaking | 2386 Hz | 3.36 | 1.2 dB  |
| Peaking | 4515 Hz | 4.29 | -0.5 dB |
| Peaking | 6336 Hz | 2.86 | 4.9 dB  |
| Peaking | 7258 Hz | 1.53 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Elear%20with%20Utopia%20Pads/Focal%20Elear%20with%20Utopia%20Pads.png)