# Focal Utopia with Elear Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.4; 28 -7.6; 31 -7.7; 34 -7.8; 37 -7.9; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.7; 60 -9.0; 66 -9.3; 72 -9.5; 79 -9.8; 87 -10.1; 96 -10.5; 106 -10.5; 116 -10.7; 128 -10.9; 141 -10.9; 155 -10.9; 170 -10.8; 187 -10.8; 206 -10.6; 227 -10.3; 249 -10.1; 274 -9.7; 302 -9.3; 332 -8.9; 365 -8.5; 402 -8.1; 442 -7.6; 486 -7.6; 535 -7.4; 588 -6.8; 647 -6.4; 712 -6.4; 783 -6.1; 861 -6.3; 947 -6.3; 1042 -6.1; 1146 -6.2; 1261 -6.3; 1387 -6.6; 1526 -6.8; 1678 -7.1; 1846 -6.6; 2031 -6.5; 2234 -6.9; 2457 -8.5; 2703 -8.7; 2973 -6.6; 3270 -5.1; 3597 -2.0; 3957 -3.0; 4353 -4.2; 4788 -2.8; 5267 -0.5; 5793 -3.5; 6373 -3.5; 7010 -3.7; 7711 -5.9; 8482 -8.3; 9330 -7.8; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -7.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Utopia with Elear Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia with Elear Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 104 Hz   |  0.51 | -3.6 dB |
| Peaking | 219 Hz   |  0.93 | -2.2 dB |
| Peaking | 2607 Hz  |  4.15 | -3.0 dB |
| Peaking | 3677 Hz  |  5.77 | 4.5 dB  |
| Peaking | 5311 Hz  |  3.62 | 5.3 dB  |
| Peaking | 784 Hz   |  2.3  | 0.5 dB  |
| Peaking | 1620 Hz  |  6.85 | -0.8 dB |
| Peaking | 6777 Hz  | 10.12 | 2.7 dB  |
| Peaking | 8787 Hz  |  6.59 | -3.2 dB |
| Peaking | 18227 Hz |  3.17 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Utopia%20with%20Elear%20Pads/Focal%20Utopia%20with%20Elear%20Pads.png)