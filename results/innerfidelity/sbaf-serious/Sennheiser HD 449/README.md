# Sennheiser HD 449
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.6; 25 -8.0; 28 -8.4; 31 -8.9; 34 -9.2; 37 -9.5; 41 -9.8; 45 -10.0; 49 -10.2; 54 -10.3; 60 -10.4; 66 -10.5; 72 -10.5; 79 -10.3; 87 -9.9; 96 -9.1; 106 -7.8; 116 -8.1; 128 -10.4; 141 -11.6; 155 -10.4; 170 -9.6; 187 -11.1; 206 -10.8; 227 -10.2; 249 -9.8; 274 -9.1; 302 -8.5; 332 -7.8; 365 -7.1; 402 -7.2; 442 -7.2; 486 -7.2; 535 -7.4; 588 -7.6; 647 -8.1; 712 -8.5; 783 -8.1; 861 -8.1; 947 -8.4; 1042 -8.1; 1146 -8.1; 1261 -8.9; 1387 -9.8; 1526 -10.2; 1678 -10.2; 1846 -9.7; 2031 -8.4; 2234 -6.8; 2457 -5.2; 2703 -5.1; 2973 -4.4; 3270 -4.3; 3597 -4.0; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 449 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 449 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.88 | -3.8 dB |
| Peaking | 189 Hz  | 1.15 | -4.0 dB |
| Peaking | 1535 Hz | 1.48 | -4.2 dB |
| Peaking | 4795 Hz | 1.4  | 7.0 dB  |
| Peaking | 111 Hz  | 7.32 | 2.1 dB  |
| Peaking | 135 Hz  | 8.84 | -2.1 dB |
| Peaking | 2452 Hz | 6.44 | 1.5 dB  |
| Peaking | 6382 Hz | 3.68 | 4.5 dB  |
| Peaking | 7161 Hz | 1.55 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20449/Sennheiser%20HD%20449.png)