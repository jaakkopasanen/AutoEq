# Philips TX2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.5; 25 -10.5; 28 -10.5; 31 -10.4; 34 -10.4; 37 -10.4; 41 -10.4; 45 -10.4; 49 -10.4; 54 -10.4; 60 -10.5; 66 -10.5; 72 -10.6; 79 -10.7; 87 -10.8; 96 -10.9; 106 -10.8; 116 -10.6; 128 -10.6; 141 -10.4; 155 -10.2; 170 -9.9; 187 -9.5; 206 -9.1; 227 -8.6; 249 -8.2; 274 -7.7; 302 -7.2; 332 -6.7; 365 -6.2; 402 -5.8; 442 -5.2; 486 -4.4; 535 -4.3; 588 -3.7; 647 -3.4; 712 -3.4; 783 -3.1; 861 -3.4; 947 -3.7; 1042 -4.1; 1146 -4.5; 1261 -5.1; 1387 -5.8; 1526 -6.6; 1678 -7.3; 1846 -7.8; 2031 -8.2; 2234 -8.2; 2457 -7.0; 2703 -5.3; 2973 -3.0; 3270 -1.1; 3597 -0.5; 3957 -1.5; 4353 -4.2; 4788 -6.2; 5267 -7.5; 5793 -7.8; 6373 -7.5; 7010 -5.4; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips TX2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips TX2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 77 Hz   | 0.16 | -4.8 dB |
| Peaking | 669 Hz  | 0.56 | 4.8 dB  |
| Peaking | 2147 Hz | 1.2  | -4.8 dB |
| Peaking | 3492 Hz | 1.85 | 7.7 dB  |
| Peaking | 5336 Hz | 2.68 | -3.3 dB |
| Peaking | 17 Hz   | 0.89 | -1.1 dB |
| Peaking | 62 Hz   | 0.35 | 0.9 dB  |
| Peaking | 113 Hz  | 0.92 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20TX2/Philips%20TX2.png)