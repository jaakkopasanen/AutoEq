# Sennheiser IE 800 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.4; 25 -11.5; 28 -11.6; 31 -11.7; 34 -11.7; 37 -11.8; 41 -11.8; 45 -11.8; 49 -11.8; 54 -11.8; 60 -11.8; 66 -11.8; 72 -11.9; 79 -11.9; 87 -12.0; 96 -12.0; 106 -11.9; 116 -11.7; 128 -11.6; 141 -11.4; 155 -11.2; 170 -10.9; 187 -10.6; 206 -10.2; 227 -9.8; 249 -9.5; 274 -9.1; 302 -8.7; 332 -8.3; 365 -7.9; 402 -7.6; 442 -7.1; 486 -7.0; 535 -6.6; 588 -6.1; 647 -6.0; 712 -5.9; 783 -5.7; 861 -5.9; 947 -6.2; 1042 -6.5; 1146 -6.7; 1261 -6.9; 1387 -7.2; 1526 -7.4; 1678 -7.2; 1846 -6.3; 2031 -5.2; 2234 -3.6; 2457 -1.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.7; 4788 -4.4; 5267 -5.3; 5793 -4.1; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.8; 10263 -9.5; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.27 | -5.0 dB |
| Peaking | 150 Hz  | 0.75 | -2.7 dB |
| Peaking | 3288 Hz | 1.63 | 7.0 dB  |
| Peaking | 6427 Hz | 6.99 | 5.0 dB  |
| Peaking | 9909 Hz | 4.1  | -3.7 dB |
| Peaking | 723 Hz  | 1.99 | 1.2 dB  |
| Peaking | 1586 Hz | 2.02 | -1.9 dB |
| Peaking | 2554 Hz | 3.89 | 2.6 dB  |
| Peaking | 3815 Hz | 1.62 | -2.1 dB |
| Peaking | 4088 Hz | 5.13 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20A/Sennheiser%20IE%20800%20sample%20A.png)