# Sterling TE-400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -2.5; 66 -4.4; 72 -6.3; 79 -8.0; 87 -9.3; 96 -10.7; 106 -11.6; 116 -11.6; 128 -11.5; 141 -11.3; 155 -11.1; 170 -10.6; 187 -10.4; 206 -10.2; 227 -10.1; 249 -10.0; 274 -9.6; 302 -9.0; 332 -9.0; 365 -8.9; 402 -8.9; 442 -8.6; 486 -8.7; 535 -8.5; 588 -7.1; 647 -2.6; 712 -0.5; 783 -0.5; 861 -3.3; 947 -5.8; 1042 -7.9; 1146 -8.4; 1261 -7.8; 1387 -7.0; 1526 -5.8; 1678 -4.7; 1846 -3.6; 2031 -2.3; 2234 -2.1; 2457 -2.4; 2703 -3.3; 2973 -4.2; 3270 -4.0; 3597 -1.5; 3957 -4.6; 4353 -11.0; 4788 -9.3; 5267 -3.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.4; 8482 -8.8; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sterling TE-400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sterling TE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 57 Hz   | 0.19 | 31.3 dB  |
| Peaking | 94 Hz   | 0.22 | -31.5 dB |
| Peaking | 737 Hz  | 3.33 | 9.7 dB   |
| Peaking | 2268 Hz | 1.66 | 6.1 dB   |
| Peaking | 6046 Hz | 5.75 | 7.0 dB   |
| Peaking | 2871 Hz | 2.72 | -0.3 dB  |
| Peaking | 3734 Hz | 4.94 | 7.8 dB   |
| Peaking | 4426 Hz | 3.16 | -8.6 dB  |
| Peaking | 5408 Hz | 3.63 | 3.9 dB   |
| Peaking | 8283 Hz | 7.45 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sterling%20TE-400/Sterling%20TE-400.png)