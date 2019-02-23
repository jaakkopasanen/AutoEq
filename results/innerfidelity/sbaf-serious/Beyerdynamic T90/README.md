# Beyerdynamic T90
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.8; 37 -1.0; 41 -1.1; 45 -1.3; 49 -1.5; 54 -1.5; 60 -1.1; 66 -2.2; 72 -3.1; 79 -3.7; 87 -4.3; 96 -4.9; 106 -5.4; 116 -5.8; 128 -6.3; 141 -6.6; 155 -6.8; 170 -6.8; 187 -7.0; 206 -7.2; 227 -7.1; 249 -7.2; 274 -7.0; 302 -7.0; 332 -6.8; 365 -6.5; 402 -6.2; 442 -5.8; 486 -5.6; 535 -5.2; 588 -4.5; 647 -4.0; 712 -3.7; 783 -3.4; 861 -3.3; 947 -3.4; 1042 -3.6; 1146 -3.6; 1261 -3.8; 1387 -4.4; 1526 -5.3; 1678 -6.1; 1846 -6.4; 2031 -6.6; 2234 -6.6; 2457 -6.4; 2703 -7.0; 2973 -7.6; 3270 -7.5; 3597 -7.0; 3957 -7.1; 4353 -7.0; 4788 -1.6; 5267 -2.8; 5793 -3.7; 6373 -10.3; 7010 -12.5; 7711 -14.1; 8482 -15.6; 9330 -14.9; 10263 -11.4; 11289 -8.6; 12418 -7.5; 13660 -6.6; 15026 -6.6; 16529 -8.6; 18182 -9.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T90 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.93 | 6.2 dB  |
| Peaking | 58 Hz    | 1.97 | 3.7 dB  |
| Peaking | 913 Hz   | 1.35 | 3.6 dB  |
| Peaking | 5299 Hz  | 3.68 | 7.8 dB  |
| Peaking | 8193 Hz  | 1.51 | -9.8 dB |
| Peaking | 229 Hz   | 0.71 | -2.8 dB |
| Peaking | 245 Hz   | 0.42 | 1.7 dB  |
| Peaking | 3149 Hz  | 2.48 | -1.0 dB |
| Peaking | 13817 Hz | 1.64 | 1.9 dB  |
| Peaking | 17910 Hz | 1.43 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T90/Beyerdynamic%20T90.png)