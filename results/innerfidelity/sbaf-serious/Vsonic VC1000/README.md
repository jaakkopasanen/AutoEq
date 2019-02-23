# Vsonic VC1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.4; 25 -4.5; 28 -4.5; 31 -4.6; 34 -4.7; 37 -4.9; 41 -5.0; 45 -5.2; 49 -5.3; 54 -5.5; 60 -5.8; 66 -6.2; 72 -6.6; 79 -7.0; 87 -7.5; 96 -7.9; 106 -8.2; 116 -8.4; 128 -8.7; 141 -8.9; 155 -9.2; 170 -9.4; 187 -9.5; 206 -9.6; 227 -9.5; 249 -9.6; 274 -9.5; 302 -9.4; 332 -9.3; 365 -9.1; 402 -9.0; 442 -8.6; 486 -8.6; 535 -8.3; 588 -7.8; 647 -7.5; 712 -7.5; 783 -7.1; 861 -7.2; 947 -7.2; 1042 -7.5; 1146 -7.6; 1261 -7.7; 1387 -7.9; 1526 -7.9; 1678 -7.9; 1846 -7.5; 2031 -6.9; 2234 -6.6; 2457 -6.0; 2703 -4.4; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -4.6; 4788 -5.0; 5267 -2.4; 5793 -1.4; 6373 -2.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -9.2; 11289 -11.4; 12418 -8.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vsonic VC1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vsonic VC1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 37 Hz    |  0.43 | 3.0 dB  |
| Peaking | 183 Hz   |  0.31 | -3.4 dB |
| Peaking | 3429 Hz  |  3.02 | 6.8 dB  |
| Peaking | 6008 Hz  |  3.35 | 5.2 dB  |
| Peaking | 11243 Hz |  3.87 | -5.5 dB |
| Peaking | 752 Hz   |  1.79 | 0.8 dB  |
| Peaking | 1626 Hz  |  1.49 | -1.4 dB |
| Peaking | 2972 Hz  | 11.19 | 2.0 dB  |
| Peaking | 4572 Hz  | 16.5  | -1.7 dB |
| Peaking | 13476 Hz |  6.79 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Vsonic%20VC1000/Vsonic%20VC1000.png)