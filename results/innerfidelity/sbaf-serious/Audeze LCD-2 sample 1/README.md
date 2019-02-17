# Audeze LCD-2 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.5; 31 -1.6; 34 -1.6; 37 -1.6; 41 -1.7; 45 -1.7; 49 -1.8; 54 -2.1; 60 -2.6; 66 -3.3; 72 -3.7; 79 -3.8; 87 -4.0; 96 -4.2; 106 -4.5; 116 -4.6; 128 -4.9; 141 -5.1; 155 -5.3; 170 -5.4; 187 -5.6; 206 -5.7; 227 -5.7; 249 -5.9; 274 -6.0; 302 -6.0; 332 -6.2; 365 -6.2; 402 -6.3; 442 -6.4; 486 -6.3; 535 -6.0; 588 -6.0; 647 -6.6; 712 -6.9; 783 -7.0; 861 -7.3; 947 -7.2; 1042 -6.0; 1146 -3.7; 1261 -3.0; 1387 -3.0; 1526 -3.4; 1678 -2.1; 1846 -0.7; 2031 -0.7; 2234 -2.0; 2457 -2.0; 2703 -2.1; 2973 -1.1; 3270 -0.7; 3597 -0.7; 3957 -0.7; 4353 -0.7; 4788 -0.7; 5267 -0.7; 5793 -0.7; 6373 -1.2; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 1.3  | 5.9 dB  |
| Peaking | 33 Hz   | 0.36 | 4.6 dB  |
| Peaking | 1863 Hz | 1.58 | 4.9 dB  |
| Peaking | 3747 Hz | 1.52 | 5.3 dB  |
| Peaking | 5758 Hz | 3.07 | 4.6 dB  |
| Peaking | 12 Hz   | 0.43 | 0.2 dB  |
| Peaking | 951 Hz  | 2.59 | -3.0 dB |
| Peaking | 1213 Hz | 1.99 | 3.0 dB  |
| Peaking | 1523 Hz | 4.4  | -1.9 dB |
| Peaking | 8323 Hz | 3.84 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sample%201/Audeze%20LCD-2%20sample%201.png)