# Sennheiser CX500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -13.6; 25 -13.7; 28 -13.7; 31 -13.7; 34 -13.7; 37 -13.8; 41 -13.9; 45 -14.0; 49 -14.2; 54 -14.4; 60 -14.6; 66 -14.8; 72 -15.1; 79 -15.4; 87 -15.5; 96 -15.7; 106 -15.8; 116 -15.8; 128 -15.9; 141 -16.0; 155 -16.0; 170 -15.9; 187 -15.7; 206 -15.4; 227 -15.1; 249 -14.7; 274 -14.3; 302 -13.7; 332 -13.1; 365 -12.3; 402 -11.7; 442 -11.2; 486 -10.7; 535 -9.9; 588 -9.1; 647 -8.4; 712 -7.7; 783 -7.2; 861 -6.8; 947 -6.6; 1042 -6.4; 1146 -6.4; 1261 -6.3; 1387 -6.4; 1526 -6.8; 1678 -6.8; 1846 -6.6; 2031 -6.1; 2234 -5.4; 2457 -4.3; 2703 -3.1; 2973 -1.8; 3270 -0.6; 3597 -0.5; 3957 -1.4; 4353 -4.0; 4788 -6.2; 5267 -8.1; 5793 -13.2; 6373 -11.2; 7010 -6.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.18 | -6.7 dB |
| Peaking | 151 Hz  | 0.64 | -5.1 dB |
| Peaking | 312 Hz  | 0.99 | -3.3 dB |
| Peaking | 3451 Hz | 2.07 | 6.7 dB  |
| Peaking | 5948 Hz | 5.86 | -9.0 dB |
| Peaking | 520 Hz  | 2.4  | -1.0 dB |
| Peaking | 1470 Hz | 0.48 | 1.3 dB  |
| Peaking | 1753 Hz | 1.76 | -1.9 dB |
| Peaking | 6086 Hz | 0.83 | -0.9 dB |
| Peaking | 7222 Hz | 5.48 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.8 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX500/Sennheiser%20CX500.png)