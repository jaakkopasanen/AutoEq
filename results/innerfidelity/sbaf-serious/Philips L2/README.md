# Philips L2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -10.2; 25 -10.6; 28 -11.1; 31 -11.4; 34 -11.6; 37 -11.8; 41 -11.9; 45 -12.0; 49 -11.9; 54 -11.9; 60 -11.8; 66 -11.7; 72 -11.5; 79 -11.3; 87 -11.1; 96 -11.0; 106 -10.9; 116 -10.9; 128 -11.2; 141 -10.7; 155 -10.3; 170 -9.7; 187 -9.8; 206 -9.7; 227 -9.3; 249 -9.1; 274 -8.7; 302 -8.1; 332 -7.9; 365 -7.5; 402 -7.1; 442 -6.6; 486 -6.3; 535 -5.8; 588 -5.1; 647 -4.7; 712 -4.8; 783 -4.9; 861 -5.4; 947 -5.8; 1042 -5.9; 1146 -5.6; 1261 -6.8; 1387 -8.7; 1526 -10.6; 1678 -11.9; 1846 -12.5; 2031 -12.6; 2234 -12.2; 2457 -12.1; 2703 -11.1; 2973 -9.9; 3270 -8.2; 3597 -6.9; 3957 -5.6; 4353 -3.4; 4788 -1.8; 5267 -0.5; 5793 -4.2; 6373 -7.6; 7010 -8.9; 7711 -8.2; 8482 -7.3; 9330 -6.3; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.9; 18182 -8.7; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips L2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips L2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.42 | -6.0 dB |
| Peaking | 171 Hz   | 0.98 | -2.6 dB |
| Peaking | 2140 Hz  | 1.6  | -7.5 dB |
| Peaking | 5057 Hz  | 4.96 | 6.7 dB  |
| Peaking | 674 Hz   | 3.16 | 1.6 dB  |
| Peaking | 1354 Hz  | 1.38 | 2.7 dB  |
| Peaking | 1547 Hz  | 2.99 | -4.1 dB |
| Peaking | 7163 Hz  | 3.96 | -3.5 dB |
| Peaking | 19072 Hz | 1.48 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20L2/Philips%20L2.png)