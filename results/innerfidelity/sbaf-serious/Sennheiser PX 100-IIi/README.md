# Sennheiser PX 100-IIi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.6; 45 -2.4; 49 -3.1; 54 -3.9; 60 -4.7; 66 -5.5; 72 -6.1; 79 -6.7; 87 -7.4; 96 -8.0; 106 -8.4; 116 -8.4; 128 -8.8; 141 -9.2; 155 -9.4; 170 -9.5; 187 -9.5; 206 -9.5; 227 -9.3; 249 -9.2; 274 -9.0; 302 -8.8; 332 -8.5; 365 -8.2; 402 -8.0; 442 -7.5; 486 -7.4; 535 -7.2; 588 -6.8; 647 -6.7; 712 -6.6; 783 -6.3; 861 -6.5; 947 -6.6; 1042 -6.8; 1146 -7.0; 1261 -7.4; 1387 -8.1; 1526 -9.1; 1678 -9.8; 1846 -10.1; 2031 -9.0; 2234 -6.8; 2457 -4.0; 2703 -2.7; 2973 -1.9; 3270 -3.3; 3597 -4.4; 3957 -3.0; 4353 -7.6; 4788 -6.8; 5267 -2.5; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 100-IIi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100-IIi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.67 | 6.8 dB  |
| Peaking | 157 Hz  | 0.58 | -3.6 dB |
| Peaking | 1823 Hz | 2.48 | -4.7 dB |
| Peaking | 2845 Hz | 2.56 | 5.4 dB  |
| Peaking | 6007 Hz | 4.33 | 6.6 dB  |
| Peaking | 772 Hz  | 2.93 | 0.7 dB  |
| Peaking | 4397 Hz | 2.74 | 3.1 dB  |
| Peaking | 4564 Hz | 7.22 | -6.9 dB |
| Peaking | 8570 Hz | 3.15 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20100-IIi/Sennheiser%20PX%20100-IIi.png)