# Vsonic VC1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.5; 25 -3.6; 28 -3.6; 31 -3.7; 34 -3.8; 37 -4.0; 41 -4.2; 45 -4.3; 49 -4.4; 54 -4.6; 60 -4.9; 66 -5.3; 72 -5.7; 79 -6.1; 87 -6.6; 96 -7.0; 106 -7.3; 116 -7.5; 128 -7.8; 141 -8.0; 155 -8.3; 170 -8.5; 187 -8.6; 206 -8.7; 227 -8.6; 249 -8.7; 274 -8.6; 302 -8.5; 332 -8.4; 365 -8.2; 402 -8.1; 442 -7.7; 486 -7.7; 535 -7.4; 588 -6.9; 647 -6.6; 712 -6.6; 783 -6.2; 861 -6.3; 947 -6.3; 1042 -6.6; 1146 -6.7; 1261 -6.8; 1387 -7.0; 1526 -7.1; 1678 -7.0; 1846 -6.6; 2031 -6.0; 2234 -5.7; 2457 -5.1; 2703 -3.5; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.7; 4788 -4.1; 5267 -1.5; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.3; 11289 -10.6; 12418 -7.8; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vsonic VC1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vsonic VC1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 26 Hz    |  0.39 | 3.1 dB  |
| Peaking | 196 Hz   |  0.56 | -2.6 dB |
| Peaking | 3406 Hz  |  2.44 | 6.6 dB  |
| Peaking | 5947 Hz  |  3.41 | 6.0 dB  |
| Peaking | 11236 Hz |  4.01 | -4.5 dB |
| Peaking | 821 Hz   |  1.42 | 1.4 dB  |
| Peaking | 1383 Hz  |  0.42 | -1.0 dB |
| Peaking | 2901 Hz  |  9.34 | 2.0 dB  |
| Peaking | 4037 Hz  | 14.47 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Vsonic%20VC1000/Vsonic%20VC1000.png)