# T-Peos Popular
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.4; 23 -14.3; 25 -14.3; 28 -14.2; 31 -14.0; 34 -13.9; 37 -13.7; 41 -13.6; 45 -13.4; 49 -13.2; 54 -13.1; 60 -12.9; 66 -12.8; 72 -12.7; 79 -12.6; 87 -12.5; 96 -12.3; 106 -12.1; 116 -11.7; 128 -11.6; 141 -11.2; 155 -10.9; 170 -10.5; 187 -10.1; 206 -9.6; 227 -9.1; 249 -8.7; 274 -8.1; 302 -7.6; 332 -7.2; 365 -6.7; 402 -6.2; 442 -5.7; 486 -5.4; 535 -5.1; 588 -4.6; 647 -4.5; 712 -4.5; 783 -4.4; 861 -4.8; 947 -5.4; 1042 -6.6; 1146 -6.0; 1261 -7.3; 1387 -8.6; 1526 -10.1; 1678 -11.5; 1846 -12.5; 2031 -13.0; 2234 -12.8; 2457 -10.3; 2703 -7.1; 2973 -3.5; 3270 -1.3; 3597 -0.5; 3957 -1.9; 4353 -5.5; 4788 -9.1; 5267 -12.3; 5793 -9.4; 6373 -5.2; 7010 -3.7; 7711 -5.7; 8482 -6.6; 9330 -8.7; 10263 -8.3; 11289 -6.0; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Popular GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Popular ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.3  | -8.2 dB |
| Peaking | 134 Hz  | 0.99 | -3.1 dB |
| Peaking | 2066 Hz | 2.09 | -8.8 dB |
| Peaking | 3479 Hz | 2.37 | 7.7 dB  |
| Peaking | 5224 Hz | 5.08 | -7.9 dB |
| Peaking | 246 Hz  | 2.12 | -0.8 dB |
| Peaking | 686 Hz  | 1.23 | 2.2 dB  |
| Peaking | 1549 Hz | 4.43 | -1.7 dB |
| Peaking | 6857 Hz | 6.82 | 3.2 dB  |
| Peaking | 9628 Hz | 4.55 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Popular/T-Peos%20Popular.png)