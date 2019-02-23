# Sennheiser PX 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.9; 87 -1.6; 96 -2.5; 106 -3.1; 116 -3.7; 128 -4.4; 141 -4.5; 155 -4.0; 170 -4.5; 187 -3.8; 206 -3.8; 227 -4.5; 249 -5.3; 274 -5.9; 302 -6.3; 332 -6.6; 365 -6.6; 402 -6.7; 442 -6.9; 486 -8.5; 535 -9.6; 588 -9.8; 647 -10.3; 712 -10.0; 783 -9.8; 861 -9.5; 947 -9.3; 1042 -9.3; 1146 -9.1; 1261 -9.3; 1387 -9.8; 1526 -10.3; 1678 -10.9; 1846 -11.0; 2031 -10.3; 2234 -9.3; 2457 -8.3; 2703 -6.8; 2973 -4.6; 3270 -2.9; 3597 -4.7; 3957 -7.5; 4353 -7.3; 4788 -5.8; 5267 -3.2; 5793 -1.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -8.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.3  | 6.3 dB  |
| Peaking | 631 Hz   | 2.01 | -3.1 dB |
| Peaking | 3138 Hz  | 0.49 | -7.3 dB |
| Peaking | 3179 Hz  | 2.23 | 9.9 dB  |
| Peaking | 5993 Hz  | 2.33 | 9.6 dB  |
| Peaking | 75 Hz    | 3.79 | 1.0 dB  |
| Peaking | 125 Hz   | 2.71 | -1.2 dB |
| Peaking | 202 Hz   | 4.79 | 1.5 dB  |
| Peaking | 9124 Hz  | 6.88 | -2.7 dB |
| Peaking | 10811 Hz | 1.43 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20200/Sennheiser%20PX%20200.png)