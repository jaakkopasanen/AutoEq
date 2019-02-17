# Radius HP-TWF31
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.1; 25 -7.2; 28 -7.4; 31 -7.5; 34 -7.7; 37 -7.8; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.6; 60 -8.9; 66 -9.2; 72 -9.5; 79 -9.9; 87 -10.3; 96 -10.7; 106 -11.0; 116 -11.3; 128 -11.5; 141 -11.7; 155 -12.0; 170 -12.1; 187 -12.1; 206 -12.2; 227 -12.1; 249 -12.0; 274 -11.8; 302 -11.6; 332 -11.3; 365 -10.9; 402 -10.7; 442 -10.2; 486 -9.8; 535 -9.2; 588 -8.3; 647 -8.0; 712 -7.7; 783 -7.0; 861 -6.7; 947 -6.5; 1042 -6.4; 1146 -6.2; 1261 -6.2; 1387 -6.4; 1526 -6.6; 1678 -6.6; 1846 -6.2; 2031 -5.8; 2234 -5.4; 2457 -4.5; 2703 -3.7; 2973 -2.5; 3270 -2.0; 3597 -2.2; 3957 -3.7; 4353 -5.6; 4788 -4.5; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -8.7; 10263 -9.5; 11289 -7.0; 12418 -6.7; 13660 -7.5; 15026 -8.7; 16529 -10.7; 18182 -9.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-TWF31 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-TWF31 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 147 Hz   | 0.53 | -5.0 dB |
| Peaking | 337 Hz   | 1.1  | -2.5 dB |
| Peaking | 3195 Hz  | 2.48 | 4.6 dB  |
| Peaking | 5884 Hz  | 3.6  | 6.7 dB  |
| Peaking | 16925 Hz | 0.87 | -4.0 dB |
| Peaking | 488 Hz   | 5.11 | -0.6 dB |
| Peaking | 1070 Hz  | 1.48 | 0.9 dB  |
| Peaking | 1531 Hz  | 1.83 | -0.5 dB |
| Peaking | 9984 Hz  | 4.08 | -4.4 dB |
| Peaking | 11632 Hz | 1.4  | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-TWF31/Radius%20HP-TWF31.png)