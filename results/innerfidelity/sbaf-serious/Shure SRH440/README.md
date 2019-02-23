# Shure SRH440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.3; 45 -2.3; 49 -3.3; 54 -4.2; 60 -5.3; 66 -6.2; 72 -6.7; 79 -6.9; 87 -6.5; 96 -5.7; 106 -7.0; 116 -8.5; 128 -8.9; 141 -8.4; 155 -7.8; 170 -6.7; 187 -7.5; 206 -7.3; 227 -6.9; 249 -6.9; 274 -6.9; 302 -6.8; 332 -6.9; 365 -8.0; 402 -8.0; 442 -7.4; 486 -7.4; 535 -7.1; 588 -6.7; 647 -6.5; 712 -6.6; 783 -6.3; 861 -6.4; 947 -6.2; 1042 -5.7; 1146 -5.4; 1261 -5.8; 1387 -6.4; 1526 -7.2; 1678 -7.6; 1846 -7.3; 2031 -7.0; 2234 -6.3; 2457 -5.6; 2703 -5.8; 2973 -5.6; 3270 -6.9; 3597 -6.9; 3957 -5.7; 4353 -5.4; 4788 -3.9; 5267 -2.9; 5793 -1.9; 6373 -1.0; 7010 -4.0; 7711 -6.7; 8482 -10.3; 9330 -12.0; 10263 -11.2; 11289 -7.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 1.01 | 6.8 dB  |
| Peaking | 128 Hz  | 2.27 | -2.7 dB |
| Peaking | 397 Hz  | 3.02 | -1.5 dB |
| Peaking | 6165 Hz | 2.44 | 6.4 dB  |
| Peaking | 9274 Hz | 2.8  | -7.0 dB |
| Peaking | 64 Hz   | 1.15 | 1.5 dB  |
| Peaking | 69 Hz   | 2.61 | -2.9 dB |
| Peaking | 1172 Hz | 2.27 | 2.2 dB  |
| Peaking | 1726 Hz | 1.02 | -1.8 dB |
| Peaking | 2487 Hz | 3.24 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH440/Shure%20SRH440.png)