# Beyerdynamic T50p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.4; 49 -1.9; 54 -2.5; 60 -3.2; 66 -3.7; 72 -4.1; 79 -4.4; 87 -4.6; 96 -5.1; 106 -4.3; 116 -4.0; 128 -4.1; 141 -4.0; 155 -3.5; 170 -3.5; 187 -5.2; 206 -7.1; 227 -8.2; 249 -8.9; 274 -8.9; 302 -9.3; 332 -9.8; 365 -9.7; 402 -9.4; 442 -9.2; 486 -9.1; 535 -8.8; 588 -8.2; 647 -8.0; 712 -7.2; 783 -6.5; 861 -6.6; 947 -6.6; 1042 -6.3; 1146 -6.0; 1261 -5.6; 1387 -5.6; 1526 -5.5; 1678 -5.2; 1846 -4.2; 2031 -2.6; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.56 | 6.4 dB  |
| Peaking | 160 Hz  | 1.69 | 4.8 dB  |
| Peaking | 291 Hz  | 0.66 | -4.2 dB |
| Peaking | 2863 Hz | 1.15 | 6.2 dB  |
| Peaking | 5393 Hz | 2.16 | 5.0 dB  |
| Peaking | 1692 Hz | 4.55 | -1.0 dB |
| Peaking | 2243 Hz | 7.78 | 1.5 dB  |
| Peaking | 6306 Hz | 6.73 | 1.5 dB  |
| Peaking | 6634 Hz | 5.91 | 1.4 dB  |
| Peaking | 7691 Hz | 1.97 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | 3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p/Beyerdynamic%20T50p.png)