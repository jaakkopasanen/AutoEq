# Focal Spirit One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.6; 25 -10.7; 28 -10.7; 31 -10.7; 34 -10.7; 37 -10.7; 41 -10.6; 45 -10.5; 49 -10.4; 54 -10.4; 60 -10.5; 66 -10.4; 72 -10.1; 79 -9.6; 87 -10.2; 96 -12.0; 106 -12.6; 116 -12.5; 128 -12.3; 141 -12.4; 155 -12.2; 170 -11.7; 187 -11.4; 206 -10.9; 227 -10.0; 249 -9.2; 274 -8.3; 302 -7.6; 332 -7.6; 365 -7.5; 402 -8.3; 442 -8.2; 486 -8.3; 535 -8.3; 588 -7.9; 647 -8.0; 712 -8.0; 783 -7.5; 861 -7.2; 947 -6.6; 1042 -6.3; 1146 -6.7; 1261 -6.4; 1387 -6.6; 1526 -6.8; 1678 -6.7; 1846 -6.0; 2031 -5.1; 2234 -4.2; 2457 -2.9; 2703 -1.9; 2973 -0.6; 3270 -0.7; 3597 -0.5; 3957 -3.2; 4353 -5.6; 4788 -6.2; 5267 -6.1; 5793 -2.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.53 | -4.1 dB |
| Peaking | 136 Hz  | 0.97 | -5.5 dB |
| Peaking | 1866 Hz | 0.15 | -0.9 dB |
| Peaking | 3096 Hz | 1.84 | 7.2 dB  |
| Peaking | 6288 Hz | 5.67 | 6.3 dB  |
| Peaking | 322 Hz  | 3.01 | 1.6 dB  |
| Peaking | 661 Hz  | 0.47 | -1.0 dB |
| Peaking | 1025 Hz | 1.76 | 1.6 dB  |
| Peaking | 4562 Hz | 1.6  | 2.3 dB  |
| Peaking | 4746 Hz | 3.2  | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One/Focal%20Spirit%20One.png)