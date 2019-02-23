# Fidue A71
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.6; 25 -7.9; 28 -8.4; 31 -8.7; 34 -8.9; 37 -9.2; 41 -9.4; 45 -9.7; 49 -9.9; 54 -10.2; 60 -10.6; 66 -10.9; 72 -11.2; 79 -11.5; 87 -11.8; 96 -12.2; 106 -12.3; 116 -12.3; 128 -12.5; 141 -12.5; 155 -12.5; 170 -12.4; 187 -12.2; 206 -12.0; 227 -11.6; 249 -11.2; 274 -10.8; 302 -10.3; 332 -9.8; 365 -9.2; 402 -8.9; 442 -7.7; 486 -7.0; 535 -6.6; 588 -5.8; 647 -5.4; 712 -5.2; 783 -4.8; 861 -4.9; 947 -5.2; 1042 -5.6; 1146 -6.2; 1261 -7.0; 1387 -8.2; 1526 -9.5; 1678 -10.5; 1846 -10.5; 2031 -9.2; 2234 -7.6; 2457 -5.5; 2703 -2.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -3.4; 7010 -7.5; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A71 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A71 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 75 Hz   | 0.39 | -2.0 dB |
| Peaking | 181 Hz  | 0.4  | -4.8 dB |
| Peaking | 743 Hz  | 0.82 | 3.4 dB  |
| Peaking | 1799 Hz | 1.76 | -7.0 dB |
| Peaking | 3703 Hz | 1.05 | 7.6 dB  |
| Peaking | 2954 Hz | 5.85 | 2.3 dB  |
| Peaking | 3734 Hz | 1.45 | -1.3 dB |
| Peaking | 5278 Hz | 2.84 | 2.5 dB  |
| Peaking | 6023 Hz | 4.67 | 5.9 dB  |
| Peaking | 6709 Hz | 2.41 | -5.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A71/Fidue%20A71.png)