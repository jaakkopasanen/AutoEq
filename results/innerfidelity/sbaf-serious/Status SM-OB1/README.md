# Status SM-OB1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -1.7; 41 -2.5; 45 -3.1; 49 -3.6; 54 -4.2; 60 -4.7; 66 -5.2; 72 -5.5; 79 -5.6; 87 -5.9; 96 -6.5; 106 -6.8; 116 -7.3; 128 -7.8; 141 -8.0; 155 -8.0; 170 -7.9; 187 -8.0; 206 -7.9; 227 -7.5; 249 -7.0; 274 -7.1; 302 -7.7; 332 -7.4; 365 -7.0; 402 -6.9; 442 -6.8; 486 -7.0; 535 -6.9; 588 -6.8; 647 -6.8; 712 -6.7; 783 -6.6; 861 -6.7; 947 -6.6; 1042 -6.2; 1146 -5.4; 1261 -5.3; 1387 -5.2; 1526 -4.9; 1678 -4.0; 1846 -3.2; 2031 -2.9; 2234 -3.0; 2457 -2.7; 2703 -2.1; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Status SM-OB1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Status SM-OB1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.73 | 6.3 dB  |
| Peaking | 148 Hz  | 1.23 | -1.9 dB |
| Peaking | 379 Hz  | 0.97 | -0.6 dB |
| Peaking | 883 Hz  | 3.82 | -0.7 dB |
| Peaking | 3832 Hz | 0.8  | 6.6 dB  |
| Peaking | 1855 Hz | 5.64 | 1.1 dB  |
| Peaking | 3909 Hz | 4.08 | -0.6 dB |
| Peaking | 6268 Hz | 2.41 | 5.3 dB  |
| Peaking | 7349 Hz | 1.44 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Status%20SM-OB1/Status%20SM-OB1.png)