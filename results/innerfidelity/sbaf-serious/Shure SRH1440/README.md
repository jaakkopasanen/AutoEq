# Shure SRH1440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.1; 96 -1.8; 106 -2.4; 116 -2.9; 128 -3.5; 141 -4.1; 155 -4.5; 170 -4.6; 187 -4.9; 206 -5.0; 227 -5.0; 249 -5.0; 274 -5.0; 302 -5.0; 332 -4.8; 365 -4.8; 402 -4.6; 442 -4.2; 486 -4.2; 535 -4.0; 588 -3.8; 647 -3.1; 712 -3.6; 783 -3.8; 861 -4.5; 947 -4.9; 1042 -5.3; 1146 -5.7; 1261 -6.2; 1387 -7.0; 1526 -8.2; 1678 -9.5; 1846 -10.4; 2031 -10.6; 2234 -11.1; 2457 -10.9; 2703 -10.8; 2973 -11.3; 3270 -11.4; 3597 -11.4; 3957 -10.9; 4353 -10.4; 4788 -8.7; 5267 -6.5; 5793 -4.9; 6373 -3.8; 7010 -4.2; 7711 -6.7; 8482 -10.6; 9330 -12.6; 10263 -9.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.39 | 6.6 dB  |
| Peaking | 764 Hz   | 0.82 | 3.8 dB  |
| Peaking | 2997 Hz  | 0.58 | -6.0 dB |
| Peaking | 6454 Hz  | 1.94 | 6.2 dB  |
| Peaking | 9184 Hz  | 3.92 | -6.9 dB |
| Peaking | 17 Hz    | 1.25 | 1.9 dB  |
| Peaking | 61 Hz    | 0.5  | -1.4 dB |
| Peaking | 78 Hz    | 1.52 | 2.1 dB  |
| Peaking | 876 Hz   | 5.65 | -0.3 dB |
| Peaking | 11345 Hz | 5.63 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1440/Shure%20SRH1440.png)