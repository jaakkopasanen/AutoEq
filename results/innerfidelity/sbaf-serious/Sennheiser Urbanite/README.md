# Sennheiser Urbanite
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.8; 25 -10.9; 28 -11.0; 31 -11.0; 34 -11.0; 37 -11.0; 41 -11.0; 45 -11.0; 49 -11.0; 54 -11.1; 60 -11.2; 66 -11.3; 72 -11.3; 79 -11.5; 87 -11.8; 96 -11.8; 106 -11.8; 116 -11.6; 128 -11.5; 141 -11.6; 155 -11.9; 170 -11.3; 187 -11.6; 206 -11.5; 227 -11.1; 249 -10.7; 274 -10.3; 302 -9.9; 332 -9.5; 365 -9.3; 402 -9.2; 442 -9.1; 486 -9.0; 535 -9.0; 588 -8.9; 647 -9.3; 712 -9.7; 783 -9.5; 861 -9.7; 947 -9.8; 1042 -9.9; 1146 -9.8; 1261 -9.6; 1387 -9.8; 1526 -10.1; 1678 -10.0; 1846 -8.8; 2031 -7.0; 2234 -5.1; 2457 -2.8; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Urbanite GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Urbanite ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.23 | -4.4 dB |
| Peaking | 181 Hz  | 0.76 | -2.6 dB |
| Peaking | 2823 Hz | 0.34 | -7.5 dB |
| Peaking | 2897 Hz | 1.4  | 10.5 dB |
| Peaking | 5189 Hz | 1.05 | 9.7 dB  |
| Peaking | 1613 Hz | 1.85 | 1.2 dB  |
| Peaking | 1667 Hz | 3.55 | -2.3 dB |
| Peaking | 5132 Hz | 8.26 | -2.9 dB |
| Peaking | 6737 Hz | 1.63 | 3.1 dB  |
| Peaking | 7599 Hz | 2.89 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Urbanite/Sennheiser%20Urbanite.png)