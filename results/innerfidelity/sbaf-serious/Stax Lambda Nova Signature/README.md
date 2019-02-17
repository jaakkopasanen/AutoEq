# Stax Lambda Nova Signature
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.1; 28 -2.9; 31 -3.4; 34 -3.5; 37 -3.5; 41 -3.4; 45 -3.2; 49 -2.9; 54 -2.7; 60 -2.6; 66 -2.6; 72 -2.6; 79 -2.7; 87 -3.0; 96 -3.4; 106 -3.5; 116 -3.5; 128 -3.7; 141 -3.8; 155 -3.8; 170 -3.9; 187 -4.0; 206 -4.0; 227 -4.0; 249 -4.1; 274 -4.1; 302 -4.1; 332 -4.1; 365 -4.1; 402 -4.1; 442 -3.9; 486 -4.1; 535 -4.2; 588 -4.0; 647 -4.3; 712 -4.5; 783 -4.6; 861 -5.2; 947 -5.7; 1042 -6.1; 1146 -6.6; 1261 -7.6; 1387 -8.9; 1526 -9.1; 1678 -9.7; 1846 -8.8; 2031 -6.0; 2234 -2.9; 2457 -2.4; 2703 -4.2; 2973 -5.5; 3270 -5.5; 3597 -4.8; 3957 -3.9; 4353 -4.1; 4788 -4.0; 5267 -1.4; 5793 -4.1; 6373 -4.4; 7010 -3.5; 7711 -5.7; 8482 -8.4; 9330 -9.4; 10263 -6.6; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax Lambda Nova Signature GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax Lambda Nova Signature ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 13 Hz    |  1.16 | 6.3 dB  |
| Peaking | 89 Hz    |  0.07 | 2.4 dB  |
| Peaking | 1666 Hz  |  1.57 | -5.6 dB |
| Peaking | 2345 Hz  |  3.61 | 5.9 dB  |
| Peaking | 5272 Hz  |  3.16 | 4.0 dB  |
| Peaking | 35 Hz    |  2.31 | -0.9 dB |
| Peaking | 65 Hz    |  2.44 | 1.2 dB  |
| Peaking | 6815 Hz  | 10.02 | 2.9 dB  |
| Peaking | 9100 Hz  |  4.43 | -4.3 dB |
| Peaking | 10644 Hz |  3.93 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20Lambda%20Nova%20Signature/Stax%20Lambda%20Nova%20Signature.png)