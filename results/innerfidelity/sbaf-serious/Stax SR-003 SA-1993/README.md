# Stax SR-003 SA-1993
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.2; 25 -2.4; 28 -2.7; 31 -2.9; 34 -3.1; 37 -3.2; 41 -3.4; 45 -3.7; 49 -3.9; 54 -4.1; 60 -4.5; 66 -4.8; 72 -5.2; 79 -5.6; 87 -6.1; 96 -6.5; 106 -6.9; 116 -7.1; 128 -7.5; 141 -7.8; 155 -8.2; 170 -8.2; 187 -8.4; 206 -8.7; 227 -8.7; 249 -8.9; 274 -9.0; 302 -9.2; 332 -9.2; 365 -9.4; 402 -9.6; 442 -9.7; 486 -10.0; 535 -10.0; 588 -9.5; 647 -9.1; 712 -8.3; 783 -7.2; 861 -5.8; 947 -5.9; 1042 -6.7; 1146 -7.5; 1261 -8.9; 1387 -10.1; 1526 -12.1; 1678 -12.2; 1846 -9.9; 2031 -8.4; 2234 -6.9; 2457 -5.0; 2703 -4.1; 2973 -1.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.4; 6373 -3.4; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.8; 16529 -10.4; 18182 -7.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-003 SA-1993 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-003 SA-1993 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.5  | 4.3 dB  |
| Peaking | 329 Hz   | 0.6  | -3.2 dB |
| Peaking | 1644 Hz  | 2.91 | -6.9 dB |
| Peaking | 3958 Hz  | 1.22 | 7.1 dB  |
| Peaking | 16259 Hz | 2.16 | -4.4 dB |
| Peaking | 567 Hz   | 2.97 | -1.3 dB |
| Peaking | 896 Hz   | 4.5  | 2.5 dB  |
| Peaking | 5206 Hz  | 6.97 | 0.6 dB  |
| Peaking | 5361 Hz  | 8.39 | 1.5 dB  |
| Peaking | 7799 Hz  | 2.27 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-003%20SA-1993/Stax%20SR-003%20SA-1993.png)