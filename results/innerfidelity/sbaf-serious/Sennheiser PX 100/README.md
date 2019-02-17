# Sennheiser PX 100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -3.1; 25 -3.7; 28 -4.4; 31 -4.9; 34 -5.4; 37 -5.8; 41 -6.3; 45 -6.7; 49 -7.0; 54 -7.3; 60 -7.7; 66 -8.0; 72 -8.4; 79 -8.6; 87 -9.0; 96 -9.4; 106 -9.6; 116 -9.7; 128 -9.9; 141 -9.9; 155 -10.0; 170 -10.0; 187 -9.7; 206 -9.4; 227 -9.1; 249 -8.9; 274 -8.7; 302 -8.5; 332 -8.2; 365 -7.8; 402 -7.6; 442 -7.1; 486 -6.9; 535 -6.7; 588 -6.4; 647 -6.2; 712 -6.2; 783 -6.1; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.3; 1387 -8.2; 1526 -9.2; 1678 -10.0; 1846 -10.0; 2031 -8.7; 2234 -6.9; 2457 -4.6; 2703 -1.6; 2973 -0.5; 3270 -0.5; 3597 -1.4; 3957 -8.6; 4353 -11.8; 4788 -6.1; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.33 | 4.3 dB   |
| Peaking | 138 Hz   | 0.7  | -3.7 dB  |
| Peaking | 3311 Hz  | 1.97 | 15.7 dB  |
| Peaking | 4319 Hz  | 1.21 | -24.9 dB |
| Peaking | 5369 Hz  | 1.36 | 19.4 dB  |
| Peaking | 886 Hz   | 1.24 | 1.5 dB   |
| Peaking | 1768 Hz  | 2.83 | -3.1 dB  |
| Peaking | 2652 Hz  | 7.47 | 2.7 dB   |
| Peaking | 8005 Hz  | 5.34 | -1.5 dB  |
| Peaking | 10936 Hz | 0.46 | 0.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20100/Sennheiser%20PX%20100.png)