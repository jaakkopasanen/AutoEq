# Radius HP-TWF31
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.6; 25 -6.7; 28 -6.9; 31 -7.0; 34 -7.2; 37 -7.3; 41 -7.5; 45 -7.7; 49 -7.8; 54 -8.0; 60 -8.3; 66 -8.6; 72 -9.0; 79 -9.3; 87 -9.8; 96 -10.2; 106 -10.5; 116 -10.7; 128 -11.0; 141 -11.2; 155 -11.5; 170 -11.6; 187 -11.6; 206 -11.6; 227 -11.5; 249 -11.5; 274 -11.3; 302 -11.1; 332 -10.8; 365 -10.4; 402 -10.2; 442 -9.7; 486 -9.3; 535 -8.7; 588 -7.8; 647 -7.5; 712 -7.2; 783 -6.5; 861 -6.2; 947 -5.9; 1042 -5.8; 1146 -5.7; 1261 -5.7; 1387 -5.9; 1526 -6.1; 1678 -6.1; 1846 -5.7; 2031 -5.3; 2234 -4.9; 2457 -4.0; 2703 -3.2; 2973 -2.0; 3270 -1.4; 3597 -1.7; 3957 -3.2; 4353 -5.1; 4788 -4.0; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -8.2; 10263 -9.0; 11289 -6.6; 12418 -6.5; 13660 -7.0; 15026 -8.2; 16529 -10.1; 18182 -9.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-TWF31 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-TWF31 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 149 Hz   | 0.62 | -4.6 dB |
| Peaking | 330 Hz   | 1.26 | -2.5 dB |
| Peaking | 3171 Hz  | 2.01 | 4.9 dB  |
| Peaking | 5863 Hz  | 3.6  | 6.4 dB  |
| Peaking | 16999 Hz | 1.17 | -3.8 dB |
| Peaking | 485 Hz   | 4.85 | -0.7 dB |
| Peaking | 893 Hz   | 2.79 | 0.9 dB  |
| Peaking | 1191 Hz  | 4    | 0.7 dB  |
| Peaking | 9961 Hz  | 4.18 | -3.7 dB |
| Peaking | 11877 Hz | 1.47 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-TWF31/Radius%20HP-TWF31.png)