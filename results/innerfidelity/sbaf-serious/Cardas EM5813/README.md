# Cardas EM5813
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.8; 25 -12.8; 28 -12.8; 31 -12.9; 34 -12.9; 37 -13.0; 41 -13.1; 45 -13.3; 49 -13.4; 54 -13.5; 60 -13.8; 66 -14.1; 72 -14.3; 79 -14.7; 87 -15.0; 96 -15.3; 106 -15.5; 116 -15.6; 128 -15.8; 141 -15.9; 155 -16.0; 170 -16.0; 187 -15.8; 206 -15.8; 227 -15.5; 249 -15.2; 274 -14.9; 302 -14.6; 332 -14.1; 365 -13.7; 402 -13.3; 442 -12.6; 486 -12.2; 535 -11.6; 588 -10.8; 647 -10.3; 712 -9.8; 783 -9.4; 861 -8.2; 947 -6.6; 1042 -6.7; 1146 -6.9; 1261 -7.1; 1387 -7.7; 1526 -7.9; 1678 -8.1; 1846 -7.7; 2031 -8.1; 2234 -9.0; 2457 -10.7; 2703 -11.1; 2973 -6.8; 3270 -4.5; 3597 -4.7; 3957 -7.6; 4353 -12.2; 4788 -9.6; 5267 -2.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cardas EM5813 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cardas EM5813 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.22 | -5.7 dB |
| Peaking | 123 Hz  | 0.66 | -4.1 dB |
| Peaking | 292 Hz  | 0.55 | -6.2 dB |
| Peaking | 4515 Hz | 6.37 | -8.1 dB |
| Peaking | 5856 Hz | 3.4  | 7.4 dB  |
| Peaking | 1022 Hz | 2.35 | 3.0 dB  |
| Peaking | 1085 Hz | 0.81 | -1.2 dB |
| Peaking | 2611 Hz | 4.11 | -5.3 dB |
| Peaking | 3327 Hz | 4.39 | 3.9 dB  |
| Peaking | 8186 Hz | 5.01 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -7.2 dB |
| Peaking | 500 Hz   | 1.41 | -4.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cardas%20EM5813/Cardas%20EM5813.png)