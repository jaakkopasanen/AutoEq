# Stax SR-3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.9; 96 -3.4; 106 -5.6; 116 -7.2; 128 -8.5; 141 -9.5; 155 -9.8; 170 -9.8; 187 -9.8; 206 -9.5; 227 -9.0; 249 -8.4; 274 -7.8; 302 -7.5; 332 -7.0; 365 -6.6; 402 -6.3; 442 -6.2; 486 -6.2; 535 -6.0; 588 -6.8; 647 -8.6; 712 -6.8; 783 -5.6; 861 -6.3; 947 -6.8; 1042 -7.8; 1146 -8.0; 1261 -7.2; 1387 -7.7; 1526 -7.8; 1678 -6.9; 1846 -7.4; 2031 -8.0; 2234 -7.8; 2457 -8.2; 2703 -8.4; 2973 -9.1; 3270 -8.5; 3597 -8.6; 3957 -7.4; 4353 -7.1; 4788 -3.9; 5267 -2.5; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.9; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 68 Hz   | 0.32 | 8.8 dB   |
| Peaking | 155 Hz  | 0.9  | -10.2 dB |
| Peaking | 3359 Hz | 2.78 | -1.1 dB  |
| Peaking | 4348 Hz | 0.39 | -2.3 dB  |
| Peaking | 5859 Hz | 2.24 | 8.4 dB   |
| Peaking | 20 Hz   | 1.24 | 2.3 dB   |
| Peaking | 47 Hz   | 0.49 | -1.1 dB  |
| Peaking | 82 Hz   | 4.32 | 2.5 dB   |
| Peaking | 650 Hz  | 6.55 | -4.4 dB  |
| Peaking | 666 Hz  | 2.74 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 7.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-3/Stax%20SR-3.png)