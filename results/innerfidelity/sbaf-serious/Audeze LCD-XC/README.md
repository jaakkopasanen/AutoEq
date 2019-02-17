# Audeze LCD-XC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -1.9; 25 -1.8; 28 -1.7; 31 -1.6; 34 -1.8; 37 -2.1; 41 -2.3; 45 -2.3; 49 -2.4; 54 -2.8; 60 -3.9; 66 -4.7; 72 -5.0; 79 -5.3; 87 -5.5; 96 -5.8; 106 -5.9; 116 -6.0; 128 -6.1; 141 -6.2; 155 -6.1; 170 -6.3; 187 -6.3; 206 -6.2; 227 -5.8; 249 -5.5; 274 -5.1; 302 -4.9; 332 -4.7; 365 -4.4; 402 -4.3; 442 -4.3; 486 -4.6; 535 -4.5; 588 -4.2; 647 -4.2; 712 -4.7; 783 -5.1; 861 -5.7; 947 -6.2; 1042 -6.8; 1146 -7.4; 1261 -8.2; 1387 -9.2; 1526 -10.2; 1678 -10.7; 1846 -10.5; 2031 -9.3; 2234 -7.7; 2457 -5.9; 2703 -4.6; 2973 -3.8; 3270 -3.3; 3597 -4.1; 3957 -5.7; 4353 -6.3; 4788 -5.9; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.3; 15026 -7.9; 16529 -8.0; 18182 -10.0; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.8  | 5.2 dB  |
| Peaking | 538 Hz   | 0.86 | 2.5 dB  |
| Peaking | 1694 Hz  | 1.62 | -5.1 dB |
| Peaking | 3001 Hz  | 2.62 | 4.0 dB  |
| Peaking | 5968 Hz  | 4.1  | 6.8 dB  |
| Peaking | 52 Hz    | 4.67 | 1.1 dB  |
| Peaking | 134 Hz   | 1.27 | -0.4 dB |
| Peaking | 4421 Hz  | 3.87 | -3.2 dB |
| Peaking | 4487 Hz  | 1.84 | 1.8 dB  |
| Peaking | 19447 Hz | 0.66 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC/Audeze%20LCD-XC.png)