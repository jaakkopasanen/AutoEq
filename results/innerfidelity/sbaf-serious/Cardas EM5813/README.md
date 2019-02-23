# Cardas EM5813
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.3; 25 -10.3; 28 -10.3; 31 -10.4; 34 -10.4; 37 -10.5; 41 -10.6; 45 -10.8; 49 -10.9; 54 -11.1; 60 -11.3; 66 -11.6; 72 -11.9; 79 -12.2; 87 -12.5; 96 -12.8; 106 -13.0; 116 -13.1; 128 -13.3; 141 -13.4; 155 -13.5; 170 -13.5; 187 -13.3; 206 -13.3; 227 -13.0; 249 -12.7; 274 -12.4; 302 -12.1; 332 -11.6; 365 -11.2; 402 -10.8; 442 -10.1; 486 -9.7; 535 -9.1; 588 -8.3; 647 -7.8; 712 -7.4; 783 -6.9; 861 -5.7; 947 -4.1; 1042 -4.2; 1146 -4.4; 1261 -4.6; 1387 -5.2; 1526 -5.4; 1678 -5.6; 1846 -5.2; 2031 -5.6; 2234 -6.5; 2457 -8.2; 2703 -8.6; 2973 -4.3; 3270 -2.0; 3597 -2.2; 3957 -5.1; 4353 -9.7; 4788 -7.1; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cardas EM5813 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cardas EM5813 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.42 | -3.2 dB |
| Peaking | 101 Hz  | 0.54 | -2.4 dB |
| Peaking | 221 Hz  | 0.42 | -5.3 dB |
| Peaking | 1054 Hz | 1.36 | 3.5 dB  |
| Peaking | 5926 Hz | 3.88 | 6.9 dB  |
| Peaking | 1951 Hz | 5.84 | 0.7 dB  |
| Peaking | 2614 Hz | 4.81 | -4.8 dB |
| Peaking | 3421 Hz | 2.65 | 6.2 dB  |
| Peaking | 4451 Hz | 4.32 | -6.7 dB |
| Peaking | 5201 Hz | 9.4  | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cardas%20EM5813/Cardas%20EM5813.png)