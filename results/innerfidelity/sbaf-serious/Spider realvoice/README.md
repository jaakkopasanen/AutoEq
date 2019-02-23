# Spider realvoice
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.5; 25 -12.4; 28 -12.3; 31 -12.2; 34 -12.1; 37 -12.0; 41 -11.9; 45 -11.9; 49 -11.8; 54 -11.7; 60 -11.7; 66 -11.6; 72 -11.6; 79 -11.7; 87 -11.7; 96 -11.7; 106 -11.6; 116 -11.4; 128 -11.3; 141 -11.2; 155 -11.0; 170 -10.7; 187 -10.5; 206 -10.2; 227 -9.8; 249 -9.7; 274 -9.4; 302 -9.1; 332 -8.8; 365 -8.5; 402 -8.3; 442 -8.0; 486 -7.9; 535 -7.7; 588 -7.3; 647 -7.2; 712 -6.7; 783 -7.1; 861 -7.3; 947 -7.6; 1042 -7.9; 1146 -8.2; 1261 -8.5; 1387 -9.1; 1526 -9.6; 1678 -9.9; 1846 -9.6; 2031 -8.8; 2234 -7.5; 2457 -5.4; 2703 -3.3; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.4; 4788 -3.3; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spider realvoice GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider realvoice ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.34 | -5.5 dB |
| Peaking | 129 Hz  | 0.46 | -4.0 dB |
| Peaking | 1809 Hz | 1.39 | -4.7 dB |
| Peaking | 3303 Hz | 1.63 | 7.4 dB  |
| Peaking | 5868 Hz | 3.52 | 5.5 dB  |
| Peaking | 712 Hz  | 6.07 | 0.8 dB  |
| Peaking | 6612 Hz | 8.78 | 1.8 dB  |
| Peaking | 7856 Hz | 2.35 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Spider%20realvoice/Spider%20realvoice.png)