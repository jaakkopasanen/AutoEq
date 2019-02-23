# Nuforce NE 600X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.2; 23 -16.1; 25 -16.0; 28 -15.8; 31 -15.6; 34 -15.3; 37 -15.2; 41 -14.9; 45 -14.7; 49 -14.5; 54 -14.3; 60 -14.0; 66 -13.9; 72 -13.7; 79 -13.6; 87 -13.3; 96 -13.2; 106 -12.9; 116 -12.5; 128 -12.2; 141 -11.9; 155 -11.4; 170 -11.0; 187 -10.4; 206 -9.9; 227 -9.2; 249 -8.7; 274 -8.1; 302 -7.5; 332 -6.8; 365 -6.2; 402 -5.6; 442 -4.9; 486 -4.5; 535 -4.0; 588 -3.2; 647 -3.0; 712 -2.7; 783 -2.4; 861 -2.5; 947 -2.8; 1042 -3.1; 1146 -3.5; 1261 -3.9; 1387 -4.6; 1526 -5.4; 1678 -6.1; 1846 -6.5; 2031 -6.9; 2234 -7.5; 2457 -7.9; 2703 -8.2; 2973 -7.5; 3270 -6.0; 3597 -4.4; 3957 -5.6; 4353 -9.0; 4788 -9.2; 5267 -6.0; 5793 -1.5; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nuforce NE 600X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nuforce NE 600X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.55 | -8.5 dB |
| Peaking | 95 Hz   | 0.37 | -6.1 dB |
| Peaking | 849 Hz  | 0.62 | 6.0 dB  |
| Peaking | 1946 Hz | 0.42 | -3.2 dB |
| Peaking | 6246 Hz | 4.99 | 7.4 dB  |
| Peaking | 1279 Hz | 5.21 | 0.4 dB  |
| Peaking | 2805 Hz | 2.4  | -1.5 dB |
| Peaking | 3684 Hz | 3.05 | 4.8 dB  |
| Peaking | 4598 Hz | 3.48 | -4.7 dB |
| Peaking | 5655 Hz | 7.04 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nuforce%20NE%20600X/Nuforce%20NE%20600X.png)