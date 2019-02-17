# Sennheiser Urbanite
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.4; 25 -7.5; 28 -7.6; 31 -7.6; 34 -7.6; 37 -7.6; 41 -7.6; 45 -7.6; 49 -7.6; 54 -7.7; 60 -7.8; 66 -7.9; 72 -7.9; 79 -8.1; 87 -8.3; 96 -8.4; 106 -8.3; 116 -8.2; 128 -8.1; 141 -8.2; 155 -8.5; 170 -7.9; 187 -8.2; 206 -8.1; 227 -7.6; 249 -7.3; 274 -6.9; 302 -6.5; 332 -6.1; 365 -5.9; 402 -5.8; 442 -5.6; 486 -5.6; 535 -5.6; 588 -5.5; 647 -5.8; 712 -6.2; 783 -6.1; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.4; 1261 -6.2; 1387 -6.3; 1526 -6.7; 1678 -6.6; 1846 -5.4; 2031 -3.6; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Urbanite GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Urbanite ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 214 Hz  | 3.59 | -0.4 dB |
| Peaking | 425 Hz  | 0.16 | -3.4 dB |
| Peaking | 440 Hz  | 0.61 | 4.1 dB  |
| Peaking | 3502 Hz | 0.77 | 8.0 dB  |
| Peaking | 1695 Hz | 4.37 | -1.8 dB |
| Peaking | 2384 Hz | 3.72 | 2.1 dB  |
| Peaking | 3577 Hz | 2.61 | -1.3 dB |
| Peaking | 6196 Hz | 2.19 | 5.5 dB  |
| Peaking | 7493 Hz | 1.47 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Urbanite/Sennheiser%20Urbanite.png)