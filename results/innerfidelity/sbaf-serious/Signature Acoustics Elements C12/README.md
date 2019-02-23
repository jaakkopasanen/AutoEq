# Signature Acoustics Elements C12
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.6; 25 -9.0; 28 -9.6; 31 -10.1; 34 -10.6; 37 -11.0; 41 -11.5; 45 -11.8; 49 -12.1; 54 -12.5; 60 -13.0; 66 -13.4; 72 -13.8; 79 -14.1; 87 -14.6; 96 -15.0; 106 -15.1; 116 -15.3; 128 -15.4; 141 -15.5; 155 -15.5; 170 -15.4; 187 -15.2; 206 -14.9; 227 -14.5; 249 -14.1; 274 -13.6; 302 -13.0; 332 -12.3; 365 -11.6; 402 -10.8; 442 -9.8; 486 -9.1; 535 -8.0; 588 -6.7; 647 -5.6; 712 -4.5; 783 -3.2; 861 -2.1; 947 -1.0; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -1.0; 1678 -2.3; 1846 -2.8; 2031 -3.1; 2234 -2.6; 2457 -1.2; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.1; 4788 -5.6; 5267 -7.5; 5793 -9.9; 6373 -8.1; 7010 -5.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Signature Acoustics Elements C12 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Signature Acoustics Elements C12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.42 | -3.4 dB |
| Peaking | 195 Hz  | 0.4  | -7.4 dB |
| Peaking | 1054 Hz | 0.93 | 7.3 dB  |
| Peaking | 3396 Hz | 1.33 | 6.0 dB  |
| Peaking | 5692 Hz | 3.97 | -5.5 dB |
| Peaking | 1461 Hz | 7.01 | 1.1 dB  |
| Peaking | 2094 Hz | 2.16 | -1.6 dB |
| Peaking | 2603 Hz | 2.23 | 1.9 dB  |
| Peaking | 3153 Hz | 5.15 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Signature%20Acoustics%20Elements%20C12/Signature%20Acoustics%20Elements%20C12.png)