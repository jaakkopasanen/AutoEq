# Beyerdynamic T51i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -6.1; 25 -6.6; 28 -7.3; 31 -7.9; 34 -8.4; 37 -8.9; 41 -9.3; 45 -9.7; 49 -10.0; 54 -10.7; 60 -11.2; 66 -11.6; 72 -11.9; 79 -12.2; 87 -12.4; 96 -12.6; 106 -13.1; 116 -13.5; 128 -13.2; 141 -13.5; 155 -13.4; 170 -12.7; 187 -12.3; 206 -11.5; 227 -10.5; 249 -9.7; 274 -8.8; 302 -8.2; 332 -8.4; 365 -8.9; 402 -9.2; 442 -8.9; 486 -8.8; 535 -8.5; 588 -7.9; 647 -7.6; 712 -7.4; 783 -6.4; 861 -5.9; 947 -5.9; 1042 -5.6; 1146 -5.2; 1261 -4.9; 1387 -4.6; 1526 -4.3; 1678 -3.5; 1846 -2.0; 2031 -0.9; 2234 -2.2; 2457 -4.0; 2703 -4.1; 2973 -2.6; 3270 -1.0; 3597 -0.5; 3957 -0.5; 4353 -2.3; 4788 -4.0; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -10.3; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T51i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T51i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 1.44 | -1.6 dB |
| Peaking | 128 Hz  | 0.62 | -6.7 dB |
| Peaking | 1946 Hz | 2.15 | 4.8 dB  |
| Peaking | 3671 Hz | 2.74 | 5.9 dB  |
| Peaking | 5939 Hz | 4.25 | 6.0 dB  |
| Peaking | 291 Hz  | 2.5  | 2.1 dB  |
| Peaking | 641 Hz  | 0.59 | -2.5 dB |
| Peaking | 901 Hz  | 1.07 | 2.8 dB  |
| Peaking | 6726 Hz | 6.54 | 1.3 dB  |
| Peaking | 9287 Hz | 4.89 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T51i/Beyerdynamic%20T51i.png)