# Astrotec AM90
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.7; 25 -4.8; 28 -4.8; 31 -4.9; 34 -5.0; 37 -5.2; 41 -5.3; 45 -5.5; 49 -5.6; 54 -5.8; 60 -6.1; 66 -6.5; 72 -6.8; 79 -7.2; 87 -7.7; 96 -8.2; 106 -8.4; 116 -8.6; 128 -9.0; 141 -9.3; 155 -9.5; 170 -9.7; 187 -9.8; 206 -9.8; 227 -9.8; 249 -9.9; 274 -9.7; 302 -9.7; 332 -9.5; 365 -9.4; 402 -9.2; 442 -8.8; 486 -8.8; 535 -8.5; 588 -7.9; 647 -7.7; 712 -7.6; 783 -7.1; 861 -7.3; 947 -7.6; 1042 -7.9; 1146 -8.2; 1261 -8.4; 1387 -8.1; 1526 -7.2; 1678 -7.1; 1846 -7.4; 2031 -7.5; 2234 -8.1; 2457 -9.0; 2703 -10.8; 2973 -8.9; 3270 -2.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec AM90 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AM90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.42 | 2.0 dB  |
| Peaking | 206 Hz  | 0.48 | -3.6 dB |
| Peaking | 1753 Hz | 0.88 | -1.9 dB |
| Peaking | 2762 Hz | 4.22 | -8.1 dB |
| Peaking | 4092 Hz | 1.09 | 8.1 dB  |
| Peaking | 3031 Hz | 8.62 | -1.3 dB |
| Peaking | 3372 Hz | 5.95 | 2.3 dB  |
| Peaking | 4197 Hz | 3.72 | -1.3 dB |
| Peaking | 6259 Hz | 2.84 | 4.8 dB  |
| Peaking | 7322 Hz | 1.55 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AM90/Astrotec%20AM90.png)